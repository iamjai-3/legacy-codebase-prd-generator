"""Storage activities for PRD generation workflow."""

from datetime import datetime
from typing import Any

from temporalio import activity

from src.extractors.jira_extractor import JiraExtractor
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
    jira_data: dict[str, Any] | None = None,
    recreate_collection: bool = False,
) -> dict[str, Any]:
    """Store all extracted data as vectors in Qdrant."""
    logger.info("Starting vector storage", form_name=form_name)

    qdrant = QdrantManager()
    collection_name = qdrant.create_collection(form_name=form_name, recreate=recreate_collection)
    total_vectors = 0

    # Store code vectors
    if code_data:
        for file_info in code_data.get("files", []):
            content = _format_code_for_vector(file_info)
            count = qdrant.add_text(
                form_name=form_name, text=content, metadata=file_info, doc_type="code"
            )
            total_vectors += count

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

    # Store Jira vectors
    if jira_data:
        jira_extractor = JiraExtractor()
        issues = jira_data.get("raw_issues", [])
        if issues:
            documents = jira_extractor.to_documents(issues, form_name)
            count = qdrant.add_documents(form_name, documents)
            total_vectors += count

    stats = qdrant.get_collection_stats(form_name)

    return {
        "success": True,
        "collection_name": collection_name,
        "total_vectors_added": total_vectors,
        "collection_stats": stats,
    }


def _format_code_for_vector(file_info: dict[str, Any]) -> str:
    """Format code file info for vectorization."""
    return f"""
File: {file_info.get("path", "")}
Language: {file_info.get("language", "")}
Type: {file_info.get("file_type", "")}
Classes: {", ".join(file_info.get("classes", []))}
Methods: {", ".join(file_info.get("methods", []))}
"""


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
    risk_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Store analysis results in the vector knowledge base."""
    logger.info("Storing analysis results in vector store", form_name=form_name)

    qdrant = QdrantManager()
    total_vectors = 0

    # Store screenshot analysis results
    if screenshot_analysis and screenshot_analysis.get("success"):
        total_vectors += _store_screenshot_analysis(qdrant, form_name, screenshot_analysis)

    # Store requirements analysis
    if requirements_analysis and requirements_analysis.get("success"):
        total_vectors += _store_requirements_analysis(qdrant, form_name, requirements_analysis)

    # Store user flow analysis
    if user_flow_analysis and user_flow_analysis.get("success"):
        total_vectors += _store_user_flow_analysis(qdrant, form_name, user_flow_analysis)

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
