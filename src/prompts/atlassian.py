"""Prompts for Atlassian Integration Agent."""


class AtlassianPrompts:
    """Prompts used by the AtlassianIntegrationAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for Jira analysis."""
        return f"""You are an expert business analyst specializing in extracting requirements from Jira issues.
Your task is to analyze Jira documentation for the "{form_name}" form/module.

When analyzing Jira issues, you should:
1. Identify functional requirements (features and capabilities)
2. Identify non-functional requirements (performance, security, usability)
3. Extract business rules and validation logic
4. Note technical constraints and dependencies
5. Capture stakeholder feedback from comments
6. Identify gaps in documentation
7. Flag open questions that need clarification

Provide structured analysis that helps in:
- Understanding the complete requirements scope
- Identifying edge cases and business rules
- Planning the migration effort
- Ensuring nothing is missed in the modernization

Be thorough and precise. Requirements will inform the PRD document."""

    @staticmethod
    def extract_requirement(
        issue_key: str,
        issue_type: str,
        summary: str,
        description: str,
        priority: str,
        acceptance_criteria: str,
    ) -> str:
        """Prompt for extracting a requirement from a Jira issue."""
        return f"""Analyze this Jira issue and extract requirements:

Issue: {issue_key}
Type: {issue_type}
Summary: {summary}
Description: {description}
Priority: {priority}
Acceptance Criteria: {acceptance_criteria}

Respond in JSON format:
{{
    "requirement_type": "functional|non_functional|business_rule",
    "title": "Concise requirement title",
    "description": "Clear requirement description",
    "acceptance_criteria": ["criterion 1", "criterion 2"],
    "dependencies": ["dependency 1"]
}}

If this is not a requirements-related issue, return {{"skip": true}}"""

    @staticmethod
    def business_rules(form_name: str, all_descriptions: str) -> str:
        """Prompt for extracting business rules from issues."""
        return f"""From these Jira issues, extract all business rules mentioned:

{all_descriptions}

List each business rule clearly and concisely.
Format: One rule per line, starting with "BR-" identifier.
Example: BR-001: Users must have valid credentials to access the system."""

    @staticmethod
    def technical_constraints(form_name: str) -> str:
        """Prompt for identifying technical constraints."""
        return f"""From the {form_name} module issues, identify any technical constraints related to:
- Performance requirements
- Security requirements
- Integration constraints
- Platform limitations

List each constraint clearly."""

    @staticmethod
    def summary(
        form_name: str, total_issues: int, issue_summary: str, req_count: int, rule_count: int
    ) -> str:
        """Prompt for generating Jira analysis summary."""
        return f"""Provide a 2-3 paragraph executive summary of the Jira documentation for "{form_name}":

- Total issues analyzed: {total_issues}
- Issues by type: {issue_summary}
- Requirements extracted: {req_count}
- Business rules identified: {rule_count}

Focus on the overall scope, key features, and any notable patterns or concerns."""
