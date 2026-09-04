import pytest

from adf_lib import ADF, Mark, MarkType, Node, NodeType
from adf_lib.exceptions.validation import (
    InvalidMarkError,
    InvalidNodeError,
    RequiredFieldError,
)


def test_text_node_to_dict():
    """Text nodes support the latest mark set."""
    node = Node(
        NodeType.TEXT,
        text="Hello world",
        marks=[Mark("backgroundColor", {"color": "#6554C0"}), "strong"],
    )

    assert node.to_dict() == {
        "type": "text",
        "text": "Hello world",
        "marks": [
            {"type": "backgroundColor", "attrs": {"color": "#6554C0"}},
            {"type": "strong"},
        ],
    }


def test_non_text_node_to_dict():
    """Generic nodes can represent unsupported-by-helper ADF structures."""
    node = Node(
        NodeType.BULLET_LIST,
        content=[
            Node(
                NodeType.LIST_ITEM,
                content=[Node(NodeType.PARAGRAPH, content=[Node(NodeType.TEXT, text="Item")])],
            )
        ],
    )

    assert node.to_dict() == {
        "type": "bulletList",
        "content": [
            {
                "type": "listItem",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": "Item"}],
                    }
                ],
            }
        ],
    }


def test_node_includes_attrs():
    """Generic nodes preserve attrs."""
    node = Node(NodeType.PANEL, attrs={"panelType": "warning"})
    assert node.to_dict() == {"type": "panel", "attrs": {"panelType": "warning"}}


def test_node_preserves_explicit_empty_attrs():
    """Explicit empty attrs are serialized."""
    assert Node(NodeType.PANEL, attrs={}).to_dict() == {"type": "panel", "attrs": {}}


def test_node_preserves_explicit_empty_content():
    """Explicit empty content is serialized for container nodes."""
    assert Node(NodeType.PARAGRAPH, content=[]).to_dict() == {
        "type": "paragraph",
        "content": [],
    }


def test_text_node_requires_text():
    """Text nodes require text content."""
    with pytest.raises(RequiredFieldError):
        Node(NodeType.TEXT)


def test_invalid_node_type():
    """Unknown node types are rejected."""
    with pytest.raises(InvalidNodeError):
        Node("not-a-node")


def test_text_node_allows_empty_string():
    """Empty strings are preserved when text is explicitly supplied."""
    assert Node(NodeType.TEXT, text="").to_dict() == {"type": "text", "text": ""}


def test_non_text_node_preserves_marks():
    """Generic nodes preserve marks for schema variants that use them."""
    assert Node(
        NodeType.PARAGRAPH,
        content=[],
        marks=[Mark(MarkType.ALIGNMENT, {"align": "center"})],
    ).to_dict() == {
        "type": "paragraph",
        "marks": [{"type": "alignment", "attrs": {"align": "center"}}],
        "content": [],
    }


def test_document_accepts_node_instances():
    """Documents accept generic node objects directly."""
    doc = ADF()
    rule = Node(NodeType.RULE)
    doc.add(rule)

    assert doc.content == [rule]
    assert doc.to_dict()["content"] == [{"type": "rule"}]


def test_mark_supports_enum_types():
    """Generic marks accept enum values."""
    assert Mark(MarkType.ALIGNMENT, {"align": "center"}).to_dict() == {
        "type": "alignment",
        "attrs": {"align": "center"},
    }


def test_mark_preserves_explicit_empty_attrs():
    """Explicit empty mark attrs are serialized."""
    assert Mark(MarkType.ANNOTATION, {}).to_dict() == {"type": "annotation", "attrs": {}}


def test_mark_rejects_invalid_type():
    """Unknown mark types are rejected."""
    with pytest.raises(InvalidMarkError):
        Mark("not-a-mark").to_dict()


def test_document_rejects_unknown_content_objects():
    """Only supported ADF content objects are serialized."""
    doc = ADF()
    with pytest.raises(TypeError):
        doc.add(object())


@pytest.mark.parametrize(
    ("node_type", "attrs", "content", "expected"),
    [
        (
            NodeType.PANEL,
            {"panelType": "info"},
            [Node(NodeType.PARAGRAPH, content=[Node(NodeType.TEXT, text="Panel body")])],
            {
                "type": "panel",
                "attrs": {"panelType": "info"},
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": "Panel body"}],
                    }
                ],
            },
        ),
        (
            NodeType.ORDERED_LIST,
            None,
            [
                Node(
                    NodeType.LIST_ITEM,
                    content=[Node(NodeType.PARAGRAPH, content=[Node(NodeType.TEXT, text="Step 1")])],
                )
            ],
            {
                "type": "orderedList",
                "content": [
                    {
                        "type": "listItem",
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [{"type": "text", "text": "Step 1"}],
                            }
                        ],
                    }
                ],
            },
        ),
    ],
)
def test_representative_container_nodes_serialize(node_type, attrs, content, expected):
    """Representative populated container nodes serialize correctly."""
    assert Node(node_type, attrs=attrs, content=content).to_dict() == expected


@pytest.mark.parametrize(
    "node_type",
    list(NodeType),
)
def test_all_latest_node_types_can_be_built(node_type):
    """Every latest node enum can be constructed through the generic node API."""
    node = Node(node_type, text="" if node_type is NodeType.TEXT else None)
    assert node.to_dict()["type"] == node_type.value
