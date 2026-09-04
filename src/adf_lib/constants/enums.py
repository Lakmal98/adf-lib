from enum import Enum


class ContentType(Enum):
    """Defines the available content types in the ADF document."""

    TEXT = "text"
    TABLE = "table"


class NodeType(Enum):
    """Defines the node types supported by the latest published ADF schema."""

    BLOCK_CARD = "blockCard"
    BLOCKQUOTE = "blockquote"
    BLOCK_TASK_ITEM = "blockTaskItem"
    BODIED_EXTENSION = "bodiedExtension"
    BODIED_SYNC_BLOCK = "bodiedSyncBlock"
    BULLET_LIST = "bulletList"
    CAPTION = "caption"
    CODE_BLOCK = "codeBlock"
    DATE = "date"
    DECISION_ITEM = "decisionItem"
    DECISION_LIST = "decisionList"
    DOC = "doc"
    EMBED_CARD = "embedCard"
    EMOJI = "emoji"
    EXPAND = "expand"
    EXTENSION = "extension"
    HARD_BREAK = "hardBreak"
    HEADING = "heading"
    INLINE_CARD = "inlineCard"
    INLINE_EXTENSION = "inlineExtension"
    LAYOUT_COLUMN = "layoutColumn"
    LAYOUT_SECTION = "layoutSection"
    LIST_ITEM = "listItem"
    MEDIA = "media"
    MEDIA_GROUP = "mediaGroup"
    MEDIA_INLINE = "mediaInline"
    MEDIA_SINGLE = "mediaSingle"
    MENTION = "mention"
    NESTED_EXPAND = "nestedExpand"
    ORDERED_LIST = "orderedList"
    PANEL = "panel"
    PARAGRAPH = "paragraph"
    PLACEHOLDER = "placeholder"
    RULE = "rule"
    STATUS = "status"
    SYNC_BLOCK = "syncBlock"
    TABLE = "table"
    TABLE_CELL = "tableCell"
    TABLE_HEADER = "tableHeader"
    TABLE_ROW = "tableRow"
    TASK_ITEM = "taskItem"
    TASK_LIST = "taskList"
    TEXT = "text"


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

    ALIGNMENT = "alignment"
    ANNOTATION = "annotation"
    BACKGROUND_COLOR = "backgroundColor"
    BORDER = "border"
    BREAKOUT = "breakout"
    CODE = "code"
    DATA_CONSUMER = "dataConsumer"
    EM = "em"
    FONT_SIZE = "fontSize"
    FRAGMENT = "fragment"
    INDENTATION = "indentation"
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
