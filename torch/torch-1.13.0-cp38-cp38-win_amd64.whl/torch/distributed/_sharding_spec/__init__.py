# Keep old package for BC purposes, this file should be removed once
# everything moves to the `torch.distributed._shard` package.
import sys
import torch
import warnings

from torch.distributed._shard.sharding_spec import *  # noqa: F403
warnings.warn(
    "torch.distributed._sharding_spec will be deprecated, use torch.distributed._shard.sharding_spec instead",
    DeprecationWarning
)

import torch.distributed._shard.sharding_spec as _sharding_spec
sys.modules['torch.distributed._sharding_spec'] = _sharding_spec
