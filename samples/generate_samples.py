import json
from pathlib import Path
from typing import Dict, List

from adf_lib import ADF, Link, Mark, Node, NodeType, Table, Text


def basic_document() -> ADF:
    document = ADF()
    document.add(Text("ADF sample document").heading(1))
    document.add(Text("This paragraph contains ", "strong").paragraph())
    document.add(Text("formatted text", "strong", "em").paragraph())
    return document


def rich_document() -> ADF:
    document = ADF()
    document.add(
        Text(
            "Open the Atlassian ADF documentation",
            Link(href="https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/").to_mark(),
        ).paragraph()
    )
    document.add(
        Node(
            NodeType.PANEL,
            attrs={"panelType": "info"},
            content=[Text("Review this panel in Atlassian.").paragraph()],
        )
    )
    document.add(
        Node(
            NodeType.BULLET_LIST,
            content=[
                Node(
                    NodeType.LIST_ITEM,
                    content=[
                        Node(
                            NodeType.PARAGRAPH,
                            content=[
                                Node(
                                    NodeType.TEXT,
                                    text="Strong and highlighted",
                                    marks=[
                                        "strong",
                                        Mark("backgroundColor", {"color": "#FFF0B3"}),
                                    ],
                                )
                            ],
                        )
                    ],
                )
            ],
        )
    )
    return document


def table_document() -> ADF:
    document = ADF()
    document.add(Text("Service status").heading(2))

    table = Table(width=100)
    table.add_row(
        [
            table.header([Text("Service").paragraph()]),
            table.header([Text("Status").paragraph()]),
        ]
    )
    table.add_row(
        [
            table.cell([Text("Search").paragraph()]),
            table.cell([Text("Operational").paragraph()]),
        ]
    )
    document.add(table)
    return document


def sample_documents() -> Dict[str, ADF]:
    return {
        "basic.json": basic_document(),
        "rich.json": rich_document(),
        "table.json": table_document(),
    }


def generate_samples(output_dir: Path = Path(__file__).parent / "generated") -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    generated_files = []

    for filename, document in sample_documents().items():
        output_file = output_dir / filename
        output_file.write_text(
            json.dumps(document.to_dict(), indent=2) + "\n",
            encoding="utf-8",
        )
        generated_files.append(output_file)

    return generated_files


if __name__ == "__main__":
    for sample_file in generate_samples():
        print(sample_file)