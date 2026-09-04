from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional, Union

from ..constants.enums import MarkType
from ..exceptions.validation import InvalidMarkError


@dataclass(frozen=True)
class Mark:
    """Represents a generic ADF mark."""

    type: Union[str, MarkType]
    attrs: Optional[Dict[str, Any]] = None

    def to_dict(self) -> dict:
        mark_type = self.type.value if isinstance(self.type, MarkType) else self.type
        valid_marks = {mark.value for mark in MarkType}

        if mark_type not in valid_marks:
            raise InvalidMarkError(f"Invalid mark: {self.type}")

        mark = {"type": mark_type}
        if self.attrs is not None:
            mark["attrs"] = self.attrs

        return mark


def normalize_mark(mark: Union[str, dict, Mark]) -> dict:
    """Normalize supported mark representations to an ADF mark dictionary."""
    if isinstance(mark, Mark):
        return mark.to_dict()

    if isinstance(mark, dict):
        if mark.get("type") not in {mark_type.value for mark_type in MarkType}:
            raise InvalidMarkError(f"Invalid mark: {mark}")
        return mark

    if mark in {mark_type.value for mark_type in MarkType}:
        return {"type": mark}

    raise InvalidMarkError(f"Invalid mark: {mark}")


def normalize_marks(marks: Iterable[Union[str, dict, Mark]]) -> list:
    """Normalize a sequence of marks to ADF mark dictionaries."""
    return [normalize_mark(mark) for mark in marks]
