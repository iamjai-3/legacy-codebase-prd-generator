"""
Utility to parse dependency files and extract file paths from MinIO.
"""

import re
from pathlib import Path

from src.utils.logging_config import get_logger
from src.utils.minio_sync import MinioSync

logger = get_logger(__name__)


_PATH_EXTENSIONS = (
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
_EXTENSIONS_CODE = (".java", ".sql", ".form")  # subset used for section/path detection
_PATH_PATTERN = re.compile(
    r"(?:^|\s)([a-zA-Z0-9_\-./\\]+\.(?:java|sql|form|xml|properties|py|js|ts|cs|tsx|jsx))(?:\s|$)",
    re.MULTILINE,
)


def _load_dependency_content(minio_sync: MinioSync, object_name: str, form_name: str) -> str | None:
    """Load dependency file content from MinIO; return None on failure or missing."""
    try:
        if not minio_sync.file_exists(object_name, bucket=None):
            logger.warning(
                "Dependency file not found in MinIO",
                form_name=form_name,
                object_name=object_name,
                bucket=minio_sync.bucket,
            )
            return None
        content = minio_sync.get_file_text(object_name, bucket=None)
        logger.info(
            "Loaded dependency file from MinIO",
            form_name=form_name,
            object_name=object_name,
        )
        return content
    except Exception as e:
        logger.error("Failed to load dependency file from MinIO", form_name=form_name, error=str(e))
        return None


def _should_skip_line(line: str) -> bool:
    """Return True if line should be skipped (empty, comment, section header)."""
    if not line or line.startswith("#") or line.startswith("="):
        return True
    if line.startswith("-") and not line.endswith(_PATH_EXTENSIONS):
        return True
    if line.upper().startswith("SECTION") or line.upper().startswith("END"):
        return True
    if line.upper().startswith("EXTERNAL") and "DEPENDENCIES" in line.upper():
        return True
    if ":" in line and "/" not in line and not line.endswith(_EXTENSIONS_CODE):
        return True
    return False


def _normalize_path(path: str) -> str:
    """Strip quotes, normalize separators, remove leading slash."""
    p = path.strip().strip("\"'").replace("\\", "/")
    return p[1:] if p.startswith("/") else p


def _extract_paths_from_pattern(line: str) -> list[str]:
    """Extract and normalize paths from line using path pattern."""
    out = []
    for match in _PATH_PATTERN.findall(line):
        normalized = _normalize_path(match)
        if normalized:
            out.append(normalized)
    return out


def _is_section_or_description(line: str) -> bool:
    """Return True if line looks like a section header or description (not a path)."""
    if re.match(r"^\d+\.", line) or line.startswith("="):
        return True
    if line.startswith(("This", "The", "Field", "The following")):
        return True
    if any(kw in line.lower() for kw in ("contains", "handles", "used")):
        return True
    if len(line.split()) >= 15 and not line.endswith(_EXTENSIONS_CODE):
        return True
    return False


def _looks_like_file_path(cleaned: str) -> bool:
    """Return True if string looks like a file path (extension or dir/file structure)."""
    if not cleaned:
        return False
    if cleaned.endswith(_PATH_EXTENSIONS):
        return True
    return "/" in cleaned and "." in cleaned and ":" not in cleaned


def _add_line_as_path_if_valid(line: str, paths: set[str]) -> None:
    """If line looks like a path and passes filters, normalize and add to paths."""
    if "/" not in line and not line.endswith(_PATH_EXTENSIONS):
        return
    if _is_section_or_description(line):
        return
    cleaned = _normalize_path(line)
    if _looks_like_file_path(cleaned):
        paths.add(cleaned)


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
    minio_sync = MinioSync(bucket=bucket)
    object_name = (
        f"FORMS/{form_name_upper}/FORM_FILE_DEPENDENCIES/{form_name_lower}_dependencies.txt"
    )

    logger.info(
        "Loading dependencies from MinIO",
        form_name=form_name,
        bucket=minio_sync.bucket,
        object_name=object_name,
    )

    content = _load_dependency_content(minio_sync, object_name, form_name)
    if not content:
        return []

    paths: set[str] = set()
    for line in content.splitlines():
        line = line.strip()
        if _should_skip_line(line):
            continue
        for path in _extract_paths_from_pattern(line):
            paths.add(path)
        _add_line_as_path_if_valid(line, paths)

    paths_list = sorted(paths)
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


_EXTRACT_PREFIXES = ("oases-master/", "java/", "src/")


def _normalize_relative_paths(file_path: Path, extract_root: Path) -> tuple[str, str]:
    """Get normalized relative path and a version with common ZIP prefixes stripped."""
    try:
        relative_path = file_path.relative_to(extract_root)
    except ValueError:
        relative_path = Path(file_path.name)
    normalized = str(relative_path).replace("\\", "/")
    clean = normalized
    for prefix in _EXTRACT_PREFIXES:
        if clean.startswith(prefix):
            clean = clean[len(prefix) :]
            break
    return normalized, clean


def _matches_one_dependency(
    normalized_relative: str,
    normalized_relative_clean: str,
    file_name: str,
    dep_path: str,
) -> bool:
    """Return True if file paths match this dependency path."""
    normalized_dep = normalize_path_for_matching(dep_path)
    if normalized_relative == normalized_dep or normalized_relative_clean == normalized_dep:
        return True
    if normalized_relative.endswith(normalized_dep) or normalized_relative_clean.endswith(
        normalized_dep
    ):
        return True
    if normalized_dep.endswith(normalized_relative) or normalized_dep.endswith(
        normalized_relative_clean
    ):
        return True
    if "/" not in normalized_dep and file_name == normalized_dep:
        return True
    dep_filename = Path(normalized_dep).name
    return bool(dep_filename and dep_filename == file_name)


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
    normalized_relative, normalized_relative_clean = _normalize_relative_paths(
        file_path, extract_root
    )
    file_name = file_path.name
    for dep_path in dependency_paths:
        if _matches_one_dependency(
            normalized_relative, normalized_relative_clean, file_name, dep_path
        ):
            return True
    return False
