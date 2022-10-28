"""
GENERATED CODE - DO NOT EDIT DIRECTLY
This file is generated by gen_diagnostics.py.
See tools/onnx/gen_diagnostics.py for more information.

Diagnostic rules for PyTorch ONNX export.
"""

import dataclasses

# flake8: noqa
from torch.onnx._internal.diagnostics import infra


@dataclasses.dataclass
class _POERules(infra.RuleCollection):
    node_missing_onnx_shape_inference: infra.Rule = dataclasses.field(
        default=infra.Rule.from_sarif(
            **{
                "id": "POE0001",
                "name": "node-missing-onnx-shape-inference",
                "short_description": {"text": "Node is missing ONNX shape inference."},
                "full_description": {
                    "text": "",
                    "markdown": "Node is missing ONNX shape inference.\nThis usually happens when the node is not valid under standard ONNX operator spec.\n",
                },
                "message_strings": {
                    "default": {
                        "text": "The shape inference of {0} type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function."
                    }
                },
                "help_uri": None,
                "properties": {"deprecated": False, "tags": []},
            }
        ),
        init=False,
    )
    """Node is missing ONNX shape inference."""

    missing_custom_symbolic_function: infra.Rule = dataclasses.field(
        default=infra.Rule.from_sarif(
            **{
                "id": "POE0002",
                "name": "missing-custom-symbolic-function",
                "short_description": {
                    "text": "Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX."
                },
                "full_description": {
                    "text": "",
                    "markdown": "Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX.\n",
                },
                "message_strings": {
                    "default": {
                        "text": "ONNX export failed on an operator with unrecognized namespace {0}. If you are trying to export a custom operator, make sure you registered it with the right domain and version."
                    }
                },
                "help_uri": None,
                "properties": {"deprecated": False, "tags": []},
            }
        ),
        init=False,
    )
    """Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX."""

    missing_standard_symbolic_function: infra.Rule = dataclasses.field(
        default=infra.Rule.from_sarif(
            **{
                "id": "POE0003",
                "name": "missing-standard-symbolic-function",
                "short_description": {
                    "text": "Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX."
                },
                "full_description": {
                    "text": "",
                    "markdown": "Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX.\n",
                },
                "message_strings": {
                    "default": {
                        "text": "Exporting the operator '{0}' to ONNX opset version {1} is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub: {2}."
                    }
                },
                "help_uri": None,
                "properties": {"deprecated": False, "tags": []},
            }
        ),
        init=False,
    )
    """Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX."""

    operator_supported_in_newer_opset_version: infra.Rule = dataclasses.field(
        default=infra.Rule.from_sarif(
            **{
                "id": "POE0004",
                "name": "operator-supported-in-newer-opset-version",
                "short_description": {
                    "text": "Operator is supported in newer opset version."
                },
                "full_description": {
                    "text": "",
                    "markdown": "Operator is supported in newer opset version.\n\nExample:\n```python\ntorch.onnx.export(model, args, ..., opset_version=9)\n```\n",
                },
                "message_strings": {
                    "default": {
                        "text": "Exporting the operator '{0}' to ONNX opset version {1} is not supported. Support for this operator was added in version {2}, try exporting with this version."
                    }
                },
                "help_uri": None,
                "properties": {"deprecated": False, "tags": []},
            }
        ),
        init=False,
    )
    """Operator is supported in newer opset version."""


rules = _POERules()
