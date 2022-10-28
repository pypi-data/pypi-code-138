"""Elementary computations for genno."""
# Notes:
# - To avoid ambiguity, computations should not have default arguments. Define default
#   values for the corresponding methods on the Computer class.
import logging
import re
from pathlib import Path
from typing import Any, Collection, Hashable, Mapping, Optional, Union, cast

import pandas as pd
import pint
from xarray.core.types import InterpOptions
from xarray.core.utils import either_dict_or_kwargs

from genno.core.attrseries import AttrSeries, _multiindex_of
from genno.core.quantity import Quantity, assert_quantity, maybe_densify
from genno.core.sparsedataarray import SparseDataArray
from genno.util import UnitLike, collect_units, filter_concat_args

__all__ = [
    "add",
    "aggregate",
    "apply_units",
    "assign_units",
    "broadcast_map",
    "combine",
    "concat",
    "convert_units",
    "disaggregate_shares",
    "div",
    "group_sum",
    "index_to",
    "interpolate",
    "load_file",
    "mul",
    "pow",
    "product",
    "ratio",
    "relabel",
    "rename_dims",
    "select",
    "sum",
    "write_report",
]


import xarray as xr  # noqa: E402

log = logging.getLogger(__name__)

# Carry unit attributes automatically
xr.set_options(keep_attrs=True)


def add(*quantities, fill_value=0.0):
    """Sum across multiple `quantities`.

    Raises
    ------
    ValueError
        if any of the `quantities` have incompatible units.

    Returns
    -------
    .Quantity
        Units are the same as the first of `quantities`.
    """
    # Ensure arguments are all quantities
    assert_quantity(*quantities)

    if isinstance(quantities[0], AttrSeries):
        # map() returns an iterable
        quantities = iter(quantities)
    else:
        # Use xarray's built-in broadcasting, return to Quantity class
        quantities = map(Quantity, xr.broadcast(*quantities))

    # Initialize result values with first entry
    result = next(quantities)
    ref_unit = collect_units(result)[0]

    # Iterate over remaining entries
    for q in quantities:
        u = collect_units(q)[0]
        if not u.is_compatible_with(ref_unit):
            raise ValueError(f"Units '{ref_unit:~}' and '{u:~}' are incompatible")

        factor = u.from_(1.0, strict=False).to(ref_unit).magnitude

        if isinstance(q, AttrSeries):
            result = result.add(factor * q, fill_value=fill_value).dropna()
        else:
            result = result + factor * q

    return result


def aggregate(quantity, groups: Mapping[Hashable, Mapping], keep: bool):
    """Aggregate *quantity* by *groups*.

    Parameters
    ----------
    quantity : :class:`Quantity <genno.utils.Quantity>`
    groups: dict of dict
        Top-level keys are the names of dimensions in `quantity`. Second-level keys are
        group names; second-level values are lists of labels along the dimension to sum
        into a group.
    keep : bool
        If True, the members that are aggregated into a group are returned with the
        group sums. If False, they are discarded.

    Returns
    -------
    :class:`Quantity <genno.utils.Quantity>`
        Same dimensionality as `quantity`.

    """
    result = quantity

    for dim, dim_groups in groups.items():
        # Optionally keep the original values
        values = [result] if keep else []

        # Aggregate each group
        for group, members in dim_groups.items():
            if keep and group in values[0].coords[dim]:
                log.warning(
                    f"{dim}={group!r} is already present in quantity {quantity.name!r} "
                    "with keep=True"
                )

            agg = result.sel({dim: members}).sum(dim=dim).expand_dims({dim: [group]})

            if isinstance(agg, AttrSeries):
                # .transpose() is necessary for AttrSeries
                agg = agg.transpose(*quantity.dims)
            else:
                # Restore fill_value=NaN for compatibility
                agg = agg._sda.convert()
            values.append(agg)

        # Reassemble to a single dataarray
        result = concat(
            *values, **({} if isinstance(quantity, AttrSeries) else {"dim": dim})
        )

    # Preserve attrs
    result.attrs = quantity.attrs
    result.name = quantity.name

    return result


def _unit_args(qty, units):
    result = [pint.get_application_registry(), qty.attrs.get("_unit", None)]
    return *result, getattr(result[1], "dimensionality", {}), result[0].Unit(units)


def apply_units(qty: Quantity, units: UnitLike) -> Quantity:
    """Apply `units` to `qty`.

    If `qty` has existing units…

    - …with compatible dimensionality to `units`, the magnitudes are adjusted, i.e.
      behaves like :func:`convert_units`.
    - …with incompatible dimensionality to `units`, the units attribute is overwritten
      and magnitudes are not changed, i.e. like :func:`assign_units`, with a log message
      on level ``WARNING``.

    To avoid ambiguities between the two cases, use :func:`convert_units` or
    :func:`assign_units` instead.

    Parameters
    ----------
    qty : Quantity
    units : str or pint.Unit
        Units to apply to `qty`.
    """
    registry, existing, existing_dims, new_units = _unit_args(qty, units)

    if len(existing_dims):
        # Some existing dimensions: log a message either way
        if existing_dims == new_units.dimensionality:
            log.debug(f"Convert '{existing}' to '{new_units}'")
            # NB use a factor because pint.Quantity cannot wrap AttrSeries
            result = qty * registry.Quantity(1.0, existing).to(new_units).magnitude
        else:
            log.warning(f"Replace '{existing}' with incompatible '{new_units}'")
            result = qty.copy()
    else:
        # No units, or dimensionless
        result = qty.copy()

    result.units = new_units

    return result


def assign_units(qty: Quantity, units: UnitLike) -> Quantity:
    """Set the `units` of `qty` without changing magnitudes.

    Logs on level ``INFO`` if `qty` has existing units.

    Parameters
    ----------
    qty : Quantity
    units : str or pint.Unit
        Units to assign to `qty`.
    """
    registry, existing, existing_dims, new_units = _unit_args(qty, units)

    if len(existing_dims):
        msg = f"Replace '{existing}' with '{new_units}'"
        # Some existing dimensions: log a message either way
        if existing_dims == new_units.dimensionality:
            # NB use a factor because pint.Quantity cannot wrap AttrSeries
            if registry.Quantity(1.0, existing).to(new_units).magnitude != 1.0:
                log.info(f"{msg} without altering magnitudes")
        else:
            log.info(f"{msg} with different dimensionality")

    result = qty.copy()
    result.units = new_units

    return result


def convert_units(qty: Quantity, units: UnitLike) -> Quantity:
    """Convert magnitude of `qty` from its current units to `units`.

    Parameters
    ----------
    qty : Quantity
    units : str or pint.Unit
        Units to assign to `qty`.

    Raises
    ------
    ValueError
        if `units` does not match the dimensionality of the current units of `qty`.
    """
    registry, existing, existing_dims, new_units = _unit_args(qty, units)

    try:
        # NB use a factor because pint.Quantity cannot wrap AttrSeries
        factor = registry.Quantity(1.0, existing).to(new_units).magnitude
    except pint.DimensionalityError:
        raise ValueError(
            f"Existing dimensionality {existing_dims!r} cannot be converted to {units} "
            f"with dimensionality {new_units.dimensionality!r}"
        ) from None

    result = qty * factor
    result.units = new_units

    return result


def broadcast_map(quantity, map, rename={}, strict=False):
    """Broadcast `quantity` using a `map`.

    The `map` must be a 2-dimensional Quantity with dimensions (``d1``, ``d2``), such as
    returned by :func:`map_as_qty`. `quantity` must also have a dimension ``d1``.
    Typically ``len(d2) > len(d1)``.

    `quantity` is 'broadcast' by multiplying it with `map`, and then summing on the
    common dimension ``d1``. The result has the dimensions of `quantity`, but with
    ``d2`` in place of ``d1``.

    Parameters
    ----------
    rename : dict (str -> str), optional
        Dimensions to rename on the result.
    strict : bool, optional
        Require that each element of ``d2`` is mapped from exactly 1 element of ``d1``.
    """
    # NB int() is for AttrSeries
    if strict and int(map.sum()) != len(map.coords[map.dims[1]]):
        raise ValueError("invalid map")

    return product(quantity, map).sum(map.dims[0]).rename(rename)


def combine(*quantities, select=None, weights=None):  # noqa: F811
    """Sum distinct *quantities* by *weights*.

    Parameters
    ----------
    *quantities : Quantity
        The quantities to be added.
    select : list of dict
        Elements to be selected from each quantity. Must have the same number of
        elements as `quantities`.
    weights : list of float
        Weight applied to each quantity. Must have the same number of elements as
        `quantities`.

    Raises
    ------
    ValueError
        If the *quantities* have mismatched units.
    """
    # Handle arguments
    select = select or len(quantities) * [{}]
    weights = weights or len(quantities) * [1.0]

    # Check units
    units = collect_units(*quantities)
    for u in units:
        # TODO relax this condition: modify the weights with conversion factors if the
        #      units are compatible, but not the same
        if u != units[0]:
            raise ValueError(f"Cannot combine() units {units[0]} and {u}")
    units = units[0]

    args = []

    for quantity, indexers, weight in zip(quantities, select, weights):
        # Select data
        temp = globals()["select"](quantity, indexers)

        # Dimensions along which multiple values are selected
        multi = [dim for dim, values in indexers.items() if isinstance(values, list)]
        if len(multi):
            # Sum along these dimensions
            temp = temp.sum(dim=multi)

        args.append(weight * temp)

    result = add(*args)
    result.attrs["_unit"] = units

    return result


def concat(*objs, **kwargs):
    """Concatenate Quantity `objs`.

    Any strings included amongst `objs` are discarded, with a logged warning; these
    usually indicate that a quantity is referenced which is not in the Computer.
    """
    objs = filter_concat_args(objs)
    if Quantity._get_class() is AttrSeries:
        try:
            # Retrieve a "dim" keyword argument
            dim = kwargs.pop("dim")
        except KeyError:
            pass
        else:
            if isinstance(dim, pd.Index):
                # Convert a pd.Index argument to names and keys
                kwargs["names"] = [dim.name]
                kwargs["keys"] = dim.values
            else:
                # Something else; warn and discard
                log.warning(f"Ignore concat(…, dim={repr(dim)})")

        # Ensure objects have aligned dimensions
        _objs = [next(objs)]
        _objs.extend(map(lambda o: o.align_levels(_objs[0]), objs))

        return pd.concat(_objs, **kwargs)
    else:
        # Correct fill-values
        return xr.concat(objs, **kwargs)._sda.convert()


def disaggregate_shares(quantity, shares):
    """Disaggregate *quantity* by *shares*."""
    result = quantity * shares
    result.attrs["_unit"] = collect_units(quantity)[0]
    return result


def div(numerator, denominator):
    """Compute the ratio `numerator` / `denominator`.

    Parameters
    ----------
    numerator : .Quantity
    denominator : .Quantity
    """
    # Handle units
    u_num, u_denom = collect_units(numerator, denominator)

    if isinstance(numerator, AttrSeries):
        result = numerator / denominator.align_levels(numerator)
    else:
        result = numerator / denominator

    # This shouldn't be necessary; would instead prefer:
    # result.attrs["_unit"] = u_num / u_denom
    # … but is necessary to avoid an issue when the operands are different Unit classes
    ureg = pint.get_application_registry()
    result.attrs["_unit"] = ureg.Unit(u_num) / ureg.Unit(u_denom)

    if isinstance(result, AttrSeries):
        result.dropna(inplace=True)

    return result


#: Alias of :func:`mul`, for backwards compatibility.
#:
#: .. note:: This may be deprecated and possibly removed in a future version.
ratio = div


def group_sum(qty, group, sum):
    """Group by dimension *group*, then sum across dimension *sum*.

    The result drops the latter dimension.
    """
    return concat(
        *[values.sum(dim=[sum]) for _, values in qty.groupby(group)],
        dim=group,
    )


@maybe_densify
def interpolate(
    qty: Quantity,
    coords: Mapping[Hashable, Any] = None,
    method: InterpOptions = "linear",
    assume_sorted: bool = True,
    kwargs: Mapping[str, Any] = None,
    **coords_kwargs: Any,
) -> Quantity:
    """Interpolate `qty`.

    For the meaning of arguments, see :meth:`xarray.DataArray.interp`. When
    :data:`.CLASS` is :class:`.AttrSeries`, only 1-dimensional interpolation (one key
    in `coords`) is tested/supported.
    """
    if assume_sorted is not True:
        log.warning(f"interpolate(…, assume_sorted={assume_sorted}) ignored")

    return qty.interp(coords, method, assume_sorted, kwargs, **coords_kwargs)


def load_file(
    path: Path,
    dims: Union[Collection[Hashable], Mapping[Hashable, Hashable]] = {},
    units: UnitLike = None,
    name: Optional[str] = None,
) -> Any:
    """Read the file at *path* and return its contents as a :class:`.Quantity`.

    Some file formats are automatically converted into objects for direct use in genno
    computations:

    :file:`.csv`:
       Converted to :class:`.Quantity`. CSV files must have a 'value' column; all others
       are treated as indices, except as given by `dims`. Lines beginning with '#' are
       ignored.

    Parameters
    ----------
    path : pathlib.Path
        Path to the file to read.
    dims : collections.abc.Collection or collections.abc.Mapping, optional
        If a collection of names, other columns besides these and 'value' are discarded.
        If a mapping, the keys are the column labels in `path`, and the values are the
        target dimension names.
    units : str or pint.Unit
        Units to apply to the loaded Quantity.
    name : str
        Name for the loaded Quantity.
    """
    # TODO optionally cache: if the same Computer is used repeatedly, then the file will
    #      be read each time; instead cache the contents in memory.
    # TODO strip leading/trailing whitespace from column names
    if path.suffix == ".csv":
        return _load_file_csv(path, dims, units, name)
    elif path.suffix in (".xls", ".xlsx"):
        # TODO define expected Excel data input format
        raise NotImplementedError  # pragma: no cover
    elif path.suffix == ".yaml":
        # TODO define expected YAML data input format
        raise NotImplementedError  # pragma: no cover
    else:
        # Default
        return open(path).read()


UNITS_RE = re.compile(r"# Units?: (.*)\s+")


def _load_file_csv(
    path: Path,
    dims: Union[Collection[Hashable], Mapping[Hashable, Hashable]] = {},
    units: UnitLike = None,
    name: Optional[str] = None,
) -> Quantity:
    # Peek at the header, if any, and match a units expression
    with open(path, "r", encoding="utf-8") as f:
        for line, match in map(lambda l: (l, UNITS_RE.fullmatch(l)), f):
            if match:
                if units:
                    log.warning(f"Replace {match.group(1)!r} from file with {units!r}")
                else:
                    units = match.group(1)
                break
            elif not line.startswith("#"):
                break  # Give up at first non-commented line

    # Read the data
    data = pd.read_csv(path, comment="#", skipinitialspace=True)

    # Index columns
    index_columns = data.columns.tolist()
    index_columns.remove("value")

    try:
        # Retrieve the unit column from the file
        units_col = data.pop("unit").unique()
        index_columns.remove("unit")
    except KeyError:
        pass  # No such column; use None or argument value
    else:
        # Use a unique value for units of the quantity
        if len(units_col) > 1:
            raise ValueError(
                f"Cannot load {path} with non-unique units {repr(units_col)}"
            )
        elif units and units not in units_col:
            raise ValueError(
                f"Explicit units {units} do not match {units_col[0]} in {path}"
            )
        units = units_col[0]

    if dims:
        # Convert a list, set, etc. to a dict
        dims = dims if isinstance(dims, Mapping) else {d: d for d in dims}

        # - Drop columns not mentioned in *dims*
        # - Rename columns according to *dims*
        data = data.drop(columns=set(index_columns) - set(dims.keys())).rename(
            columns=dims
        )

        index_columns = list(data.columns)
        index_columns.pop(index_columns.index("value"))

    # Prepare a Quantity object with the (bare) units and any conversion factor
    registry = pint.get_application_registry()
    units = units or "1.0 dimensionless"
    if isinstance(units, str):
        uq = registry(units)
    elif isinstance(units, pint.Unit):
        uq = registry.Quantity(1.0, units)
    else:
        uq = units

    return Quantity(
        uq.magnitude * data.set_index(index_columns)["value"], units=uq.units, name=name
    )


def index_to(
    qty: Quantity,
    dim_or_selector: Union[str, Mapping],
    label: Optional[Hashable] = None,
) -> Quantity:
    """Compute an index of `qty` against certain of its values.

    If the label is not provided, :func:`index_to` uses the label in the first position
    along the identified dimension.

    Parameters
    ----------
    qty : :class:`~genno.Quantity`
    dim_or_selector : str or mapping
        If a string, the ID of the dimension to index along.
        If a mapping, it must have only one element, mapping a dimension ID to a label.
    label : Hashable
        Label to select along the dimension, required if `dim_or_selector` is a string.
    Raises
    ------
    TypeError
        if `dim_or_selector` is a mapping with length != 1.
    """
    if isinstance(dim_or_selector, Mapping):
        if len(dim_or_selector) != 1:
            raise TypeError(
                f"Got {dim_or_selector}; expected a mapping from 1 key to 1 value"
            )
        dim, label = dict(dim_or_selector).popitem()
    else:
        # Unwrap dask.core.literals
        dim = getattr(dim_or_selector, "data", dim_or_selector)
        label = getattr(label, "data", label)

    if label is None:
        # Choose a label on which to normalize
        label = qty.coords[dim][0].item()
        log.info(f"Normalize quantity {qty.name} on {dim}={label}")

    return div(qty, qty.sel({dim: label}))


def pow(a, b):
    """Compute `a` raised to the power of `b`.

    .. todo:: Provide units on the result in the special case where `b` is a Quantity
       but all its values are the same :class:`int`.

    Returns
    -------
    .Quantity
        If `b` is :class:`int`, then the quantity has the units of `a` raised to this
        power; e.g. "kg²" → "kg⁴" if `b` is 2. In other cases, there are no meaningful
        units, so the returned quantity is dimensionless.
    """
    if isinstance(b, int):
        unit_exponent = b
        b = Quantity(float(b))
    else:
        unit_exponent = 0

    u_a, u_b = collect_units(a, b)

    if not u_b.dimensionless:
        raise ValueError(f"Cannot raise to a power with units ({u_b:~})")

    if isinstance(a, AttrSeries):
        result = a ** b.align_levels(a)
    else:
        result = a**b

    result.attrs["_unit"] = (
        a.attrs["_unit"] ** unit_exponent
        if unit_exponent
        else pint.get_application_registry().dimensionless
    )

    return result


def mul(*quantities: Quantity) -> Quantity:
    """Compute the product of any number of *quantities*."""
    # Iterator over (quantity, unit) tuples
    items = zip(quantities, collect_units(*quantities))

    # Initialize result values with first entry
    result, u_result = next(items)

    # Iterate over remaining entries
    for q, u in items:
        if isinstance(q, AttrSeries):
            # Work around pandas-dev/pandas#25760; see attrseries.py
            result = (result * q.align_levels(result)).dropna()
        else:
            result = result * q
        u_result *= u

    result.attrs["_unit"] = u_result

    return result


#: Alias of :func:`mul`, for backwards compatibility.
#:
#: .. note:: This may be deprecated and possibly removed in a future version.
product = mul


def relabel(
    qty: Quantity,
    labels: Mapping[Hashable, Mapping] = None,
    **dim_labels: Mapping,
) -> Quantity:
    """Replace specific labels along dimensions of `qty`.

    Parameters
    ----------
    labels :
        Keys are strings identifying dimensions of `qty`; values are further mappings
        from original labels to new labels. Dimensions and labels not appearing in `qty`
        have no effect.
    dim_labels :
        Mappings given as keyword arguments, where argument name is the dimension.

    Raises
    ------
    ValueError
        if both `labels` and `dim_labels` are given.
    """
    # NB pandas uses the term "levels [of a MultiIndex]"; xarray uses "coords [for a
    # dimension]".
    # TODO accept callables as values in `mapper`, as DataArray.assign_coords() does
    maps = either_dict_or_kwargs(labels, dim_labels, "relabel")

    # Iterate over (dim, label_map) for only dims included in `qty`
    iter = filter(lambda kv: kv[0] in qty.dims, maps.items())

    def map_labels(mapper, values):
        """Generate the new labels for a single dimension."""
        return list(map(lambda label: mapper.get(label, label), values))

    if isinstance(qty, AttrSeries):
        # Prepare a new index
        idx = _multiindex_of(qty)
        for dim, label_map in iter:
            # - Look up numerical index of the dimension in `idx`
            # - Retrieve the existing levels.
            # - Map to new levels.
            # - Assign, creating a new index
            idx = idx.set_levels(
                map_labels(label_map, idx.levels[idx.names.index(dim)]), level=dim
            )

        # Assign the new index to a copy of qty
        result = cast(AttrSeries, qty.copy())
        result.index = idx

        return result
    else:
        return cast(SparseDataArray, qty).assign_coords(
            {dim: map_labels(m, qty.coords[dim].data) for dim, m in iter}
        )


def rename_dims(
    qty: Quantity,
    new_name_or_name_dict: Union[Hashable, Mapping[Any, Hashable]] = None,
    **names: Hashable,
) -> Quantity:
    """Rename the dimensions of `qty`.

    Like :meth:`xarray.DataArray.rename`.
    """
    return qty.rename(new_name_or_name_dict, **names)


def select(qty, indexers, inverse=False):
    """Select from *qty* based on *indexers*.

    Parameters
    ----------
    qty : .Quantity
    indexers : dict (str -> list of str)
        Elements to be selected from *qty*. Mapping from dimension names to labels
        along each dimension.
    inverse : bool, optional
        If :obj:`True`, *remove* the items in indexers instead of keeping them.
    """
    if inverse:
        new_indexers = {}
        for dim, labels in indexers.items():
            new_indexers[dim] = list(
                filter(lambda l: l not in labels, qty.coords[dim].data)
            )
        indexers = new_indexers

    return qty.sel(indexers)


def sum(quantity, weights=None, dimensions=None):
    """Sum *quantity* over *dimensions*, with optional *weights*.

    Parameters
    ----------
    quantity : .Quantity
    weights : .Quantity, optional
        If *dimensions* is given, *weights* must have at least these
        dimensions. Otherwise, any dimensions are valid.
    dimensions : list of str, optional
        If not provided, sum over all dimensions. If provided, sum over these
        dimensions.
    """
    if weights is None:
        weights, w_total = 1, 1
    else:
        w_total = weights.sum(dim=dimensions)
        if 0 == len(w_total.dims):
            w_total = w_total.item()

    result = (quantity * weights).sum(dim=dimensions) / w_total
    result.units = collect_units(quantity)[0]
    return result


def write_report(quantity, path):
    """Write a quantity to a file.

    Parameters
    ----------
    path : str or Path
        Path to the file to be written.
    """
    path = Path(path)

    if path.suffix == ".csv":
        quantity.to_dataframe().to_csv(path)
    elif path.suffix == ".xlsx":
        quantity.to_dataframe().to_excel(path, merge_cells=False)
    else:
        path.write_text(quantity)
