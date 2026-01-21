"""Utility functions for code migration parsing and file operations."""

import json
import re
import zipfile
from pathlib import Path
from typing import Any

from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def parse_llm_code_response(
    response: str,
) -> tuple[list[dict[str, str]], str, dict[str, Any] | None]:
    """
    Parse LLM response to extract files, documentation, and Swagger JSON.

    Args:
        response: LLM response string containing code files

    Returns:
        Tuple of (files_list, documentation, swagger_json)
        files_list: List of dicts with "path" and "content" keys
        documentation: Documentation text
        swagger_json: Parsed Swagger JSON or None
    """
    files: list[dict[str, str]] = []
    documentation = ""
    swagger_json: dict[str, Any] | None = None

    # Extract filenames from delimiter list
    # Look for patterns like: ```filenames\nfile1\nfile2\n``` or just a list
    filename_pattern = r"```filenames\s*\n(.*?)\n```"
    filename_match = re.search(filename_pattern, response, re.DOTALL)

    filenames: list[str] = []
    if filename_match:
        filename_text = filename_match.group(1)
        filenames = [
            f.strip() for f in filename_text.split("\n") if f.strip() and not f.startswith("#")
        ]
    else:
        # Try alternative pattern: just a list of filenames
        lines = response.split("\n")
        filename_lines = []
        in_filename_section = False
        for line in lines:
            if "filenames" in line.lower() or (
                line.strip().startswith("```") and "filename" in line.lower()
            ):
                in_filename_section = True
                continue
            if in_filename_section and line.strip().startswith("```"):
                break
            if in_filename_section and line.strip():
                filename_lines.append(line.strip())

        if filename_lines:
            filenames = [f for f in filename_lines if f and not f.startswith("#")]

    # Extract file contents from code blocks
    # Pattern: ```filename\ncontent\n``` or ```filename\n...\ncontent\n...\n```
    # Also handle language identifiers like ```cs, ```tsx, etc.
    code_block_pattern = r"```([^\n]+)\n(.*?)```"
    code_blocks = re.finditer(code_block_pattern, response, re.DOTALL)

    # Create a map of filename to content
    file_content_map: dict[str, str] = {}
    for match in code_blocks:
        first_line = match.group(1).strip()
        content = match.group(2).strip()

        # Check if first_line is a file path (contains / or \ or has extension)
        is_file_path = "/" in first_line or "\\" in first_line or "." in first_line.split()[-1]

        # Skip if it's just a language identifier (like cs, tsx, json, etc.)
        if not is_file_path and len(first_line.split()) == 1:
            # Common language identifiers
            lang_ids = [
                "cs",
                "tsx",
                "ts",
                "js",
                "jsx",
                "json",
                "xml",
                "yaml",
                "yml",
                "md",
                "txt",
                "sql",
            ]
            if first_line.lower() in lang_ids:
                continue

        # Use first_line as the key (it's the file path)
        file_content_map[first_line] = content

    # Match filenames with content
    for filename in filenames:
        # Try exact match first
        if filename in file_content_map:
            files.append({"path": filename, "content": file_content_map[filename]})
        else:
            # Try partial match (filename might be in the path)
            matched = False
            filename_base = Path(filename).name if "/" in filename or "\\" in filename else filename

            for file_path, content in file_content_map.items():
                file_path_base = (
                    Path(file_path).name if "/" in file_path or "\\" in file_path else file_path
                )

                # Match by base name or if filename is contained in file_path
                if (
                    filename_base == file_path_base
                    or filename in file_path
                    or file_path.endswith(filename)
                    or filename.endswith(file_path_base)
                ):
                    files.append({"path": filename, "content": content})
                    matched = True
                    break
            if not matched:
                logger.warning(f"Could not find content for file: {filename}")

    # Extract documentation
    doc_pattern = r"===DOCUMENTATION_START===\s*(.*?)\s*===DOCUMENTATION_END==="
    doc_match = re.search(doc_pattern, response, re.DOTALL)
    if doc_match:
        documentation = doc_match.group(1).strip()

    # Extract Swagger JSON
    swagger_pattern = r"===SWAGGER_START===\s*(.*?)\s*===SWAGGER_END==="
    swagger_match = re.search(swagger_pattern, response, re.DOTALL)
    if swagger_match:
        swagger_text = swagger_match.group(1).strip()
        try:
            swagger_json = json.loads(swagger_text)
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse Swagger JSON: {e}")
            swagger_json = None

    return files, documentation, swagger_json


def create_directory_structure(base_path: Path, files: list[dict[str, str]]) -> None:
    """
    Create directory structure and write files.

    Args:
        base_path: Base directory path
        files: List of dicts with "path" and "content" keys
    """
    base_path = Path(base_path)
    base_path.mkdir(parents=True, exist_ok=True)

    for file_info in files:
        file_path = base_path / file_info["path"]

        # Create parent directories
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file content
        try:
            file_path.write_text(file_info["content"], encoding="utf-8")
            logger.debug(f"Created file: {file_path}")
        except Exception as e:
            logger.error(f"Failed to write file {file_path}: {e}")
            raise


def create_zip_archive(source_dir: Path, output_path: Path) -> Path:
    """
    Create a zip archive from a directory.

    Args:
        source_dir: Source directory to zip
        output_path: Output zip file path

    Returns:
        Path to created zip file
    """
    source_dir = Path(source_dir)
    output_path = Path(output_path)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Creating zip archive: {output_path} from {source_dir}")

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in source_dir.rglob("*"):
            if file_path.is_file():
                # Get relative path for archive
                arcname = file_path.relative_to(source_dir)
                zipf.write(file_path, arcname)
                logger.debug(f"Added to zip: {arcname}")

    logger.info(f"Zip archive created: {output_path}")
    return output_path
