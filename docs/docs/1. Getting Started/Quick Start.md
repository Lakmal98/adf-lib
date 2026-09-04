# Quick Start

ADF Library helps you create Atlassian Document Format (ADF) documents for Jira and Confluence with Python.

## Import the core components

```python
from adf_lib import ADF, Link, Mark, Node, NodeType, Table, Text
from adf_lib.constants.enums import HeadingLevel
```

## Create a document

```python
doc = ADF()
```

## Add headings and paragraphs

```python
doc.add(Text("My Document").heading(HeadingLevel.H1))
doc.add(Text("This is a paragraph").paragraph())
doc.add(Text("Bold and italic", "strong", "em").paragraph())
```

## Add links

```python
link = Link(href="https://example.com", title="Example")
doc.add(Text("Open example", link.to_mark()).paragraph())
```

## Add a table

```python
table = Table(width=100)
table.add_row(
    [
        table.header([Text("Name").paragraph()]),
        table.header([Text("Status").paragraph()]),
    ]
)
table.add_row(
    [
        table.cell([Text("Search indexing").paragraph()]),
        table.cell([Text("Healthy").paragraph()]),
    ]
)
doc.add(table.to_dict())
```

## Use the latest ADF nodes

```python
doc.add(
    Node(
        NodeType.PANEL,
        attrs={"panelType": "info"},
        content=[Text("Deployment completed").paragraph()],
    )
)

doc.add(
    Node(
        NodeType.PARAGRAPH,
        content=[
            Node(
                NodeType.TEXT,
                text="Highlighted",
                marks=[Mark("backgroundColor", {"color": "#FFFAE6"})],
            )
        ],
    )
)
```

## Export to a dictionary

```python
adf_dict = doc.to_dict()
```
