import pytest
from adf_lib import ADF, Text, Table, Link


@pytest.fixture
def empty_document():
    return ADF()


@pytest.fixture
def sample_document():
    doc = ADF()
    doc.add(Text("Test Document").heading(1))
    doc.add(Text("Sample paragraph").paragraph())
    return doc


@pytest.fixture
def sample_table():
    table = Table(width=100)
    table.add_row(
        [
            table.header([Text("Header 1").paragraph()]),
            table.header([Text("Header 2").paragraph()]),
        ]
    )
    return table


@pytest.fixture
def sample_link():
    return Link(
        href="https://example.com", title="Example Link", collection="test-collection"
    )
