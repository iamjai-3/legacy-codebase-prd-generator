"""Prompts for PRD Aggregator Agent."""


class PRDAggregatorPrompts:
    """Prompts used by the PRDAggregatorAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for PRD aggregation."""
        return f"""You are a senior technical writer specializing in Product Requirements Documents for software migration projects.
Your task is to aggregate analysis from multiple sources into a comprehensive PRD for "{form_name}".

When creating the PRD:
1. Maintain consistent terminology and style throughout
2. Ensure all sections are well-structured and complete
3. Cross-reference between sections where relevant
4. Highlight critical information and decisions
5. Include executive summary for stakeholders
6. Add technical appendices for developers

The PRD should be:
- Clear and actionable for development teams
- Comprehensive enough for independent implementation
- Structured for easy navigation
- Suitable for both technical and non-technical readers

Use professional technical writing standards."""

    @staticmethod
    def overview_section(form_name: str, jira_context: str) -> str:
        """Prompt for generating the overview section."""
        return f"""Write the Overview section for "{form_name}" PRD:

{jira_context}

Include:
1. Purpose and Scope
2. Background
3. Goals and Objectives
4. Target Audience
5. Document Conventions

Write in professional technical documentation style."""

    @staticmethod
    def executive_summary(form_name: str, req_count: int, risk_level: str) -> str:
        """Prompt for generating executive summary."""
        return f"""Write an executive summary for the "{form_name}" PRD:

Key metrics:
- Functional requirements: {req_count}
- Migration complexity: {risk_level}

The summary should:
1. Describe the module purpose
2. Summarize key functionality
3. Highlight critical risks
4. Provide migration recommendation
5. State estimated effort

Write 3-4 paragraphs suitable for executive stakeholders."""
