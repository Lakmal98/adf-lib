from adf_lib import ADF, HeadingLevel, Text

def test_document_initialization():
    """Test document initialization with default values."""
    doc = ADF()
    assert doc.version == 1
    assert doc.type == "doc"
    assert doc.content == []

def test_document_custom_initialization():
    """Test document initialization with custom values."""
    doc = ADF(version=2, type="custom")
    assert doc.version == 2
    assert doc.type == "custom"

def test_document_add_content(empty_document):
    """Test adding content to document."""
    content = Text("Test").paragraph()
    empty_document.add(content)
    assert len(empty_document.content) == 1
    assert empty_document.content[0] == content

def test_document_to_dict(sample_document):
    """Test converting document to dictionary."""
    doc_dict = sample_document.to_dict()
    assert isinstance(doc_dict, dict)
    assert "version" in doc_dict
    assert "type" in doc_dict
    assert "content" in doc_dict
    assert len(doc_dict["content"]) == 2

def test_document_multiple_content_types(empty_document, sample_table):
    """Test adding multiple content types to document."""
    empty_document.add(Text("Heading").heading(HeadingLevel.H1))
    empty_document.add(Text("Paragraph").paragraph())
    empty_document.add(sample_table.to_dict())
    
    doc_dict = empty_document.to_dict()
    assert len(doc_dict["content"]) == 3
    assert doc_dict["content"][0]["type"] == "heading"
    assert doc_dict["content"][1]["type"] == "paragraph"
    assert doc_dict["content"][2]["type"] == "table"