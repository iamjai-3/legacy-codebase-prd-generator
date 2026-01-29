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
    # Also handle patterns like:
    # - ```csharp:FleetManagement.Data/Entities/Fleet.cs
    # - ```typescript:src/types/fleet.ts
    # - ```tsx:src/components/FleetForm.tsx
    code_block_pattern = r"```([^\n]+)\n(.*?)```"
    code_blocks = re.finditer(code_block_pattern, response, re.DOTALL)

    # Create a map of filename to content
    file_content_map: dict[str, str] = {}
    for match in code_blocks:
        first_line = match.group(1).strip()
        content = match.group(2).strip()

        # Handle language:filepath format (e.g., "csharp:FleetManagement.Data/Entity.cs")
        if ":" in first_line and "/" in first_line:
            # Split by first colon to get filepath
            parts = first_line.split(":", 1)
            if len(parts) == 2 and "/" in parts[1]:
                # It's a language:filepath format
                file_path = parts[1].strip()
                file_content_map[file_path] = content
                continue

        # Check if first_line is a file path (contains / or \ or has extension)
        is_file_path = "/" in first_line or "\\" in first_line or "." in first_line.split()[-1]

        # Skip if it's just a language identifier (like cs, tsx, json, etc.)
        if not is_file_path and len(first_line.split()) == 1:
            # Common language identifiers
            lang_ids = [
                "cs",
                "csharp",
                "tsx",
                "ts",
                "typescript",
                "js",
                "javascript",
                "jsx",
                "json",
                "xml",
                "yaml",
                "yml",
                "md",
                "txt",
                "sql",
                "python",
                "py",
            ]
            if first_line.lower() in lang_ids:
                continue

        # Use first_line as the key (it's the file path)
        file_content_map[first_line] = content

    # Match filenames with content
    if filenames:
        # If we have a filename list, match with content
        for filename in filenames:
            # Try exact match first
            if filename in file_content_map:
                files.append({"path": filename, "content": file_content_map[filename]})
            else:
                # Try partial match (filename might be in the path)
                matched = False
                filename_base = (
                    Path(filename).name if "/" in filename or "\\" in filename else filename
                )

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
    else:
        # No filename list provided - use all extracted code blocks directly
        # This handles multi-pass generation where we don't have a separate filename list
        for file_path, content in file_content_map.items():
            # Only add if it looks like a valid file path
            if "/" in file_path or "\\" in file_path or "." in file_path:
                files.append({"path": file_path, "content": content})
                logger.debug(f"Extracted file from code block: {file_path}")

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


def validate_backend_structure(
    files: list[dict[str, str]], entities: list[str] | None = None
) -> dict[str, Any]:
    """
    Validate that generated backend code has the required structure.

    Args:
        files: List of generated files with "path" and "content" keys
        entities: List of entity names to validate (optional)

    Returns:
        Validation result with missing files and structure issues
    """
    validation_result = {
        "valid": True,
        "missing_folders": [],
        "missing_files": [],
        "generated_files": len(files),
        "structure_issues": [],
    }

    file_paths = [f.get("path", "") for f in files]

    # Required folder patterns (works with any project name like LE11Management, LE07Management, etc.)
    # These patterns use the common suffixes without hardcoding the project name
    required_folder_patterns = [
        ".API/Controllers",
        ".Business/DTOs",
        ".Business/Services/Interfaces",
        ".Business/Services/Implementations",
        ".Data/Entities",
        ".Data/Configurations",
        ".Data/Context",
        ".Data/Repositories/Interfaces",
        ".Data/Repositories/Implementations",
    ]

    # Check folders exist (by checking if any file path contains the pattern)
    for pattern in required_folder_patterns:
        folder_exists = any(pattern in path for path in file_paths)
        if not folder_exists:
            validation_result["missing_folders"].append(pattern)
            validation_result["valid"] = False

    # Required base files
    required_files = [
        "Program.cs",
        "DbContext.cs",
    ]

    for req_file in required_files:
        file_exists = any(req_file in path for path in file_paths)
        if not file_exists:
            validation_result["missing_files"].append(req_file)
            validation_result["valid"] = False

    # Check entity-specific files if entities provided
    if entities:
        for entity in entities:
            entity_files = [
                f"Entities/{entity}.cs",
                f"Configurations/{entity}Configuration.cs",
                f"I{entity}Repository.cs",
                f"{entity}Repository.cs",
                f"I{entity}Service.cs",
                f"{entity}Service.cs",
                f"{entity}Controller.cs",
            ]

            for entity_file in entity_files:
                file_exists = any(entity_file in path for path in file_paths)
                if not file_exists:
                    validation_result["structure_issues"].append(
                        f"Missing {entity_file} for entity {entity}"
                    )

    # Check for controller files
    controller_files = [f for f in file_paths if "Controller" in f and f.endswith(".cs")]
    if not controller_files:
        validation_result["structure_issues"].append("No controller files found")
        validation_result["valid"] = False

    # Check for service files
    service_files = [f for f in file_paths if "Service" in f and "Implementations" in f]
    if not service_files:
        validation_result["structure_issues"].append("No service implementation files found")
        validation_result["valid"] = False

    logger.info(
        f"Backend validation complete: valid={validation_result['valid']}, "
        f"files={len(files)}, issues={len(validation_result['structure_issues'])}"
    )

    return validation_result


def validate_frontend_structure(
    files: list[dict[str, str]], screens: list[str] | None = None
) -> dict[str, Any]:
    """
    Validate that generated frontend code has the required structure.

    Args:
        files: List of generated files with "path" and "content" keys
        screens: List of screen names to validate (optional)

    Returns:
        Validation result with missing files and structure issues
    """
    validation_result = {
        "valid": True,
        "missing_folders": [],
        "missing_files": [],
        "generated_files": len(files),
        "structure_issues": [],
    }

    file_paths = [f.get("path", "") for f in files]

    # Required folder structure
    required_folders = [
        "src/types",
        "src/hooks",
        "src/components",
    ]

    # Check folders exist
    for folder in required_folders:
        folder_exists = any(folder in path for path in file_paths)
        if not folder_exists:
            validation_result["missing_folders"].append(folder)
            validation_result["valid"] = False

    # Required base files
    required_files = [
        "types/",
        "hooks/",
    ]

    for req_file in required_files:
        file_exists = any(req_file in path for path in file_paths)
        if not file_exists:
            validation_result["missing_files"].append(req_file)
            validation_result["valid"] = False

    # Check for component files
    component_files = [
        f for f in file_paths if "components" in f and (f.endswith(".tsx") or f.endswith(".ts"))
    ]
    if not component_files:
        validation_result["structure_issues"].append("No component files found")
        validation_result["valid"] = False

    # Check for hook files
    hook_files = [f for f in file_paths if "hooks" in f or "use" in f.lower()]
    if not hook_files:
        validation_result["structure_issues"].append("No hook files found")
        validation_result["valid"] = False

    # Check for type files
    type_files = [f for f in file_paths if "types" in f or "types/" in f]
    if not type_files:
        validation_result["structure_issues"].append("No type definition files found")
        validation_result["valid"] = False

    # Check screen-specific files if screens provided
    if screens:
        for screen in screens:
            screen_name = screen.replace(" ", "")
            screen_exists = any(screen_name.lower() in path.lower() for path in file_paths)
            if not screen_exists:
                validation_result["structure_issues"].append(
                    f"Missing component for screen: {screen}"
                )

    logger.info(
        f"Frontend validation complete: valid={validation_result['valid']}, "
        f"files={len(files)}, issues={len(validation_result['structure_issues'])}"
    )

    return validation_result


def generate_validation_report(
    backend_validation: dict[str, Any],
    frontend_validation: dict[str, Any],
    form_name: str,
) -> str:
    """
    Generate a human-readable validation report.

    Args:
        backend_validation: Backend validation result
        frontend_validation: Frontend validation result
        form_name: Form name for the report

    Returns:
        Markdown-formatted validation report
    """
    report_lines = [
        f"# Code Migration Validation Report: {form_name}",
        "",
        "## Summary",
        f"- Backend Valid: {'Yes' if backend_validation['valid'] else 'No'}",
        f"- Frontend Valid: {'Yes' if frontend_validation['valid'] else 'No'}",
        f"- Backend Files: {backend_validation['generated_files']}",
        f"- Frontend Files: {frontend_validation['generated_files']}",
        "",
    ]

    # Backend issues
    if not backend_validation["valid"]:
        report_lines.extend(
            [
                "## Backend Issues",
                "",
            ]
        )

        if backend_validation["missing_folders"]:
            report_lines.append("### Missing Folders")
            for folder in backend_validation["missing_folders"]:
                report_lines.append(f"- {folder}")
            report_lines.append("")

        if backend_validation["missing_files"]:
            report_lines.append("### Missing Files")
            for file in backend_validation["missing_files"]:
                report_lines.append(f"- {file}")
            report_lines.append("")

        if backend_validation["structure_issues"]:
            report_lines.append("### Structure Issues")
            for issue in backend_validation["structure_issues"]:
                report_lines.append(f"- {issue}")
            report_lines.append("")

    # Frontend issues
    if not frontend_validation["valid"]:
        report_lines.extend(
            [
                "## Frontend Issues",
                "",
            ]
        )

        if frontend_validation["missing_folders"]:
            report_lines.append("### Missing Folders")
            for folder in frontend_validation["missing_folders"]:
                report_lines.append(f"- {folder}")
            report_lines.append("")

        if frontend_validation["missing_files"]:
            report_lines.append("### Missing Files")
            for file in frontend_validation["missing_files"]:
                report_lines.append(f"- {file}")
            report_lines.append("")

        if frontend_validation["structure_issues"]:
            report_lines.append("### Structure Issues")
            for issue in frontend_validation["structure_issues"]:
                report_lines.append(f"- {issue}")
            report_lines.append("")

    if backend_validation["valid"] and frontend_validation["valid"]:
        report_lines.extend(
            [
                "## All Validations Passed",
                "",
                "The generated code structure meets all requirements.",
            ]
        )

    return "\n".join(report_lines)
