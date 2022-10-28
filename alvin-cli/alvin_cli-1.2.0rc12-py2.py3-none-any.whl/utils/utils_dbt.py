# Based on https://github.com/offbi/pre-commit-dbt/blob/main/pre_commit_dbt/utils.py
import argparse
import json
import re
import subprocess
import traceback
from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Text
from typing import Union

import yaml

from alvin_cli.config import settings
from alvin_cli.schemas.models import CalledProcessError
from alvin_cli.schemas.models import JsonOpenError
from alvin_cli.schemas.models import Macro
from alvin_cli.schemas.models import MacroSchema
from alvin_cli.schemas.models import Model
from alvin_cli.schemas.models import ModelSchema
from alvin_cli.schemas.models import Source
from alvin_cli.schemas.models import SourceSchema
from alvin_cli.schemas.models import Test

SUCCESS_RETURN_CODE = 0
ERROR_RETURN_CODE = 1
ERROR_MISSING_DEPS_RUN_RETURN_CODE = 2
MISSING_DEPS_RUN_MSG = 'Run "dbt deps"'

def convert_to_datetime_utc(datetime_obj: datetime) -> datetime:

    if datetime_obj.tzinfo:
        utcoffset = datetime_obj.utcoffset()

        # If it's already the utc time, we return the object,
        # so we don't convert it again
        if utcoffset and utcoffset.total_seconds() == 0:
            return datetime_obj

    return datetime.fromtimestamp(datetime_obj.timestamp(), tz=timezone.utc)


def convert_str_to_datetime(date_as_str: str) -> Optional[datetime]:
    try:
        formatted_time = datetime.fromisoformat(date_as_str)
        formatted_time = convert_to_datetime_utc(formatted_time)
        return formatted_time
    except:  # noqa: E722
        try:
            # FIX to remove microseconds
            fixed_formatted_time = re.sub(r"\.[\d]+", "", date_as_str)
            formatted_time = datetime.fromisoformat(fixed_formatted_time)
            return formatted_time
        except:  # noqa: E722
            print(f"Invalid start_time: {date_as_str} iso format!!!")
    return None


def num_of_days_from_now(date: Any) -> Optional[str]:
    if date:
        try:
            if isinstance(date, str):
                date_obj = convert_str_to_datetime(date)
                if date_obj:
                    return f"{(convert_to_datetime_utc(datetime.now()) - date_obj).days} days ago"
            elif isinstance(date, datetime):
                return f"{(datetime.now() - date).days} days ago"
        except:  # noqa: E722
            pass

    return None


def cmd_output(
    *cmd: str,
    expected_code: Optional[int] = 0,
    **kwargs: Any,
) -> str:
    kwargs.setdefault("stdout", subprocess.PIPE)
    kwargs.setdefault("stderr", subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if expected_code is not None and proc.returncode != expected_code:
        raise CalledProcessError(
            cmd,
            expected_code,
            proc.returncode,
            stdout,
            stderr,
        )
    return stdout


def paths_to_dbt_models(
    paths: Sequence[str],
    prefix: str = "",
    postfix: str = "",
) -> List[str]:
    return [prefix + Path(path).stem + postfix for path in paths]


def get_json(json_filename: str) -> Dict[str, Any]:
    try:
        file_content = Path(json_filename).read_text(encoding="utf-8")
        return json.loads(file_content)
    except Exception as e:
        raise JsonOpenError(e)


def get_models(
    manifest: Dict[str, Any],
    filenames: Set[str],
) -> Generator[Model, None, None]:
    nodes = manifest.get("nodes", {})
    for key, node in nodes.items():
        split_key = key.split(".")
        filename = split_key[-1]
        if filename in filenames and split_key[0] == "model":
            yield Model(
                model_id=key, model_name=node.get("name"), filename=filename, node=node
            )


def get_macros(
    manifest: Dict[str, Any],
    filenames: Set[str],
) -> Generator[Macro, None, None]:
    macros = manifest.get("macros", {})
    for key, macro in macros.items():
        split_key = key.split(".")
        filename = split_key[-1]
        if filename in filenames and split_key[0] == "macro":
            yield Macro(
                macro_id=key,
                macro_name=macro.get("name"),
                filename=filename,
                macro=macro,
            )


def get_flags(flags: Optional[Sequence[str]] = None) -> List[str]:
    if flags:
        return [flag.replace("+", "-") for flag in flags if flag]
    else:
        return []


def get_macro_sqls(paths: Sequence[str], manifest: Dict[str, Any]) -> Dict[str, Path]:
    sqls = get_filenames(paths, [".sql"])
    macro_paths = [m["path"] for m in manifest.get("macros", {}).values()]
    macro_sqls = get_filenames(macro_paths, extensions=[".sql"])
    return {k: v for k, v in sqls.items() if k in macro_sqls and v == macro_sqls[k]}


def get_model_sqls(paths: Sequence[str], manifest: Dict[str, Any]) -> Dict[str, Any]:
    """Generates compiled sql"""
    sqls = get_filenames(paths, [".sql"])
    # print(sqls)
    macro_sqls = get_macro_sqls(paths, manifest)
    # print(macro_sqls)
    return {k: v for k, v in sqls.items() if k not in macro_sqls}


def get_model_schemas(
    yml_files: Sequence[Path], filenames: Set[str], all_schemas: bool = False
) -> Generator[ModelSchema, None, None]:
    for yml_file in yml_files:
        schema = yaml.safe_load(yml_file.open())
        for model in schema.get("models", []):
            if isinstance(model, dict) and model.get("name"):
                model_name = model.get("name", "")  # pragma: no mutate
                if model_name in filenames or all_schemas:
                    yield ModelSchema(
                        model_name=model_name,
                        file=yml_file,
                        filename=yml_file.stem,
                        model_schema=model,
                    )


def get_macro_schemas(
    yml_files: Sequence[Path], filenames: Set[str], all_schemas: bool = False
) -> Generator[MacroSchema, None, None]:
    for yml_file in yml_files:
        schema = yaml.safe_load(yml_file.open())
        for macro in schema.get("macros", []):
            if isinstance(macro, dict) and macro.get("name"):
                macro_name = macro.get("name", "")  # pragma: no mutate
                if macro_name in filenames or all_schemas:
                    yield MacroSchema(
                        macro_name=macro_name,
                        file=yml_file,
                        filename=yml_file.stem,
                        macro_schema=macro,
                    )


def get_source_schemas(
    yml_files: Sequence[Path],
) -> Generator[SourceSchema, None, None]:
    for yml_file in yml_files:
        schema = yaml.safe_load(yml_file.open())
        for source in schema.get("sources", []):
            source_name = source.get("name")
            tables = source.pop("tables", [])
            for table in tables:
                table_name = table.get("name")
                yield SourceSchema(
                    source_name=source_name,
                    table_name=table_name,
                    filename=yml_file.stem,
                    source_schema=source,
                    table_schema=table,
                )


def obj_in_deps(obj: Any, dep_name: str) -> bool:
    dep_split = set(dep_name.split("."))
    result = False
    if isinstance(obj, SourceSchema):
        result = {obj.prefix, obj.source_name, obj.table_name}.issubset(dep_split)
    elif isinstance(obj, ModelSchema):
        result = {obj.prefix, obj.model_name}.issubset(dep_split)
    elif isinstance(obj, Model):
        result = obj.model_id == dep_name
    return result


def get_test(node_id: str, manifest: Dict[str, Any]) -> Test:
    test_node = manifest.get("nodes", {}).get(node_id)
    test_type = "data" if "data" in test_node.get("tags", []) else "schema"
    test_name = test_node.get("test_metadata", {}).get("name") or "data"
    return Test(
        test_id=node_id,
        test_type=test_type,
        test_name=test_name,
        node=test_node,
    )


def get_parent_childs(
    manifest: Dict[str, Any], obj: Any, manifest_node: str, node_types: List[str]
) -> Generator[Union[Test, Model, Source], None, None]:
    deps = manifest.get(manifest_node, {})
    for dep_name, dep_items in deps.items():
        if obj_in_deps(obj, dep_name):
            for node_id in dep_items:
                node_type = node_id.split(".")[0]
                if node_type in node_types:
                    if node_type == "test":
                        yield get_test(node_id, manifest)
                    elif node_type == "model":
                        node = manifest.get("nodes", {}).get(node_id)
                        yield Model(
                            model_id=node_id,
                            model_name=node.get("name", ""),
                            filename=node.get("path", ""),
                            node=node,
                        )
                    else:  # Source
                        node = manifest.get("sources", {}).get(node_id)
                        yield Source(
                            source_id=node_id,
                            source_name=node.get("source_name", ""),
                            table_name=node.get("name", ""),
                            filename=node.get("path", ""),
                            node=node,
                        )


def get_filenames(
    paths: Sequence[str],
    extensions: Optional[Sequence[str]] = None,
) -> Dict[str, Path]:
    result = {}
    for path in paths:
        file = Path(path)
        filename = file.stem
        if extensions and file.suffix not in extensions:
            pass
        else:
            result[filename] = file
    return result


def run_dbt_cmd(cmd: Sequence[Any]) -> int:
    status_code = SUCCESS_RETURN_CODE
    print(f"Executing cmd: `{' '.join(cmd)}`")
    try:
        output = cmd_output(*list(filter(None, cmd)), expected_code=0)
        print(output)
    except:  # noqa: E722
        if settings.alvin_verbose_log:
            traceback.print_exc()

        format_exc = traceback.format_exc()
        if MISSING_DEPS_RUN_MSG in format_exc:
            status_code = ERROR_MISSING_DEPS_RUN_RETURN_CODE
        else:
            status_code = ERROR_RETURN_CODE

        return status_code
    return status_code


def add_filenames_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames pre-commit believes are changed.",
    )


def add_manifest_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--manifest",
        type=str,
        default="target/manifest.json",
        help="""Location of manifest.json file. Usually target/manifest.json.
        This file contains a full representation of dbt project.
        """,
    )


def add_catalog_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--catalog",
        type=str,
        default="target/catalog.json",
        help="""Location of catalog.json file. Usually target/catalog.json.
        dbt uses this file to render information like column types and table
        statistics into the docs site. In pre-commit-dbt is used for columns
        operations.
        """,
    )


def add_dbt_cmd_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--global-flags",
        nargs="*",
        help="""Global dbt flags applicable to all subcommands.
        Instead of dash `-` please use `+`.""",
    )
    parser.add_argument(
        "--cmd-flags",
        nargs="*",
        help="Command-specific dbt flags. Instead of dash `-` please use `+`.",
    )


def add_dbt_cmd_model_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--model-prefix",
        type=str,
        default="",
        help="Prefix dbt selector, for selecting parents.",
    )
    parser.add_argument(
        "--model-postfix",
        type=str,
        default="",
        help="Postfix dbt selector, for selecting children.",
    )
    parser.add_argument(
        "--models",
        nargs="*",
        help="""pre-commit-dbt is by default running changed files.
        If you need to override that, e.g. in case of Slim CI (state:modified),
        you can use this option.""",
    )


class ParseDict(argparse.Action):  # pragma: no cover
    """Parse a KEY=VALUE string-list into a dictionary"""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[Text, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        """Perform the parsing"""
        result = {}

        if values:
            for item in values:
                split_items = item.split("=", 1)
                key = split_items[0].strip()
                value = split_items[1]

                result[key] = value

        setattr(namespace, self.dest, result)
