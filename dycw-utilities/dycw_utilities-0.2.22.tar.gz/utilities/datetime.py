import datetime as dt
from collections.abc import Iterator
from contextlib import suppress

from beartype import beartype

from utilities.re import extract_groups


@beartype
def add_weekdays(date: dt.date, /, *, n: int = 1) -> dt.date:
    """Add a number of a weekdays to a given date. If the initial date is a
    weekend, then moving to the adjacent weekday counts as 1 move.
    """

    if n >= 1:
        for _ in range(n):
            date = round_to_next_weekday(date + dt.timedelta(days=1))
    elif n == 0 and not is_weekday(date):
        raise IsWeekend(date)
    elif n <= -1:
        for _ in range(-n):
            date = round_to_prev_weekday(date - dt.timedelta(days=1))
    return date


class IsWeekend(ValueError):
    ...


@beartype
def date_to_datetime(date: dt.date, /) -> dt.datetime:
    """Expand a date into a datetime"""

    return dt.datetime.combine(date, dt.time())


@beartype
def ensure_date(date: dt.date | str, /) -> dt.date:
    """Ensure the object is a date."""

    return date if isinstance(date, dt.date) else parse_date(date)


@beartype
def ensure_datetime(datetime: dt.datetime | str, /) -> dt.datetime:
    """Ensure the object is a datetime."""

    if isinstance(datetime, dt.datetime):
        return datetime
    else:
        return parse_datetime(datetime)


@beartype
def ensure_time(time: dt.time | str, /) -> dt.time:
    """Ensure the object is a time."""

    return time if isinstance(time, dt.time) else parse_time(time)


@beartype
def ensure_timedelta(timedelta: dt.timedelta | str, /) -> dt.timedelta:
    """Ensure the object is a timedelta."""

    if isinstance(timedelta, dt.timedelta):
        return timedelta
    else:
        return parse_timedelta(timedelta)


@beartype
def is_weekday(date: dt.date, /) -> bool:
    """Check if a date is a weekday."""

    return date.isoweekday() <= 5


@beartype
def parse_date(date: str, /) -> dt.date:
    """Parse a string into a date."""

    with suppress(ValueError):
        return dt.date.fromisoformat(date)
    with suppress(ValueError):
        return dt.datetime.strptime(date, "%Y%m%d").date()
    raise InvalidDate(date)


class InvalidDate(ValueError):
    ...


@beartype
def parse_datetime(datetime: str, /) -> dt.datetime:
    """Parse a string into a datetime."""

    with suppress(ValueError):
        return dt.datetime.fromisoformat(datetime)
    for format in [
        "%Y%m%d",
        "%Y%m%dT%H",
        "%Y%m%dT%H%M",
        "%Y%m%dT%H%M%S",
        "%Y%m%dT%H%M%S.%f",
    ]:
        with suppress(ValueError):
            return dt.datetime.strptime(datetime, format)
    raise InvalidDateTime(datetime)


class InvalidDateTime(ValueError):
    ...


@beartype
def parse_time(time: str) -> dt.time:
    """Parse a string into a time."""

    with suppress(ValueError):
        return dt.time.fromisoformat(time)
    for format in ["%H", "%H%M", "%H%M%S", "%H%M%S.%f"]:
        with suppress(ValueError):
            return dt.datetime.strptime(time, format).time()
    raise InvalidTime(time)


class InvalidTime(ValueError):
    ...


@beartype
def parse_timedelta(timedelta: str) -> dt.timedelta:
    """Parse a string into a timedelta."""

    for format in ["%H:%M:%S", "%H:%M:%S.%f"]:
        try:
            as_dt = dt.datetime.strptime(timedelta, format)
        except ValueError:
            pass
        else:
            return dt.timedelta(
                hours=as_dt.hour,
                minutes=as_dt.minute,
                seconds=as_dt.second,
                microseconds=as_dt.microsecond,
            )
    try:
        days, tail = extract_groups(
            r"([-\d]+)\s*(?:days?)?,?\s*([\d:\.]+)", timedelta
        )
    except ValueError:
        raise InvalidTimedelta(timedelta)
    else:
        return dt.timedelta(days=int(days)) + parse_timedelta(tail)


class InvalidTimedelta(ValueError):
    ...


@beartype
def round_to_next_weekday(date: dt.date, /) -> dt.date:
    """Round a date to the next weekday."""

    return _round_to_weekday(date, True)


@beartype
def round_to_prev_weekday(date: dt.date, /) -> dt.date:
    """Round a date to the previous weekday."""

    return _round_to_weekday(date, False)


@beartype
def _round_to_weekday(date: dt.date, is_next: bool, /) -> dt.date:
    """Round a date to the previous weekday."""

    n = 1 if is_next else -1
    while not is_weekday(date):
        date = add_weekdays(date, n=n)
    return date


@beartype
def serialize_date(date: dt.date, /) -> str:
    """Serialize a date."""

    return date.isoformat()


@beartype
def serialize_datetime(datetime: dt.datetime, /) -> str:
    """Serialize a datetime."""

    return datetime.isoformat()


@beartype
def serialize_time(time: dt.time, /) -> str:
    """Serialize a time."""

    return time.isoformat()


@beartype
def serialize_timedelta(timedelta: dt.timedelta, /) -> str:
    """Serialize a timedelta."""

    if (days := timedelta.days) != 0:
        tail = serialize_timedelta(timedelta - dt.timedelta(days=days))
        return f"d{days},{tail}"
    else:
        return str(timedelta)


@beartype
def yield_weekdays(
    *,
    start: dt.date | None = None,
    end: dt.date | None = None,
    days: int | None = None,
) -> Iterator[dt.date]:
    """Yield the weekdays in a range."""

    if (start is not None) and (end is not None) and (days is None):
        date = round_to_next_weekday(start)
        while date < end:
            yield date
            date = round_to_next_weekday(date + dt.timedelta(days=1))
    elif (start is not None) and (end is None) and (days is not None):
        date = round_to_next_weekday(start)
        for _ in range(days):
            yield date
            date = round_to_next_weekday(date + dt.timedelta(days=1))
    elif (start is None) and (end is not None) and (days is not None):
        date = round_to_prev_weekday(end)
        for _ in range(days):
            yield date
            date = round_to_prev_weekday(date - dt.timedelta(days=1))
    else:
        raise ValueError(f"Invalid options: {start=}, {end=}, {days=}")
