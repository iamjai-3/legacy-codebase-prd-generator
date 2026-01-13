"""
Serialization utilities for dataclass to/from dict conversion.

Provides type-safe serialization for Temporal activities and data persistence.
"""

import json
import re
from dataclasses import asdict, fields, is_dataclass
from typing import Any, TypeVar

from src.utils.logging_config import get_logger

logger = get_logger(__name__)

T = TypeVar("T")


def to_dict_safe(obj: Any) -> dict[str, Any]:
    """
    Safely convert an object to a dictionary.

    Handles dataclasses, dicts, and other objects gracefully.

    Args:
        obj: Object to convert

    Returns:
        Dictionary representation
    """
    if obj is None:
        return {}
    if is_dataclass(obj) and not isinstance(obj, type):
        return asdict(obj)
    if isinstance(obj, dict):
        return obj
    return {"value": str(obj)}


def from_dict_safe(data: dict[str, Any] | Any, cls: type[T]) -> T | None:
    """
    Safely reconstruct a dataclass from a dictionary.

    Args:
        data: Dictionary or object to convert
        cls: Target dataclass type

    Returns:
        Reconstructed dataclass instance or None on failure
    """
    if data is None:
        return None

    # If already the correct type, return as-is
    if isinstance(data, cls):
        return data

    if not isinstance(data, dict):
        logger.warning(
            "Cannot reconstruct dataclass from non-dict",
            expected_type=cls.__name__,
            actual_type=type(data).__name__,
        )
        return None

    if not is_dataclass(cls):
        logger.warning("Target class is not a dataclass", cls=cls.__name__)
        return None

    try:
        # Get field names and filter data to only include valid fields
        valid_fields = {f.name for f in fields(cls)}
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        return cls(**filtered_data)
    except Exception as e:
        logger.warning("Failed to reconstruct dataclass", cls=cls.__name__, error=str(e))
        return None


def from_dict_list(data_list: list[dict[str, Any]] | None, cls: type[T]) -> list[T]:
    """
    Reconstruct a list of dataclass instances from a list of dicts.

    Args:
        data_list: List of dictionaries
        cls: Target dataclass type

    Returns:
        List of reconstructed dataclass instances
    """
    if not data_list:
        return []

    results = []
    for item in data_list:
        obj = from_dict_safe(item, cls)
        if obj is not None:
            results.append(obj)
    return results


def extract_json_from_response(response: str) -> dict[str, Any] | list[Any] | None:
    """
    Extract JSON object or array from LLM response text.

    Handles common cases where JSON is embedded in markdown or prose.

    Args:
        response: LLM response text

    Returns:
        Parsed JSON (dict or list) or None if not found
    """
    if not response:
        return None

    # Try to find JSON array first (most common for lists)
    array_match = re.search(r"\[[\s\S]*\]", response)
    if array_match:
        try:
            return json.loads(array_match.group())
        except json.JSONDecodeError:
            pass

    # Try to find JSON object
    object_match = re.search(r"\{[\s\S]*\}", response)
    if object_match:
        try:
            return json.loads(object_match.group())
        except json.JSONDecodeError:
            pass

    # Try parsing the entire response as JSON
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        logger.debug("No valid JSON found in response", response_length=len(response))
        return None


def extract_json_array(response: str) -> list[dict[str, Any]]:
    """
    Extract a JSON array from LLM response, returning empty list on failure.

    Args:
        response: LLM response text

    Returns:
        List of dictionaries (empty if extraction fails)
    """
    result = extract_json_from_response(response)
    if isinstance(result, list):
        return result
    return []


def extract_json_object(response: str) -> dict[str, Any]:
    """
    Extract a JSON object from LLM response, returning empty dict on failure.

    Args:
        response: LLM response text

    Returns:
        Dictionary (empty if extraction fails)
    """
    result = extract_json_from_response(response)
    if isinstance(result, dict):
        return result
    return {}


def parse_list_response(response: str, prefix: str = "") -> list[str]:
    """
    Parse a text response containing a list into individual items.

    Handles various list formats: numbered, bulleted, or prefix-based.

    Args:
        response: Text response to parse
        prefix: Optional prefix to filter lines (e.g., "BR-", "VR-")

    Returns:
        List of extracted items
    """
    if not response:
        return []

    items = []
    for line in response.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Filter by prefix if specified
        if prefix and prefix not in line:
            continue

        # Clean up common list markers
        cleaned = line.lstrip("0123456789.-) •*")
        if cleaned:
            items.append(cleaned.strip())

    return items
