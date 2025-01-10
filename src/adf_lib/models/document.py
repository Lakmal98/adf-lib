from typing import List
from dataclasses import dataclass, field


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
    content: List[dict] = field(default_factory=list)

    def add(self, content: dict) -> None:
        """
        Adds content to the document.

        Args:
            content: The content element to add
        """
        self.content.append(content)

    def to_dict(self) -> dict:
        """
        Converts the document to a dictionary format.

        Returns:
            dict: The complete ADF document
        """
        return {"version": self.version, "type": self.type, "content": self.content}
