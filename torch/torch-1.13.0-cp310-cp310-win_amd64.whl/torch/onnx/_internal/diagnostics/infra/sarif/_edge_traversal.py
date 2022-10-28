# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any, Optional

from torch.onnx._internal.diagnostics.infra.sarif import _message, _property_bag


@dataclasses.dataclass
class EdgeTraversal(object):
    """Represents the traversal of a single edge during a graph traversal."""

    edge_id: str = dataclasses.field(metadata={"schema_property_name": "edgeId"})
    final_state: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "finalState"}
    )
    message: Optional[_message.Message] = dataclasses.field(
        default=None, metadata={"schema_property_name": "message"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    step_over_edge_count: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "stepOverEdgeCount"}
    )


# flake8: noqa
