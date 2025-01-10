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