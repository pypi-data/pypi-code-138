import json
from typing import List, Optional

from botocore.client import BaseClient

from dstack.aws import runners
from dstack.backend import Secret


def list_secret_names(secretsmanager_client: BaseClient, bucket_name: str) -> List[str]:
    prefix = f"/dstack/{bucket_name}/secrets/"
    response = secretsmanager_client.list_secrets(
        MaxResults=50,
        Filters=[
            {
                "Key": "name",
                "Values": [prefix]
            },
            {
                "Key": "tag-key",
                "Values": ["dstack_bucket"]
            },
            {
                "Key": "tag-value",
                "Values": [bucket_name]
            },
        ]
    )
    return [s["Name"][len(prefix):] for s in response["SecretList"]]


def get_secret(secretsmanager_client: BaseClient, bucket_name: str, secret_name: str) -> Optional[Secret]:
    try:
        return Secret(secret_name, secretsmanager_client.get_secret_value(
            SecretId=f"/dstack/{bucket_name}/secrets/{secret_name}"
        )["SecretString"])
    except Exception as e:
        if hasattr(e, "response") and e.response.get("Error") and e.response["Error"].get(
                "Code") in ["ResourceNotFoundException", "InvalidRequestException"]:
            return None
        else:
            raise e


def add_secret(sts_client: BaseClient, iam_client: BaseClient, secretsmanager_client: BaseClient, bucket_name: str,
               secret: Secret):
    secret_id = f"/dstack/{bucket_name}/secrets/{secret.secret_name}"
    secretsmanager_client.create_secret(
        Name=secret_id,
        SecretString=secret.secret_value,
        Description="Generated by dstack",
        Tags=[
            {
                'Key': 'owner',
                'Value': 'dstack'
            },
            {
                'Key': 'dstack_bucket',
                'Value': bucket_name
            }
        ],
    )
    role_name = runners.role_name(iam_client, bucket_name)
    account_id = sts_client.get_caller_identity()["Account"]
    secretsmanager_client.put_resource_policy(
        SecretId=secret_id,
        ResourcePolicy=json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"AWS": f"arn:aws:iam::{account_id}:role/{role_name}"},
                        "Action": [
                            "secretsmanager:GetSecretValue",
                            "secretsmanager:ListSecrets",
                        ],
                        "Resource": "*"
                    }
                ]
            }
        )
    )


def update_secret(secretsmanager_client: BaseClient, bucket_name: str,
                  secret: Secret):
    secret_id = f"/dstack/{bucket_name}/secrets/{secret.secret_name}"
    secretsmanager_client.put_secret_value(
        SecretId=secret_id,
        SecretString=secret.secret_value,
    )


def delete_secret(secretsmanager_client: BaseClient, bucket_name: str, secret_name: str):
    secretsmanager_client.delete_secret(
        SecretId=f"/dstack/{bucket_name}/secrets/{secret_name}",
        ForceDeleteWithoutRecovery=True
    )
