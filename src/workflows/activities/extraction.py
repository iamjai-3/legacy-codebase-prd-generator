"""Extraction activities for PRD generation workflow."""

from pathlib import Path
from typing import Any

from temporalio import activity

from src.extractors.code_extractor import CodeExtractor
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
) -> dict[str, Any]:
    """Extract and analyze code from a ZIP file or directory.

    This activity extracts code files and stores their content directly in the vector store
    to avoid exceeding Temporal activity result size limits. Only metadata is returned.
    """
    logger.info(
        "Starting code extraction",
        form_name=form_name,
        zip_path=zip_path,
        directory=code_directory,
    )

    extractor = CodeExtractor()
    extract_dir = None
    temp_zip_path: str | None = None

    # If no local path provided, try to load from MinIO LEGACY_CODEBASE/
    if not zip_path and not code_directory:
        from src.utils.minio_sync import MinioSync

        # Use default bucket (metadatas) for all MinIO operations
        minio_sync = MinioSync(bucket=None)  # None = use default from settings (metadatas)
        logger.info("Using MinIO bucket for legacy codebase", bucket=minio_sync.bucket)
        
        # Look for ZIP files in LEGACY_CODEBASE/ within the metadatas bucket
        legacy_objects = minio_sync.list_objects(prefix="LEGACY_CODEBASE/", bucket=None)
        logger.info("Checking MinIO for legacy codebase", bucket=minio_sync.bucket, prefix="LEGACY_CODEBASE/", objects_found=len(legacy_objects))
        
        zip_files = [obj for obj in legacy_objects if obj.lower().endswith('.zip')]
        
        if zip_files:
            # Use the first ZIP file found (or could be smarter about selection)
            zip_object_name = zip_files[0]
            logger.info("Loading legacy codebase from MinIO", object_name=zip_object_name, total_zips=len(zip_files))
            
            # Download ZIP to temporary location
            import tempfile
            with tempfile.NamedTemporaryFile(delete=False, suffix='.zip', delete_on_close=False) as tmp_file:
                zip_data = minio_sync.get_file_content(zip_object_name, bucket=None)  # Uses default metadatas bucket
                tmp_file.write(zip_data)
                zip_path = tmp_file.name
                temp_zip_path = zip_path  # Track for cleanup
                logger.info("Downloaded ZIP from MinIO to temporary file", path=zip_path, size=len(zip_data))
        else:
            logger.warning(
                "No ZIP file found in MinIO LEGACY_CODEBASE/",
                total_objects=len(legacy_objects),
                objects=legacy_objects[:10] if legacy_objects else []
            )
            return {
                "success": True,
                "files_count": 0,
                "files": [],
                "extract_dir": None,
            }

    if zip_path:
        # Determine extract directory (CodeExtractor uses uploads_dir by default)
        from src.config.settings import get_settings

        settings = get_settings()
        zip_path_obj = Path(zip_path)
        extract_dir = Path(settings.uploads_dir) / zip_path_obj.stem

        logger.info("Extracting code from ZIP", zip_path=zip_path, form_name=form_name, extract_dir=str(extract_dir))
        code_files = extractor.extract_from_zip(
            zip_path=zip_path, form_name=form_name
        )
        logger.info("Code extraction complete", files_extracted=len(code_files))
    elif code_directory:
        extract_dir = Path(code_directory)
        code_files = extractor.extract_from_directory(
            directory=code_directory, form_name=form_name
        )
    else:
        # No code source available
        logger.warning("No code source provided and none found in MinIO")
        return {
            "success": True,
            "files_count": 0,
            "files": [],
            "extract_dir": None,
        }

    # Limit metadata to avoid exceeding gRPC message size limits
    # Store only essential information, full content will be in vector store
    MAX_METHODS = 10
    MAX_IMPORTS = 10
    MAX_CLASSES = 5

    files_metadata = []
    total_size = 0
    MAX_METADATA_SIZE = 3 * 1024 * 1024  # 3MB limit for metadata

    for cf in code_files:
        # Calculate approximate size of this file's metadata
        file_meta_size = (
            len(cf.path)
            + len(cf.language)
            + len(cf.file_type)
            + sum(len(c) for c in cf.classes[:MAX_CLASSES])
            + sum(len(m) for m in cf.methods[:MAX_METHODS])
            + sum(len(i) for i in cf.imports[:MAX_IMPORTS])
            + 100  # overhead
        )

        # Skip if adding this would exceed limit
        if total_size + file_meta_size > MAX_METADATA_SIZE and len(files_metadata) > 0:
            logger.warning(
                f"Truncating file metadata at {len(files_metadata)} files to avoid size limit",
                form_name=form_name,
            )
            break

        files_metadata.append(
            {
                "path": cf.path,
                "language": cf.language,
                "file_type": cf.file_type,
                "classes": cf.classes[:MAX_CLASSES],
                "methods": cf.methods[:MAX_METHODS],
                "imports": cf.imports[:MAX_IMPORTS],
                "line_count": cf.line_count,
                "content_length": len(cf.content) if cf.content else 0,  # Store size, not content
            }
        )
        total_size += file_meta_size

    result = {
        "form_name": form_name,
        "file_count": len(code_files),
        "files": files_metadata,
        "languages": list({cf.language for cf in code_files}),
        "extract_dir": (
            str(extract_dir) if extract_dir else None
        ),  # Pass extract directory for file reading
        # Full file content is stored in vector store via store_vectors_activity
        # This avoids exceeding Temporal gRPC message size limits (4MB default)
    }
    
    # Clean up temporary ZIP file if it was downloaded from MinIO
    if temp_zip_path and Path(temp_zip_path).exists():
        try:
            import os
            os.unlink(temp_zip_path)
            logger.info("Cleaned up temporary ZIP file", path=temp_zip_path)
        except Exception as e:
            logger.warning("Failed to clean up temporary ZIP file", path=temp_zip_path, error=str(e))
    
    return result


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
async def extract_existing_prd_activity(
    form_name: str,
) -> dict[str, Any]:
    """
    Extract existing PRD documentation from MinIO only.

    This extracts markdown documents and images from:
    - FORMS/{form_name}/FORM_DOCS/ (markdown documents)
    - FORMS/{form_name}/UI_SCREENSHOTS/ (images)

    These are combined into the knowledge base for migration purposes.
    """
    logger.info(
        "Starting existing PRD extraction from MinIO",
        form_name=form_name,
    )

    # Only use MinIO, no local fallback
    extractor = PRDExtractor(use_minio=True)
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
