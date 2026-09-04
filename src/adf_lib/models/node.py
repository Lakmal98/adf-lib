from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Mapping, Optional, Union

from ..constants.enums import NodeType
from ..exceptions.validation import InvalidNodeError, RequiredFieldError
from ._serialization import to_adf_content, validate_adf_content
from .mark import Mark, normalize_marks

if TYPE_CHECKING:
    from .table import Table


@dataclass
class Node:
    """Represents a generic ADF node."""

    type: Union[str, NodeType]
    attrs: Optional[Dict[str, Any]] = None
    content: Optional[List[Union[Mapping[str, Any], "Node", "Table"]]] = None
    text: Optional[str] = None
    marks: List[Union[str, dict, Mark]] = field(default_factory=list)

    def __post_init__(self):
        node_type = self.type.value if isinstance(self.type, NodeType) else self.type

        if node_type not in {item.value for item in NodeType}:
            raise InvalidNodeError(f"Invalid node type: {self.type}")

        if node_type == NodeType.TEXT.value and self.text is None:
            raise RequiredFieldError("text is required for text nodes")

        if self.content is not None:
            for item in self.content:
                validate_adf_content(item)

        self.type = node_type

    def to_dict(self) -> dict:
        node = {"type": self.type}

        if self.attrs is not None:
            node["attrs"] = self.attrs

        if self.marks:
            node["marks"] = normalize_marks(self.marks)

        if self.type == NodeType.TEXT.value:
            node["text"] = self.text
            return node

        if self.content is not None:
            node["content"] = [to_adf_content(item) for item in self.content]

        return node
