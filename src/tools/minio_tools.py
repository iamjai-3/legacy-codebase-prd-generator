"""
MinIO Tools for Agentic AI.

Provides access to form documentation, screenshots, and dependencies
stored in MinIO object storage.
"""

import base64

from minio import Minio

from src.config.settings import get_settings
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

CONTENT_SEPARATOR = "\n---\n"

# Cached MinIO client singleton
_minio_client: Minio | None = None


def _get_minio_client() -> Minio:
    """Get or create a cached MinIO client singleton."""
    global _minio_client
    if _minio_client is None:
        settings = get_settings()
        _minio_client = Minio(
            settings.minio.endpoint,
            access_key=settings.minio.access_key,
            secret_key=settings.minio.secret_key,
            secure=settings.minio.secure,
        )
    return _minio_client


def list_screenshots(form_name: str, bucket: str | None = None) -> str:
    """
    List available UI screenshots for a form.

    Args:
        form_name: Form name (e.g., 'LE11')
        bucket: Optional bucket name (defaults to configured bucket)

    Returns:
        List of available screenshots with metadata
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        # Construct path: FORMS/{FORM_NAME}/UI_SCREENSHOTS/
        prefix = f"FORMS/{form_name.upper()}/UI_SCREENSHOTS/"

        objects = list(client.list_objects(bucket, prefix=prefix, recursive=True))

        if not objects:
            return f"No screenshots found for form: {form_name}"

        lines = [f"# Screenshots for: {form_name}\n"]
        lines.append(f"Location: {bucket}/{prefix}\n")

        for obj in objects:
            if obj.object_name.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                name = obj.object_name.split("/")[-1]
                size_kb = obj.size / 1024
                lines.append(f"- {name} ({size_kb:.1f} KB)")

        if len(lines) == 2:  # Only header and location
            return f"No image files found in {prefix}"

        return "\n".join(lines)

    except Exception as e:
        logger.error(f"Error listing screenshots: {e}")
        return f"Error listing screenshots: {str(e)}"


def get_screenshot(form_name: str, screenshot_name: str, bucket: str | None = None) -> str:
    """
    Get a specific screenshot as base64 data.

    Args:
        form_name: Form name (e.g., 'LE11')
        screenshot_name: Name of the screenshot file
        bucket: Optional bucket name

    Returns:
        Base64-encoded image data or error message
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        # Construct path
        object_name = f"FORMS/{form_name.upper()}/UI_SCREENSHOTS/{screenshot_name}"

        response = client.get_object(bucket, object_name)
        data = response.read()
        response.close()

        # Return base64 encoded
        encoded = base64.b64encode(data).decode("utf-8")
        return f"data:image/png;base64,{encoded}"

    except Exception as e:
        logger.error(f"Error getting screenshot: {e}")
        return f"Error getting screenshot: {str(e)}"


def get_form_docs(form_name: str, bucket: str | None = None) -> str:
    """
    Get form documentation from MinIO.

    Retrieves all documentation files for a form including requirements,
    descriptions, and source table mappings.

    Args:
        form_name: Form name (e.g., 'LE11')
        bucket: Optional bucket name

    Returns:
        Concatenated form documentation
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        # Construct path: FORMS/{FORM_NAME}/FORM_DOCS/
        prefix = f"FORMS/{form_name.upper()}/FORM_DOCS/"

        objects = list(client.list_objects(bucket, prefix=prefix, recursive=True))

        if not objects:
            return f"No documentation found for form: {form_name}"

        lines = [f"# Form Documentation: {form_name}\n"]

        for obj in objects:
            if obj.object_name.lower().endswith((".md", ".txt", ".json")):
                try:
                    response = client.get_object(bucket, obj.object_name)
                    content = response.read().decode("utf-8")
                    response.close()

                    name = obj.object_name.split("/")[-1]
                    lines.append(f"## {name}\n")
                    lines.append(content)
                    lines.append(CONTENT_SEPARATOR)
                except Exception as e:
                    lines.append(f"## {obj.object_name.split('/')[-1]} (Error reading: {e})\n")

        return "\n".join(lines)

    except Exception as e:
        logger.error(f"Error getting form docs: {e}")
        return f"Error getting form documentation: {str(e)}"


def get_dependencies(form_name: str, bucket: str | None = None) -> str:
    """
    Get the dependency file for a form.

    The dependency file lists all code files that belong to the form.

    Args:
        form_name: Form name (e.g., 'LE11')
        bucket: Optional bucket name

    Returns:
        Contents of the dependency file
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        # Construct path: FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/{form_name}_dependencies.txt
        form_upper = form_name.upper()
        form_lower = form_name.lower()
        object_name = f"FORMS/{form_upper}/FORM_FILE_DEPENDENCIES/{form_lower}_dependencies.txt"

        response = client.get_object(bucket, object_name)
        content = response.read().decode("utf-8")
        response.close()

        lines = content.strip().split("\n")

        output = [f"# Dependencies for: {form_name}"]
        output.append(f"Total files: {len(lines)}\n")

        for line in lines:
            if line.strip():
                output.append(f"- {line.strip()}")

        return "\n".join(output)

    except Exception as e:
        logger.error(f"Error getting dependencies: {e}")
        return f"Error getting dependencies: {str(e)}"


def get_db_prd(bucket: str | None = None) -> str:
    """
    Get database PRD documentation from MinIO.

    Retrieves global database documentation from DB_PRD folder.

    Args:
        bucket: Optional bucket name

    Returns:
        Database PRD documentation
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        prefix = "DB_PRD/"

        objects = list(client.list_objects(bucket, prefix=prefix, recursive=True))

        if not objects:
            return "No database PRD found"

        lines = ["# Database PRD Documentation\n"]

        for obj in objects:
            if obj.object_name.lower().endswith((".md", ".txt", ".sql")):
                try:
                    response = client.get_object(bucket, obj.object_name)
                    content = response.read().decode("utf-8")
                    response.close()

                    name = obj.object_name.split("/")[-1]
                    lines.append(f"## {name}\n")
                    lines.append(content)
                    lines.append(CONTENT_SEPARATOR)
                except Exception:
                    pass

        return "\n".join(lines)

    except Exception as e:
        logger.error(f"Error getting DB PRD: {e}")
        return f"Error getting database PRD: {str(e)}"


def get_conversion_prompt(prompt_type: str, bucket: str | None = None) -> str:
    """
    Get code conversion prompt template from MinIO.

    Args:
        prompt_type: Type of prompt ('backend' or 'frontend')
        bucket: Optional bucket name

    Returns:
        Conversion prompt template
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        if prompt_type.lower() == "backend":
            object_name = "EXPORT_CODEBASE_PRD/BE/dotnet_backend_conversion_prompt.txt"
        elif prompt_type.lower() == "frontend":
            object_name = "EXPORT_CODEBASE_PRD/FE/react_frontend_conversion_prompt.txt"
        else:
            return f"Unknown prompt type: {prompt_type}. Use 'backend' or 'frontend'."

        response = client.get_object(bucket, object_name)
        content = response.read().decode("utf-8")
        response.close()

        return content

    except Exception as e:
        logger.error(f"Error getting conversion prompt: {e}")
        return f"Error getting conversion prompt: {str(e)}"


def get_export_template(template_type: str, template_name: str, bucket: str | None = None) -> str:
    """
    Get export template from EXPORT_CODEBASE_PRD folder.

    Templates define the exact output format for generated code to ensure
    100% parity with expected structure.

    Args:
        template_type: 'BE' for backend or 'FE' for frontend
        template_name: Name of the template file
        bucket: Optional bucket name

    Returns:
        Template content or list of available templates
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        prefix = f"EXPORT_CODEBASE_PRD/{template_type.upper()}/"

        if template_name == "list":
            # List available templates
            objects = list(client.list_objects(bucket, prefix=prefix, recursive=True))
            if not objects:
                return f"No templates found in {prefix}"

            lines = [f"# Available {template_type.upper()} Templates:\n"]
            for obj in objects:
                name = obj.object_name.split("/")[-1]
                size_kb = obj.size / 1024
                lines.append(f"- {name} ({size_kb:.1f} KB)")
            return "\n".join(lines)

        # Get specific template
        object_name = f"{prefix}{template_name}"
        response = client.get_object(bucket, object_name)
        content = response.read().decode("utf-8")
        response.close()

        return content

    except Exception as e:
        logger.error(f"Error getting export template: {e}")
        return f"Error getting export template: {str(e)}"


def get_all_form_knowledge(form_name: str, bucket: str | None = None) -> str:
    """
    Get aggregated knowledge for a form including docs, dependencies, and schema.

    This retrieves all critical information needed for accurate code migration:
    - Form documentation
    - File dependencies
    - Database schema mappings
    - UI screenshots list

    Args:
        form_name: Form name (e.g., 'LE11')
        bucket: Optional bucket name

    Returns:
        Aggregated form knowledge as structured markdown
    """
    try:
        settings = get_settings()
        bucket = bucket or settings.minio.bucket
        form_upper = form_name.upper()

        output = [f"# Complete Knowledge for Form: {form_upper}\n"]
        output.append("=" * 60 + "\n")

        # 1. Form Documentation
        output.append("\n## 1. Form Documentation\n")
        docs = get_form_docs(form_name, bucket)
        if "Error" not in docs:
            # Truncate if too long (reduced from 10k to lower token usage)
            if len(docs) > 6000:
                docs = docs[:6000] + "\n\n[... truncated for brevity ...]"
            output.append(docs)
        else:
            output.append(f"Not available: {docs}\n")

        # 2. Dependencies
        output.append("\n## 2. File Dependencies\n")
        deps = get_dependencies(form_name, bucket)
        if "Error" not in deps:
            output.append(deps)
        else:
            output.append(f"Not available: {deps}\n")

        # 3. UI Screenshots
        output.append("\n## 3. UI Screenshots Available\n")
        screenshots = list_screenshots(form_name, bucket)
        if "Error" not in screenshots and "No screenshots" not in screenshots:
            output.append(screenshots)
        else:
            output.append("No screenshots available.\n")

        # 4. Database PRD summary
        output.append("\n## 4. Database Schema (Summary)\n")
        db_prd = get_db_prd(bucket)
        if "Error" not in db_prd:
            # Only include first section for summary
            lines = db_prd.split("\n")[:50]
            output.append("\n".join(lines))
            output.append("\n\n[Use get_db_prd for full schema details]\n")
        else:
            output.append(f"Not available: {db_prd}\n")

        output.append("\n" + "=" * 60)
        output.append(f"\nTotal knowledge sources retrieved for {form_upper}.")

        return "\n".join(output)

    except Exception as e:
        logger.error(f"Error getting form knowledge: {e}")
        return f"Error getting form knowledge: {str(e)}"


def get_ui_flow_docs(form_name: str, bucket: str | None = None) -> str:
    """
    Get UI flow documentation describing user interactions and screen flows.

    This helps understand the legacy UI behavior for accurate React migration.

    Args:
        form_name: Form name (e.g., 'LE11')
        bucket: Optional bucket name

    Returns:
        UI flow documentation if available
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket
        form_upper = form_name.upper()

        # Check for UI flow docs in FORM_DOCS
        prefix = f"FORMS/{form_upper}/FORM_DOCS/"
        objects = list(client.list_objects(bucket, prefix=prefix, recursive=True))

        flow_docs = []
        for obj in objects:
            name = obj.object_name.lower()
            # Look for UI-related documentation
            if any(keyword in name for keyword in ["ui", "flow", "screen", "navigation", "user"]):
                try:
                    response = client.get_object(bucket, obj.object_name)
                    content = response.read().decode("utf-8")
                    response.close()

                    flow_docs.append(f"## {obj.object_name.split('/')[-1]}\n")
                    flow_docs.append(content)
                    flow_docs.append(CONTENT_SEPARATOR)
                except Exception:
                    pass

        if flow_docs:
            return f"# UI Flow Documentation for {form_upper}\n\n" + "\n".join(flow_docs)

        # Fallback: check metadata bucket
        try:
            meta_prefix = f"metadata/{form_upper}/"
            meta_objects = list(client.list_objects(bucket, prefix=meta_prefix, recursive=True))

            for obj in meta_objects:
                if obj.object_name.lower().endswith((".md", ".txt")):
                    response = client.get_object(bucket, obj.object_name)
                    content = response.read().decode("utf-8")
                    response.close()
                    return f"# UI Metadata for {form_upper}\n\n{content}"
        except Exception:
            pass

        return f"No UI flow documentation found for {form_upper}. Analyze screenshots directly."

    except Exception as e:
        logger.error(f"Error getting UI flow docs: {e}")
        return f"Error getting UI flow docs: {str(e)}"


def list_export_templates(bucket: str | None = None) -> str:
    """
    List all available export templates in EXPORT_CODEBASE_PRD.

    Returns:
        List of BE and FE templates available
    """
    try:
        settings = get_settings()
        client = _get_minio_client()
        bucket = bucket or settings.minio.bucket

        output = ["# Export Code Templates\n"]

        for folder in ["BE", "FE"]:
            prefix = f"EXPORT_CODEBASE_PRD/{folder}/"
            objects = list(client.list_objects(bucket, prefix=prefix, recursive=True))

            output.append(f"\n## {folder} Templates:\n")
            if objects:
                for obj in objects:
                    name = obj.object_name.split("/")[-1]
                    size_kb = obj.size / 1024
                    output.append(f"- {name} ({size_kb:.1f} KB)")
            else:
                output.append("No templates found.")

        return "\n".join(output)

    except Exception as e:
        logger.error(f"Error listing export templates: {e}")
        return f"Error listing export templates: {str(e)}"
