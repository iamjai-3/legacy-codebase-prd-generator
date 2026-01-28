"""
PRD Extractor for processing existing PRD documentation from MinIO only.

Extracts markdown documents and images from:
- MinIO bucket: FORMS/{form_name}/FORM_DOCS/ and FORMS/{form_name}/UI_SCREENSHOTS/

to build a comprehensive knowledge base for migration.
"""

import base64
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.config.settings import get_settings
from src.utils.logging_config import get_logger
from src.utils.minio_sync import MinioSync

logger = get_logger(__name__)


@dataclass
class PRDDocument:
    """Represents a PRD markdown document."""

    path: str
    filename: str
    content: str
    document_type: str  # description, prompt, requirements, source_tables, etc.
    title: str = ""
    word_count: int = 0
    section_count: int = 0


# Default content type constant
DEFAULT_IMAGE_CONTENT_TYPE = "image/png"


@dataclass
class PRDImage:
    """Represents a PRD image/screenshot."""

    path: str
    filename: str
    image_data: bytes | None = None
    base64_data: str = ""
    content_type: str = DEFAULT_IMAGE_CONTENT_TYPE
    description: str = ""  # Derived from filename
    size: int = 0


@dataclass
class ExistingPRD:
    """Represents an existing PRD folder with all its contents."""

    form_name: str
    prd_directory: str
    documents: list[PRDDocument] = field(default_factory=list)
    images: list[PRDImage] = field(default_factory=list)
    total_documents: int = 0
    total_images: int = 0
    combined_content: str = ""  # All markdown content combined


class PRDExtractor:

    DOCUMENT_TYPES = {
        "description": "Business description and overview",
        "prompt": "AI prompt for analysis",
        "requirementsprompt": "Requirements generation prompt",
        "sourcetables": "Database source tables documentation",
        "sourcetablesprompt": "Source tables analysis prompt",
    }

    IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}
    MARKDOWN_EXTENSIONS = {".md", ".markdown"}

    def __init__(
        self,
        use_minio: bool = True,
        minio_bucket: str | None = None,
    ) -> None:
        """
        Initialize the PRD extractor (MinIO only).

        Args:
            use_minio: Whether to read from MinIO bucket (default: True, required)
            minio_bucket: MinIO bucket name (defaults to configured bucket: metadatas)
        """
        self.settings = get_settings()
        self.use_minio = use_minio
        self.minio_bucket = minio_bucket or self.settings.minio.bucket
        self._minio_sync: MinioSync | None = None

    @property
    def minio_sync(self) -> MinioSync:
        """Get or create MinIO sync instance."""
        if self._minio_sync is None:
            self._minio_sync = MinioSync(bucket=self.minio_bucket)
        return self._minio_sync


    def extract_existing_prd(self, form_name: str) -> ExistingPRD | None:
        """
        Extract all PRD documentation for a form from MinIO only.

        Looks in: FORMS/{form_name}/FORM_DOCS/ and FORMS/{form_name}/UI_SCREENSHOTS/

        Args:
            form_name: Form identifier

        Returns:
            ExistingPRD object with all documents and images, or None if not found
        """
        # Only use MinIO, no local fallback
        try:
            existing_prd = self._extract_from_minio(form_name)
            if existing_prd:
                return existing_prd
        except Exception as e:
            logger.error(f"Failed to extract from MinIO: {e}", form_name=form_name, bucket=self.minio_bucket)
            return None

        logger.info(f"No existing PRD found in MinIO for {form_name}", bucket=self.minio_bucket)
        return None

    def _extract_from_minio(self, form_name: str) -> ExistingPRD | None:
        """Extract PRD from MinIO bucket using FORMS/{form_name}/ structure."""
        form_name_upper = form_name.upper()
        prefix = f"FORMS/{form_name_upper}/"

        logger.info("Extracting PRD from MinIO", form_name=form_name, prefix=prefix)

        # List all objects for this form
        objects = self.minio_sync.list_objects(prefix=prefix, bucket=self.minio_bucket)

        if not objects:
            logger.info(f"No objects found in MinIO for {form_name}")
            return None

        documents: list[PRDDocument] = []
        images: list[PRDImage] = []

        # Extract documents from FORM_DOCS/
        form_docs_prefix = f"{prefix}FORM_DOCS/"
        for obj_name in objects:
            if obj_name.startswith(form_docs_prefix) and obj_name.endswith((".md", ".markdown")):
                try:
                    content = self.minio_sync.get_file_text(obj_name, bucket=self.minio_bucket)
                    filename = Path(obj_name).name
                    doc_type = self._determine_document_type(filename, form_name)
                    title = self._extract_title(content)

                    document = PRDDocument(
                        path=obj_name,
                        filename=filename,
                        content=content,
                        document_type=doc_type,
                        title=title,
                        word_count=len(content.split()),
                        section_count=content.count("## ") + content.count("# "),
                    )
                    documents.append(document)
                    logger.debug("Extracted document from MinIO", filename=filename, doc_type=doc_type)
                except Exception as e:
                    logger.warning(f"Failed to read document {obj_name} from MinIO: {e}")

        # Extract images from UI_SCREENSHOTS/
        screenshots_prefix = f"{prefix}UI_SCREENSHOTS/"
        for obj_name in objects:
            if obj_name.startswith(screenshots_prefix):
                ext = Path(obj_name).suffix.lower()
                if ext in self.IMAGE_EXTENSIONS:
                    try:
                        image_data = self.minio_sync.get_file_content(obj_name, bucket=self.minio_bucket)
                        base64_data = base64.b64encode(image_data).decode("utf-8")
                        filename = Path(obj_name).name
                        description = self._filename_to_description(Path(obj_name).stem)
                        content_type = self._get_content_type(ext)

                        image = PRDImage(
                            path=obj_name,
                            filename=filename,
                            image_data=image_data,
                            base64_data=base64_data,
                            content_type=content_type,
                            description=description,
                            size=len(image_data),
                        )
                        images.append(image)
                        logger.debug(f"Extracted image from MinIO: {filename}")
                    except Exception as e:
                        logger.warning(f"Failed to read image {obj_name} from MinIO: {e}")

        if not documents and not images:
            return None

        # Sort documents by type importance
        type_order = ["description", "requirements", "sourcetables", "prompt"]
        documents.sort(
            key=lambda d: (
                type_order.index(d.document_type)
                if d.document_type in type_order
                else len(type_order)
            )
        )

        combined_content = self._combine_documents(documents)

        existing_prd = ExistingPRD(
            form_name=form_name,
            prd_directory=f"MinIO:{self.minio_bucket}/{prefix}",
            documents=documents,
            images=images,
            total_documents=len(documents),
            total_images=len(images),
            combined_content=combined_content,
        )

        logger.info(
            f"Extracted PRD from MinIO for {form_name}: "
            f"{len(documents)} documents, {len(images)} images"
        )

        return existing_prd


    def _determine_document_type(self, filename: str, form_name: str) -> str:
        """Determine the document type from filename."""
        lower_filename = filename.lower()

        # Remove form name prefix if present
        lower_form = form_name.lower()
        if lower_filename.startswith(lower_form):
            lower_filename = lower_filename[len(lower_form) :]
            if lower_filename.startswith("_"):
                lower_filename = lower_filename[1:]

        # Check for known document types
        for doc_type, description in self.DOCUMENT_TYPES.items():
            if doc_type in lower_filename.replace("_", "").replace(".md", ""):
                return doc_type

        return "general"

    def _extract_title(self, content: str) -> str:
        """Extract the first heading as title."""
        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
        return ""

    def _filename_to_description(self, stem: str) -> str:
        """Convert filename stem to human-readable description."""
        # Replace hyphens and underscores with spaces
        description = stem.replace("-", " ").replace("_", " ")
        # Title case
        return description.title()

    def _get_content_type(self, suffix: str) -> str:
        """Get MIME content type for image."""
        content_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".webp": "image/webp",
            ".bmp": "image/bmp",
        }
        return content_types.get(suffix.lower(), DEFAULT_IMAGE_CONTENT_TYPE)

    def _combine_documents(self, documents: list[PRDDocument]) -> str:
        """Combine all document content into a single string for embedding."""
        combined_parts = []

        for doc in documents:
            header = f"\n\n{'='*60}\n"
            header += f"DOCUMENT: {doc.filename}\n"
            header += f"TYPE: {doc.document_type}\n"
            header += f"{'='*60}\n\n"

            combined_parts.append(header + doc.content)

        return "\n".join(combined_parts)

