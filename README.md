# ADF Library

ADF Library is a Python package for creating, validating, and exporting Atlassian Document Format (ADF) content for Jira, Confluence, and other Atlassian Cloud products.

## Overview

The library provides:

- high-level helpers for headings, paragraphs, tables, and links
- generic `Node` and `Mark` builders for the latest published ADF node and mark types
- plain Python dictionaries that can be sent directly to Atlassian APIs

## Installation

```bash
pip install adf_lib
```

## Quick Start

```python
from adf_lib import ADF, Link, Mark, Node, NodeType, Table, Text
from adf_lib.constants.enums import HeadingLevel

doc = ADF()
doc.add(Text("My Document").heading(HeadingLevel.H1))
doc.add(Text("This is a formatted paragraph", "strong", "em").paragraph())

link = Link(href="https://example.com", title="Example")
doc.add(Text("Open example", link.to_mark()).paragraph())

doc.add(
    Node(
        NodeType.PANEL,
        attrs={"panelType": "info"},
        content=[Text("This uses a latest-schema node").paragraph()],
    )
)

doc.add(
    Node(
        NodeType.PARAGRAPH,
        content=[
            Node(
                NodeType.TEXT,
                text="Highlighted text",
                marks=[Mark("backgroundColor", {"color": "#FFF0B3"})],
            )
        ],
    )
)

adf_dict = doc.to_dict()
```

## Latest ADF Node Coverage

Use `Text`, `Table`, and `Link` for common authoring flows. Use `Node`, `NodeType`, and `Mark` for newer ADF structures such as:

- lists: `bulletList`, `orderedList`, `listItem`
- rich blocks: `codeBlock`, `panel`, `blockquote`, `rule`, `expand`, `nestedExpand`
- smart content: `inlineCard`, `blockCard`, `embedCard`, `status`, `date`, `mention`, `emoji`
- layout and media: `layoutSection`, `layoutColumn`, `media`, `mediaGroup`, `mediaSingle`

This keeps the public API small while allowing the library to emit the latest published ADF node names.

## API Summary

### Core helpers

- `ADF`: document container
- `Text`: heading and paragraph helper
- `Table`: table helper
- `Link`: link mark helper

### Generic schema helpers

- `Node`: generic ADF node builder
- `NodeType`: enum of latest published node names
- `Mark`: generic ADF mark builder
- `MarkType`: enum of latest published mark names

## Documentation

Project documentation is available in `/docs` and published at:

- https://docs.py-adf.lakmal.dev/
- https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/
- http://go.atlassian.com/adf-json-schema
