from enum import Enum


class ContentType(Enum):
    """Defines the available content types in the ADF document."""

    TEXT = "text"
    TABLE = "table"


class TextType(Enum):
    """Defines the available text types in the ADF document."""

    HEADING = "heading"
    PARAGRAPH = "paragraph"


class HeadingLevel(Enum):
    """Defines the available heading levels (H1-H6)."""

    H1 = 1
    H2 = 2
    H3 = 3
    H4 = 4
    H5 = 5
    H6 = 6


class MarkType(Enum):
    """Defines the available text marking types."""

    CODE = "code"
    EM = "em"
    LINK = "link"
    STRIKE = "strike"
    STRONG = "strong"
    SUBSUP = "subsup"
    UNDERLINE = "underline"
    TEXT_COLOR = "textColor"


class TableLayout(Enum):
    """Defines the available table layout options."""

    CENTER = "center"
    ALIGN_START = "align-start"


class TableDisplayMode(Enum):
    """Defines the available table display modes."""

    DEFAULT = "default"
    FIXED = "fixed"
