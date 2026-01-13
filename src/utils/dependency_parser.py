"""
Utility to parse dependency files and extract file paths.
"""

import re
from pathlib import Path
from typing import Set

from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def parse_dependency_file(dependency_file: str | Path) -> list[str]:
    """
    Parse a dependency file and extract all file paths.

    The dependency file format can be:
    - Plain text with file paths (one per line or in sections)
    - Paths may be absolute or relative
    - May contain comments or section headers

    Args:
        dependency_file: Path to the dependency file

    Returns:
        List of file paths extracted from the dependency file
    """
    dependency_file = Path(dependency_file)

    if not dependency_file.exists():
        logger.warning("Dependency file not found", file=str(dependency_file))
        return []

    content = dependency_file.read_text(encoding="utf-8")
    paths: Set[str] = set()

    # Pattern to match file paths (handles various formats)
    # Matches paths like:
    # - src/main/java/options/le07.java
    # - /absolute/path/to/file.java
    # - file.java (simple filename)
    path_pattern = re.compile(
        r"(?:^|\s)([a-zA-Z0-9_\-./\\]+\.(?:java|sql|form|xml|properties|py|js|ts|cs|tsx))(?:\s|$)",
        re.MULTILINE,
    )

    # Also match paths in lines that look like file paths
    for line in content.splitlines():
        line = line.strip()

        # Skip empty lines, comments, and section headers
        if (
            not line
            or line.startswith("#")
            or line.startswith("=")
            or line.startswith("-")
            or line.upper().startswith("SECTION")
            or line.upper().startswith("END")
            or ":" in line and not "/" in line  # Likely a section header like "1. MAIN FORM FILES"
        ):
            continue

        # Check if line contains a file path
        matches = path_pattern.findall(line)
        for match in matches:
            # Clean up the path
            path = match.strip()
            # Remove leading/trailing quotes if present
            path = path.strip('"\'')
            # Normalize path separators
            path = path.replace("\\", "/")
            # Remove leading slash if present (to make it relative)
            if path.startswith("/"):
                path = path[1:]
            if path:
                paths.add(path)

        # If the line itself looks like a path, add it
        if "/" in line or line.endswith((".java", ".sql", ".form", ".xml", ".properties")):
            # Check if it's not a section header or description text
            if (
                not re.match(r"^\d+\.", line)
                and not line.startswith("=")
                and not line.startswith("This")
                and not line.startswith("The")
                and not "contains" in line.lower()
                and not "handles" in line.lower()
                and len(line.split()) < 10  # Avoid long descriptive text
            ):
                cleaned = line.strip('"\'')
                cleaned = cleaned.replace("\\", "/")
                if cleaned.startswith("/"):
                    cleaned = cleaned[1:]
                # Only add if it looks like a file path (has extension or directory structure)
                if cleaned and (
                    cleaned.endswith((".java", ".sql", ".form", ".xml", ".properties", ".py", ".js", ".ts"))
                    or ("/" in cleaned and "." in cleaned)
                ):
                    paths.add(cleaned)

    paths_list = sorted(list(paths))
    logger.info(
        "Parsed dependency file",
        file=str(dependency_file),
        total_paths=len(paths_list),
    )

    return paths_list


def normalize_path_for_matching(path: str, zip_root: Path | None = None) -> str:
    """
    Normalize a path for matching against extracted files.

    Args:
        path: Path to normalize
        zip_root: Optional root directory of the zip (to make paths relative)

    Returns:
        Normalized path string
    """
    # Normalize separators
    normalized = path.replace("\\", "/")
    # Remove leading slash
    if normalized.startswith("/"):
        normalized = normalized[1:]
    # If zip_root is provided and path is absolute, make it relative
    if zip_root and Path(normalized).is_absolute():
        try:
            normalized = str(Path(normalized).relative_to(zip_root))
        except ValueError:
            # Path is not under zip_root, keep as is
            pass
    return normalized


def match_file_path(file_path: Path, dependency_paths: list[str], extract_root: Path) -> bool:
    """
    Check if a file path matches any of the dependency paths.

    Args:
        file_path: Path to the file (absolute or relative to extract_root)
        dependency_paths: List of dependency paths to match against
        extract_root: Root directory where files were extracted

    Returns:
        True if the file matches any dependency path
    """
    # Get relative path from extract root
    try:
        relative_path = file_path.relative_to(extract_root)
    except ValueError:
        # File is not under extract_root, use filename only
        relative_path = Path(file_path.name)

    # Normalize the relative path
    normalized_relative = str(relative_path).replace("\\", "/")

    # Check against each dependency path
    for dep_path in dependency_paths:
        normalized_dep = normalize_path_for_matching(dep_path)

        # Match by full path
        if normalized_relative == normalized_dep:
            return True

        # Match by filename if dependency path is just a filename
        if "/" not in normalized_dep and file_path.name == normalized_dep:
            return True

        # Match by path ending (handles cases where zip structure differs)
        if normalized_relative.endswith(normalized_dep) or normalized_dep.endswith(normalized_relative):
            return True

        # Match by filename component
        if Path(normalized_dep).name == file_path.name:
            return True

    return False

