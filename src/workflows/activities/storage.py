"""Storage activities for PRD generation workflow."""

from datetime import datetime
from pathlib import Path
from typing import Any

from temporalio import activity

from src.extractors.minio_extractor import MinioExtractor, Screenshot
from src.utils.data_reconstruction import _restore_image_data
from src.utils.file_utils import ensure_directory, read_file_content, write_json
from src.utils.logging_config import get_logger
from src.utils.minio_sync import MinioSync
from src.vector_store.qdrant_manager import QdrantManager

logger = get_logger(__name__)

# Constants for content length limits - MAXIMIZED for complete business logic capture
# These limits are per chunk - long files will be split into multiple chunks
MAX_JAVA_SOURCE_CONTENT = 30000  # Main source files with business logic - INCREASED
MAX_JAVA_CONTENT = 25000  # Other Java files - INCREASED
MAX_SQL_CONTENT = 30000  # SQL files - store complete schemas
MAX_DEFAULT_CONTENT = 20000  # Other files - INCREASED
MAX_FORM_CONTENT = 35000  # Form definitions - store full content
MAX_METHOD_CONTENT = 20000  # Individual method content - for complete method bodies

# Default values
DEFAULT_CONTENT_TYPE = "image/png"
DEFAULT_SCREEN_TYPE = "general"


@activity.defn
async def store_vectors_activity(
    form_name: str,
    code_data: dict[str, Any] | None = None,
    screenshot_data: dict[str, Any] | None = None,
    existing_prd_data: dict[str, Any] | None = None,
    recreate_collection: bool = False,
    extract_dir: str | None = None,
    db_prd_data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Store all extracted data as vectors in Qdrant.

    Creates a unified knowledge base for migration purposes containing:
    - Legacy code (business logic, data models, API specs)
    - Screenshots (UI context)
    - Existing PRD documents (form docs, requirements)
    - DB_PRD documents (database schemas, table relationships, data mappings)
    """
    logger.info("Starting vector storage", form_name=form_name)

    qdrant = QdrantManager()
    collection_name = qdrant.create_collection(form_name=form_name, recreate=recreate_collection)
    total_vectors = 0

    # Store all data sources in the unified knowledge base
    code_vectors = _store_code_vectors(qdrant, form_name, code_data, extract_dir)
    total_vectors += code_vectors
    logger.info(f"Stored {code_vectors} code vectors")

    screenshot_vectors = _store_screenshot_vectors(qdrant, form_name, screenshot_data)
    total_vectors += screenshot_vectors
    logger.info(f"Stored {screenshot_vectors} screenshot vectors")

    prd_vectors = _store_prd_vectors(qdrant, form_name, existing_prd_data)
    total_vectors += prd_vectors
    logger.info(f"Stored {prd_vectors} existing PRD vectors")

    db_prd_vectors = _store_db_prd_vectors(qdrant, form_name, db_prd_data)
    total_vectors += db_prd_vectors
    logger.info(f"Stored {db_prd_vectors} DB_PRD vectors")

    stats = qdrant.get_collection_stats(form_name)

    return {
        "success": True,
        "collection_name": collection_name,
        "total_vectors_added": total_vectors,
        "vectors_breakdown": {
            "code": code_vectors,
            "screenshots": screenshot_vectors,
            "existing_prd": prd_vectors,
            "db_prd": db_prd_vectors,
        },
        "collection_stats": stats,
    }


def _store_code_vectors(
    qdrant: QdrantManager,
    form_name: str,
    code_data: dict[str, Any] | None,
    extract_dir: str | None,
) -> int:
    """Store code vectors in Qdrant."""
    if not code_data:
        return 0

    if extract_dir:
        return _store_code_with_content(qdrant, form_name, code_data, extract_dir)
    return _store_code_metadata_only(qdrant, form_name, code_data)


def _store_code_with_content(
    qdrant: QdrantManager,
    form_name: str,
    code_data: dict[str, Any],
    extract_dir: str,
) -> int:
    """Store code files with actual content read from extract directory."""
    extract_path = Path(extract_dir)
    total_vectors = 0
    files_stored = 0

    for file_info in code_data.get("files", []):
        file_path = _find_file_path(extract_path, file_info.get("path", ""))
        if not file_path:
            continue

        vectors = _store_single_code_file(qdrant, form_name, file_info, file_path)
        if vectors > 0:
            total_vectors += vectors
            files_stored += 1

    logger.info(f"Stored {files_stored} code files with content")
    return total_vectors


def _find_file_path(extract_path: Path, file_path_str: str) -> Path | None:
    """Find file in extract directory, checking multiple possible locations."""
    if not file_path_str:
        return None

    possible_paths = [
        extract_path / file_path_str,
        extract_path / "oases-master" / file_path_str,
        extract_path / "java" / file_path_str,
    ]

    for path in possible_paths:
        if path.exists() and path.is_file():
            return path

    logger.warning(f"File not found in extract directory: {file_path_str}")
    return None


def _store_single_code_file(
    qdrant: QdrantManager,
    form_name: str,
    file_info: dict[str, Any],
    file_path: Path,
) -> int:
    """
    Store a single code file in the vector store.

    For large files with business logic, creates multiple chunks to ensure
    complete coverage of all methods and logic.
    """
    try:
        content = read_file_content(file_path)
        file_info_with_content = {**file_info, "content": content}
        total_vectors = 0

        # Determine if this is a key business logic file
        path_lower = file_info.get("path", "").lower()
        is_business_logic_file = any(
            keyword in path_lower
            for keyword in ["options", "adapter", "service", "action", "controller", "form"]
        )

        # For business logic files, store full content with chunking
        if is_business_logic_file and len(content) > MAX_JAVA_SOURCE_CONTENT:
            total_vectors += _store_large_file_in_chunks(
                qdrant, form_name, file_info_with_content, content
            )
        else:
            # Standard storage for smaller files
            formatted_content = _format_code_for_vector(file_info_with_content)
            total_vectors += qdrant.add_text(
                form_name=form_name,
                text=formatted_content,
                metadata=file_info,
                doc_type="code",
            )

        return total_vectors
    except OSError as e:
        logger.warning(f"Failed to read/store file {file_info.get('path', '')}: {e}")
        return 0


def _store_large_file_in_chunks(
    qdrant: QdrantManager,
    form_name: str,
    file_info: dict[str, Any],
    content: str,
) -> int:
    """
    Store a large file in multiple chunks to preserve full business logic.

    Splits by methods/functions to keep logical units together.
    """
    total_vectors = 0
    path = file_info.get("path", "")
    language = file_info.get("language", "")

    # First, store the file header/class definition
    header_content = _extract_file_header(content, language)
    if header_content:
        header_text = f"""
FILE HEADER: {path}
Language: {language}
Type: {file_info.get("file_type", "")}
Classes: {", ".join(file_info.get("classes", []))}

{header_content}
"""
        total_vectors += qdrant.add_text(
            form_name=form_name,
            text=header_text,
            metadata={**file_info, "chunk_type": "file_header"},
            doc_type="code",
        )

    # Extract and store individual methods/functions - ALL of them for business logic
    methods = _extract_methods_from_content(content, language)
    logger.info(f"Extracting {len(methods)} methods from {path}")

    for method_name, method_content in methods:
        # Store complete method body (up to MAX_METHOD_CONTENT)
        method_content_trimmed = method_content[:MAX_METHOD_CONTENT]
        method_text = f"""
METHOD: {method_name}
FILE: {path}
Language: {language}
Classes: {", ".join(file_info.get("classes", []))}

FULL METHOD IMPLEMENTATION:
{method_content_trimmed}
"""
        total_vectors += qdrant.add_text(
            form_name=form_name,
            text=method_text,
            metadata={
                **file_info,
                "chunk_type": "method_implementation",
                "method_name": method_name,
                "method_length": len(method_content),
            },
            doc_type="business_logic",
        )

    # Also store the full file in larger chunks for context
    chunk_size = MAX_JAVA_SOURCE_CONTENT
    for i in range(0, len(content), chunk_size):
        chunk = content[i : i + chunk_size]
        chunk_num = i // chunk_size + 1

        chunk_text = f"""
FILE CONTENT (Part {chunk_num}): {path}
Language: {language}

{chunk}
"""
        total_vectors += qdrant.add_text(
            form_name=form_name,
            text=chunk_text,
            metadata={
                **file_info,
                "chunk_type": "file_content",
                "chunk_number": chunk_num,
            },
            doc_type="code",
        )

    logger.debug(f"Stored large file {path} in multiple chunks: {total_vectors} vectors")
    return total_vectors


def _extract_file_header(content: str, language: str) -> str:
    """Extract file header (imports, class declaration, fields)."""
    lines = content.split("\n")
    header_lines = []
    in_class = False
    brace_count = 0

    for line in lines:
        header_lines.append(line)

        if language == "java":
            if "class " in line or "interface " in line:
                in_class = True
            if in_class:
                brace_count += line.count("{") - line.count("}")
                # Stop after class fields (before first method)
                if brace_count > 0 and (
                    "public " in line or "private " in line or "protected " in line
                ):
                    if "(" in line and ")" in line:  # This is a method
                        break

        # Limit header size
        if len("\n".join(header_lines)) > 3000:
            break

    return "\n".join(header_lines)


def _extract_methods_from_content(content: str, language: str) -> list[tuple[str, str]]:
    """Extract ALL individual methods/functions from code content.

    Extracts complete method bodies with proper brace matching to ensure
    no business logic is truncated.
    """
    import re

    methods = []

    if language == "java":
        # Match Java methods - improved pattern for better matching
        method_pattern = r"((?:public|private|protected)\s+(?:static\s+)?(?:synchronized\s+)?(?:final\s+)?(?:\w+(?:<[^>]+>)?\s+)+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{)"
        matches = list(re.finditer(method_pattern, content))

        for i, match in enumerate(matches):
            method_name = match.group(2)
            start = match.start()

            # Find method end by counting braces - handle nested braces and strings
            brace_count = 0
            end = start
            in_method = False
            in_string = False
            string_char = None

            j = start
            while j < len(content):
                char = content[j]

                # Handle string literals to avoid counting braces inside strings
                if char in "\"'":
                    if not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char and (j == 0 or content[j - 1] != "\\"):
                        in_string = False
                        string_char = None

                # Only count braces outside of strings
                if not in_string:
                    if char == "{":
                        brace_count += 1
                        in_method = True
                    elif char == "}":
                        brace_count -= 1
                        if in_method and brace_count == 0:
                            end = j + 1
                            break
                j += 1

            method_content = content[start:end]
            # Store ALL methods with any code content (lowered threshold from 100 to 50)
            if len(method_content) > 50:
                methods.append((method_name, method_content))

    return methods


def _store_code_metadata_only(
    qdrant: QdrantManager,
    form_name: str,
    code_data: dict[str, Any],
) -> int:
    """Store code files with metadata only (fallback when no extract_dir)."""
    logger.warning("No extract_dir provided, storing code metadata only (limited context)")
    total_vectors = 0

    for file_info in code_data.get("files", []):
        content = _format_code_for_vector(file_info)
        total_vectors += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata=file_info,
            doc_type="code",
        )

    logger.info(f"Stored {len(code_data.get('files', []))} code files (metadata only)")
    return total_vectors


def _store_screenshot_vectors(
    qdrant: QdrantManager,
    form_name: str,
    screenshot_data: dict[str, Any] | None,
) -> int:
    """Store screenshot vectors in Qdrant."""
    if not screenshot_data:
        return 0

    minio_extractor = MinioExtractor()
    total_vectors = 0

    for item in screenshot_data.get("raw_screenshots", []):
        content, metadata = _format_screenshot_for_vector(item, form_name, minio_extractor)
        if content:
            total_vectors += qdrant.add_text(
                form_name=form_name,
                text=content,
                metadata=metadata,
                doc_type="screenshot",
            )

    return total_vectors


def _store_prd_vectors(
    qdrant: QdrantManager,
    form_name: str,
    existing_prd_data: dict[str, Any] | None,
) -> int:
    """Store existing PRD document vectors in Qdrant."""
    if not existing_prd_data or not existing_prd_data.get("success"):
        return 0

    prd_vectors = _store_existing_prd_vectors(qdrant, form_name, existing_prd_data)
    logger.info(f"Stored {prd_vectors} vectors from existing PRD documents")
    return prd_vectors


def _store_existing_prd_vectors(
    qdrant: QdrantManager, form_name: str, prd_data: dict[str, Any]
) -> int:
    """Store existing PRD documents in vector store."""
    count = 0
    count += _store_prd_documents(qdrant, form_name, prd_data.get("documents", []))
    count += _store_prd_images(qdrant, form_name, prd_data.get("images", []))
    return count


def _store_prd_documents(
    qdrant: QdrantManager, form_name: str, documents: list[dict[str, Any]]
) -> int:
    """Store PRD document content in vector store."""
    count = 0
    for doc in documents:
        content = f"""
PRD Document: {doc.get("filename", "")}
Type: {doc.get("document_type", "")}
Title: {doc.get("title", "")}

Content:
{doc.get("content", "")}
"""
        metadata = {
            "filename": doc.get("filename", ""),
            "document_type": doc.get("document_type", ""),
            "title": doc.get("title", ""),
            "word_count": doc.get("word_count", 0),
            "form_name": form_name,
            "source": "existing_prd",
        }
        count += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata=metadata,
            doc_type="existing_prd",
        )
    return count


def _store_prd_images(qdrant: QdrantManager, form_name: str, images: list[dict[str, Any]]) -> int:
    """Store PRD image descriptions in vector store."""
    count = 0
    for img in images:
        description = img.get("description", "UI screenshot or diagram")
        content = f"""
PRD Image: {img.get("filename", "")}
Description: {description}

This image is part of the existing PRD documentation for {form_name}.
It shows: {description}
"""
        metadata = {
            "filename": img.get("filename", ""),
            "description": description,
            "content_type": img.get("content_type", DEFAULT_CONTENT_TYPE),
            "form_name": form_name,
            "source": "existing_prd_image",
        }
        count += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata=metadata,
            doc_type="existing_prd_image",
        )
    return count


def _store_db_prd_vectors(
    qdrant: QdrantManager,
    form_name: str,
    db_prd_data: dict[str, Any] | None,
) -> int:
    """Store DB_PRD document vectors in Qdrant."""
    if not db_prd_data or not db_prd_data.get("success"):
        return 0

    count = 0
    for doc in db_prd_data.get("documents", []):
        content = f"""
DATABASE DOCUMENTATION: {doc.get("filename", "")}
Type: {doc.get("document_type", "")}
Title: {doc.get("title", "")}

CONTENT:
{doc.get("content", "")}

This document contains database schema information, table relationships, 
and data mappings critical for code migration.
"""
        metadata = {
            "filename": doc.get("filename", ""),
            "document_type": doc.get("document_type", ""),
            "title": doc.get("title", ""),
            "word_count": doc.get("word_count", 0),
            "form_name": form_name,
            "source": "db_prd",
        }
        count += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata=metadata,
            doc_type="database",
        )

    logger.info(f"Stored {count} DB_PRD document vectors")
    return count


def _format_code_for_vector(file_info: dict[str, Any]) -> str:
    """Format code file info for vectorization with content for searchability."""
    path = file_info.get("path", "")
    language = file_info.get("language", "")
    file_type = file_info.get("file_type", "")
    content = file_info.get("content", "")

    parts = [
        f"File: {path}",
        f"Language: {language}",
        f"Type: {file_type}",
    ]

    if file_info.get("classes"):
        parts.append(f"Classes: {', '.join(file_info.get('classes', []))}")

    if file_info.get("methods"):
        parts.append(f"Methods: {', '.join(file_info.get('methods', []))}")

    parts.append(_get_content_section(language, file_type, path, content))

    return "\n".join(parts)


def _get_content_section(language: str, file_type: str, path: str, content: str) -> str:
    """Get the appropriate content section based on file type with generous limits."""
    path_lower = path.lower()

    # SQL files - store full content
    if language == "sql" or file_type in ("ddl", "dml", "query"):
        return f"\nSQL DDL Content:\n{content[:MAX_SQL_CONTENT]}"

    # Form definitions - store full content
    if file_type == "form_definition" or path_lower.endswith(".form"):
        return f"\nForm Definition:\n{content[:MAX_FORM_CONTENT]}"

    # Business logic files - store more content
    if language == "java":
        is_business_file = any(
            keyword in path_lower
            for keyword in ["options", "adapter", "service", "action", "controller"]
        )
        if is_business_file or file_type == "source":
            return f"\nJava Source Code (Business Logic):\n{content[:MAX_JAVA_SOURCE_CONTENT]}"
        return f"\nJava Code:\n{content[:MAX_JAVA_CONTENT]}"

    return f"\nContent:\n{content[:MAX_DEFAULT_CONTENT]}"


def _format_screenshot_for_vector(
    item: dict[str, Any], form_name: str, minio_extractor: MinioExtractor
) -> tuple[str, dict[str, Any]]:
    """Format screenshot for vectorization."""
    try:
        if isinstance(item, dict):
            return _format_dict_screenshot(item, form_name, minio_extractor)
        return _format_object_screenshot(item, form_name, minio_extractor)
    except (OSError, ValueError, TypeError) as e:
        logger.warning("Failed to format screenshot for vector", error=str(e))
        return "", {}


def _format_dict_screenshot(
    item: dict[str, Any], form_name: str, minio_extractor: MinioExtractor
) -> tuple[str, dict[str, Any]]:
    """Format a screenshot dictionary for vectorization."""
    image_data = _restore_image_data(item, minio_extractor, form_name)
    width, height = _get_image_dimensions(image_data, item, form_name, minio_extractor)

    object_name = item.get("object_name", "")
    screen_type = item.get("screen_type", DEFAULT_SCREEN_TYPE)
    size = item.get("size", 0)
    content_type = item.get("content_type", DEFAULT_CONTENT_TYPE)
    bucket = item.get("bucket", "")

    return _build_screenshot_result(
        form_name, object_name, screen_type, width, height, size, content_type, bucket
    )


def _format_object_screenshot(
    item: Screenshot, form_name: str, minio_extractor: MinioExtractor
) -> tuple[str, dict[str, Any]]:
    """Format a Screenshot object for vectorization."""
    width, height = minio_extractor.get_image_dimensions(item)

    return _build_screenshot_result(
        form_name,
        item.object_name,
        item.screen_type,
        width,
        height,
        item.size,
        item.content_type,
        item.bucket,
    )


def _get_image_dimensions(
    image_data: bytes | None,
    item: dict[str, Any],
    form_name: str,
    minio_extractor: MinioExtractor,
) -> tuple[int, int]:
    """Get image dimensions from image data."""
    if not image_data:
        return 0, 0

    try:
        screenshot_obj = Screenshot(
            object_name=item.get("object_name", ""),
            bucket=item.get("bucket", ""),
            form_name=form_name,
            screen_type=item.get("screen_type", DEFAULT_SCREEN_TYPE),
            image_data=image_data,
            content_type=item.get("content_type", DEFAULT_CONTENT_TYPE),
            size=len(image_data),
            metadata={},
        )
        return minio_extractor.get_image_dimensions(screenshot_obj)
    except (OSError, ValueError):
        return 0, 0


def _build_screenshot_result(
    form_name: str,
    object_name: str,
    screen_type: str,
    width: int,
    height: int,
    size: int,
    content_type: str,
    bucket: str,
) -> tuple[str, dict[str, Any]]:
    """Build the content and metadata for a screenshot."""
    content = f"""
Screenshot Analysis for {form_name}:
- File: {object_name}
- Screen Type: {screen_type}
- Dimensions: {width}x{height} pixels
- Size: {size} bytes
This screenshot shows a UI screen from the {form_name} module.
"""
    metadata = {
        "object_name": object_name,
        "screen_type": screen_type,
        "width": width,
        "height": height,
        "size_bytes": size,
        "content_type": content_type,
        "bucket": bucket,
        "form_name": form_name,
    }
    return content, metadata


def _is_valid_analysis(data: Any) -> bool:
    """Check if analysis data is valid and successful."""
    return isinstance(data, dict) and data.get("success", False)


@activity.defn
async def store_analysis_results_activity(
    form_name: str,
    screenshot_analysis: dict[str, Any] | None = None,
    requirements_analysis: dict[str, Any] | None = None,
    user_flow_analysis: dict[str, Any] | None = None,
    database_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Store analysis results in the vector knowledge base."""
    logger.info("Storing analysis results in vector store", form_name=form_name)

    qdrant = QdrantManager()
    total_vectors = 0

    if _is_valid_analysis(screenshot_analysis):
        total_vectors += _store_screenshot_analysis(qdrant, form_name, screenshot_analysis)

    if _is_valid_analysis(requirements_analysis):
        total_vectors += _store_requirements_analysis(qdrant, form_name, requirements_analysis)

    if _is_valid_analysis(user_flow_analysis):
        total_vectors += _store_user_flow_analysis(qdrant, form_name, user_flow_analysis)

    if _is_valid_analysis(database_analysis):
        logger.info(
            "Database analysis already stored",
            form_name=form_name,
            vectors_stored=database_analysis.get("vectors_stored", 0),
        )

    logger.info("Stored analysis results", form_name=form_name, total_vectors=total_vectors)
    return {"success": True, "total_vectors_added": total_vectors}


def _store_screenshot_analysis(qdrant: QdrantManager, form_name: str, data: dict[str, Any]) -> int:
    """Store screenshot analysis in vector store."""
    count = _store_screen_analyses(qdrant, form_name, data.get("screen_analyses", []))

    if data.get("ui_flow_summary"):
        count += _store_ui_flow_summary(qdrant, form_name, data)

    return count


def _store_screen_analyses(
    qdrant: QdrantManager, form_name: str, screen_analyses: list[dict[str, Any]]
) -> int:
    """Store individual screen analyses."""
    count = 0
    for screen in screen_analyses:
        elements_text = "\n".join(
            f"- {e.get('element_type', '')}: {e.get('label', '')} - {e.get('description', '')}"
            for e in screen.get("ui_elements", [])
        )

        content = f"""
UI Screen Analysis for {form_name}:
- Screen Name: {screen.get("screen_name", "")}
- Screen Type: {screen.get("screen_type", "")}
- Purpose: {screen.get("purpose", "")}
- Layout: {screen.get("layout_description", "")}

UI Elements:
{elements_text}

User Actions:
{chr(10).join("- " + a for a in screen.get("user_actions", []))}

Validation Rules:
{chr(10).join("- " + r for r in screen.get("validation_rules", []))}
"""
        count += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata={"screen_name": screen.get("screen_name"), "form_name": form_name},
            doc_type="screenshot_analysis",
        )
    return count


def _store_ui_flow_summary(qdrant: QdrantManager, form_name: str, data: dict[str, Any]) -> int:
    """Store UI flow summary in vector store."""
    patterns = chr(10).join("- " + p for p in data.get("common_patterns", []))
    inventory = chr(10).join(f"- {k}: {v}" for k, v in data.get("component_inventory", {}).items())

    content = f"""
UI Flow Summary for {form_name}:
{data.get("ui_flow_summary")}

Common Patterns:
{patterns}

Component Inventory:
{inventory}
"""
    return qdrant.add_text(
        form_name=form_name,
        text=content,
        metadata={"form_name": form_name, "analysis_type": "ui_flow_summary"},
        doc_type="screenshot_analysis",
    )


def _store_requirements_analysis(
    qdrant: QdrantManager, form_name: str, data: dict[str, Any]
) -> int:
    """Store requirements analysis in vector store."""
    count = 0
    for req in data.get("functional_requirements", []):
        criteria = chr(10).join("- " + ac for ac in req.get("acceptance_criteria", []))

        content = f"""
Functional Requirement: {req.get("req_id", "")} - {req.get("title", "")}
Priority: {req.get("priority", "")}
Category: {req.get("category", "")}

Description: {req.get("description", "")}

User Story: {req.get("user_story", "")}

Acceptance Criteria:
{criteria}

Dependencies: {", ".join(req.get("dependencies", []))}
"""
        count += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata={"req_id": req.get("req_id"), "form_name": form_name},
            doc_type="requirement",
        )
    return count


def _store_user_flow_analysis(qdrant: QdrantManager, form_name: str, data: dict[str, Any]) -> int:
    """Store user flow analysis in vector store."""
    count = 0
    for flow in data.get("user_flows", []):
        steps_text = chr(10).join(
            f"{s.get('step_number', '')}. {s.get('action', '')} - {s.get('screen', '')}"
            for s in flow.get("steps", [])
        )

        content = f"""
User Flow: {flow.get("flow_id", "")} - {flow.get("name", "")}
Actor: {flow.get("actor", "")}
Description: {flow.get("description", "")}

Steps:
{steps_text}

Success Criteria: {flow.get("success_criteria", "")}
"""
        count += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata={"flow_id": flow.get("flow_id"), "form_name": form_name},
            doc_type="user_flow",
        )
    return count


@activity.defn
async def save_prd_activity(
    form_name: str,
    prd_content: str,
    output_dir: str = "./output",
) -> dict[str, Any]:
    """Save the generated PRD to file."""
    logger.info("Saving PRD", form_name=form_name, output_dir=output_dir)

    output_path = ensure_directory(output_dir)

    md_file = output_path / f"{form_name}_PRD.md"
    md_file.write_text(prd_content, encoding="utf-8")

    metadata = {
        "form_name": form_name,
        "generated_at": datetime.now().isoformat(),
        "file_path": str(md_file),
        "word_count": len(prd_content.split()),
    }

    metadata_file = output_path / f"{form_name}_PRD_metadata.json"
    write_json(metadata_file, metadata)

    logger.info("PRD saved successfully", form_name=form_name, file_path=str(md_file))

    return {
        "success": True,
        "markdown_file": str(md_file),
        "metadata_file": str(metadata_file),
        "word_count": metadata["word_count"],
    }


@activity.defn
async def verify_minio_bucket_activity(bucket: str | None = None) -> dict[str, Any]:
    """
    Verify MinIO bucket exists (does not create folders).

    Args:
        bucket: Optional bucket name (defaults to "metadatas")

    Returns:
        Dictionary with verification status

    Raises:
        ValueError: If bucket does not exist
    """
    sync = MinioSync(bucket=bucket)
    logger.info("Verifying MinIO bucket exists", bucket=sync.bucket)

    try:
        sync.ensure_bucket(bucket=None)
        logger.info("MinIO bucket verified", bucket=sync.bucket)
        return {"success": True, "bucket": sync.bucket}
    except ValueError:
        logger.error("Bucket does not exist", bucket=sync.bucket)
        raise
