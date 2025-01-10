import pytest
from adf_lib import HeadingLevel, Text
from adf_lib.exceptions.validation import InvalidMarkError, RequiredFieldError


def test_text_initialization():
    """Test basic text initialization."""
    text = Text("Sample text")
    assert text.text == "Sample text"
    assert text.marks == ()


def test_text_with_marks():
    """Test text initialization with marks."""
    text = Text("Sample text", "strong", "em")
    assert text.text == "Sample text"
    assert len(text.marks) == 2


def test_empty_text():
    """Test text initialization with empty string."""
    with pytest.raises(RequiredFieldError):
        Text("")


def test_invalid_mark():
    """Test text with invalid mark."""
    with pytest.raises(InvalidMarkError):
        Text("Sample text", "invalid_mark").paragraph()


def test_heading_creation():
    """Test creating heading."""
    text = Text("Heading")
    heading = text.heading(HeadingLevel.H1)
    assert heading["type"] == "heading"
    assert heading["attrs"]["level"] == 1
    assert len(heading["content"]) == 1


def test_heading_with_local_id():
    """Test creating heading with local ID."""
    text = Text("Heading")
    heading = text.heading(HeadingLevel.H1, local_id="test-id")
    assert heading["attrs"]["localId"] == "test-id"


def test_paragraph_creation():
    """Test creating paragraph."""
    text = Text("Paragraph")
    paragraph = text.paragraph()
    assert paragraph["type"] == "paragraph"
    assert len(paragraph["content"]) == 1


def test_paragraph_with_marks():
    """Test creating paragraph with multiple marks."""
    text = Text("Paragraph", "strong", "em")
    paragraph = text.paragraph()
    content = paragraph["content"][0]
    assert len(content["marks"]) == 2
    mark_types = [mark["type"] for mark in content["marks"]]
    assert "strong" in mark_types
    assert "em" in mark_types


def test_complex_formatting():
    """Test text with complex formatting."""
    color_mark = {"type": "textColor", "attrs": {"color": "#FF0000"}}
    text = Text("Complex", "strong", color_mark)
    paragraph = text.paragraph()
    content = paragraph["content"][0]
    assert len(content["marks"]) == 2
    assert any(mark["type"] == "textColor" for mark in content["marks"])
    assert any(mark["type"] == "strong" for mark in content["marks"])
