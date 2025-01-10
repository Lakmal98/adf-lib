from typing import List, Optional, Union
from ..constants.enums import ContentType, TableLayout, TableDisplayMode


class Table:
    """
    Represents a table in the ADF document.

    Attributes:
        width: The width of the table
        is_number_column_enabled: Whether to show numbered columns
        layout: The table layout style
        display_mode: The table display mode
    """

    def __init__(
        self,
        width: int,
        is_number_column_enabled: bool = False,
        layout: Union[str, TableLayout] = TableLayout.CENTER,
        display_mode: Union[str, TableDisplayMode] = TableDisplayMode.DEFAULT,
    ):
        self.width = width
        self.is_number_column_enabled = is_number_column_enabled
        self.layout = layout.value if isinstance(layout, TableLayout) else layout
        self.display_mode = (
            display_mode.value
            if isinstance(display_mode, TableDisplayMode)
            else display_mode
        )
        self.rows: List[dict] = []

    def _create_cell(
        self, cell_type: str, content: List[dict], col_span: int = 1, row_span: int = 1
    ) -> dict:
        """
        Creates a table cell (header or regular cell).

        Args:
            cell_type: The type of cell ("tableHeader" or "tableCell")
            content: The cell content
            col_span: Number of columns the cell spans
            row_span: Number of rows the cell spans

        Returns:
            dict: The cell in ADF format
        """
        return {
            "type": cell_type,
            "attrs": {"colspan": col_span, "rowspan": row_span},
            "content": content,
        }

    def header(self, content: List[dict], col_span: int = 1, row_span: int = 1) -> dict:
        """Creates a table header cell."""
        return self._create_cell("tableHeader", content, col_span, row_span)

    def cell(self, content: List[dict], col_span: int = 1, row_span: int = 1) -> dict:
        """Creates a regular table cell."""
        return self._create_cell("tableCell", content, col_span, row_span)

    def add_row(self, cells: List[dict]) -> None:
        """Adds a row to the table."""
        self.rows.append({"type": "tableRow", "content": cells})

    def to_dict(self) -> dict:
        """
        Converts the table to ADF format.

        Returns:
            dict: The table in ADF format
        """
        return {
            "type": ContentType.TABLE.value,
            "attrs": {
                "isNumberColumnEnabled": self.is_number_column_enabled,
                "layout": self.layout,
                "width": self.width,
                "displayMode": self.display_mode,
            },
            "content": self.rows,
        }
