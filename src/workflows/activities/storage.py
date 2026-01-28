"""Storage activities for PRD generation workflow."""

from src.utils.minio_sync import MinioSync

from datetime import datetime
from typing import Any

from temporalio import activity

from src.extractors.minio_extractor import MinioExtractor, Screenshot
from src.utils.data_reconstruction import _restore_image_data
from src.utils.file_utils import ensure_directory, write_json
from src.utils.logging_config import get_logger
from src.vector_store.qdrant_manager import QdrantManager

logger = get_logger(__name__)


@activity.defn
async def store_vectors_activity(
    form_name: str,
    code_data: dict[str, Any] | None = None,
    screenshot_data: dict[str, Any] | None = None,
    existing_prd_data: dict[str, Any] | None = None,
    recreate_collection: bool = False,
    extract_dir: str | None = None,
) -> dict[str, Any]:
    """
    Store all extracted data as vectors in Qdrant.

    This creates a unified knowledge base containing:
    - Legacy code (for understanding existing implementation)
    - Screenshots (for UI context)
    - Existing PRD documents (for business logic and app flow context)

    This combined knowledge base is used for migration purposes.

    Args:
        form_name: Form identifier
        code_data: Code extraction metadata (files list with paths)
        screenshot_data: Screenshot data
        existing_prd_data: Existing PRD documents
        recreate_collection: Whether to recreate the collection
        extract_dir: Directory where files were extracted (to read actual content)
    """
    logger.info("Starting vector storage", form_name=form_name)

    qdrant = QdrantManager()
    collection_name = qdrant.create_collection(form_name=form_name, recreate=recreate_collection)
    total_vectors = 0

    # Store code vectors (legacy code knowledge)
    # Re-read files from extract_dir to get actual content (avoids passing large data through Temporal)
    if code_data and extract_dir:
        from pathlib import Path

        from src.utils.file_utils import read_file_content

        extract_path = Path(extract_dir)
        files_stored = 0

        for file_info in code_data.get("files", []):
            file_path_str = file_info.get("path", "")
            if not file_path_str:
                continue

            # Try to find the file in the extract directory
            # Handle both relative paths and paths with ZIP root prefix
            possible_paths = [
                extract_path / file_path_str,
                extract_path / "oases-master" / file_path_str,
                extract_path / "java" / file_path_str,
            ]

            file_path = None
            for pp in possible_paths:
                if pp.exists() and pp.is_file():
                    file_path = pp
                    break

            if not file_path:
                logger.warning(f"File not found in extract directory: {file_path_str}")
                continue

            try:
                # Read actual file content
                content = read_file_content(file_path)
                file_info_with_content = file_info.copy()
                file_info_with_content["content"] = content

                # Format for vector storage
                formatted_content = _format_code_for_vector(file_info_with_content)

                count = qdrant.add_text(
                    form_name=form_name,
                    text=formatted_content,
                    metadata=file_info,
                    doc_type="code",
                )
                total_vectors += count
                files_stored += 1
            except Exception as e:
                logger.warning(f"Failed to read/store file {file_path_str}: {e}")
                continue

        logger.info(f"Stored {files_stored} code files with content")
    elif code_data:
        # Fallback: use metadata only (limited context)
        logger.warning("No extract_dir provided, storing code metadata only (limited context)")
        for file_info in code_data.get("files", []):
            content = _format_code_for_vector(file_info)
            count = qdrant.add_text(
                form_name=form_name, text=content, metadata=file_info, doc_type="code"
            )
            total_vectors += count
        logger.info(f"Stored {len(code_data.get('files', []))} code files (metadata only)")

    # Store screenshot vectors
    if screenshot_data:
        minio_extractor = MinioExtractor()
        for item in screenshot_data.get("raw_screenshots", []):
            content, metadata = _format_screenshot_for_vector(item, form_name, minio_extractor)
            if content:
                count = qdrant.add_text(
                    form_name=form_name, text=content, metadata=metadata, doc_type="screenshot"
                )
                total_vectors += count

    # Store existing PRD documents (business logic and app flow context)
    if existing_prd_data and existing_prd_data.get("success"):
        prd_vectors = _store_existing_prd_vectors(qdrant, form_name, existing_prd_data)
        total_vectors += prd_vectors
        logger.info(f"Stored {prd_vectors} vectors from existing PRD documents")

    stats = qdrant.get_collection_stats(form_name)

    return {
        "success": True,
        "collection_name": collection_name,
        "total_vectors_added": total_vectors,
        "collection_stats": stats,
    }


def _store_existing_prd_vectors(
    qdrant: QdrantManager, form_name: str, prd_data: dict[str, Any]
) -> int:
    """
    Store existing PRD documents in vector store.

    These documents contain critical business logic, requirements, and app flow
    information that's essential for the migration knowledge base.
    """
    count = 0

    # Store each PRD document
    for doc in prd_data.get("documents", []):
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

    # Store image descriptions (for context about UI flows in existing PRDs)
    for img in prd_data.get("images", []):
        content = f"""
PRD Image: {img.get("filename", "")}
Description: {img.get("description", "")}

This image is part of the existing PRD documentation for {form_name}.
It shows: {img.get("description", "UI screenshot or diagram")}
"""
        metadata = {
            "filename": img.get("filename", ""),
            "description": img.get("description", ""),
            "content_type": img.get("content_type", "image/png"),
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


def _format_code_for_vector(file_info: dict[str, Any]) -> str:
    """Format code file info for vectorization with FULL content for searchability.

    This is critical for the knowledge base to contain actual code content,
    not just metadata. The semantic search needs the actual implementation.
    """
    path = file_info.get("path", "")
    language = file_info.get("language", "")
    file_type = file_info.get("file_type", "")
    content = file_info.get("content", "")

    # Build a comprehensive searchable document
    parts = [
        f"File: {path}",
        f"Language: {language}",
        f"Type: {file_type}",
    ]

    if file_info.get("classes"):
        parts.append(f"Classes: {', '.join(file_info.get('classes', []))}")

    if file_info.get("methods"):
        parts.append(f"Methods: {', '.join(file_info.get('methods', []))}")

    # For SQL DDL files, include FULL content (critical for table extraction)
    if language == "sql" or file_type in ["ddl", "dml", "query"]:
        parts.append(f"\nSQL DDL Content:\n{content}")

    # For Java option files (form code), include significant portions
    elif language == "java" and ("options" in path.lower() or file_type == "source"):
        # Include more content for key source files
        parts.append(f"\nJava Source Code:\n{content[:8000]}")  # First 8000 chars

    # For other Java files, include full content but with size limit
    elif language == "java":
        parts.append(f"\nCode:\n{content[:4000]}")  # First 4000 chars

    # For form definition files, include full content
    elif file_type == "form_definition":
        parts.append(f"\nForm Definition:\n{content}")

    # For other files, include a reasonable portion
    else:
        parts.append(f"\nContent:\n{content[:3000]}")

    return "\n".join(parts)


def _format_screenshot_for_vector(
    item: dict[str, Any], form_name: str, minio_extractor: MinioExtractor
) -> tuple[str, dict[str, Any]]:
    """Format screenshot for vectorization."""
    try:
        if isinstance(item, dict):
            image_data = _restore_image_data(item, minio_extractor, form_name)

            # Get dimensions if we have image data
            width, height = 0, 0
            if image_data:
                try:
                    screenshot_obj = Screenshot(
                        object_name=item.get("object_name", ""),
                        bucket=item.get("bucket", ""),
                        form_name=form_name,
                        screen_type=item.get("screen_type", "general"),
                        image_data=image_data,
                        content_type=item.get("content_type", "image/png"),
                        size=len(image_data),
                        metadata={},
                    )
                    width, height = minio_extractor.get_image_dimensions(screenshot_obj)
                except Exception:
                    pass

            object_name = item.get("object_name", "")
            screen_type = item.get("screen_type", "general")
            size = item.get("size", 0)
            content_type = item.get("content_type", "image/png")
            bucket = item.get("bucket", "")
        else:
            # Screenshot object
            width, height = minio_extractor.get_image_dimensions(item)
            object_name = item.object_name
            screen_type = item.screen_type
            size = item.size
            content_type = item.content_type
            bucket = item.bucket

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

    except Exception as e:
        logger.warning("Failed to format screenshot for vector", error=str(e))
        return "", {}


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

    # Store screenshot analysis results
    if screenshot_analysis and isinstance(screenshot_analysis, dict) and screenshot_analysis.get("success"):
        total_vectors += _store_screenshot_analysis(qdrant, form_name, screenshot_analysis)

    # Store requirements analysis
    if requirements_analysis and isinstance(requirements_analysis, dict) and requirements_analysis.get("success"):
        total_vectors += _store_requirements_analysis(qdrant, form_name, requirements_analysis)

    # Store user flow analysis
    if user_flow_analysis and isinstance(user_flow_analysis, dict) and user_flow_analysis.get("success"):
        total_vectors += _store_user_flow_analysis(qdrant, form_name, user_flow_analysis)

    # Note: Database analysis results are already stored by DatabaseAnalysisAgent
    # This is just for logging consistency
    if database_analysis and isinstance(database_analysis, dict) and database_analysis.get("success"):
        logger.info(
            "Database analysis already stored",
            form_name=form_name,
            vectors_stored=database_analysis.get("vectors_stored", 0),
        )

    logger.info("Stored analysis results", form_name=form_name, total_vectors=total_vectors)

    return {"success": True, "total_vectors_added": total_vectors}


def _store_screenshot_analysis(qdrant: QdrantManager, form_name: str, data: dict[str, Any]) -> int:
    """Store screenshot analysis in vector store."""
    count = 0

    for screen in data.get("screen_analyses", []):
        elements_text = "\n".join(
            [
                f"- {e.get('element_type', '')}: {e.get('label', '')} - {e.get('description', '')}"
                for e in screen.get("ui_elements", [])
            ]
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

    # Store UI flow summary
    if data.get("ui_flow_summary"):
        patterns = chr(10).join("- " + p for p in data.get("common_patterns", []))
        inventory = chr(10).join(
            f"- {k}: {v}" for k, v in data.get("component_inventory", {}).items()
        )

        content = f"""
UI Flow Summary for {form_name}:
{data.get("ui_flow_summary")}

Common Patterns:
{patterns}

Component Inventory:
{inventory}
"""
        count += qdrant.add_text(
            form_name=form_name,
            text=content,
            metadata={"form_name": form_name, "analysis_type": "ui_flow_summary"},
            doc_type="screenshot_analysis",
        )

    return count


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
            [
                f"{s.get('step_number', '')}. {s.get('action', '')} - {s.get('screen', '')}"
                for s in flow.get("steps", [])
            ]
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

    # Save markdown file
    md_file = output_path / f"{form_name}_PRD.md"
    md_file.write_text(prd_content, encoding="utf-8")

    # Save metadata
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
async def ensure_minio_folders_activity(form_name: str, bucket: str | None = None) -> dict[str, Any]:
    """
    Ensure MinIO folder structure exists for a form (only creates if missing).

    Verifies bucket exists (throws error if not), then ensures folders exist:
    - FORMS/{FORM_NAME}/FORM_DOCS/
    - FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/
    - FORMS/{FORM_NAME}/UI_SCREENSHOTS/

    Args:
        form_name: Form identifier
        bucket: Optional bucket name (defaults to "metadatas")

    Returns:
        Dictionary with creation status
    """
    from src.utils.minio_sync import MinioSync

    try:
        # Use default bucket (metadatas) if not specified
        sync = MinioSync(bucket=bucket)  # bucket=None uses default "metadatas" from settings
        logger.info("Ensuring MinIO folder structure", bucket=sync.bucket, form_name=form_name)
        
        # Verify bucket exists (throws error if not)
        sync.ensure_bucket(bucket=None, must_exist=True)
        
        # Create base folder structure if needed (only creates if missing)
        base_results = sync.create_folder_structure(bucket=None)  # Uses sync.bucket (metadatas)
        # Create form-specific folders (only creates if missing)
        form_results = sync.create_form_folders(form_name, bucket=None)  # Uses sync.bucket (metadatas)

        logger.info(
            "Ensured MinIO folder structure",
            form_name=form_name,
            base_folders=base_results,
            form_folders=form_results,
        )

        return {
            "success": True,
            "form_name": form_name,
            "base_folders": base_results,
            "form_folders": form_results,
        }
    except ValueError as e:
        # Bucket doesn't exist - this is a critical error
        logger.error("Bucket does not exist - workflow terminated", bucket=sync.bucket if 'sync' in locals() else bucket, error=str(e))
        raise  # Re-raise to terminate workflow
    except Exception as e:
        logger.error("Failed to ensure MinIO folders", form_name=form_name, error=str(e))
        raise  # Re-raise to fail the workflow
