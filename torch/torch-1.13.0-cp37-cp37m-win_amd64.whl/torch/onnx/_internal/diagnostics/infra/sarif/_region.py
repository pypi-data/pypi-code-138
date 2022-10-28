# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Optional

from torch.onnx._internal.diagnostics.infra.sarif import (
    _artifact_content,
    _message,
    _property_bag,
)


@dataclasses.dataclass
class Region(object):
    """A region within an artifact where a result was detected."""

    byte_length: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "byteLength"}
    )
    byte_offset: int = dataclasses.field(
        default=-1, metadata={"schema_property_name": "byteOffset"}
    )
    char_length: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "charLength"}
    )
    char_offset: int = dataclasses.field(
        default=-1, metadata={"schema_property_name": "charOffset"}
    )
    end_column: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "endColumn"}
    )
    end_line: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "endLine"}
    )
    message: Optional[_message.Message] = dataclasses.field(
        default=None, metadata={"schema_property_name": "message"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    snippet: Optional[_artifact_content.ArtifactContent] = dataclasses.field(
        default=None, metadata={"schema_property_name": "snippet"}
    )
    source_language: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "sourceLanguage"}
    )
    start_column: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "startColumn"}
    )
    start_line: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "startLine"}
    )


# flake8: noqa
