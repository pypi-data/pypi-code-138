from .code_utils import deprecate_module

deprecate_module("SolverUtils", "solver_utils", "0.16.0", future_warn=True)

from .solver_utils import *
