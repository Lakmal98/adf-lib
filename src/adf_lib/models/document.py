from typing import TYPE_CHECKING, Any, List, Mapping, Union
from dataclasses import dataclass, field

from ._serialization import to_adf_content, validate_adf_content

if TYPE_CHECKING:
    from .node import Node
    from .table import Table


@dataclass
class ADF:
    """
    Represents an ADF document.

    Attributes:
        version: The ADF version number
        type: The document type
        content: List of content elements
    """

    version: int = 1
    type: str = "doc"
    content: List[Union[Mapping[str, Any], "Node", "Table"]] = field(default_factory=list)

    def add(self, content: Union[Mapping[str, Any], "Node", "Table"]) -> None:
        """
        Adds content to the document.

        Args:
            content: The content element to add
        """
        validate_adf_content(content)
        self.content.append(content)

    def to_dict(self) -> dict:
        """
        Converts the document to a dictionary format.

        Returns:
            dict: The complete ADF document
        """
        return {
            "version": self.version,
            "type": self.type,
            "content": [to_adf_content(item) for item in self.content],
        }
