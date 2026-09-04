# Document Structure

ADF documents are hierarchical JSON objects with a root `doc` node, a `version`, and a `content` array.

```python
{
    "version": 1,
    "type": "doc",
    "content": [
        # child nodes
    ]
}
```

## Core helpers

The library includes dedicated helpers for common ADF authoring:

```python
class ContentType(Enum):
    TEXT = "text"
    TABLE = "table"
```

## Latest node coverage

For the latest published ADF schema, use `NodeType` with the generic `Node` builder.

```python
class NodeType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    BULLET_LIST = "bulletList"
    ORDERED_LIST = "orderedList"
    LIST_ITEM = "listItem"
    CODE_BLOCK = "codeBlock"
    PANEL = "panel"
    BLOCKQUOTE = "blockquote"
    RULE = "rule"
    HARD_BREAK = "hardBreak"
    # ... plus cards, media, layout, task, decision, and extension nodes
```

## Text helper

```python
class Text:
    def __init__(self, text: str, *marks: Union[str, dict, Mark])
    def heading(self, level: Union[int, HeadingLevel] = HeadingLevel.H1,
                local_id: Optional[str] = None) -> dict
    def paragraph(self, local_id: Optional[str] = None) -> dict
```

## Generic node helper

```python
@dataclass
class Node:
    type: Union[str, NodeType]
    attrs: Optional[dict] = None
    content: Optional[List[Union[dict, Node, Table]]] = None
    text: Optional[str] = None
    marks: List[Union[str, dict, Mark]] = field(default_factory=list)
```

Use `Node` for:

- lists
- cards
- panels
- status and date nodes
- layout and media nodes
- extension and expand nodes

Pass child content as:

- ADF dictionaries
- `Node` instances
- `Table` instances

If you are using `Text`, first convert it with `.paragraph()` or `.heading()`. Those helper methods return ADF dictionaries, which are valid `content` items.

## Mark coverage

The library supports the existing text marks plus latest-schema marks through `MarkType` and `Mark`.

```python
class MarkType(Enum):
    ALIGNMENT = "alignment"
    ANNOTATION = "annotation"
    BACKGROUND_COLOR = "backgroundColor"
    CODE = "code"
    EM = "em"
    LINK = "link"
    STRIKE = "strike"
    STRONG = "strong"
    SUBSUP = "subsup"
    TEXT_COLOR = "textColor"
    UNDERLINE = "underline"
```
