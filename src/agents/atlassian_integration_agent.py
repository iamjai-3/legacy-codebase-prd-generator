"""
Atlassian Integration Agent for retrieving and processing Jira/Confluence documentation.
"""

from dataclasses import dataclass
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.extractors.jira_extractor import JiraExtractor, JiraIssue
from src.prompts.atlassian import AtlassianPrompts
from src.utils.logging_config import ExecutionTimer


@dataclass
class RequirementItem:
    """A single requirement extracted from Jira."""

    source_key: str
    requirement_type: str  # functional, non-functional, business_rule
    title: str
    description: str
    priority: str
    acceptance_criteria: list[str]
    dependencies: list[str]


@dataclass
class AtlassianIntegrationResult:
    """Result from Atlassian integration analysis."""

    form_name: str
    total_issues: int
    issues_by_type: dict[str, int]
    issues_by_status: dict[str, int]
    requirements: list[RequirementItem]
    business_rules: list[str]
    technical_constraints: list[str]
    stakeholder_notes: list[str]
    open_questions: list[str]
    documentation_gaps: list[str]
    summary: str


class AtlassianIntegrationAgent(BaseAgent[AtlassianIntegrationResult]):
    """
    Agent for integrating with Atlassian Jira to extract requirements and documentation.
    Processes Jira issues to identify requirements, business rules, and constraints.
    """

    def __init__(self) -> None:
        """Initialize the Atlassian integration agent."""
        super().__init__("AtlassianIntegrationAgent")
        self.jira_extractor = JiraExtractor()

    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for Jira analysis."""
        return AtlassianPrompts.system_prompt(context.form_name)

    async def analyze(
        self,
        context: AgentContext,
        issues: list[JiraIssue] | None = None,
        project_key: str | None = None,
        jql: str | None = None,
        **kwargs: Any,
    ) -> AgentResult[AtlassianIntegrationResult]:
        """
        Analyze Jira issues for requirements extraction.

        Args:
            context: Agent execution context
            issues: Optional pre-loaded Jira issues
            project_key: Optional Jira project key
            jql: Optional custom JQL query

        Returns:
            AgentResult with AtlassianIntegrationResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting Jira analysis", form_name=context.form_name, project_key=project_key
        )

        try:
            # Get issues if not provided
            if issues is None:
                issues = self.jira_extractor.get_form_issues(
                    form_name=context.form_name,
                    project_key=project_key,
                    additional_jql=jql,
                )

            if not issues:
                return self._create_empty_result(context.form_name, timer)

            # Calculate statistics
            issues_by_type = self._count_by_field(issues, "issue_type")
            issues_by_status = self._count_by_field(issues, "status")

            # Extract all analysis components
            requirements = await self._extract_requirements(context, issues)
            business_rules = await self._extract_business_rules(context, issues)
            technical_constraints = await self._extract_technical_constraints(context, issues)
            stakeholder_notes = self._extract_stakeholder_notes(issues)
            open_questions = await self._identify_open_questions(context, issues)
            documentation_gaps = await self._identify_documentation_gaps(
                context, issues, requirements
            )
            summary = await self._generate_summary(context, issues, requirements, business_rules)

            result = AtlassianIntegrationResult(
                form_name=context.form_name,
                total_issues=len(issues),
                issues_by_type=issues_by_type,
                issues_by_status=issues_by_status,
                requirements=requirements,
                business_rules=business_rules,
                technical_constraints=technical_constraints,
                stakeholder_notes=stakeholder_notes,
                open_questions=open_questions,
                documentation_gaps=documentation_gaps,
                summary=summary,
            )

            self.logger.info(
                "Jira analysis complete",
                form_name=context.form_name,
                total_issues=len(issues),
                requirements_extracted=len(requirements),
                business_rules_found=len(business_rules),
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            return self.create_error_result(e, timer)

    def _create_empty_result(
        self, form_name: str, timer: ExecutionTimer
    ) -> AgentResult[AtlassianIntegrationResult]:
        """Create result for when no issues are found."""
        self.logger.info("No Jira issues found", form_name=form_name)
        empty_data = AtlassianIntegrationResult(
            form_name=form_name,
            total_issues=0,
            issues_by_type={},
            issues_by_status={},
            requirements=[],
            business_rules=[],
            technical_constraints=[],
            stakeholder_notes=[],
            open_questions=[],
            documentation_gaps=["No Jira issues found for this form"],
            summary="No Jira documentation available for analysis.",
        )
        return self.create_success_result(empty_data, timer)

    def _count_by_field(self, issues: list[JiraIssue], field: str) -> dict[str, int]:
        """Count issues by a specific field."""
        counts: dict[str, int] = {}
        for issue in issues:
            value = getattr(issue, field, "Unknown")
            counts[value] = counts.get(value, 0) + 1
        return counts

    async def _extract_requirements(
        self, context: AgentContext, issues: list[JiraIssue]
    ) -> list[RequirementItem]:
        """Extract structured requirements from issues."""
        requirements: list[RequirementItem] = []

        for issue in issues:
            requirement = await self._extract_single_requirement(context, issue)
            if requirement:
                requirements.append(requirement)

        return requirements

    async def _extract_single_requirement(
        self, context: AgentContext, issue: JiraIssue
    ) -> RequirementItem | None:
        """Extract a single requirement from a Jira issue."""
        prompt = f"""Analyze this Jira issue and extract requirements:

Issue: {issue.key}
Type: {issue.issue_type}
Summary: {issue.summary}
Description: {issue.description}
Priority: {issue.priority}
Acceptance Criteria: {issue.acceptance_criteria}

Respond in JSON format:
{{
    "requirement_type": "functional|non_functional|business_rule",
    "title": "Concise requirement title",
    "description": "Clear requirement description",
    "acceptance_criteria": ["criterion 1", "criterion 2"],
    "dependencies": ["dependency 1"]
}}

If this is not a requirements-related issue, return {{"skip": true}}"""

        try:
            response = await self.invoke_llm(context, prompt)
            data = self._parse_json_response(response)

            if data and not data.get("skip"):
                return RequirementItem(
                    source_key=issue.key,
                    requirement_type=data.get("requirement_type", "functional"),
                    title=data.get("title", issue.summary),
                    description=data.get("description", ""),
                    priority=issue.priority,
                    acceptance_criteria=data.get("acceptance_criteria", []),
                    dependencies=data.get("dependencies", []),
                )
        except Exception as e:
            self.logger.warning("Failed to extract requirement", issue_key=issue.key, error=str(e))

        return None

    async def _extract_business_rules(
        self, context: AgentContext, issues: list[JiraIssue]
    ) -> list[str]:
        """Extract business rules from issues."""
        all_descriptions = "\n---\n".join(
            [
                f"[{issue.key}] {issue.summary}\n{issue.description}"
                for issue in issues[:10]  # Limit to avoid token overflow
            ]
        )

        prompt = f"""From these Jira issues, extract all business rules mentioned:

{all_descriptions}

List each business rule clearly and concisely.
Format: One rule per line, starting with "BR-" identifier.
Example: BR-001: Users must have valid credentials to access the system."""

        response = await self.invoke_llm(context, prompt)

        rules = [
            line.strip()
            for line in response.split("\n")
            if line.strip() and ("BR-" in line or "business rule" in line.lower())
        ]

        return rules

    async def _extract_technical_constraints(
        self, context: AgentContext, issues: list[JiraIssue]
    ) -> list[str]:
        """Extract technical constraints and limitations."""
        technical_issues = [
            issue
            for issue in issues
            if any(
                label in ["technical", "constraint", "limitation", "infrastructure"]
                for label in issue.labels
            )
            or "technical" in issue.summary.lower()
        ]

        if not technical_issues:
            # Look in all issues for technical mentions
            all_text = " ".join([issue.description for issue in issues])
            if "performance" in all_text.lower() or "security" in all_text.lower():
                prompt = f"""From the {context.form_name} module issues, identify any technical constraints related to:
- Performance requirements
- Security requirements
- Integration constraints
- Platform limitations

List each constraint clearly."""

                response = await self.invoke_llm(context, prompt)
                return [line.strip() for line in response.split("\n") if line.strip()]

        return []

    def _extract_stakeholder_notes(self, issues: list[JiraIssue]) -> list[str]:
        """Extract relevant notes from stakeholder comments."""
        notes: list[str] = []

        for issue in issues:
            for comment in issue.comments[:3]:  # Limit comments per issue
                body = comment.get("body", "")
                if len(body) > 50:  # Skip very short comments
                    notes.append(
                        f"[{issue.key}] {comment.get('author', 'Unknown')}: {body[:200]}..."
                    )

        return notes[:20]  # Limit total notes

    async def _identify_open_questions(
        self, context: AgentContext, issues: list[JiraIssue]
    ) -> list[str]:
        """Identify open questions that need clarification."""
        # Look for issues with question-like content
        question_indicators = ["?", "unclear", "tbd", "to be determined", "clarify"]

        questions: list[str] = []

        for issue in issues:
            text = f"{issue.summary} {issue.description}".lower()
            if any(indicator in text for indicator in question_indicators):
                questions.append(f"[{issue.key}] {issue.summary}")

        return questions

    async def _identify_documentation_gaps(
        self, context: AgentContext, issues: list[JiraIssue], requirements: list[RequirementItem]
    ) -> list[str]:
        """Identify gaps in documentation."""
        gaps: list[str] = []

        # Check for missing acceptance criteria
        issues_without_ac = [
            issue
            for issue in issues
            if not issue.acceptance_criteria and issue.issue_type in ["Story", "Task"]
        ]
        if issues_without_ac:
            gaps.append(f"{len(issues_without_ac)} issues missing acceptance criteria")

        # Check for empty descriptions
        empty_descriptions = [
            issue for issue in issues if not issue.description or len(issue.description) < 20
        ]
        if empty_descriptions:
            gaps.append(f"{len(empty_descriptions)} issues with inadequate descriptions")

        # Check requirement coverage
        issue_types = [issue.issue_type for issue in issues]
        if "Epic" not in issue_types:
            gaps.append("No Epic-level documentation found")

        return gaps

    async def _generate_summary(
        self,
        context: AgentContext,
        issues: list[JiraIssue],
        requirements: list[RequirementItem],
        business_rules: list[str],
    ) -> str:
        """Generate an executive summary of the Jira analysis."""
        issue_summary = ", ".join(
            [
                f"{type}: {count}"
                for type, count in self._count_by_field(issues, "issue_type").items()
            ]
        )

        prompt = f"""Provide a 2-3 paragraph executive summary of the Jira documentation for "{context.form_name}":

- Total issues analyzed: {len(issues)}
- Issues by type: {issue_summary}
- Requirements extracted: {len(requirements)}
- Business rules identified: {len(business_rules)}

Focus on the overall scope, key features, and any notable patterns or concerns."""

        return await self.invoke_llm(context, prompt)
