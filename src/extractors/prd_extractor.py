"""
PRD Extractor for processing existing PRD documentation.

Extracts markdown documents and images from the src/PRDs/{form_name}/ folder
to build a comprehensive knowledge base for migration.
"""

import base64
from dataclasses import dataclass, field
from pathlib import Path

from src.config.settings import get_settings
from src.utils.logging_config import get_logger

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


@dataclass
class PRDImage:
    """Represents a PRD image/screenshot."""

    path: str
    filename: str
    image_data: bytes | None = None
    base64_data: str = ""
    content_type: str = "image/png"
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

    def __init__(self, prd_base_dir: str | Path | None = None) -> None:
        """
        Initialize the PRD extractor.

        Args:
            prd_base_dir: Base directory for PRDs. Defaults to src/PRDs
        """
        self.settings = get_settings()

        if prd_base_dir:
            self.prd_base_dir = Path(prd_base_dir)
        else:
            # Default to src/PRDs relative to project root
            self.prd_base_dir = Path(__file__).parent.parent / "PRDs"

    def get_form_prd_directory(self, form_name: str) -> Path | None:
        """
        Get the PRD directory for a specific form.

        Args:
            form_name: Form identifier (e.g., "le11", "LE11", "leo7")

        Returns:
            Path to PRD directory if exists, None otherwise
        """
        # Normalize form name: handle typos like "leo7" -> "le07"
        normalized = form_name.lower().replace("leo", "le0") if "leo" in form_name.lower() else form_name
        
        # Try different case variations, prioritizing uppercase (standard format)
        variations = [
            normalized.upper(),  # LE07, LE11 (standard format)
            normalized.lower(),  # le07, le11
            normalized.capitalize(),  # Le07, Le11
            normalized,  # Original
            form_name.upper(),  # Also try original in uppercase
            form_name.lower(),  # Also try original in lowercase
        ]

        for variant in variations:
            prd_dir = self.prd_base_dir / variant
            if prd_dir.exists() and prd_dir.is_dir():
                logger.info(f"Found PRD directory: {prd_dir} (searched for: {form_name})")
                return prd_dir

        logger.warning(f"No PRD directory found for form: {form_name} (tried variations: {variations})")
        return None

    def extract_existing_prd(self, form_name: str) -> ExistingPRD | None:
        """
        Extract all PRD documentation for a form.

        Args:
            form_name: Form identifier

        Returns:
            ExistingPRD object with all documents and images, or None if not found
        """
        prd_dir = self.get_form_prd_directory(form_name)

        if not prd_dir:
            logger.info(f"No existing PRD found for {form_name}")
            return None

        logger.info(f"Extracting existing PRD from: {prd_dir}")

        documents = self._extract_documents(prd_dir, form_name)
        images = self._extract_images(prd_dir, form_name)

        # Combine all markdown content for knowledge base
        combined_content = self._combine_documents(documents)

        existing_prd = ExistingPRD(
            form_name=form_name,
            prd_directory=str(prd_dir),
            documents=documents,
            images=images,
            total_documents=len(documents),
            total_images=len(images),
            combined_content=combined_content,
        )

        logger.info(
            f"Extracted PRD for {form_name}: " f"{len(documents)} documents, {len(images)} images"
        )

        return existing_prd

    def _extract_documents(self, prd_dir: Path, form_name: str) -> list[PRDDocument]:
        """Extract all markdown documents from the PRD directory."""
        documents = []

        for file_path in prd_dir.iterdir():
            if file_path.suffix.lower() in self.MARKDOWN_EXTENSIONS:
                try:
                    content = file_path.read_text(encoding="utf-8")
                    doc_type = self._determine_document_type(file_path.name, form_name)
                    title = self._extract_title(content)

                    document = PRDDocument(
                        path=str(file_path),
                        filename=file_path.name,
                        content=content,
                        document_type=doc_type,
                        title=title,
                        word_count=len(content.split()),
                        section_count=content.count("## ") + content.count("# "),
                    )
                    documents.append(document)

                    logger.debug(f"Extracted document: {file_path.name} ({doc_type})")

                except Exception as e:
                    logger.warning(f"Failed to read document {file_path}: {e}")

        # Sort by document type importance
        type_order = ["description", "requirements", "sourcetables", "prompt"]
        documents.sort(
            key=lambda d: (
                type_order.index(d.document_type)
                if d.document_type in type_order
                else len(type_order)
            )
        )

        return documents

    def _extract_images(self, prd_dir: Path, form_name: str) -> list[PRDImage]:
        """Extract all images from the PRD directory."""
        images = []

        for file_path in prd_dir.iterdir():
            if file_path.suffix.lower() in self.IMAGE_EXTENSIONS:
                try:
                    image_data = file_path.read_bytes()
                    base64_data = base64.b64encode(image_data).decode("utf-8")

                    # Derive description from filename
                    description = self._filename_to_description(file_path.stem)

                    # Determine content type
                    content_type = self._get_content_type(file_path.suffix)

                    image = PRDImage(
                        path=str(file_path),
                        filename=file_path.name,
                        image_data=image_data,
                        base64_data=base64_data,
                        content_type=content_type,
                        description=description,
                        size=len(image_data),
                    )
                    images.append(image)

                    logger.debug(f"Extracted image: {file_path.name}")

                except Exception as e:
                    logger.warning(f"Failed to read image {file_path}: {e}")

        return images

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
        return content_types.get(suffix.lower(), "image/png")

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

    def list_available_prds(self) -> list[str]:
        """List all available PRD form names."""
        if not self.prd_base_dir.exists():
            return []

        return [
            d.name for d in self.prd_base_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
        ]
