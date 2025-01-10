from dataclasses import dataclass, asdict
from typing import Optional
from ..constants.enums import MarkType


@dataclass
class Link:
    """
    Represents a hyperlink in the ADF document.

    Attributes:
        href: The URL of the link
        title: Optional title for the link
        collection: Optional collection identifier
        id: Optional unique identifier
        occurrence_key: Optional key to track occurrences
    """

    href: str
    title: Optional[str] = None
    collection: Optional[str] = None
    id: Optional[str] = None
    occurrence_key: Optional[str] = None

    def __post_init__(self):
        """Validates the link after initialization."""
        if not self.href:
            raise ValueError("href is required")

    def to_mark(self) -> dict:
        """
        Converts the link to a mark dictionary format.

        Returns:
            dict: The link in mark format
        """
        attrs = asdict(self)
        # Remove None values
        attrs = {k: v for k, v in attrs.items() if v is not None}

        return {"type": MarkType.LINK.value, "attrs": attrs}
