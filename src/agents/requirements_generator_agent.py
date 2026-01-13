"""
Requirements Generator Agent for synthesizing requirements from multiple sources.

Analyzes code, Jira documentation, and screenshots to generate comprehensive
functional and non-functional requirements for legacy system migration.
"""

from dataclasses import dataclass, field
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.extractors.code_extractor import CodeFile
from src.prompts.requirements import RequirementsPrompts
from src.utils.logging_config import ExecutionTimer
from src.utils.serialization import extract_json_array


@dataclass
class FunctionalRequirement:
    """A functional requirement with full specification."""

    req_id: str
    title: str
    description: str
    priority: str  # P0, P1, P2, P3
    category: str  # CRUD, validation, workflow, integration, reporting
    user_story: str
    acceptance_criteria: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    source_references: list[str] = field(default_factory=list)


@dataclass
class NonFunctionalRequirement:
    """A non-functional requirement."""

    req_id: str
    category: str  # performance, security, usability, reliability
    description: str
    metric: str
    target_value: str
    validation_method: str


@dataclass
class DataRequirement:
    """Data model and storage requirements."""

    entity_name: str
    description: str
    fields: list[dict[str, str]] = field(default_factory=list)
    relationships: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    source_table: str | None = None


@dataclass
class RequirementsGeneratorResult:
    """Complete requirements specification."""

    form_name: str
    functional_requirements: list[FunctionalRequirement]
    non_functional_requirements: list[NonFunctionalRequirement]
    data_requirements: list[DataRequirement]
    integration_requirements: list[str]
    validation_rules: list[str]
    business_rules: list[str]
    assumptions: list[str]
    out_of_scope: list[str]
    summary: str


class RequirementsGeneratorAgent(BaseAgent[RequirementsGeneratorResult]):
    """
    Agent for generating comprehensive requirements from code analysis,
    screenshots, and Jira documentation.
    """

    def __init__(self) -> None:
        """Initialize the requirements generator agent."""
        super().__init__("RequirementsGeneratorAgent")

    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for requirements generation."""
        return RequirementsPrompts.system_prompt(context.form_name)

    async def analyze(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None = None,
        jira_context: str | None = None,
        screenshot_context: str | None = None,
        **kwargs: Any,
    ) -> AgentResult[RequirementsGeneratorResult]:
        """
        Generate requirements from multiple input sources.

        Args:
            context: Agent execution context
            code_files: Analyzed code files
            jira_context: Summary from Jira analysis
            screenshot_context: Summary from screenshot analysis

        Returns:
            AgentResult with RequirementsGeneratorResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting requirements generation",
            form_name=context.form_name,
            code_files_count=len(code_files) if code_files else 0,
            has_jira_context=jira_context is not None,
        )

        try:
            # Retrieve context from vector store
            stored_context = self.retrieve_context(
                context.form_name, "requirements business logic validation", limit=10
            )

            # Generate all requirement types
            functional_reqs = await self._generate_functional_requirements(
                context, code_files, stored_context
            )
            non_functional_reqs = await self._generate_non_functional_requirements(
                context, code_files
            )
            data_reqs = await self._generate_data_requirements(context, code_files)

            # Extract rules and integration requirements
            integration_reqs = await self._extract_integration_requirements(context, code_files)
            validation_rules = await self._extract_validation_rules(
                context, code_files, stored_context
            )
            business_rules = await self._extract_business_rules(context, stored_context)

            # Identify scope boundaries
            assumptions, out_of_scope = await self._identify_assumptions(context, functional_reqs)

            # Generate executive summary
            summary = await self._generate_summary(
                context, functional_reqs, non_functional_reqs, data_reqs
            )

            result = RequirementsGeneratorResult(
                form_name=context.form_name,
                functional_requirements=functional_reqs,
                non_functional_requirements=non_functional_reqs,
                data_requirements=data_reqs,
                integration_requirements=integration_reqs,
                validation_rules=validation_rules,
                business_rules=business_rules,
                assumptions=assumptions,
                out_of_scope=out_of_scope,
                summary=summary,
            )

            self.logger.info(
                "Requirements generation complete",
                form_name=context.form_name,
                functional_count=len(functional_reqs),
                nfr_count=len(non_functional_reqs),
                data_entities=len(data_reqs),
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            return self.create_error_result(e, timer)

    async def _generate_functional_requirements(
        self, context: AgentContext, code_files: list[CodeFile] | None, stored_context: list[str]
    ) -> list[FunctionalRequirement]:
        """Generate functional requirements from code and context."""
        code_summary = self._build_code_summary(code_files, limit=15)
        context_summary = self.format_context_for_prompt(stored_context, max_contexts=5)

        prompt = f"""Based on the code analysis and context for "{context.form_name}", generate functional requirements.

Code Analysis:
{code_summary}

Additional Context:
{context_summary}

Generate requirements in JSON array format:
[
    {{
        "req_id": "FR-001",
        "title": "Requirement title",
        "description": "Detailed description",
        "priority": "P0|P1|P2|P3",
        "category": "CRUD|validation|workflow|integration|reporting",
        "user_story": "As a [user], I want [capability] so that [benefit]",
        "acceptance_criteria": ["Given..When..Then.."],
        "dependencies": ["FR-XXX"],
        "source_references": ["ClassName.java"]
    }}
]

Generate 5-15 requirements covering the main functionality."""

        data = extract_json_array(await self.invoke_llm(context, prompt))
        return [
            FunctionalRequirement(
                req_id=r.get("req_id", f"FR-{i:03d}"),
                title=r.get("title", ""),
                description=r.get("description", ""),
                priority=r.get("priority", "P2"),
                category=r.get("category", "CRUD"),
                user_story=r.get("user_story", ""),
                acceptance_criteria=r.get("acceptance_criteria", []),
                dependencies=r.get("dependencies", []),
                source_references=r.get("source_references", []),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _generate_non_functional_requirements(
        self, context: AgentContext, code_files: list[CodeFile] | None
    ) -> list[NonFunctionalRequirement]:
        """Generate non-functional requirements."""
        prompt = f"""Generate non-functional requirements for "{context.form_name}" modernization.

Consider these categories:
- Performance: Response times, throughput
- Security: Authentication, authorization, data protection
- Usability: Accessibility, user experience
- Reliability: Availability, error handling
- Scalability: User capacity, data growth

Generate in JSON array format:
[
    {{
        "req_id": "NFR-001",
        "category": "performance|security|usability|reliability|scalability",
        "description": "Requirement description",
        "metric": "What is measured",
        "target_value": "Specific target",
        "validation_method": "How to verify"
    }}
]

Generate 5-8 key non-functional requirements."""

        data = extract_json_array(await self.invoke_llm(context, prompt))
        return [
            NonFunctionalRequirement(
                req_id=r.get("req_id", f"NFR-{i:03d}"),
                category=r.get("category", "performance"),
                description=r.get("description", ""),
                metric=r.get("metric", ""),
                target_value=r.get("target_value", ""),
                validation_method=r.get("validation_method", ""),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _generate_data_requirements(
        self, context: AgentContext, code_files: list[CodeFile] | None
    ) -> list[DataRequirement]:
        """Generate data model requirements from code analysis."""
        model_files = self._get_model_files(code_files)
        model_summary = "\n".join(f"- {cf.path}: {cf.classes}" for cf in model_files[:10])

        prompt = f"""Based on the data models for "{context.form_name}":

{model_summary}

Generate data requirements in JSON array format:
[
    {{
        "entity_name": "EntityName",
        "description": "Entity purpose",
        "fields": [
            {{"name": "field_name", "type": "string|number|date|boolean", "required": "yes|no"}}
        ],
        "relationships": ["Related to Entity via foreign_key"],
        "constraints": ["Unique constraint on field"],
        "source_table": "ORIGINAL_TABLE_NAME"
    }}
]

Generate data requirements for the main entities."""

        data = extract_json_array(await self.invoke_llm(context, prompt))
        return [
            DataRequirement(
                entity_name=r.get("entity_name", "Unknown"),
                description=r.get("description", ""),
                fields=r.get("fields", []),
                relationships=r.get("relationships", []),
                constraints=r.get("constraints", []),
                source_table=r.get("source_table"),
            )
            for r in data
        ]

    def _build_code_summary(self, code_files: list[CodeFile] | None, limit: int = 15) -> str:
        """Build a summary of code files for prompts."""
        if not code_files:
            return "No code files available for analysis."

        return "\n".join(
            [
                f"- {cf.path}: {cf.file_type}, classes: {cf.classes}, methods: {cf.methods[:5]}"
                for cf in code_files[:limit]
            ]
        )

    def _get_model_files(self, code_files: list[CodeFile] | None) -> list[CodeFile]:
        """Extract model/entity files from code files."""
        if not code_files:
            return []

        # First try model/entity files
        model_files = [
            cf
            for cf in code_files
            if cf.file_type in ["model", "entity"] or "model" in cf.path.lower()
        ]

        # Fall back to SQL files
        if not model_files:
            model_files = [cf for cf in code_files if cf.language == "sql"][:5]

        return model_files

    async def _extract_integration_requirements(
        self, context: AgentContext, code_files: list[CodeFile] | None
    ) -> list[str]:
        """Extract integration requirements from code analysis."""
        integration_files = self._get_integration_files(code_files)

        if not integration_files:
            return ["Integration requirements to be determined during analysis"]

        file_list = ", ".join(cf.path for cf in integration_files[:10])
        prompt = f"""Based on these integration-related files: {file_list}

List the integration requirements for "{context.form_name}":
- External systems or APIs
- Data exchange formats
- Authentication methods
- Sync vs async requirements

Format as a simple list."""

        return await self.invoke_llm_for_list(context, prompt)

    def _get_integration_files(self, code_files: list[CodeFile] | None) -> list[CodeFile]:
        """Get files related to integrations."""
        if not code_files:
            return []

        keywords = ["api", "client", "integration"]
        return [
            cf
            for cf in code_files
            if cf.file_type in ["adapter", "service"]
            or any(kw in cf.path.lower() for kw in keywords)
        ]

    async def _extract_validation_rules(
        self, context: AgentContext, code_files: list[CodeFile] | None, stored_context: list[str]
    ) -> list[str]:
        """Extract validation rules from code and context."""
        validation_snippets = self._extract_validation_snippets(code_files)
        context_text = "\n".join(stored_context[:3])

        prompt = f"""Extract validation rules for "{context.form_name}":

Context:
{context_text}

Code snippets with validation:
{" ".join(validation_snippets[:3])}

List all validation rules in the format:
VR-001: [Field] must [condition]

Example:
VR-001: Email must be valid email format
VR-002: Amount must be greater than 0"""

        return await self.invoke_llm_for_list(context, prompt, prefix="VR-")

    def _extract_validation_snippets(self, code_files: list[CodeFile] | None) -> list[str]:
        """Extract code snippets containing validation logic."""
        if not code_files:
            return []

        keywords = ["validate", "validation", "required", "pattern"]
        snippets = []

        for cf in code_files:
            # Check if content is available (may be empty when files are filtered for size)
            if cf.content:
                if any(kw in cf.content.lower() for kw in keywords):
                    snippets.append(cf.content[:500])
            # If content is not available, use method names as hints
            elif any(kw in " ".join(cf.methods).lower() for kw in keywords):
                snippets.append(
                    f"File: {cf.path}\nMethods: {', '.join(cf.methods[:5])}\n"
                    f"(Full content not available - check vector store for details)"
                )

        return snippets

    async def _extract_business_rules(
        self, context: AgentContext, stored_context: list[str]
    ) -> list[str]:
        """Extract business rules from context."""
        context_text = self.format_context_for_prompt(stored_context, max_contexts=5)

        prompt = f"""From the following context for "{context.form_name}", extract business rules:

{context_text}

List business rules in the format:
BR-001: [Rule description]

Focus on:
- Workflow rules (what triggers what)
- Calculation rules
- Access control rules
- State transition rules"""

        return await self.invoke_llm_for_list(context, prompt, prefix="BR-")

    async def _identify_assumptions(
        self, context: AgentContext, functional_reqs: list[FunctionalRequirement]
    ) -> tuple[list[str], list[str]]:
        """Identify assumptions and out-of-scope items."""
        req_summary = "\n".join(f"- {r.req_id}: {r.title}" for r in functional_reqs[:10])

        prompt = f"""Based on these requirements for "{context.form_name}":

{req_summary}

Identify:
1. Key assumptions being made
2. Items explicitly out of scope for this migration

Format response as:
ASSUMPTIONS:
- Assumption 1
- Assumption 2

OUT OF SCOPE:
- Item 1
- Item 2"""

        response = await self.invoke_llm(context, prompt)
        return self._parse_assumptions_response(response)

    def _parse_assumptions_response(self, response: str) -> tuple[list[str], list[str]]:
        """Parse assumptions and out-of-scope items from response."""
        assumptions: list[str] = []
        out_of_scope: list[str] = []
        current_section = None

        for line in response.split("\n"):
            upper_line = line.upper()
            if "ASSUMPTION" in upper_line:
                current_section = "assumptions"
            elif "OUT OF SCOPE" in upper_line or "SCOPE" in upper_line:
                current_section = "out_of_scope"
            elif line.strip().startswith("-"):
                item = line.strip().lstrip("- ")
                if current_section == "assumptions":
                    assumptions.append(item)
                elif current_section == "out_of_scope":
                    out_of_scope.append(item)

        return assumptions, out_of_scope

    async def _generate_summary(
        self,
        context: AgentContext,
        functional_reqs: list[FunctionalRequirement],
        non_functional_reqs: list[NonFunctionalRequirement],
        data_reqs: list[DataRequirement],
    ) -> str:
        """Generate requirements summary."""
        categories = ", ".join({r.category for r in functional_reqs}) or "N/A"
        high_priority = [r.title for r in functional_reqs if r.priority == "P0"][:5]

        prompt = f"""Summarize the requirements for "{context.form_name}" migration:

- {len(functional_reqs)} functional requirements
- {len(non_functional_reqs)} non-functional requirements
- {len(data_reqs)} data entities

Key functional areas: {categories}

High priority requirements: {", ".join(high_priority) or "None identified"}

Provide a 2-paragraph executive summary suitable for stakeholders."""

        return await self.invoke_llm(context, prompt)
