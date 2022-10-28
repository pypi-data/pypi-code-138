from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from beartype import beartype

from utilities.tempfile import gettempdir


@beartype
@dataclass
class Config:
    """Settings for the `clean_dir` script."""

    path: Path = gettempdir()
    days: int = 7
    chunk_size: int | None = None
    dry_run: bool = False


@beartype
@dataclass
class Item:
    """An item to clean up."""

    path: Path
    clean: Callable[[], None]
