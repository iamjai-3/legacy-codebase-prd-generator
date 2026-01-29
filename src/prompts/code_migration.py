"""Prompts for Code Migration Agent."""

from pathlib import Path

from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class CodeMigrationPrompts:
    """Prompts used by the CodeMigrationAgent for generating .NET and React code."""

    _backend_prompt_template: str | None = None
    _frontend_prompt_template: str | None = None

    @classmethod
    def _load_from_minio(cls, object_name: str) -> str | None:
        """
        Load a prompt template from MinIO.

        Args:
            object_name: Object name in MinIO (e.g., 'EXPORT_CODEBASE_PRD/dotnet_backend_conversion_prompt.txt')

        Returns:
            Template content as string, or None if not found
        """
        try:
            from src.utils.minio_sync import MinioSync

            minio_sync = MinioSync()
            if minio_sync.file_exists(object_name):
                content = minio_sync.get_file_text(object_name)
                logger.info(f"Loaded prompt template from MinIO: {object_name}")
                return content
            else:
                logger.debug(f"Prompt template not found in MinIO: {object_name}")
                return None
        except Exception as e:
            logger.warning(f"Failed to load prompt template from MinIO: {object_name}, error: {e}")
            return None

    @classmethod
    def _load_from_local(cls, filename: str) -> str | None:
        """
        Load a prompt template from local filesystem.

        Args:
            filename: Filename of the template (e.g., 'dotnet_backend_conversion_prompt.txt')

        Returns:
            Template content as string, or None if not found
        """
        try:
            template_path = Path(__file__).parent.parent / "export_codebase" / filename
            if template_path.exists():
                with open(template_path, encoding="utf-8") as f:
                    content = f.read()
                logger.info(f"Loaded prompt template from local: {template_path}")
                return content
            else:
                logger.debug(f"Prompt template not found locally: {template_path}")
                return None
        except Exception as e:
            logger.warning(f"Failed to load prompt template from local: {filename}, error: {e}")
            return None

    @classmethod
    def _load_backend_template(cls) -> str:
        """Load the .NET backend conversion prompt template from MinIO or local fallback."""
        if cls._backend_prompt_template is None:
            filename = "dotnet_backend_conversion_prompt.txt"
            minio_object = f"EXPORT_CODEBASE_PRD/BE/{filename}"

            # Try MinIO first
            template = cls._load_from_minio(minio_object)

            # Fallback to local file
            if template is None:
                template = cls._load_from_local(filename)

            if template is None:
                raise FileNotFoundError(
                    f"Backend conversion prompt template not found. "
                    f"Please upload '{filename}' to MinIO at '{minio_object}' "
                    f"or place it in 'src/export_codebase/' directory."
                )

            cls._backend_prompt_template = template
        return cls._backend_prompt_template

    @classmethod
    def _load_frontend_template(cls) -> str:
        """Load the React frontend conversion prompt template from MinIO or local fallback."""
        if cls._frontend_prompt_template is None:
            filename = "react_frontend_conversion_prompt.txt"
            minio_object = f"EXPORT_CODEBASE_PRD/FE/{filename}"

            # Try MinIO first
            template = cls._load_from_minio(minio_object)

            # Fallback to local file
            if template is None:
                template = cls._load_from_local(filename)

            if template is None:
                raise FileNotFoundError(
                    f"Frontend conversion prompt template not found. "
                    f"Please upload '{filename}' to MinIO at '{minio_object}' "
                    f"or place it in 'src/export_codebase/' directory."
                )

            cls._frontend_prompt_template = template
        return cls._frontend_prompt_template

    @staticmethod
    def backend_conversion_prompt(json_str: str, dependencies: str = "") -> str:
        """
        Format the .NET backend conversion prompt.

        Args:
            json_str: JSON specification of the Java Swing form backend
            dependencies: Dependencies information (optional)

        Returns:
            Formatted prompt string
        """
        template = CodeMigrationPrompts._load_backend_template()
        prompt = template.replace("{json_str}", json_str)
        prompt = prompt.replace(
            "{dependencies}", dependencies if dependencies else "No specific dependencies."
        )
        return prompt

    @staticmethod
    def frontend_conversion_prompt(json_str: str, swagger_json: str, dependencies: str = "") -> str:
        """
        Format the React frontend conversion prompt.

        Args:
            json_str: JSON specification of the Java Swing form frontend
            swagger_json: Swagger/OpenAPI JSON specification from backend
            dependencies: Dependencies information (optional)

        Returns:
            Formatted prompt string
        """
        template = CodeMigrationPrompts._load_frontend_template()
        prompt = template.replace("{json_str}", json_str)
        prompt = prompt.replace("{swagger_json}", swagger_json)
        prompt = prompt.replace(
            "{dependencies}", dependencies if dependencies else "No specific dependencies."
        )
        return prompt

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for code migration."""
        return f"""You are a code migration specialist converting legacy Java Swing applications to modern .NET backend and React frontend.

Your task is to analyze the knowledge base for "{form_name}" and generate:
1. Complete .NET backend solution with ASP.NET Core, Entity Framework, and PostgreSQL
2. Complete React frontend application with TypeScript, TanStack Query, and shadcn/ui

You must:
- Extract all business logic, data models, and API specifications from the knowledge base
- Generate production-ready code following best practices
- Ensure proper error handling and validation
- Create complete, runnable applications
- Follow the exact format specified in the conversion prompts

The generated code should be migration-ready and maintain all functionality from the legacy system."""
