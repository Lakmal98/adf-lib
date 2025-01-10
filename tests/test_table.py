from adf_lib import Table, TableDisplayMode, TableLayout, Text


def test_table_initialization():
    """Test basic table initialization."""
    table = Table(width=100)
    assert table.width == 100
    assert table.is_number_column_enabled is False
    assert table.layout == TableLayout.CENTER.value
    assert table.display_mode == TableDisplayMode.DEFAULT.value


def test_table_custom_initialization():
    """Test table initialization with custom values."""
    table = Table(
        width=50,
        is_number_column_enabled=True,
        layout=TableLayout.ALIGN_START,
        display_mode=TableDisplayMode.FIXED,
    )
    assert table.width == 50
    assert table.is_number_column_enabled is True
    assert table.layout == TableLayout.ALIGN_START.value
    assert table.display_mode == TableDisplayMode.FIXED.value


def test_table_header_creation():
    """Test creating table header."""
    table = Table(width=100)
    header = table.header([Text("Test").paragraph()])
    assert header["type"] == "tableHeader"
    assert header["attrs"]["colspan"] == 1
    assert header["attrs"]["rowspan"] == 1
    assert len(header["content"]) == 1


def test_table_cell_creation():
    """Test creating table cell."""
    table = Table(width=100)
    cell = table.cell([Text("Test").paragraph()])
    assert cell["type"] == "tableCell"
    assert cell["attrs"]["colspan"] == 1
    assert cell["attrs"]["rowspan"] == 1
    assert len(cell["content"]) == 1


def test_table_add_row():
    """Test adding row to table."""
    table = Table(width=100)
    cells = [
        table.cell([Text("Cell 1").paragraph()]),
        table.cell([Text("Cell 2").paragraph()]),
    ]
    table.add_row(cells)
    assert len(table.rows) == 1
    assert len(table.rows[0]["content"]) == 2


def test_table_to_dict():
    """Test converting table to dictionary."""
    table = Table(width=100)
    table.add_row(
        [
            table.header([Text("Header").paragraph()]),
            table.cell([Text("Content").paragraph()]),
        ]
    )

    table_dict = table.to_dict()
    assert table_dict["type"] == "table"
    assert table_dict["attrs"]["width"] == 100
    assert len(table_dict["content"]) == 1
