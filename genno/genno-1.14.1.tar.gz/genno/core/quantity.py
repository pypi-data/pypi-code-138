from functools import update_wrapper
from typing import Any, Dict, Hashable, Mapping, Optional, Tuple, Union

import numpy as np
import pandas as pd
import pint
import xarray
from xarray.core.types import InterpOptions

from .types import Dims

#: Name of the class used to implement :class:`.Quantity`.
CLASS = "AttrSeries"
# CLASS = "SparseDataArray"


class Quantity:
    """A sparse data structure that behaves like :class:`xarray.DataArray`.

    Depending on the value of :data:`CLASS`, Quantity is either :class:`.AttrSeries` or
    :class:`SparseDataArray`.
    """

    # To silence a warning in xarray
    __slots__: Tuple[str, ...] = tuple()

    _name: Optional[Hashable]

    def __new__(cls, *args, **kwargs):
        # Use _get_class() to retrieve either AttrSeries or SparseDataArray
        return object.__new__(Quantity._get_class(cls))

    def to_series(self) -> pd.Series:
        """Like :meth:`xarray.DataArray.to_series`."""
        # Provided only for type-checking in other packages. AttrSeries implements;
        # SparseDataArray uses the xr.DataArray method.

    @classmethod
    def from_series(cls, series, sparse=True):
        """Convert `series` to the Quantity class given by :data:`.CLASS`."""
        # NB signature is the same as xr.DataArray.from_series(); except sparse=True
        assert sparse
        return cls._get_class().from_series(series, sparse)

    @property
    def name(self) -> Optional[Hashable]:
        """The name of this quantity."""
        return self._name  # pragma: no cover

    @name.setter
    def name(self, value: Optional[Hashable]) -> None:
        self._name = value  # pragma: no cover

    @property
    def units(self):
        """Retrieve or set the units of the Quantity.

        Examples
        --------
        Create a quantity without units:

        >>> qty = Quantity(...)

        Set using a string; automatically converted to pint.Unit:

        >>> qty.units = "kg"
        >>> qty.units
        <Unit('kilogram')>

        """
        return self.attrs.setdefault(
            "_unit", pint.get_application_registry().dimensionless
        )

    @units.setter
    def units(self, value):
        self.attrs["_unit"] = pint.get_application_registry().Unit(value)

    # Type hints for mypy in downstream applications
    def __len__(self) -> int:
        ...  # pragma: no cover

    def __mul__(self, other) -> "Quantity":
        ...  # pragma: no cover

    def __radd__(self, other):
        ...  # pragma: no cover

    def __rmul__(self, other):
        ...  # pragma: no cover

    def __rsub__(self, other):
        ...  # pragma: no cover

    def __rtruediv__(self, other):
        ...  # pragma: no cover

    def __truediv__(self, other) -> "Quantity":
        ...  # pragma: no cover

    @property
    def attrs(self) -> Dict[Any, Any]:
        ...  # pragma: no cover

    @property
    def coords(self) -> xarray.core.coordinates.DataArrayCoordinates:
        ...  # pragma: no cover

    @property
    def dims(self) -> Tuple[Hashable, ...]:
        ...  # pragma: no cover

    def assign_coords(
        self,
        coords: Optional[Mapping[Any, Any]] = None,
        **coords_kwargs: Any,
    ):
        ...  # pragma: no cover

    def copy(
        self,
        deep: bool = True,
        data: Any = None,
    ):  # NB "Quantity" here offends mypy
        ...  # pragma: no cover

    def expand_dims(
        self,
        dim=None,
        axis=None,
        **dim_kwargs: Any,
    ):  # NB "Quantity" here offends mypy
        ...  # pragma: no cover

    def interp(
        self,
        coords: Mapping[Any, Any] = None,
        method: InterpOptions = "linear",
        assume_sorted: bool = False,
        kwargs: Mapping[str, Any] = None,
        **coords_kwargs: Any,
    ):
        ...  # pragma: no cover

    def item(self, *args):
        ...  # pragma: no cover

    def rename(
        self,
        new_name_or_name_dict: Union[Hashable, Mapping[Any, Hashable]] = None,
        **names: Hashable,
    ):  # NB "Quantity" here offends mypy
        ...  # pragma: no cover

    def sel(
        self,
        indexers: Mapping[Any, Any] = None,
        method: str = None,
        tolerance=None,
        drop: bool = False,
        **indexers_kwargs: Any,
    ) -> "Quantity":
        ...  # pragma: no cover

    def shift(
        self,
        shifts: Mapping[Hashable, int] = None,
        fill_value: Any = None,
        **shifts_kwargs: int,
    ):  # NB "Quantity" here offends mypy
        ...  # pragma: no cover

    def sum(
        self,
        dim: Dims = None,
        # Signature from xarray.DataArray
        *,
        skipna: Optional[bool] = None,
        min_count: Optional[int] = None,
        keep_attrs: Optional[bool] = None,
        **kwargs: Any,
    ):  # NB "Quantity" here offends mypy
        ...  # pragma: no cover

    def to_numpy(self) -> np.ndarray:
        ...  # pragma: no cover

    # Internal methods

    @staticmethod
    def _get_class(cls=None):
        """Get :class:`.AttrSeries` or :class:`.SparseDataArray`, per :data:`.CLASS`."""
        if cls in (Quantity, None):
            if CLASS == "AttrSeries":
                from .attrseries import AttrSeries as cls
            elif CLASS == "SparseDataArray":
                from .sparsedataarray import SparseDataArray as cls
            else:  # pragma: no cover
                raise ValueError(CLASS)

        return cls

    @staticmethod
    def _single_column_df(data, name):
        """Handle `data` and `name` arguments to Quantity constructors."""
        if isinstance(data, pd.DataFrame):
            if len(data.columns) != 1:
                raise TypeError(
                    f"Cannot instantiate Quantity from {len(data.columns)}-D data frame"
                )

            # Unpack a single column; use its name if not overridden by `name`
            return data.iloc[:, 0], (name or data.columns[0])
        # NB would prefer to do this, but pandas has several bugs for MultiIndex with
        #    only 1 level
        # elif (
        #     isinstance(data, pd.Series) and not isinstance(data.index, pd.MultiIndex)
        # ):
        #     return data.set_axis(pd.MultiIndex.from_product([data.index])), name
        else:
            return data, name

    @staticmethod
    def _collect_attrs(data, attrs_arg, kwargs):
        """Handle `attrs` and 'units' `kwargs` to Quantity constructors."""
        # Use attrs, if any, from an existing object, if any
        new_attrs = getattr(data, "attrs", dict()).copy()

        # Overwrite with values from an explicit attrs argument
        new_attrs.update(attrs_arg or dict())

        # Store the "units" keyword argument as an attr
        units = kwargs.pop("units", None)
        if units is not None:
            new_attrs["_unit"] = pint.Unit(units)

        return new_attrs


def assert_quantity(*args):
    """Assert that each of `args` is a Quantity object.

    Raises
    ------
    TypeError
        with a indicative message.
    """
    for i, arg in enumerate(args):
        if not isinstance(arg, Quantity):
            raise TypeError(
                f"arg #{i+1} ({repr(arg)}) is not Quantity; likely an incorrect key"
            )


def maybe_densify(func):
    """Wrapper for computations that densifies :class:`.SparseDataArray` input."""

    def wrapped(*args, **kwargs):
        if CLASS == "SparseDataArray":

            def densify(arg):
                return arg._sda.dense if isinstance(arg, Quantity) else arg

            def sparsify(result):
                return result._sda.convert()

        else:

            def densify(arg):
                return arg

            sparsify = densify

        return sparsify(func(*map(densify, args), **kwargs))

    update_wrapper(wrapped, func)

    return wrapped
