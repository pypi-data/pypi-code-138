"""S3 storage module."""
import re
import typing as t

import boto3
import boto3.s3.transfer
import botocore.client
import botocore.config
import botocore.exceptions as s3_errors
from fw_utils import AnyFile, Filters

from .. import errors
from ..fileinfo import FileInfo
from ..filters import StorageFilter
from ..storage import AnyPath, CloudStorage

__all__ = ["S3"]

# TODO consider making these configurable
CHUNKSIZE = 8 << 20
TRANSFER_CONFIG = boto3.s3.transfer.TransferConfig(
    multipart_chunksize=CHUNKSIZE, io_chunksize=CHUNKSIZE
)


def create_default_client(
    access_key_id: str = None,
    secret_access_key: str = None,
) -> botocore.client.BaseClient:
    """Boto3 S3 client factory.

    Uses the AWS Access Key Id and AWS Secret Access Key passed in directly
    OR provided via the envvars AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

    See Amazon's docs for the full list of supported credential sources:
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
    """
    config = botocore.config.Config(
        signature_version="s3v4",
        retries={"max_attempts": 3},
    )
    session = boto3.session.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
    )
    return session.client("s3", config=config)


s3_error_map = {
    s3_errors.ClientError: errors.StorageError,
    s3_errors.BotoCoreError: errors.StorageError,
}


def convert_s3_error(exc: Exception) -> t.Type[errors.StorageError]:
    """Return specific S3 errors mapped to StorageError types."""
    if isinstance(exc, s3_errors.ClientError):
        status_code = exc.response["ResponseMetadata"]["HTTPStatusCode"]
        if status_code == 403:
            return errors.PermError
        if status_code == 404:
            return errors.FileNotFound
    return errors.StorageError


errmap = errors.ErrorMapper(*s3_error_map, convert=convert_s3_error)


class S3(CloudStorage):
    """AWS S3 Storage class."""

    url_re = re.compile(
        r"s3://(?P<bucket>[^:/?#]+)((?P<prefix>/[^?#]+))?(\?(?P<query>[^#]+))?"
    )

    def __init__(
        self,
        bucket: str,
        *,
        prefix: str = "",
        access_key_id: t.Optional[str] = None,
        secret_access_key: t.Optional[str] = None,
        create_client: t.Optional[t.Callable] = None,
        **kwargs,
    ):
        """AWS S3 Storage class for working with blobs in S3 buckets.

        Args:
            bucket: AWS S3 bucket name.
            prefix: Common object key prefix. (optional, default is "")
            access_key_id: AWS Access Key Id. (optional, defaults from SDK)
            secret_access_key: AWS Secret Access Key. (optional, defaults from SDK)
            create_client: boto3 S3 client factory.
                (optional, default is create_default_client)
        """
        self.bucket = bucket
        self.prefix = prefix.strip("/")
        create_client = create_client or create_default_client
        self.client = create_client(access_key_id, secret_access_key)
        super().__init__(**kwargs)

    def abspath(self, path: AnyPath) -> str:
        """Return path string relative to the storage URL, including the perfix."""
        return f"{self.prefix}/{self.relpath(path)}".lstrip("/")

    def fullpath(self, path: AnyPath) -> str:
        """Return path string including the storage URL and prefix."""
        return f"s3://{self.bucket}/{self.abspath(path)}".rstrip("/")

    @errmap
    def ls(
        self,
        path: AnyPath = "",
        *,
        include: Filters = None,
        exclude: Filters = None,
        **_,
    ) -> t.Iterator[FileInfo]:
        """Yield each item under prefix matching the include/exclude filters."""
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html
        filt = StorageFilter(include=include, exclude=exclude)
        paginator = self.client.get_paginator("list_objects_v2")
        prefix = f"{self.prefix}/{path}".strip("/")
        if prefix:
            prefix += "/"
        pages = paginator.paginate(Bucket=self.bucket, Prefix=prefix)
        for page in pages:
            for content in page.get("Contents", []):
                filepath: str = content["Key"]
                relpath = re.sub(rf"^{self.prefix}", "", filepath).lstrip("/")
                info = FileInfo(
                    path=relpath,
                    size=content["Size"],
                    created=content["LastModified"].timestamp(),  # TODO consider None
                    modified=content["LastModified"].timestamp(),
                )
                # skip s3 "folders" - path is empty if the prefix itself is a "folder"
                if not relpath or relpath.endswith("/") and info.size == 0:
                    continue  # pragma: no cover
                if filt.match(info):
                    yield info

    @errmap
    def stat(self, path: AnyPath) -> FileInfo:
        """Return FileInfo for a single file."""
        key = f"{self.prefix}/{path}".lstrip("/")
        meta = self.client.head_object(Bucket=self.bucket, Key=key)
        return FileInfo(
            path=str(path),
            size=meta["ContentLength"],
            created=meta["LastModified"].timestamp(),  # TODO consider None
            modified=meta["LastModified"].timestamp(),
        )

    @errmap
    def download_file(self, path: str, dst: t.IO[bytes]) -> None:
        """Download file and it opened for reading in binary mode."""
        bucket = self.bucket
        self.client.download_fileobj(bucket, path, dst, Config=TRANSFER_CONFIG)

    @errmap
    def upload_file(self, path: str, file: AnyFile) -> None:
        """Upload file to the given path."""
        upload_args: list = []
        upload_kwargs: dict = dict(Bucket=self.bucket, Key=path)
        acl = "bucket-owner-full-control"
        if isinstance(file, bytes):
            upload_func = self.client.put_object
            upload_kwargs.update(Body=file, ACL=acl)
        elif isinstance(file, str):
            upload_func = self.client.upload_file
            upload_args = [file]
            upload_kwargs.update(Config=TRANSFER_CONFIG, ExtraArgs={"ACL": acl})
        else:
            upload_func = self.client.upload_fileobj
            upload_args = [file]
            upload_kwargs.update(Config=TRANSFER_CONFIG, ExtraArgs={"ACL": acl})
        upload_func(*upload_args, **upload_kwargs)

    @errmap
    def flush_delete(self):
        """Flush pending remove operations."""
        keys = sorted(self.delete_keys)
        objects = {"Objects": [{"Key": key} for key in keys], "Quiet": True}
        resp = self.client.delete_objects(Bucket=self.bucket, Delete=objects)
        errs = resp.get("Errors", [])
        # TODO only clear keys that don't apper among the errors
        self.delete_keys.clear()
        if errs:
            raise errors.StorageError(
                f"Bulk delete operation failed for {len(errs)} files",
                context=f"flush_delete({self.fullpath('')!r})",
                errors=[f"{err['Key']}: {err['Message']}" for err in errs],
            )
