"""
Utility to sync PRD files from local filesystem to MinIO bucket.

Maintains the same folder structure:
- FORMS/{FORM_NAME}/FORM_DOCS/
- FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/
- FORMS/{FORM_NAME}/UI_SCREENSHOTS/
- DB_PRD/
- EXPORT_CODEBASE_PRD/
- LEGACY_CODEBASE/
"""

import mimetypes
from pathlib import Path
from typing import Any

from minio import Minio
from minio.error import S3Error

from src.config.settings import get_settings
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class MinioSync:
    """Utility class for syncing PRD files to MinIO bucket."""

    def __init__(self, bucket: str | None = None) -> None:
        """Initialize MinIO sync utility."""
        self.settings = get_settings()
        self.bucket = bucket or self.settings.minio.bucket
        self._client: Minio | None = None

    @property
    def client(self) -> Minio:
        """Get or create the MinIO client."""
        if self._client is None:
            self._client = Minio(
                self.settings.minio.endpoint,
                access_key=self.settings.minio.access_key,
                secret_key=self.settings.minio.secret_key,
                secure=self.settings.minio.secure,
            )
            logger.info("Connected to MinIO", endpoint=self.settings.minio.endpoint)
        return self._client

    def ensure_bucket(self, bucket: str | None = None, must_exist: bool = True) -> None:
        """
        Verify bucket exists (never creates buckets).
        
        Args:
            bucket: Bucket name (defaults to configured bucket: "metadatas")
            must_exist: If True, throw error if bucket doesn't exist (default: True)
        
        Raises:
            ValueError: If bucket doesn't exist and must_exist=True
        """
        bucket = bucket or self.bucket
        try:
            if not self.client.bucket_exists(bucket):
                error_msg = f"Bucket '{bucket}' does not exist. Please create the 'metadatas' bucket in MinIO first before running the workflow."
                logger.error(error_msg)
                raise ValueError(error_msg)
            logger.debug("Bucket exists", bucket=bucket)
        except S3Error as e:
            logger.error("Failed to check bucket", bucket=bucket, error=str(e))
            raise ValueError(f"Failed to verify bucket '{bucket}': {e}") from e

    def upload_file(
        self,
        local_path: str | Path,
        object_name: str,
        bucket: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> str:
        """
        Upload a file to MinIO.

        Args:
            local_path: Local file path
            object_name: Object name in MinIO (path within bucket)
            bucket: Bucket name (defaults to configured bucket)
            metadata: Optional metadata dict

        Returns:
            Object name
        """
        local_path = Path(local_path)
        bucket = bucket or self.bucket

        if not local_path.exists():
            raise FileNotFoundError(f"File not found: {local_path}")

        # Verify bucket exists (don't create)
        self.ensure_bucket(bucket, must_exist=True)

        # Determine content type
        content_type, _ = mimetypes.guess_type(str(local_path))
        if not content_type:
            content_type = "application/octet-stream"

        # Upload file
        self.client.fput_object(
            bucket,
            object_name,
            str(local_path),
            content_type=content_type,
            metadata=metadata or {},
        )

        logger.info(
            "Uploaded file to MinIO",
            local_path=str(local_path),
            object_name=object_name,
            bucket=bucket,
            size=local_path.stat().st_size,
        )

        return object_name

    def upload_directory(
        self,
        local_dir: str | Path,
        prefix: str = "",
        bucket: str | None = None,
        exclude_patterns: list[str] | None = None,
    ) -> int:
        """
        Upload a directory tree to MinIO, preserving structure.

        Args:
            local_dir: Local directory path
            prefix: Prefix to add to all object names (e.g., "FORMS/LE07/")
            bucket: Bucket name
            exclude_patterns: List of patterns to exclude (e.g., ["*.pyc", "__pycache__"])

        Returns:
            Number of files uploaded
        """
        local_dir = Path(local_dir)
        bucket = bucket or self.bucket
        exclude_patterns = exclude_patterns or []

        if not local_dir.exists() or not local_dir.is_dir():
            raise ValueError(f"Directory not found: {local_dir}")

        # Verify bucket exists (don't create)
        self.ensure_bucket(bucket, must_exist=True)

        uploaded_count = 0

        # Walk directory tree
        for file_path in local_dir.rglob("*"):
            if not file_path.is_file():
                continue

            # Check exclude patterns
            if any(file_path.match(pattern) for pattern in exclude_patterns):
                continue

            # Calculate relative path and object name
            relative_path = file_path.relative_to(local_dir)
            object_name = f"{prefix}{relative_path.as_posix()}" if prefix else relative_path.as_posix()

            try:
                self.upload_file(file_path, object_name, bucket)
                uploaded_count += 1
            except Exception as e:
                logger.warning(
                    "Failed to upload file",
                    file_path=str(file_path),
                    object_name=object_name,
                    error=str(e),
                )

        logger.info(
            "Uploaded directory to MinIO",
            local_dir=str(local_dir),
            prefix=prefix,
            bucket=bucket,
            files_uploaded=uploaded_count,
        )

        return uploaded_count

    def create_folder_structure(self, bucket: str | None = None) -> dict[str, bool]:
        """
        Create empty folder structure in MinIO bucket (only if they don't exist).

        Creates:
        - FORMS/ (parent folder for all forms)
        - DB_PRD/
        - EXPORT_CODEBASE_PRD/
        - LEGACY_CODEBASE/

        Args:
            bucket: Bucket name

        Returns:
            Dictionary with creation status for each folder
        """
        bucket = bucket or self.bucket
        # Check bucket exists, don't create it
        self.ensure_bucket(bucket, must_exist=True)

        results = {
            "FORMS": False,
            "DB_PRD": False,
            "EXPORT_CODEBASE_PRD": False,
            "LEGACY_CODEBASE": False,
        }

        # Create folders by uploading empty placeholder files
        # MinIO doesn't have true folders, so we create empty marker files
        folders = ["FORMS/", "DB_PRD/", "EXPORT_CODEBASE_PRD/", "LEGACY_CODEBASE/"]

        for folder in folders:
            try:
                # Check if folder already exists (check for .keep file or any object with prefix)
                marker_name = f"{folder}.keep"
                # List objects with this prefix to see if folder exists
                existing_objects = list(self.client.list_objects(bucket, prefix=folder, recursive=False))
                if any(existing_objects):
                    # Folder already exists
                    results[folder.rstrip("/")] = True
                    logger.debug(f"Folder already exists: {folder}", bucket=bucket)
                    continue
                
                # Create a .keep file to establish the folder structure
                from io import BytesIO
                empty_content = BytesIO(b"")
                self.client.put_object(
                    bucket,
                    marker_name,
                    empty_content,
                    length=0,
                    content_type="application/octet-stream",
                )
                results[folder.rstrip("/")] = True
                logger.info(f"Created folder structure: {folder}", bucket=bucket)
            except Exception as e:
                logger.warning(f"Failed to create folder {folder}: {e}")
                results[folder.rstrip("/")] = False

        return results

    def create_form_folders(self, form_name: str, bucket: str | None = None) -> dict[str, bool]:
        """
        Create folder structure for a specific form in MinIO (only if they don't exist).

        Creates:
        - FORMS/{FORM_NAME}/FORM_DOCS/
        - FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/
        - FORMS/{FORM_NAME}/UI_SCREENSHOTS/

        Args:
            form_name: Form identifier (e.g., "LE11", "le11")
            bucket: Bucket name

        Returns:
            Dictionary with creation status for each folder
        """
        bucket = bucket or self.bucket
        form_name_upper = form_name.upper()

        # Ensure base FORMS folder exists (only creates if missing)
        self.create_folder_structure(bucket)

        # Check bucket exists, don't create it
        self.ensure_bucket(bucket, must_exist=True)

        results = {
            "FORM_DOCS": False,
            "FORM_FILE_DEPENDENCIES": False,
            "UI_SCREENSHOTS": False,
        }

        # Create form-specific folders
        folders = [
            f"FORMS/{form_name_upper}/FORM_DOCS/",
            f"FORMS/{form_name_upper}/FORM_FILE_DEPENDENCIES/",
            f"FORMS/{form_name_upper}/UI_SCREENSHOTS/",
        ]

        for folder in folders:
            try:
                # Check if folder already exists
                existing_objects = list(self.client.list_objects(bucket, prefix=folder, recursive=False))
                if any(existing_objects):
                    # Folder already exists
                    folder_key = folder.split("/")[-2]
                    results[folder_key] = True
                    logger.debug(f"Form folder already exists: {folder}", form_name=form_name_upper, bucket=bucket)
                    continue
                
                # Create a .keep file to establish the folder structure
                marker_name = f"{folder}.keep"
                from io import BytesIO
                empty_content = BytesIO(b"")
                self.client.put_object(
                    bucket,
                    marker_name,
                    empty_content,
                    length=0,
                    content_type="application/octet-stream",
                )
                folder_key = folder.split("/")[-2]  # Get folder name like "FORM_DOCS"
                results[folder_key] = True
                logger.info(f"Created form folder: {folder}", form_name=form_name_upper, bucket=bucket)
            except Exception as e:
                logger.warning(f"Failed to create folder {folder}: {e}")
                folder_key = folder.split("/")[-2]
                results[folder_key] = False

        return results

    def sync_prd_structure(self, prd_base_dir: str | Path, bucket: str | None = None) -> dict[str, int]:
        """
        Sync the entire PRD directory structure to MinIO.

        Structure in MinIO:
        - FORMS/{FORM_NAME}/FORM_DOCS/
        - FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/
        - FORMS/{FORM_NAME}/UI_SCREENSHOTS/
        - DB_PRD/
        - EXPORT_CODEBASE_PRD/
        - LEGACY_CODEBASE/

        Local structure (src/PRDs):
        - {FORM_NAME}/FORM_DOCS/
        - {FORM_NAME}/FORM_FILE_DEPENDENCIES/
        - {FORM_NAME}/UI_SCREENSHOTS/
        - DB_PRD/
        - EXPORT_CODEBASE_PRD/
        - LEGACY_CODEBASE/

        Args:
            prd_base_dir: Base directory containing PRDs (e.g., src/PRDs)
            bucket: Bucket name

        Returns:
            Dictionary with counts per folder type
        """
        prd_base_dir = Path(prd_base_dir)
        bucket = bucket or self.bucket

        if not prd_base_dir.exists():
            raise ValueError(f"PRD base directory not found: {prd_base_dir}")

        # Verify bucket exists (don't create)
        self.ensure_bucket(bucket, must_exist=True)

        counts = {
            "forms": 0,
            "db_prd": 0,
            "export_codebase_prd": 0,
            "legacy_codebase": 0,
            "total": 0,
        }

        # Sync form directories - wrap them in FORMS/ prefix
        # Look for directories that look like form names (LE07, LE11, etc.)
        for item in prd_base_dir.iterdir():
            if not item.is_dir():
                continue

            # Check if it's a form directory (has FORM_DOCS, FORM_FILE_DEPENDENCIES, or UI_SCREENSHOTS subdirectories)
            is_form_dir = False
            for subdir in item.iterdir():
                if subdir.is_dir() and subdir.name in ("FORM_DOCS", "FORM_FILE_DEPENDENCIES", "UI_SCREENSHOTS"):
                    is_form_dir = True
                    break

            if is_form_dir:
                # This is a form directory - wrap in FORMS/ prefix
                prefix = f"FORMS/{item.name}/"
                count = self.upload_directory(item, prefix=prefix, bucket=bucket)
                counts["forms"] += count
                counts["total"] += count
                logger.info(f"Synced form: {item.name}", files=count, prefix=prefix)

        # Sync DB_PRD directory
        db_prd_dir = prd_base_dir / "DB_PRD"
        if db_prd_dir.exists():
            count = self.upload_directory(db_prd_dir, prefix="DB_PRD/", bucket=bucket)
            counts["db_prd"] = count
            counts["total"] += count
            logger.info("Synced DB_PRD", files=count)

        # Sync EXPORT_CODEBASE_PRD directory
        export_dir = prd_base_dir / "EXPORT_CODEBASE_PRD"
        if export_dir.exists():
            count = self.upload_directory(export_dir, prefix="EXPORT_CODEBASE_PRD/", bucket=bucket)
            counts["export_codebase_prd"] = count
            counts["total"] += count
            logger.info("Synced EXPORT_CODEBASE_PRD", files=count)

        # Sync LEGACY_CODEBASE directory
        legacy_dir = prd_base_dir / "LEGACY_CODEBASE"
        if legacy_dir.exists():
            count = self.upload_directory(legacy_dir, prefix="LEGACY_CODEBASE/", bucket=bucket)
            counts["legacy_codebase"] = count
            counts["total"] += count
            logger.info("Synced LEGACY_CODEBASE", files=count)

        logger.info("PRD structure sync complete", bucket=bucket, **counts)

        return counts

    def download_file(
        self, object_name: str, local_path: str | Path, bucket: str | None = None
    ) -> Path:
        """
        Download a file from MinIO.

        Args:
            object_name: Object name in MinIO
            local_path: Local file path to save to
            bucket: Bucket name

        Returns:
            Path to downloaded file
        """
        bucket = bucket or self.bucket
        local_path = Path(local_path)

        # Ensure parent directory exists
        local_path.parent.mkdir(parents=True, exist_ok=True)

        # Download file
        self.client.fget_object(bucket, object_name, str(local_path))

        logger.info(
            "Downloaded file from MinIO",
            object_name=object_name,
            local_path=str(local_path),
            bucket=bucket,
        )

        return local_path

    def list_objects(
        self, prefix: str = "", bucket: str | None = None, recursive: bool = True
    ) -> list[str]:
        """
        List objects in MinIO bucket.

        Args:
            prefix: Prefix to filter objects
            bucket: Bucket name
            recursive: Whether to list recursively

        Returns:
            List of object names
        """
        bucket = bucket or self.bucket

        if not self.client.bucket_exists(bucket):
            return []

        objects = self.client.list_objects(bucket, prefix=prefix, recursive=recursive)
        return [obj.object_name for obj in objects]

    def get_file_content(self, object_name: str, bucket: str | None = None) -> bytes:
        """
        Get file content from MinIO as bytes.

        Args:
            object_name: Object name in MinIO
            bucket: Bucket name

        Returns:
            File content as bytes
        """
        bucket = bucket or self.bucket

        response = self.client.get_object(bucket, object_name)
        content = response.read()
        response.close()
        response.release_conn()

        logger.debug("Retrieved file content from MinIO", object_name=object_name, size=len(content))

        return content

    def get_file_text(self, object_name: str, bucket: str | None = None, encoding: str = "utf-8") -> str:
        """
        Get file content from MinIO as text.

        Args:
            object_name: Object name in MinIO
            bucket: Bucket name
            encoding: Text encoding (default: utf-8)

        Returns:
            File content as string
        """
        content = self.get_file_content(object_name, bucket)
        return content.decode(encoding)

    def file_exists(self, object_name: str, bucket: str | None = None) -> bool:
        """
        Check if a file exists in MinIO.

        Args:
            object_name: Object name in MinIO
            bucket: Bucket name

        Returns:
            True if file exists, False otherwise
        """
        bucket = bucket or self.bucket

        if not self.client.bucket_exists(bucket):
            return False

        try:
            self.client.stat_object(bucket, object_name)
            return True
        except S3Error:
            return False

    def delete_form_data(self, form_name: str, bucket: str | None = None) -> dict[str, Any]:
        """
        Delete all data for a specific form from MinIO bucket.

        Deletes:
        - FORMS/{FORM_NAME}/FORM_DOCS/*
        - FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/*
        - FORMS/{FORM_NAME}/UI_SCREENSHOTS/*

        Args:
            form_name: Form identifier
            bucket: Bucket name

        Returns:
            Dictionary with deletion results
        """
        bucket = bucket or self.bucket
        form_name_upper = form_name.upper()
        prefix = f"FORMS/{form_name_upper}/"

        if not self.client.bucket_exists(bucket):
            logger.warning("Bucket does not exist", bucket=bucket)
            return {
                "success": False,
                "error": f"Bucket {bucket} does not exist",
                "deleted_count": 0,
            }

        deleted_count = 0
        errors = []

        try:
            # List all objects with the form prefix
            objects = self.client.list_objects(bucket, prefix=prefix, recursive=True)

            for obj in objects:
                try:
                    self.client.remove_object(bucket, obj.object_name)
                    deleted_count += 1
                    logger.debug("Deleted object", object_name=obj.object_name, bucket=bucket)
                except S3Error as e:
                    error_msg = f"Failed to delete {obj.object_name}: {str(e)}"
                    errors.append(error_msg)
                    logger.warning(error_msg)

            logger.info(
                "Deleted form data from MinIO",
                form_name=form_name_upper,
                bucket=bucket,
                deleted_count=deleted_count,
                errors=len(errors),
            )

            return {
                "success": True,
                "form_name": form_name_upper,
                "deleted_count": deleted_count,
                "errors": errors,
            }

        except S3Error as e:
            logger.error("Failed to delete form data from MinIO", form_name=form_name_upper, error=str(e))
            return {
                "success": False,
                "error": str(e),
                "deleted_count": deleted_count,
            }

    def delete_bucket(self, bucket: str | None = None, force: bool = False) -> dict[str, Any]:
        """
        Delete a MinIO bucket.

        Args:
            bucket: Bucket name (defaults to configured bucket)
            force: If True, delete all objects in bucket before deleting bucket

        Returns:
            Dictionary with deletion result
        """
        bucket = bucket or self.bucket

        if not self.client.bucket_exists(bucket):
            logger.warning("Bucket does not exist", bucket=bucket)
            return {
                "success": False,
                "error": f"Bucket {bucket} does not exist",
            }

        try:
            if force:
                # Delete all objects first
                objects = self.client.list_objects(bucket, recursive=True)
                for obj in objects:
                    try:
                        self.client.remove_object(bucket, obj.object_name)
                        logger.debug("Deleted object", object_name=obj.object_name, bucket=bucket)
                    except S3Error as e:
                        logger.warning(f"Failed to delete object {obj.object_name}: {e}")

            # Delete the bucket
            self.client.remove_bucket(bucket)
            logger.info("Deleted bucket", bucket=bucket)

            return {
                "success": True,
                "bucket": bucket,
            }

        except S3Error as e:
            logger.error("Failed to delete bucket", bucket=bucket, error=str(e))
            return {
                "success": False,
                "error": str(e),
                "bucket": bucket,
            }
