"""
Utility to parse dependency files and extract file paths from MinIO.
"""

import re
from pathlib import Path

from src.utils.logging_config import get_logger
from src.utils.minio_sync import MinioSync

logger = get_logger(__name__)


def parse_dependency_file(form_name: str, bucket: str | None = None) -> list[str]:
    """
    Parse a dependency file from MinIO and extract all file paths.

    Looks for: FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/{FORM_NAME}_dependencies.txt

    The dependency file format can be:
    - Plain text with file paths (one per line or in sections)
    - Paths may be absolute or relative
    - May contain comments or section headers

    Args:
        form_name: Form identifier (e.g., "le07", "LE11")
        bucket: Optional MinIO bucket name (defaults to configured bucket)

    Returns:
        List of file paths extracted from the dependency file
    """
    form_name_lower = form_name.lower()
    form_name_upper = form_name.upper()
    
    # Use default bucket (metadatas) if not specified
    minio_sync = MinioSync(bucket=bucket)  # bucket=None uses default "metadatas" from settings
    dependency_object_name = f"FORMS/{form_name_upper}/FORM_FILE_DEPENDENCIES/{form_name_lower}_dependencies.txt"
    
    logger.info("Loading dependencies from MinIO", form_name=form_name, bucket=minio_sync.bucket, object_name=dependency_object_name)
    
    try:
        # bucket=None means use the MinioSync instance's bucket (defaults to "metadatas")
        if not minio_sync.file_exists(dependency_object_name, bucket=None):
            logger.warning("Dependency file not found in MinIO", form_name=form_name, object_name=dependency_object_name, bucket=minio_sync.bucket)
            return []
        
        content = minio_sync.get_file_text(dependency_object_name, bucket=None)
        logger.info("Loaded dependency file from MinIO", form_name=form_name, object_name=dependency_object_name)
    except Exception as e:
        logger.error("Failed to load dependency file from MinIO", form_name=form_name, error=str(e))
        return []
    
    if not content:
        return []
    
    paths: set[str] = set()

    # Pattern to match file paths (handles various formats)
    # Matches paths like:
    # - src/main/java/options/le07.java
    # - src/main/database/baseline/release0/TABLES/chapter_alert_rates.sql
    # - /absolute/path/to/file.java
    # - file.java (simple filename)
    path_pattern = re.compile(
        r"(?:^|\s)([a-zA-Z0-9_\-./\\]+\.(?:java|sql|form|xml|properties|py|js|ts|cs|tsx|jsx|tsx))(?:\s|$)",
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
            or (
                line.startswith("-")
                and not line.endswith((".java", ".sql", ".form", ".xml", ".properties"))
            )
            or line.upper().startswith("SECTION")
            or line.upper().startswith("END")
            or (line.upper().startswith("EXTERNAL") and "DEPENDENCIES" in line.upper())
            or (
                ":" in line and "/" not in line and not line.endswith((".java", ".sql", ".form"))
            )  # Section header
        ):
            continue

        # Check if line contains a file path
        matches = path_pattern.findall(line)
        for match in matches:
            # Clean up the path
            path = match.strip()
            # Remove leading/trailing quotes if present
            path = path.strip("\"'")
            # Normalize path separators
            path = path.replace("\\", "/")
            # Remove leading slash if present (to make it relative)
            if path.startswith("/"):
                path = path[1:]
            if path:
                paths.add(path)

        # If the line itself looks like a path, add it
        # This handles lines that are just file paths without other text
        if "/" in line or line.endswith(
            (".java", ".sql", ".form", ".xml", ".properties", ".py", ".js", ".ts", ".jsx", ".tsx")
        ):
            # Check if it's not a section header or description text
            if (
                not re.match(r"^\d+\.", line)
                and not line.startswith("=")
                and not line.startswith("This")
                and not line.startswith("The")
                and not line.startswith("Field")
                and not line.startswith("The following")
                and "contains" not in line.lower()
                and "handles" not in line.lower()
                and "used" not in line.lower()
                or line.endswith((".java", ".sql", ".form"))  # Allow if it's a file path
                and len(line.split()) < 15  # Allow slightly longer lines for SQL paths
            ):
                cleaned = line.strip("\"'")
                cleaned = cleaned.replace("\\", "/")
                if cleaned.startswith("/"):
                    cleaned = cleaned[1:]
                # Only add if it looks like a file path (has extension or directory structure)
                if cleaned and (
                    cleaned.endswith(
                        (
                            ".java",
                            ".sql",
                            ".form",
                            ".xml",
                            ".properties",
                            ".py",
                            ".js",
                            ".ts",
                            ".jsx",
                            ".tsx",
                        )
                    )
                    or ("/" in cleaned and "." in cleaned and ":" not in cleaned)
                ):
                    paths.add(cleaned)

    paths_list = sorted(list(paths))
    logger.info(
        "Parsed dependency file",
        form_name=form_name,
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

    # Remove common ZIP extraction prefixes (e.g., "oases-master/", "java/")
    # This handles cases where ZIP contains a root folder
    normalized_relative_clean = normalized_relative
    for prefix in ["oases-master/", "java/", "src/"]:
        if normalized_relative_clean.startswith(prefix):
            normalized_relative_clean = normalized_relative_clean[len(prefix) :]
            break

    # Check against each dependency path
    for dep_path in dependency_paths:
        normalized_dep = normalize_path_for_matching(dep_path)

        # Match by full path (try both with and without prefix)
        if normalized_relative == normalized_dep or normalized_relative_clean == normalized_dep:
            return True

        # Match by path ending (handles cases where zip structure differs)
        # e.g., "oases-master/src/main/java/options/le11.java" matches "src/main/java/options/le11.java"
        if normalized_relative.endswith(normalized_dep) or normalized_relative_clean.endswith(
            normalized_dep
        ):
            return True
        if normalized_dep.endswith(normalized_relative) or normalized_dep.endswith(
            normalized_relative_clean
        ):
            return True

        # Match by filename if dependency path is just a filename
        if "/" not in normalized_dep and file_path.name == normalized_dep:
            return True

        # Match by filename component (last part of path)
        dep_filename = Path(normalized_dep).name
        if dep_filename and dep_filename == file_path.name:
            return True

    return False
