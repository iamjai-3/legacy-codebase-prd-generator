"""Prompts for Requirements Generator Agent - Migration-Focused."""

from src.prompts.loader import load_prompt


class RequirementsPrompts:
    """Prompts used by the RequirementsGeneratorAgent for migration-ready PRD generation."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for requirements generation."""
        return load_prompt("requirements/system_prompt", form_name=form_name)

    @staticmethod
    def functional_requirements(form_name: str, code_summary: str, context_summary: str) -> str:
        """Prompt for generating functional requirements with specific business logic."""
        return load_prompt(
            "requirements/functional_requirements",
            form_name=form_name,
            code_summary=code_summary,
            context_summary=context_summary,
        )

    @staticmethod
    def api_specification(form_name: str, service_code: str) -> str:
        """Prompt for extracting API specifications from service/controller code."""
        return load_prompt(
            "requirements/api_specification",
            form_name=form_name,
            service_code=service_code,
        )

    @staticmethod
    def business_logic_extraction(form_name: str, code_content: str) -> str:
        """Prompt for extracting detailed business logic from code."""
        return load_prompt(
            "requirements/business_logic_extraction",
            form_name=form_name,
            code_content=code_content,
        )

    @staticmethod
    def source_tables_extraction(form_name: str, kb_context: str) -> str:
        """Prompt for extracting source table definitions from knowledge base."""
        return load_prompt(
            "requirements/source_tables_extraction",
            form_name=form_name,
            kb_context=kb_context,
        )

    @staticmethod
    def database_mappings(form_name: str, code_context: str, kb_context: str) -> str:
        """Prompt for extracting database field mappings from code to tables."""
        return load_prompt(
            "requirements/database_mappings",
            form_name=form_name,
            code_context=code_context,
            kb_context=kb_context,
        )

    @staticmethod
    def data_requirements(form_name: str, model_summary: str, database_context: str) -> str:
        """Prompt for generating comprehensive data requirements."""
        return load_prompt(
            "requirements/data_requirements",
            form_name=form_name,
            model_summary=model_summary,
            database_context=database_context,
        )

    @staticmethod
    def data_requirements_complete(
        form_name: str, dto_code: str, normalized_schema: str, model_summary: str
    ) -> str:
        """Prompt that ensures ALL fields are extracted and mapped to normalized schema."""
        return load_prompt(
            "requirements/data_requirements_complete",
            form_name=form_name,
            dto_code=dto_code,
            normalized_schema=normalized_schema,
            model_summary=model_summary,
        )

    @staticmethod
    def validation_rules(form_name: str, validation_code: str, context_text: str) -> str:
        """Prompt for extracting precise validation rules."""
        return load_prompt(
            "requirements/validation_rules",
            form_name=form_name,
            validation_code=validation_code,
            context_text=context_text,
        )

    @staticmethod
    def integration_requirements(form_name: str, integration_code: str, context: str) -> str:
        """Prompt for extracting integration specifications."""
        return load_prompt(
            "requirements/integration_requirements",
            form_name=form_name,
            integration_code=integration_code,
            context=context,
        )

    @staticmethod
    def workflow_extraction(form_name: str, workflow_code: str) -> str:
        """Prompt for extracting workflow/state machine logic."""
        return load_prompt(
            "requirements/workflow_extraction",
            form_name=form_name,
            workflow_code=workflow_code,
        )

    @staticmethod
    def non_functional_requirements(form_name: str, code_context: str) -> str:
        """Prompt for generating specific non-functional requirements."""
        return load_prompt(
            "requirements/non_functional_requirements",
            form_name=form_name,
            code_context=code_context,
        )

    @staticmethod
    def summary(
        form_name: str,
        categories: str,
        high_priority: str,
        req_count: int,
        nfr_count: int,
        data_count: int,
    ) -> str:
        """Prompt for generating requirements summary."""
        return load_prompt(
            "requirements/summary",
            form_name=form_name,
            categories=categories,
            high_priority=high_priority,
            req_count=req_count,
            nfr_count=nfr_count,
            data_count=data_count,
        )
