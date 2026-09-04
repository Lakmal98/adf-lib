# Examples

## Build common ADF content

```python
from adf_lib import ADF, Link, Table, Text

doc = ADF()
doc.add(Text("Weekly Update").heading())
doc.add(Text("Everything looks healthy.").paragraph())

link = Link(href="https://status.example.com", title="Status page")
doc.add(Text("Open the status page", link.to_mark()).paragraph())

table = Table(width=100)
table.add_row(
    [
        table.header([Text("Service").paragraph()]),
        table.header([Text("State").paragraph()]),
    ]
)
table.add_row(
    [
        table.cell([Text("Search").paragraph()]),
        table.cell([Text("Operational").paragraph()]),
    ]
)
doc.add(table.to_dict())
```

## Build newer schema nodes with `Node`

```python
from adf_lib import Mark, Node, NodeType, Text

panel = Node(
    NodeType.PANEL,
    attrs={"panelType": "note"},
    content=[Text("Remember to rotate the credentials.").paragraph()],
)

bullet_list = Node(
    NodeType.BULLET_LIST,
    content=[
        Node(
            NodeType.LIST_ITEM,
            content=[
                Node(
                    NodeType.PARAGRAPH,
                    content=[Node(NodeType.TEXT, text="Create the change request")],
                )
            ],
        ),
        Node(
            NodeType.LIST_ITEM,
            content=[
                Node(
                    NodeType.PARAGRAPH,
                    content=[Node(NodeType.TEXT, text="Validate the deployment")],
                )
            ],
        ),
    ],
)

highlighted_text = Node(
    NodeType.TEXT,
    text="Needs follow up",
    marks=[Mark("backgroundColor", {"color": "#FFFAE6"})],
)
```
