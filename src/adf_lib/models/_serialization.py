from collections.abc import Mapping
from typing import Any


def _supported_types():
    from .node import Node
    from .table import Table

    return (Mapping, Node, Table)


def validate_adf_content(item: Any) -> None:
    """Validate supported ADF content inputs."""
    if isinstance(item, _supported_types()):
        return

    raise TypeError(
        "ADF content items must be serialized ADF dictionaries, Node instances, or Table instances"
    )


def to_adf_content(item: Any) -> dict:
    """Serialize supported ADF content inputs to dictionaries."""
    validate_adf_content(item)
    return dict(item) if isinstance(item, Mapping) else item.to_dict()
