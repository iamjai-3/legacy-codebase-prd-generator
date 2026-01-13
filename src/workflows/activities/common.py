"""Common utilities for Temporal activities."""

from typing import Any

from src.utils.logging_config import get_logger
from src.utils.serialization import to_dict_safe

logger = get_logger(__name__)


def to_dict(obj: Any) -> dict[str, Any]:
    """Safely convert dataclass to dict for serialization."""
    return to_dict_safe(obj)
