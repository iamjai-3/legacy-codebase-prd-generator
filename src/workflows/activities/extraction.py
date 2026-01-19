"""Extraction activities for PRD generation workflow."""

from typing import Any

from temporalio import activity

from src.extractors.code_extractor import CodeExtractor
from src.extractors.jira_extractor import JiraExtractor
from src.extractors.minio_extractor import MinioExtractor
from src.extractors.prd_extractor import PRDExtractor
from src.utils.logging_config import get_logger
from src.workflows.activities.common import to_dict

logger = get_logger(__name__)


@activity.defn
async def extract_code_activity(
    form_name: str,
    zip_path: str | None = None,
    code_directory: str | None = None,
    file_mappings: list[str] | None = None,
    dependency_file: str | None = None,
) -> dict[str, Any]:
    """Extract and analyze code from a ZIP file or directory."""
    logger.info(
        "Starting code extraction",
        form_name=form_name,
        zip_path=zip_path,
        directory=code_directory,
        dependency_file=dependency_file,
    )

    extractor = CodeExtractor()

    if zip_path:
        code_files = extractor.extract_from_zip(
            zip_path=zip_path, file_mappings=file_mappings, dependency_file=dependency_file
        )
    elif code_directory:
        code_files = extractor.extract_from_directory(
            directory=code_directory, file_mappings=file_mappings, dependency_file=dependency_file
        )
    else:
        raise ValueError("Either zip_path or code_directory must be provided")

    return {
        "form_name": form_name,
        "file_count": len(code_files),
        "files": [
            {
                "path": cf.path,
                "language": cf.language,
                "file_type": cf.file_type,
                "classes": cf.classes,
                "methods": cf.methods[:20],
                "imports": cf.imports[:20],
                "line_count": cf.line_count,
            }
            for cf in code_files
        ],
        "languages": list({cf.language for cf in code_files}),
        # Note: raw_files removed to avoid exceeding Temporal activity result size limit
        # Files are stored in vector store and can be retrieved from there if needed
    }


@activity.defn
async def extract_screenshots_activity(
    form_name: str,
    bucket: str | None = None,
    prefix: str | None = None,
) -> dict[str, Any]:
    """Extract screenshots from Minio storage."""
    logger.info("Starting screenshot extraction", form_name=form_name, bucket=bucket)

    extractor = MinioExtractor()
    screenshots = extractor.get_form_screenshots(form_name=form_name, bucket=bucket, prefix=prefix)

    return {
        "form_name": form_name,
        "screenshot_count": len(screenshots),
        "screenshots": [
            {
                "object_name": s.object_name,
                "screen_type": s.screen_type,
                "size": s.size,
                "content_type": s.content_type,
            }
            for s in screenshots
        ],
        "raw_screenshots": [to_dict(s) for s in screenshots],
    }


@activity.defn
async def extract_jira_activity(
    form_name: str,
    project_key: str | None = None,
    jql: str | None = None,
) -> dict[str, Any]:
    """Extract Jira issues for a form."""
    logger.info("Starting Jira extraction", form_name=form_name, project_key=project_key)

    extractor = JiraExtractor()

    try:
        issues = extractor.get_form_issues(
            form_name=form_name, project_key=project_key, additional_jql=jql
        )

        return {
            "form_name": form_name,
            "issue_count": len(issues),
            "issues": [
                {
                    "key": issue.key,
                    "summary": issue.summary,
                    "issue_type": issue.issue_type,
                    "status": issue.status,
                    "priority": issue.priority,
                }
                for issue in issues
            ],
            "raw_issues": issues,
        }
    except Exception as e:
        logger.warning("Jira extraction failed", error=str(e))
        return {
            "form_name": form_name,
            "issue_count": 0,
            "issues": [],
            "raw_issues": [],
            "error": str(e),
        }


@activity.defn
async def extract_existing_prd_activity(
    form_name: str,
    prd_base_dir: str | None = None,
) -> dict[str, Any]:
    """
    Extract existing PRD documentation from src/PRDs folder.
    
    This extracts markdown documents and images that contain:
    - Business logic descriptions
    - Requirements documentation
    - Source table mappings
    - UI screenshots with annotations
    
    These are combined into the knowledge base for migration purposes.
    """
    logger.info("Starting existing PRD extraction", form_name=form_name, prd_base_dir=prd_base_dir)

    extractor = PRDExtractor(prd_base_dir=prd_base_dir)
    existing_prd = extractor.extract_existing_prd(form_name)

    if not existing_prd:
        logger.info(f"No existing PRD found for {form_name}")
        return {
            "form_name": form_name,
            "success": False,
            "document_count": 0,
            "image_count": 0,
            "documents": [],
            "images": [],
            "combined_content": "",
        }

    # Serialize documents (exclude raw image bytes to avoid large payloads)
    documents_data = [
        {
            "path": doc.path,
            "filename": doc.filename,
            "content": doc.content,
            "document_type": doc.document_type,
            "title": doc.title,
            "word_count": doc.word_count,
            "section_count": doc.section_count,
        }
        for doc in existing_prd.documents
    ]

    # Serialize images (include base64 for vector store, exclude raw bytes)
    images_data = [
        {
            "path": img.path,
            "filename": img.filename,
            "base64_data": img.base64_data,
            "content_type": img.content_type,
            "description": img.description,
            "size": img.size,
        }
        for img in existing_prd.images
    ]

    logger.info(
        f"Extracted existing PRD for {form_name}: "
        f"{len(documents_data)} documents, {len(images_data)} images"
    )

    return {
        "form_name": form_name,
        "success": True,
        "prd_directory": existing_prd.prd_directory,
        "document_count": len(documents_data),
        "image_count": len(images_data),
        "documents": documents_data,
        "images": images_data,
        "combined_content": existing_prd.combined_content,
        "total_words": sum(doc.word_count for doc in existing_prd.documents),
    }
