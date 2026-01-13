"""
Jira Extractor for retrieving documentation and requirements from Atlassian Jira.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from atlassian import Jira
from langchain_core.documents import Document

from src.config.settings import get_settings
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class JiraIssue:
    """Represents a Jira issue."""

    key: str
    summary: str
    description: str
    issue_type: str
    status: str
    priority: str
    created: datetime
    updated: datetime
    labels: list[str] = field(default_factory=list)
    components: list[str] = field(default_factory=list)
    attachments: list[dict[str, Any]] = field(default_factory=list)
    comments: list[dict[str, Any]] = field(default_factory=list)
    custom_fields: dict[str, Any] = field(default_factory=dict)
    acceptance_criteria: str = ""
    story_points: float | None = None
    epic_link: str | None = None


@dataclass
class JiraRequirement:
    """Aggregated requirements from Jira issues."""

    form_name: str
    issues: list[JiraIssue]
    total_story_points: float
    requirement_summary: str
    business_rules: list[str]
    acceptance_criteria: list[str]


class JiraExtractor:
    """
    Extracts requirements and documentation from Jira for a given form.
    Supports querying by form name, labels, or custom JQL.
    """

    def __init__(self) -> None:
        """Initialize the Jira extractor."""
        self.settings = get_settings()
        self._client: Jira | None = None

    @property
    def client(self) -> Jira:
        """Get or create the Jira client."""
        if self._client is None:
            self._client = Jira(
                url=self.settings.jira.url,
                username=self.settings.jira.username,
                password=self.settings.jira.api_token,
            )
            logger.info("Connected to Jira", url=self.settings.jira.url)
        return self._client

    def get_form_issues(
        self,
        form_name: str,
        project_key: str | None = None,
        additional_jql: str | None = None,
        max_results: int = 100,
    ) -> list[JiraIssue]:
        """
        Retrieve all Jira issues related to a form.

        Args:
            form_name: Name of the form (e.g., 'le01')
            project_key: Optional project key (defaults to configured project)
            additional_jql: Optional additional JQL conditions
            max_results: Maximum number of results

        Returns:
            List of JiraIssue objects
        """
        project_key = project_key or self.settings.jira.project_key

        # Build JQL query
        jql_parts = []

        if project_key:
            jql_parts.append(f"project = {project_key}")

        # Search by form name in summary, labels, or custom fields
        form_search = f'(summary ~ "{form_name}" OR labels = "{form_name}" OR text ~ "{form_name}")'
        jql_parts.append(form_search)

        if additional_jql:
            jql_parts.append(f"({additional_jql})")

        jql = " AND ".join(jql_parts)

        logger.info("Querying Jira", jql=jql)

        try:
            results = self.client.jql(
                jql,
                limit=max_results,
                expand="renderedFields,changelog",
            )

            issues: list[JiraIssue] = []

            for issue_data in results.get("issues", []):
                issue = self._parse_issue(issue_data)
                if issue:
                    issues.append(issue)

            logger.info("Retrieved Jira issues", form_name=form_name, count=len(issues))

            return issues

        except Exception as e:
            logger.error("Failed to query Jira", error=str(e))
            raise

    def _parse_issue(self, issue_data: dict[str, Any]) -> JiraIssue | None:
        """
        Parse raw Jira API response into JiraIssue object.

        Args:
            issue_data: Raw issue data from Jira API

        Returns:
            Parsed JiraIssue or None if parsing fails
        """
        try:
            fields = issue_data.get("fields", {})

            # Parse dates
            created = datetime.fromisoformat(fields.get("created", "").replace("Z", "+00:00"))
            updated = datetime.fromisoformat(fields.get("updated", "").replace("Z", "+00:00"))

            # Extract components
            components = [c.get("name", "") for c in fields.get("components", [])]

            # Extract labels
            labels = fields.get("labels", [])

            # Extract attachments
            attachments = [
                {
                    "filename": a.get("filename"),
                    "size": a.get("size"),
                    "mimeType": a.get("mimeType"),
                    "content": a.get("content"),
                }
                for a in fields.get("attachment", [])
            ]

            # Extract comments
            comment_data = fields.get("comment", {})
            comments = [
                {
                    "author": c.get("author", {}).get("displayName", ""),
                    "body": c.get("body", ""),
                    "created": c.get("created", ""),
                }
                for c in comment_data.get("comments", [])
            ]

            # Extract acceptance criteria (common custom field)
            acceptance_criteria = ""
            custom_fields: dict[str, Any] = {}

            for key, value in fields.items():
                if key.startswith("customfield_"):
                    if value and isinstance(value, str):
                        if "acceptance" in key.lower() or (
                            isinstance(value, str) and "given" in value.lower()
                        ):
                            acceptance_criteria = value
                        custom_fields[key] = value

            return JiraIssue(
                key=issue_data.get("key", ""),
                summary=fields.get("summary", ""),
                description=fields.get("description", "") or "",
                issue_type=fields.get("issuetype", {}).get("name", ""),
                status=fields.get("status", {}).get("name", ""),
                priority=fields.get("priority", {}).get("name", ""),
                created=created,
                updated=updated,
                labels=labels,
                components=components,
                attachments=attachments,
                comments=comments,
                custom_fields=custom_fields,
                acceptance_criteria=acceptance_criteria,
                story_points=fields.get("customfield_10020"),  # Common story points field
                epic_link=fields.get("customfield_10014"),  # Common epic link field
            )

        except Exception as e:
            logger.warning(
                "Failed to parse Jira issue", issue_key=issue_data.get("key"), error=str(e)
            )
            return None

    def get_epic_with_children(self, epic_key: str) -> tuple[JiraIssue | None, list[JiraIssue]]:
        """
        Get an epic and all its child issues.

        Args:
            epic_key: The epic issue key

        Returns:
            Tuple of (epic issue, list of child issues)
        """
        # Get the epic
        epic_data = self.client.issue(epic_key, expand="renderedFields")
        epic = self._parse_issue({"key": epic_key, "fields": epic_data.get("fields", {})})

        # Get child issues
        jql = f'"Epic Link" = {epic_key}'
        results = self.client.jql(jql, limit=200)

        children = [self._parse_issue(issue_data) for issue_data in results.get("issues", [])]
        children = [c for c in children if c is not None]

        return epic, children

    def aggregate_requirements(self, form_name: str, issues: list[JiraIssue]) -> JiraRequirement:
        """
        Aggregate multiple issues into a requirements summary.

        Args:
            form_name: Name of the form
            issues: List of Jira issues

        Returns:
            Aggregated JiraRequirement
        """
        # Calculate total story points
        total_points = sum(i.story_points or 0 for i in issues)

        # Extract business rules from descriptions
        business_rules: list[str] = []
        acceptance_criteria: list[str] = []

        for issue in issues:
            # Look for business rules in description
            desc = issue.description.lower()
            if "business rule" in desc or "br:" in desc:
                lines = issue.description.split("\n")
                for line in lines:
                    if any(kw in line.lower() for kw in ["business rule", "br:"]):
                        business_rules.append(line.strip())

            # Collect acceptance criteria
            if issue.acceptance_criteria:
                acceptance_criteria.append(f"[{issue.key}] {issue.acceptance_criteria}")

        # Build summary
        summary_parts = [
            f"Form: {form_name}",
            f"Total Issues: {len(issues)}",
            f"Total Story Points: {total_points}",
            "",
            "Issue Summary:",
        ]

        for issue in sorted(issues, key=lambda x: x.issue_type):
            summary_parts.append(f"  - [{issue.key}] ({issue.issue_type}) {issue.summary}")

        return JiraRequirement(
            form_name=form_name,
            issues=issues,
            total_story_points=total_points,
            requirement_summary="\n".join(summary_parts),
            business_rules=business_rules,
            acceptance_criteria=acceptance_criteria,
        )

    def to_documents(self, issues: list[JiraIssue], form_name: str) -> list[Document]:
        """
        Convert Jira issues to LangChain Documents.

        Args:
            issues: List of Jira issues
            form_name: Name of the form

        Returns:
            List of LangChain Documents
        """
        documents: list[Document] = []

        for issue in issues:
            content_parts = [
                f"Jira Issue: {issue.key}",
                f"Type: {issue.issue_type}",
                f"Summary: {issue.summary}",
                f"Status: {issue.status}",
                f"Priority: {issue.priority}",
                "",
                "Description:",
                issue.description,
            ]

            if issue.acceptance_criteria:
                content_parts.extend(
                    [
                        "",
                        "Acceptance Criteria:",
                        issue.acceptance_criteria,
                    ]
                )

            if issue.comments:
                content_parts.extend(["", "Comments:"])
                for comment in issue.comments[:5]:  # Limit comments
                    content_parts.append(f"  - {comment['author']}: {comment['body'][:500]}")

            metadata = {
                "form_name": form_name,
                "jira_key": issue.key,
                "issue_type": issue.issue_type,
                "status": issue.status,
                "priority": issue.priority,
                "labels": issue.labels,
                "components": issue.components,
                "story_points": issue.story_points,
                "doc_type": "jira",
            }

            document = Document(
                page_content="\n".join(content_parts),
                metadata=metadata,
            )
            documents.append(document)

        logger.info("Converted Jira issues to documents", count=len(documents))

        return documents

    def search_by_jql(self, jql: str, max_results: int = 100) -> list[JiraIssue]:
        """
        Search Jira using custom JQL.

        Args:
            jql: JQL query string
            max_results: Maximum results

        Returns:
            List of JiraIssue objects
        """
        results = self.client.jql(jql, limit=max_results)

        issues = [self._parse_issue(issue_data) for issue_data in results.get("issues", [])]

        return [i for i in issues if i is not None]
