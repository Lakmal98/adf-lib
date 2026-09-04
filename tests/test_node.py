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


def test_text_node_requires_text():
    """Text nodes require text content."""
    with pytest.raises(RequiredFieldError):
        Node(NodeType.TEXT)


def test_invalid_node_type():
    """Unknown node types are rejected."""
    with pytest.raises(InvalidNodeError):
        Node("not-a-node")


def test_document_accepts_node_instances():
    """Documents accept generic node objects directly."""
    doc = ADF()
    doc.add(Node(NodeType.RULE))

    assert doc.to_dict()["content"] == [{"type": "rule"}]


def test_mark_supports_enum_types():
    """Generic marks accept enum values."""
    assert Mark(MarkType.ALIGNMENT, {"align": "center"}).to_dict() == {
        "type": "alignment",
        "attrs": {"align": "center"},
    }


def test_mark_rejects_invalid_type():
    """Unknown mark types are rejected."""
    with pytest.raises(InvalidMarkError):
        Mark("not-a-mark").to_dict()


@pytest.mark.parametrize(
    "node_type",
    [node_type for node_type in NodeType if node_type is not NodeType.TEXT],
)
def test_all_latest_node_types_can_be_built(node_type):
    """Every latest node enum can be constructed through the generic node API."""
    node = Node(node_type)
    assert node.to_dict()["type"] == node_type.value
