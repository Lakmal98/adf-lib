# ADF Library for Atlassian Document Format

ADF Library is a Python library for building Atlassian Document Format (ADF) JSON documents used by Jira, Confluence, and other Atlassian Cloud products.

## Why use this library?

- Build ADF documents with Python instead of hand-writing JSON
- Use focused helpers for common content such as `Text`, `Table`, and `Link`
- Use generic `Node` and `Mark` builders for the latest published ADF node and mark types
- Export plain dictionaries that can be sent directly to Atlassian APIs

## Who is this for?

This project is for Python developers integrating with Atlassian APIs, automation scripts, issue creation workflows, and content migration pipelines.

## What does it support?

The library supports:

- headings, paragraphs, tables, and links through dedicated helpers
- latest-schema ADF nodes such as lists, panels, code blocks, cards, media, layout, status, and expands through `Node`
- latest-schema ADF marks such as `backgroundColor`, `annotation`, `alignment`, `textColor`, and `link`

## Quick example

```python
from adf_lib import ADF, Node, NodeType, Text

doc = ADF()
doc.add(Text("Incident Summary").heading())
doc.add(
    Node(
        NodeType.BULLET_LIST,
        content=[
            Node(
                NodeType.LIST_ITEM,
                content=[Text("Service restored").paragraph()],
            )
        ],
    )
)
```

## FAQ

### Can I use this for Jira and Confluence?
Yes. The library generates Atlassian Document Format structures that can be used with Atlassian Cloud APIs where ADF is accepted.

### How do I build nodes not covered by helper classes?
Use `Node` with a `NodeType` value and optional `attrs`, `content`, `text`, or `marks`.

### Where can I verify the schema?
See the official Atlassian ADF documentation and schema:

- https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/
- http://go.atlassian.com/adf-json-schema
