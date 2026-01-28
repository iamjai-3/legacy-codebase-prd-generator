"""
Minio Extractor for retrieving and processing screenshots from object storage.
"""

import base64
import io
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from langchain_core.documents import Document
from minio import Minio
from minio.error import S3Error
from PIL import Image

from src.config.settings import get_settings
from src.utils.file_utils import ensure_directory
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class Screenshot:
    """Represents a screenshot from Minio storage."""

    object_name: str
    bucket: str
    form_name: str
    screen_type: str
    image_data: bytes
    content_type: str
    size: int
    metadata: dict[str, Any]


# Screen type mapping for cleaner code
SCREEN_TYPE_KEYWORDS: dict[str, list[str]] = {
    "main_screen": ["main", "home"],
    "form_screen": ["form", "input"],
    "list_screen": ["list", "grid"],
    "detail_screen": ["detail", "view"],
    "dialog": ["dialog", "modal", "popup"],
    "navigation": ["menu", "nav"],
    "error_screen": ["error", "warning"],
    "report": ["report", "print"],
}


class MinioExtractor:
    """
    Extracts screenshots from Minio object storage for a given form.
    Handles image retrieval, preprocessing, and conversion to documents.
    """

    SUPPORTED_FORMATS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}
    DEFAULT_CONTENT_TYPE = "image/png"

    def __init__(self) -> None:
        """Initialize the Minio extractor."""
        self.settings = get_settings()
        self._client: Minio | None = None

    @property
    def client(self) -> Minio:
        """Get or create the Minio client."""
        if self._client is None:
            self._client = Minio(
                self.settings.minio.endpoint,
                access_key=self.settings.minio.access_key,
                secret_key=self.settings.minio.secret_key,
                secure=self.settings.minio.secure,
            )
            logger.info("Connected to Minio", endpoint=self.settings.minio.endpoint)
        return self._client

    def get_form_screenshots(
        self, form_name: str, bucket: str | None = None, prefix: str | None = None
    ) -> list[Screenshot]:
        """
        Retrieve all screenshots for a specific form.

        Args:
            form_name: Name of the form (e.g., 'le01')
            bucket: Optional bucket name (defaults to configured bucket)
            prefix: Optional prefix to filter objects

        Returns:
            List of Screenshot objects, sorted by object name
        """
        bucket = bucket or self.settings.minio.bucket
        self._verify_bucket_exists(bucket)

        search_prefix = self._get_search_prefix(form_name, prefix)
        all_objects = self._list_objects_with_prefix(bucket, search_prefix)
        image_objects = self._filter_image_objects(all_objects, form_name, bucket)

        logger.info(
            f"Processing {len(image_objects)} images",
            form_name=form_name,
            bucket=bucket,
        )

        screenshots = self._fetch_screenshots(image_objects, bucket, form_name)

        logger.info(
            "Retrieved screenshots from Minio",
            form_name=form_name,
            bucket=bucket,
            count=len(screenshots),
        )

        return screenshots

    def _verify_bucket_exists(self, bucket: str) -> None:
        """Verify bucket exists, raise error if not."""
        if not self.client.bucket_exists(bucket):
            error_msg = f"Bucket '{bucket}' does not exist. Please create it in MinIO first."
            logger.error(error_msg)
            raise ValueError(error_msg)

    def _get_search_prefix(self, form_name: str, prefix: str | None) -> str:
        """Get the search prefix for listing objects."""
        if prefix is not None:
            return prefix
        form_name_upper = form_name.upper()
        search_prefix = f"FORMS/{form_name_upper}/UI_SCREENSHOTS/"
        logger.info("Searching screenshots in MinIO", prefix=search_prefix)
        return search_prefix

    def _list_objects_with_prefix(self, bucket: str, prefix: str) -> list[Any]:
        """List objects in bucket with given prefix."""
        try:
            objects = list(self.client.list_objects(bucket, prefix=prefix, recursive=True))
            if objects:
                logger.info(f"Found {len(objects)} objects with prefix '{prefix}'")
            return objects
        except S3Error as e:
            logger.warning(f"Error listing objects with prefix '{prefix}': {e}")
            return []

    def _filter_image_objects(self, objects: list[Any], form_name: str, bucket: str) -> list[Any]:
        """Filter objects to only include supported image formats."""
        image_objects = []
        form_name_lower = form_name.lower()
        bucket_lower = bucket.lower()

        for obj in objects:
            ext = Path(obj.object_name).suffix.lower()
            if ext not in self.SUPPORTED_FORMATS:
                continue

            if self._should_include_object(obj, form_name_lower, bucket_lower):
                image_objects.append(obj)

        # Sort by object name for consistent ordering
        image_objects.sort(key=lambda x: x.object_name)
        return image_objects

    def _should_include_object(self, obj: Any, form_name_lower: str, bucket_lower: str) -> bool:
        """Check if object should be included based on form name."""
        # If bucket name matches form name, include all images
        if bucket_lower == form_name_lower:
            return True

        # Otherwise, filter by form name in path
        obj_name_lower = obj.object_name.lower()
        return (
            obj_name_lower.startswith(form_name_lower)
            or f"/{form_name_lower}/" in obj_name_lower
            or obj_name_lower.startswith(f"{form_name_lower}.")
        )

    def _fetch_screenshots(
        self, objects: list[Any], bucket: str, form_name: str
    ) -> list[Screenshot]:
        """Fetch screenshot data for each object."""
        screenshots: list[Screenshot] = []

        for obj in objects:
            screenshot = self._fetch_single_screenshot(obj, bucket, form_name)
            if screenshot:
                screenshots.append(screenshot)

        return screenshots

    def _fetch_single_screenshot(self, obj: Any, bucket: str, form_name: str) -> Screenshot | None:
        """Fetch a single screenshot from MinIO."""
        try:
            response = self.client.get_object(bucket, obj.object_name)
            image_data = response.read()
            response.close()
            response.release_conn()

            ext = Path(obj.object_name).suffix.lower()
            screen_type = self._determine_screen_type(obj.object_name)
            content_type = obj.content_type or f"image/{ext[1:]}"

            screenshot = Screenshot(
                object_name=obj.object_name,
                bucket=bucket,
                form_name=form_name,
                screen_type=screen_type,
                image_data=image_data,
                content_type=content_type,
                size=obj.size,
                metadata=obj.metadata or {},
            )

            logger.debug(
                "Retrieved screenshot",
                object_name=obj.object_name,
                screen_type=screen_type,
                size=obj.size,
            )

            return screenshot

        except S3Error as e:
            logger.warning(
                "Failed to retrieve screenshot",
                object_name=obj.object_name,
                error=str(e),
            )
            return None

    def get_screenshot(self, bucket: str, object_name: str) -> Screenshot | None:
        """
        Get a single screenshot from Minio.

        Args:
            bucket: Minio bucket name
            object_name: Object name/path

        Returns:
            Screenshot object or None if not found
        """
        try:
            response = self.client.get_object(bucket, object_name)
            image_data = response.read()
            response.close()
            response.release_conn()

            ext = Path(object_name).suffix.lower()
            screen_type = self._determine_screen_type(object_name)
            content_type = f"image/{ext[1:]}" if ext else self.DEFAULT_CONTENT_TYPE

            return Screenshot(
                object_name=object_name,
                bucket=bucket,
                form_name=Path(object_name).stem,
                screen_type=screen_type,
                image_data=image_data,
                content_type=content_type,
                size=len(image_data),
                metadata={},
            )
        except S3Error as e:
            logger.warning(
                "Failed to get screenshot from Minio",
                bucket=bucket,
                object_name=object_name,
                error=str(e),
            )
            return None

    def _determine_screen_type(self, object_name: str) -> str:
        """Determine the type of screen from the object name."""
        name_lower = object_name.lower()

        for screen_type, keywords in SCREEN_TYPE_KEYWORDS.items():
            if any(keyword in name_lower for keyword in keywords):
                return screen_type

        return "general"

    def save_screenshots_locally(
        self, screenshots: list[Screenshot], output_dir: str | Path
    ) -> list[Path]:
        """
        Save screenshots to local filesystem.

        Args:
            screenshots: List of screenshots to save
            output_dir: Directory to save screenshots

        Returns:
            List of saved file paths
        """
        output_path = ensure_directory(output_dir)
        saved_paths: list[Path] = []

        for screenshot in screenshots:
            file_path = self._save_single_screenshot(screenshot, output_path)
            saved_paths.append(file_path)

        logger.info(
            "Saved screenshots locally",
            count=len(saved_paths),
            directory=str(output_path),
        )

        return saved_paths

    def _save_single_screenshot(self, screenshot: Screenshot, output_dir: Path) -> Path:
        """Save a single screenshot to the filesystem."""
        form_dir = output_dir / screenshot.form_name
        ensure_directory(form_dir)

        filename = Path(screenshot.object_name).name
        file_path = form_dir / filename

        file_path.write_bytes(screenshot.image_data)
        return file_path

    def get_image_base64(self, screenshot: Screenshot) -> str:
        """
        Convert screenshot to base64 string for LLM vision APIs.

        Args:
            screenshot: Screenshot object

        Returns:
            Base64 encoded string
        """
        return base64.b64encode(screenshot.image_data).decode("utf-8")

    def get_image_dimensions(self, screenshot: Screenshot) -> tuple[int, int]:
        """
        Get dimensions of a screenshot.

        Args:
            screenshot: Screenshot object

        Returns:
            Tuple of (width, height)
        """
        image = Image.open(io.BytesIO(screenshot.image_data))
        return image.size

    def to_documents(
        self, screenshots: list[Screenshot], include_base64: bool = False
    ) -> list[Document]:
        """
        Convert screenshots to LangChain Documents.

        Args:
            screenshots: List of screenshots
            include_base64: Whether to include base64 data in content

        Returns:
            List of LangChain Documents
        """
        documents = [
            self._screenshot_to_document(screenshot, include_base64) for screenshot in screenshots
        ]

        logger.info("Converted screenshots to documents", count=len(documents))
        return documents

    def _screenshot_to_document(self, screenshot: Screenshot, include_base64: bool) -> Document:
        """Convert a single screenshot to a LangChain Document."""
        width, height = self.get_image_dimensions(screenshot)

        content_parts = [
            f"Screenshot: {screenshot.object_name}",
            f"Form: {screenshot.form_name}",
            f"Screen Type: {screenshot.screen_type}",
            f"Dimensions: {width}x{height}",
            f"Size: {screenshot.size} bytes",
        ]

        if include_base64:
            content_parts.append(f"Base64: {self.get_image_base64(screenshot)}")

        metadata = {
            "form_name": screenshot.form_name,
            "object_name": screenshot.object_name,
            "screen_type": screenshot.screen_type,
            "width": width,
            "height": height,
            "size_bytes": screenshot.size,
            "content_type": screenshot.content_type,
            "doc_type": "screenshot",
        }

        return Document(page_content="\n".join(content_parts), metadata=metadata)

    def upload_screenshot(
        self, file_path: str | Path, form_name: str, bucket: str | None = None
    ) -> str:
        """
        Upload a screenshot to Minio.

        Args:
            file_path: Path to the image file
            form_name: Form name for organizing the upload
            bucket: Optional bucket name

        Returns:
            Object name in Minio

        Raises:
            ValueError: If bucket does not exist
        """
        file_path = Path(file_path)
        bucket = bucket or self.settings.minio.bucket
        object_name = f"{form_name}/{file_path.name}"

        self._verify_bucket_exists(bucket)

        self.client.fput_object(bucket, object_name, str(file_path))
        logger.info("Uploaded screenshot", object_name=object_name, bucket=bucket)

        return object_name

    def list_form_folders(self, bucket: str | None = None) -> list[str]:
        """
        List all form folders in the bucket.

        Args:
            bucket: Optional bucket name

        Returns:
            List of form folder names
        """
        bucket = bucket or self.settings.minio.bucket

        if not self.client.bucket_exists(bucket):
            return []

        folders: set[str] = set()
        objects = self.client.list_objects(bucket, recursive=False)

        for obj in objects:
            if obj.is_dir:
                folders.add(obj.object_name.rstrip("/"))

        return sorted(folders)
