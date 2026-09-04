from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from ..constants.enums import NodeType
from ..exceptions.validation import InvalidNodeError, RequiredFieldError
from .mark import Mark, normalize_marks


@dataclass
class Node:
    """Represents a generic ADF node."""

    type: Union[str, NodeType]
    attrs: Optional[Dict[str, Any]] = None
    content: List[dict] = field(default_factory=list)
    text: Optional[str] = None
    marks: List[Union[str, dict, Mark]] = field(default_factory=list)

    def __post_init__(self):
        node_type = self.type.value if isinstance(self.type, NodeType) else self.type

        if node_type not in {item.value for item in NodeType}:
            raise InvalidNodeError(f"Invalid node type: {self.type}")

        if node_type == NodeType.TEXT.value and not self.text:
            raise RequiredFieldError("text is required for text nodes")

        self.type = node_type

    def to_dict(self) -> dict:
        node = {"type": self.type}

        if self.attrs:
            node["attrs"] = self.attrs

        if self.type == NodeType.TEXT.value:
            node["text"] = self.text
            if self.marks:
                node["marks"] = normalize_marks(self.marks)
            return node

        if self.content:
            node["content"] = [
                item.to_dict() if hasattr(item, "to_dict") else item for item in self.content
            ]

        return node
