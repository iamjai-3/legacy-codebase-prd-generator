"""Prompts for Database Analysis Agent."""

from src.prompts.loader import load_prompt


class DatabaseAnalysisPrompts:
    """Prompts used by the DatabaseAnalysisAgent for analyzing database schemas."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for database analysis."""
        return load_prompt("database_analysis/system_prompt", form_name=form_name)

    @staticmethod
    def extract_tables_prompt(db_content: str, form_name: str) -> str:
        """Prompt for extracting form-specific table structures."""
        content_preview = db_content[:50000] if len(db_content) > 50000 else db_content
        return load_prompt(
            "database_analysis/extract_tables",
            form_name=form_name,
            content_preview=content_preview,
        )

    @staticmethod
    def extract_mappings_prompt(db_content: str, form_name: str) -> str:
        """Prompt for extracting form-specific table mappings."""
        content_preview = db_content[:50000] if len(db_content) > 50000 else db_content
        return load_prompt(
            "database_analysis/extract_mappings",
            form_name=form_name,
            content_preview=content_preview,
        )

    @staticmethod
    def generate_summary_prompt(
        db_content: str, table_analysis: dict, mapping_analysis: dict, form_name: str
    ) -> str:
        """Prompt for generating form-specific schema summary."""
        content_preview = db_content[:30000] if len(db_content) > 30000 else db_content
        return load_prompt(
            "database_analysis/generate_summary",
            form_name=form_name,
            content_preview=content_preview,
            table_analysis=table_analysis,
            mapping_analysis=mapping_analysis,
        )
