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


class MinioExtractor:
    """
    Extracts screenshots from Minio object storage for a given form.
    Handles image retrieval, preprocessing, and conversion to documents.
    """

    SUPPORTED_FORMATS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}

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
            prefix: Optional prefix to filter objects (if None, searches all images in bucket)

        Returns:
            List of Screenshot objects, sorted by object name
        """
        bucket = bucket or self.settings.minio.bucket

        screenshots: list[Screenshot] = []

        try:
            # Verify bucket exists (required - don't create)
            if not self.client.bucket_exists(bucket):
                error_msg = f"Bucket '{bucket}' does not exist. Please create the 'metadatas' bucket in MinIO first."
                logger.error(error_msg)
                raise ValueError(error_msg)

            # Determine search strategy:
            # Use FORMS/{FORM_NAME}/UI_SCREENSHOTS/ structure within the metadatas bucket
            form_name_upper = form_name.upper()
            form_screenshots_prefix = f"FORMS/{form_name_upper}/UI_SCREENSHOTS/"

            search_prefixes: list[str | None] = []

            if prefix is not None:
                # Explicit prefix provided
                search_prefixes = [prefix]
            else:
                # Use standard structure: FORMS/{FORM_NAME}/UI_SCREENSHOTS/
                search_prefixes = [form_screenshots_prefix]
                logger.info(
                    "Searching screenshots in MinIO", bucket=bucket, prefix=form_screenshots_prefix
                )

            all_objects: list[Any] = []

            # Collect all matching objects
            for search_prefix in search_prefixes:
                try:
                    objects = list(
                        self.client.list_objects(
                            bucket,
                            prefix=search_prefix,
                            recursive=True,
                        )
                    )

                    if objects:
                        all_objects.extend(objects)
                        logger.info(f"Found {len(objects)} objects with prefix '{search_prefix}'")
                        # If we found objects with a prefix, don't try the fallback
                        if search_prefix is not None:
                            break
                except S3Error as e:
                    logger.warning(f"Error listing objects with prefix '{search_prefix}': {e}")
                    continue

            # Filter and process images
            image_objects = []
            for obj in all_objects:
                # Check if it's a supported image format
                ext = Path(obj.object_name).suffix.lower()
                if ext in self.SUPPORTED_FORMATS:
                    # If bucket name is form name, include ALL images in the bucket
                    # (the bucket itself provides the form context)
                    if bucket.lower() == form_name.lower():
                        image_objects.append(obj)
                    else:
                        # For general buckets, filter by form name in path
                        obj_name_lower = obj.object_name.lower()
                        form_name_lower = form_name.lower()
                        if (
                            obj_name_lower.startswith(form_name_lower)
                            or f"/{form_name_lower}/" in obj_name_lower
                            or obj_name_lower.startswith(f"{form_name_lower}.")
                        ):
                            image_objects.append(obj)

            # Sort by object name to process in order
            image_objects.sort(key=lambda x: x.object_name)

            logger.info(
                f"Processing {len(image_objects)} images in order",
                form_name=form_name,
                bucket=bucket,
            )

            # Process each image
            for obj in image_objects:
                try:
                    # Get the object
                    response = self.client.get_object(bucket, obj.object_name)
                    image_data = response.read()
                    response.close()
                    response.release_conn()

                    # Determine screen type from filename
                    screen_type = self._determine_screen_type(obj.object_name)

                    screenshot = Screenshot(
                        object_name=obj.object_name,
                        bucket=bucket,
                        form_name=form_name,
                        screen_type=screen_type,
                        image_data=image_data,
                        content_type=obj.content_type or f"image/{ext[1:]}",
                        size=obj.size,
                        metadata=obj.metadata or {},
                    )
                    screenshots.append(screenshot)

                    logger.debug(
                        "Retrieved screenshot",
                        object_name=obj.object_name,
                        screen_type=screen_type,
                        size=obj.size,
                    )

                except S3Error as e:
                    logger.warning(
                        "Failed to retrieve screenshot", object_name=obj.object_name, error=str(e)
                    )

            logger.info(
                "Retrieved screenshots from Minio",
                form_name=form_name,
                bucket=bucket,
                count=len(screenshots),
            )

        except S3Error as e:
            logger.error("Minio error", error=str(e))
            raise

        return screenshots

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

            return Screenshot(
                object_name=object_name,
                bucket=bucket,
                form_name=Path(object_name).stem,
                screen_type=screen_type,
                image_data=image_data,
                content_type=f"image/{ext[1:]}" if ext else "image/png",
                size=len(image_data),
                metadata={},
            )
        except Exception as e:
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

        if "main" in name_lower or "home" in name_lower:
            return "main_screen"
        elif "form" in name_lower or "input" in name_lower:
            return "form_screen"
        elif "list" in name_lower or "grid" in name_lower:
            return "list_screen"
        elif "detail" in name_lower or "view" in name_lower:
            return "detail_screen"
        elif "dialog" in name_lower or "modal" in name_lower or "popup" in name_lower:
            return "dialog"
        elif "menu" in name_lower or "nav" in name_lower:
            return "navigation"
        elif "error" in name_lower or "warning" in name_lower:
            return "error_screen"
        elif "report" in name_lower or "print" in name_lower:
            return "report"
        else:
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
        output_dir = ensure_directory(output_dir)
        saved_paths: list[Path] = []

        for screenshot in screenshots:
            # Create subdirectory for form
            form_dir = output_dir / screenshot.form_name
            ensure_directory(form_dir)

            # Save the image
            filename = Path(screenshot.object_name).name
            file_path = form_dir / filename

            with open(file_path, "wb") as f:
                f.write(screenshot.image_data)

            saved_paths.append(file_path)

        logger.info("Saved screenshots locally", count=len(saved_paths), directory=str(output_dir))

        return saved_paths

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
        documents: list[Document] = []

        for screenshot in screenshots:
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

            document = Document(
                page_content="\n".join(content_parts),
                metadata=metadata,
            )
            documents.append(document)

        logger.info("Converted screenshots to documents", count=len(documents))

        return documents

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
        """
        file_path = Path(file_path)
        bucket = bucket or self.settings.minio.bucket
        object_name = f"{form_name}/{file_path.name}"

        # Ensure bucket exists
        if not self.client.bucket_exists(bucket):
            self.client.make_bucket(bucket)

        # Upload file
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
