# ADF Library

## Overview
ADF Library is a Python package for creating and manipulating ADF (Atlassian Document Format) documents. It provides a clean, type-safe API for building structured documents with support for headings, paragraphs, tables, and rich text formatting.

## Installation
```bash
pip install adf_lib
```

## Quick Start

```python
from adf_lib import ADF, Text, Table, Link
from adf_lib.constants.enums import HeadingLevel

# Create a new document
doc = ADF()

# Add a heading
doc.add(Text("My Document").heading(HeadingLevel.H1))

# Add a paragraph with formatting
doc.add(Text("This is a formatted paragraph", "strong", "em").paragraph())

# Export as dictionary
adf_dict = doc.to_dict()
```

## Core Components

### Document Structure
The ADF document is composed of various content types organized in a hierarchical structure:

```python
{
    "version": 1,
    "type": "doc",
    "content": [
        # Content elements go here
    ]
}
```

### Content Types
The library supports the following content types:

```python
class ContentType(Enum):
    TEXT = "text"
    TABLE = "table"
```

### Text Types
Text content can be formatted as:

```python
class TextType(Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
```

## Detailed API Reference

### ADF Class
The main document class that serves as a container for all content.

```python
class ADF:
    def __init__(self, version: int = 1, type: str = "doc")
    def add(self, content: dict) -> None
    def to_dict(self) -> dict
```

#### Parameters:
- `version`: Document version (default: 1)
- `type`: Document type (default: "doc")

#### Methods:
- `add(content)`: Adds a content element to the document
- `to_dict()`: Converts the document to a dictionary format

### Text Class
Handles text content with formatting.

```python
class Text:
    def __init__(self, text: str, *marks: Union[str, dict])
    def heading(self, level: Union[int, HeadingLevel] = HeadingLevel.H1,
                local_id: Optional[str] = None) -> dict
    def paragraph(self, local_id: Optional[str] = None) -> dict
```

#### Parameters:
- `text`: The text content
- `marks`: Optional formatting marks

#### Methods:
- `heading()`: Creates a heading element
- `paragraph()`: Creates a paragraph element

### Table Class
Handles table creation and manipulation.

```python
class Table:
    def __init__(
        self,
        width: int,
        is_number_column_enabled: bool = False,
        layout: Union[str, TableLayout] = TableLayout.CENTER,
        display_mode: Union[str, TableDisplayMode] = TableDisplayMode.DEFAULT
    )
    def header(self, content: List[dict], col_span: int = 1,
               row_span: int = 1) -> dict
    def cell(self, content: List[dict], col_span: int = 1,
             row_span: int = 1) -> dict
    def add_row(self, cells: List[dict]) -> None
    def to_dict(self) -> dict
```

#### Parameters:
- `width`: Table width (percentage)
- `is_number_column_enabled`: Enable numbered columns
- `layout`: Table layout style
- `display_mode`: Display mode

#### Methods:
- `header()`: Creates a header cell
- `cell()`: Creates a regular cell
- `add_row()`: Adds a row to the table
- `to_dict()`: Converts table to dictionary format

### Link Class
Handles hyperlinks in the document.

```python
@dataclass
class Link:
    href: str
    title: Optional[str] = None
    collection: Optional[str] = None
    id: Optional[str] = None
    occurrence_key: Optional[str] = None
```

#### Methods:
- `to_mark()`: Converts link to mark format

## Text Formatting
The library supports various text formatting options through the `MarkType` enum:

```python
class MarkType(Enum):
    CODE = "code"          # Code formatting
    EM = "em"             # Emphasis (italic)
    LINK = "link"         # Hyperlink
    STRIKE = "strike"     # Strikethrough
    STRONG = "strong"     # Bold
    SUBSUP = "subsup"     # Subscript/Superscript
    UNDERLINE = "underline"  # Underline
    TEXT_COLOR = "textColor"  # Text color
```

## Tables
Tables can be configured with different layouts and display modes:

```python
class TableLayout(Enum):
    CENTER = "center"
    ALIGN_START = "align-start"

class TableDisplayMode(Enum):
    DEFAULT = "default"
    FIXED = "fixed"
```

## Examples

### Creating a Document with Multiple Elements

```python
from adf_lib import ADF, Text, Table, Link
from adf_lib.constants.enums import HeadingLevel, TableLayout

# Create document
doc = ADF()

# Add heading
doc.add(Text("Project Report").heading(HeadingLevel.H1))

# Add paragraph with formatting
doc.add(Text("Executive Summary", "strong").paragraph())

# Add link
link = Link(href="https://example.com", title="More Info")
doc.add(Text("See details here", link.to_mark()).paragraph())

# Create table
table = Table(
    width=100,
    is_number_column_enabled=True,
    layout=TableLayout.CENTER
)

# Add table header
table.add_row([
    table.header([Text("Category").paragraph()]),
    table.header([Text("Value").paragraph()])
])

# Add table data
table.add_row([
    table.cell([Text("Revenue").paragraph()]),
    table.cell([Text("$100,000").paragraph()])
])

# Add table to document
doc.add(table.to_dict())

# Convert to dictionary
result = doc.to_dict()
```

### Advanced Text Formatting

```python
# Multiple formatting marks
doc.add(Text("Important Notice", "strong", "underline").paragraph())

# Colored text
doc.add(Text("Warning", {"type": "textColor", "attrs": {"color": "#FF0000"}}).paragraph())

# Combined formatting
doc.add(Text("Critical Update", "strong", "em", {"type": "textColor", "attrs": {"color": "#FF0000"}}).paragraph())
```

## Error Handling
The library includes custom exceptions for validation:

```python
from adf_lib.exceptions.validation import ValidationError, RequiredFieldError, InvalidMarkError

try:
    Text("").paragraph()  # Empty text
except RequiredFieldError:
    print("Text content is required")

try:
    Text("Hello", "invalid_mark").paragraph()  # Invalid mark
except InvalidMarkError:
    print("Invalid mark type")
```

## Best Practices

1. **Document Structure**
   - Start documents with a heading
   - Use appropriate heading levels (H1 -> H6)
   - Group related content in sections

2. **Text Formatting**
   - Use semantic formatting (e.g., `strong` for importance)
   - Avoid overusing text colors
   - Combine marks judiciously

3. **Tables**
   - Use headers for better structure
   - Keep tables simple and readable
   - Use appropriate widths for content

4. **Error Handling**
   - Always handle potential exceptions
   - Validate user input before creating elements
   - Check required fields