import pytest
from adf_lib import Link

def test_link_initialization():
    """Test basic link initialization."""
    link = Link(href="https://example.com")
    assert link.href == "https://example.com"
    assert link.title is None


def test_link_full_initialization():
    """Test link initialization with all attributes."""
    link = Link(
        href="https://example.com",
        title="Example",
        collection="test",
        id="123",
        occurrence_key="key1",
    )
    assert link.href == "https://example.com"
    assert link.title == "Example"
    assert link.collection == "test"
    assert link.id == "123"
    assert link.occurrence_key == "key1"


def test_link_missing_href():
    """Test link initialization without href."""
    with pytest.raises(ValueError):
        Link(href="")


def test_link_to_mark():
    """Test converting link to mark format."""
    link = Link(href="https://example.com", title="Example")
    mark = link.to_mark()
    assert mark["type"] == "link"
    assert mark["attrs"]["href"] == "https://example.com"
    assert mark["attrs"]["title"] == "Example"


def test_link_to_mark_minimal():
    """Test converting minimal link to mark format."""
    link = Link(href="https://example.com")
    mark = link.to_mark()
    assert mark["type"] == "link"
    assert mark["attrs"]["href"] == "https://example.com"
    assert "title" not in mark["attrs"]
