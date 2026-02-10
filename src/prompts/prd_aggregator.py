"""Prompts for PRD Aggregator Agent - Migration-Focused PRD Generation."""

from src.prompts.loader import load_prompt


class PRDAggregatorPrompts:
    """Prompts for generating migration-ready PRD documents."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for PRD aggregation."""
        return load_prompt("prd_aggregator/system_prompt", form_name=form_name)

    @staticmethod
    def overview_section(form_name: str, jira_context: str, kb_context: str) -> str:
        """Prompt for generating the overview section with specific details."""
        return load_prompt(
            "prd_aggregator/overview_section",
            form_name=form_name,
            jira_context=jira_context,
            kb_context=kb_context,
        )

    @staticmethod
    def business_logic_section(form_name: str, logic_data: str, kb_context: str) -> str:
        """Prompt for generating detailed business logic documentation."""
        return load_prompt(
            "prd_aggregator/business_logic_section",
            form_name=form_name,
            logic_data=logic_data,
            kb_context=kb_context,
        )

    @staticmethod
    def api_specification_section(form_name: str, api_data: str, kb_context: str) -> str:
        """Prompt for generating comprehensive API documentation."""
        return load_prompt(
            "prd_aggregator/api_specification_section",
            form_name=form_name,
            api_data=api_data,
            kb_context=kb_context,
        )

    @staticmethod
    def data_model_section(form_name: str, data_requirements: str, kb_context: str) -> str:
        """Prompt for generating detailed data model documentation."""
        return load_prompt(
            "prd_aggregator/data_model_section",
            form_name=form_name,
            data_requirements=data_requirements,
            kb_context=kb_context,
        )

    @staticmethod
    def functional_requirements_section(
        form_name: str, requirements: str, logic_context: str
    ) -> str:
        """Prompt for enhanced functional requirements with business logic."""
        return load_prompt(
            "prd_aggregator/functional_requirements_section",
            form_name=form_name,
            requirements=requirements,
            logic_context=logic_context,
        )

    @staticmethod
    def validation_rules_section(form_name: str, validation_data: str) -> str:
        """Prompt for documenting all validation rules."""
        return load_prompt(
            "prd_aggregator/validation_rules_section",
            form_name=form_name,
            validation_data=validation_data,
        )

    @staticmethod
    def integration_section(form_name: str, integration_data: str) -> str:
        """Prompt for documenting external integrations."""
        return load_prompt(
            "prd_aggregator/integration_section",
            form_name=form_name,
            integration_data=integration_data,
        )

    @staticmethod
    def workflow_section(form_name: str, workflow_data: str) -> str:
        """Prompt for documenting workflows and state machines."""
        return load_prompt(
            "prd_aggregator/workflow_section",
            form_name=form_name,
            workflow_data=workflow_data,
        )

    @staticmethod
    def executive_summary(
        form_name: str,
        req_count: int,
        api_count: int,
        entity_count: int,
        integration_count: int,
        complexity: str,
        kb_context: str = "",
    ) -> str:
        """Prompt for generating executive summary."""
        return load_prompt(
            "prd_aggregator/executive_summary",
            form_name=form_name,
            req_count=req_count,
            api_count=api_count,
            entity_count=entity_count,
            integration_count=integration_count,
            complexity=complexity,
            kb_context=kb_context,
        )

    @staticmethod
    def migration_strategy_section(form_name: str, complexity: str, tech_details: str) -> str:
        """Prompt for generating migration strategy."""
        return load_prompt(
            "prd_aggregator/migration_strategy_section",
            form_name=form_name,
            complexity=complexity,
            tech_details=tech_details,
        )

    @staticmethod
    def migration_mapping_section(
        form_name: str, data_requirements: str, normalized_schema: str
    ) -> str:
        """Prompt for generating field mapping and migration guide section."""
        return load_prompt(
            "prd_aggregator/migration_mapping_section",
            form_name=form_name,
            data_requirements=data_requirements,
            normalized_schema=normalized_schema,
        )
