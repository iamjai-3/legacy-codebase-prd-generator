"""
Side-channel data exchange for Temporal activities.

Large payloads (documents, base64 images) are written to local JSON files
instead of being returned as activity results.  This avoids the 4 MB gRPC
message-size limit imposed by the Temporal server.

Typical usage
-------------
**Producer activity** (extraction):

    from src.utils.activity_data import save_activity_data

    path = save_activity_data(form_name, "existing_prd", large_dict)
    return {"success": True, "_data_file": str(path), ...lightweight metadata...}

**Consumer activity** (vector storage):

    from src.utils.activity_data import load_activity_data

    data = load_activity_data(result.get("_data_file"))
"""

import base64
import json
import os
from pathlib import Path
from typing import Any

from src.utils.logging_config import get_logger

logger = get_logger(__name__)

_DATA_DIR = Path(".tmp/activity_data")


class _BytesEncoder(json.JSONEncoder):
    """JSON encoder that base64-encodes ``bytes`` values."""

    def default(self, o: Any) -> Any:
        if isinstance(o, bytes):
            return base64.b64encode(o).decode("ascii")
        return super().default(o)


def _ensure_dir() -> Path:
    """Create the scratch directory if it doesn't exist."""
    _DATA_DIR.mkdir(parents=True, exist_ok=True)
    return _DATA_DIR


def save_activity_data(form_name: str, label: str, data: dict[str, Any]) -> Path:
    """Persist *data* to a temp JSON file and return its path.

    Parameters
    ----------
    form_name:
        Used as part of the filename for easy identification.
    label:
        A short tag (e.g. ``"existing_prd"``, ``"db_prd"``, ``"screenshots"``).
    data:
        The full activity result dict to persist.

    Returns
    -------
    Path to the written file.

    Notes
    -----
    ``bytes`` values (e.g. ``image_data``) are base64-encoded so that
    downstream ``_restore_image_data`` can decode them transparently.
    """
    directory = _ensure_dir()
    path = directory / f"{form_name}_{label}.json"
    path.write_text(json.dumps(data, cls=_BytesEncoder), encoding="utf-8")
    logger.info(
        "Saved activity data to side-channel file",
        path=str(path),
        size_bytes=path.stat().st_size,
    )
    return path


def load_activity_data(file_path: str | None) -> dict[str, Any] | None:
    """Load a previously saved activity data file.

    Returns ``None`` when *file_path* is falsy or the file doesn't exist.
    """
    if not file_path:
        return None

    path = Path(file_path)
    if not path.exists():
        logger.warning("Activity data file not found", path=str(path))
        return None

    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    logger.info("Loaded activity data from side-channel file", path=str(path))
    return data


def cleanup_activity_data(form_name: str) -> None:
    """Remove all side-channel files for a given form."""
    if not _DATA_DIR.exists():
        return
    for f in _DATA_DIR.glob(f"{form_name}_*.json"):
        try:
            os.unlink(f)
            logger.debug("Cleaned up activity data file", path=str(f))
        except OSError as e:
            logger.warning("Failed to clean up activity data file", path=str(f), error=str(e))
