# flake8: noqa: F401
r"""Quantized Modules

This file is in the process of migration to `torch/ao/nn/quantized`, and
is kept here for compatibility while the migration process is ongoing.
If you are adding a new entry/functionality, please, add it to the
appropriate file under the `torch/ao/nn/quantized/modules`,
while adding an import statement here.
"""

from torch.ao.nn.quantized.modules.utils import _ntuple_from_first
from torch.ao.nn.quantized.modules.utils import _pair_from_first
from torch.ao.nn.quantized.modules.utils import _quantize_weight
from torch.ao.nn.quantized.modules.utils import hide_packed_params_repr
from torch.ao.nn.quantized.modules.utils import WeightedQuantizedModule
