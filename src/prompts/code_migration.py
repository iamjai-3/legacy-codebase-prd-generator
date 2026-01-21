"""Prompts for Code Migration Agent."""

from pathlib import Path


class CodeMigrationPrompts:
    """Prompts used by the CodeMigrationAgent for generating .NET and React code."""

    _backend_prompt_template: str | None = None
    _frontend_prompt_template: str | None = None

    @classmethod
    def _load_backend_template(cls) -> str:
        """Load the .NET backend conversion prompt template."""
        if cls._backend_prompt_template is None:
            template_path = (
                Path(__file__).parent.parent
                / "export_codebase"
                / "dotnet_backend_conversion_prompt.txt"
            )
            with open(template_path, encoding="utf-8") as f:
                cls._backend_prompt_template = f.read()
        return cls._backend_prompt_template

    @classmethod
    def _load_frontend_template(cls) -> str:
        """Load the React frontend conversion prompt template."""
        if cls._frontend_prompt_template is None:
            template_path = (
                Path(__file__).parent.parent
                / "export_codebase"
                / "react_frontend_conversion_prompt.txt"
            )
            with open(template_path, encoding="utf-8") as f:
                cls._frontend_prompt_template = f.read()
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
