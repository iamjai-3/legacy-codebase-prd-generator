"""
File utility functions for handling code files, archives, and documents.
"""

import json
import zipfile
from pathlib import Path
from typing import Any

from src.utils.logging_config import get_logger

logger = get_logger(__name__)

# Code file extensions we support
CODE_EXTENSIONS = {
    ".java",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".cs",
    ".cpp",
    ".c",
    ".h",
    ".hpp",
    ".sql",
    ".xml",
    ".json",
    ".yaml",
    ".yml",
    ".html",
    ".css",
    ".scss",
    ".less",
    ".form",
    ".properties",
    ".config",
}


def ensure_directory(path: str | Path) -> Path:
    """
    Ensure a directory exists, creating it if necessary.

    Args:
        path: Directory path to ensure exists

    Returns:
        Path object of the directory
    """
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def get_file_extension(file_path: str | Path) -> str:
    """Get the file extension in lowercase."""
    return Path(file_path).suffix.lower()


def is_code_file(file_path: str | Path) -> bool:
    """Check if a file is a recognized code file."""
    path = Path(file_path)
    # Ignore Mac OS metadata files
    if path.name.startswith("._"):
        return False
    return get_file_extension(path) in CODE_EXTENSIONS


def extract_zip(
    zip_path: str | Path, extract_to: str | Path, filter_extensions: set[str] | None = None
) -> list[Path]:
    """
    Extract a ZIP file to a directory.

    Args:
        zip_path: Path to the ZIP file
        extract_to: Directory to extract files to
        filter_extensions: Optional set of extensions to filter (e.g., {'.java', '.py'})

    Returns:
        List of extracted file paths
    """
    zip_path = Path(zip_path)
    extract_to = ensure_directory(extract_to)
    extracted_files: list[Path] = []

    logger.info("Extracting ZIP file", zip_path=str(zip_path), extract_to=str(extract_to))

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for file_info in zip_ref.infolist():
            # Skip directories
            if file_info.is_dir():
                continue

            # Skip Mac OS metadata files and directories
            if "__MACOSX" in file_info.filename or Path(file_info.filename).name.startswith("._"):
                continue

            # Apply extension filter if provided
            if filter_extensions:
                ext = get_file_extension(file_info.filename)
                if ext not in filter_extensions:
                    continue

            # Extract the file
            zip_ref.extract(file_info, extract_to)
            extracted_path = extract_to / file_info.filename
            extracted_files.append(extracted_path)

    logger.info("ZIP extraction complete", file_count=len(extracted_files))
    return extracted_files


def read_file_content(file_path: str | Path, encoding: str = "utf-8") -> str:
    """
    Read file content with proper encoding handling.

    Args:
        file_path: Path to the file
        encoding: Text encoding to use

    Returns:
        File content as string
    """
    file_path = Path(file_path)

    try:
        return file_path.read_text(encoding=encoding)
    except UnicodeDecodeError:
        # Try with latin-1 as fallback
        logger.warning("UTF-8 decode failed, trying latin-1", file_path=str(file_path))
        return file_path.read_text(encoding="latin-1")


def write_json(file_path: str | Path, data: Any, indent: int = 2) -> None:
    """
    Write data to a JSON file.

    Args:
        file_path: Path to write to
        data: Data to serialize as JSON
        indent: JSON indentation level
    """
    file_path = Path(file_path)
    ensure_directory(file_path.parent)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False, default=str)

    logger.debug("JSON file written", file_path=str(file_path))


def read_json(file_path: str | Path) -> Any:
    """
    Read and parse a JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        Parsed JSON data
    """
    file_path = Path(file_path)

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def find_files_by_pattern(
    directory: str | Path, patterns: list[str], recursive: bool = True
) -> list[Path]:
    """
    Find files matching given patterns in a directory.

    Args:
        directory: Directory to search
        patterns: List of glob patterns (e.g., ['*.java', '*.py'])
        recursive: Whether to search recursively

    Returns:
        List of matching file paths
    """
    directory = Path(directory)
    matching_files: list[Path] = []

    for pattern in patterns:
        if recursive:
            matching_files.extend(directory.rglob(pattern))
        else:
            matching_files.extend(directory.glob(pattern))

    return sorted(set(matching_files))


def get_relative_path(file_path: str | Path, base_path: str | Path) -> str:
    """Get the relative path from base_path to file_path."""
    return str(Path(file_path).relative_to(Path(base_path)))


def calculate_file_hash(file_path: str | Path) -> str:
    """Calculate SHA256 hash of a file."""
    import hashlib

    file_path = Path(file_path)
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)

    return sha256.hexdigest()
