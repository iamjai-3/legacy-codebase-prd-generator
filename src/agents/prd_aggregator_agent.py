"""
PRD Aggregator Agent for combining all agent outputs into a migration-ready PRD document.

Generates comprehensive PRD with:
- Specific business logic from legacy code
- Complete API specifications
- Detailed data models with schemas
- Validation rules and error handling
- Integration specifications
- Workflow documentation
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from src.agents.atlassian_integration_agent import AtlassianIntegrationResult
from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.agents.requirements_generator_agent import RequirementsGeneratorResult
from src.agents.screenshot_analysis_agent import ScreenshotAnalysisResult
from src.agents.user_flow_agent import UserFlowResult
from src.prompts.prd_aggregator import PRDAggregatorPrompts
from src.utils.logging_config import ExecutionTimer

# Constants
SECTION_SEPARATOR = "\n---\n"


@dataclass
class PRDSection:
    """A section of the PRD document."""

    title: str
    content: str
    order: int
    subsections: list["PRDSection"] = field(default_factory=list)


@dataclass
class PRDDocument:
    """Complete PRD document."""

    form_name: str
    title: str
    version: str
    created_date: str
    author: str
    sections: list[PRDSection]
    executive_summary: str
    appendices: list[dict[str, str]]
    metadata: dict[str, Any]


@dataclass
class PRDAggregatorResult:
    """Result from PRD aggregation."""

    form_name: str
    prd_document: PRDDocument
    markdown_content: str
    word_count: int
    section_count: int
    generation_metrics: dict[str, Any]


class PRDAggregatorAgent(BaseAgent[PRDAggregatorResult]):
    """
    Agent for aggregating all analysis results into a comprehensive,
    migration-ready PRD document.

    This agent queries the knowledge base for additional context and
    generates PRDs with specific business logic, APIs, and technical details.
    """

    def __init__(self) -> None:
        """Initialize the PRD aggregator agent."""
        super().__init__("PRDAggregatorAgent")

    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for PRD aggregation."""
        return PRDAggregatorPrompts.system_prompt(context.form_name)

    async def analyze(
        self,
        context: AgentContext,
        screenshot_analysis: ScreenshotAnalysisResult | None = None,
        atlassian_analysis: AtlassianIntegrationResult | None = None,
        requirements_analysis: RequirementsGeneratorResult | None = None,
        user_flow_analysis: UserFlowResult | None = None,
        **kwargs: Any,
    ) -> AgentResult[PRDAggregatorResult]:
        """
        Aggregate all agent results into a migration-ready PRD document.

        Args:
            context: Agent execution context
            screenshot_analysis: Results from screenshot analysis
            atlassian_analysis: Results from Atlassian integration
            requirements_analysis: Results from requirements generation
            user_flow_analysis: Results from user flow analysis

        Returns:
            AgentResult with PRDAggregatorResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting migration-focused PRD aggregation",
            form_name=context.form_name,
            has_screenshots=screenshot_analysis is not None,
            has_jira=atlassian_analysis is not None,
            has_requirements=requirements_analysis is not None,
        )

        try:
            # Retrieve additional context from knowledge base
            kb_contexts = self._retrieve_kb_context(context.form_name)

            # Generate all PRD sections with enhanced content
            sections = await self._build_all_sections(
                context,
                screenshot_analysis,
                atlassian_analysis,
                requirements_analysis,
                user_flow_analysis,
                kb_contexts,
            )

            # Generate executive summary with metrics
            executive_summary = await self._generate_executive_summary(
                context, requirements_analysis, kb_contexts
            )

            # Generate appendices with code references
            appendices = self._generate_appendices(
                screenshot_analysis, requirements_analysis, user_flow_analysis
            )

            # Create PRD document
            prd_document = self._create_prd_document(
                context,
                sections,
                executive_summary,
                appendices,
                screenshot_analysis,
                atlassian_analysis,
                requirements_analysis,
            )

            # Generate markdown content
            markdown_content = self._generate_markdown(prd_document)

            result = PRDAggregatorResult(
                form_name=context.form_name,
                prd_document=prd_document,
                markdown_content=markdown_content,
                word_count=len(markdown_content.split()),
                section_count=len(sections),
                generation_metrics={
                    "execution_time_ms": timer.elapsed_ms(),
                    "sections_generated": len(sections),
                    "appendices_count": len(appendices),
                    "has_api_specs": requirements_analysis is not None
                    and len(requirements_analysis.api_specifications) > 0,
                    "has_business_logic": requirements_analysis is not None
                    and len(requirements_analysis.business_logic) > 0,
                },
            )

            self.logger.info(
                "Migration-focused PRD generation complete",
                form_name=context.form_name,
                sections=len(sections),
                word_count=result.word_count,
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            return self.create_error_result(e, timer)

    def _retrieve_kb_context(self, form_name: str) -> dict[str, list[str]]:
        """Retrieve context from knowledge base for PRD enhancement."""
        contexts = {}

        queries = {
            "overview": "module purpose functionality description features overview",
            "business_logic": "business logic rules calculation workflow process",
            "api": "API endpoint service controller method request response",
            "data": "database table entity field column relationship schema",
            "validation": "validation rule required constraint check error",
            "integration": "integration external system API connection service",
            "existing_prd": "PRD requirements specification documentation",
        }

        for key, query in queries.items():
            try:
                results = self.retrieve_context(form_name, query, limit=5)
                contexts[key] = results
            except Exception as e:
                self.logger.warning(f"Failed to retrieve {key} context: {e}")
                contexts[key] = []

        return contexts

    async def _build_all_sections(
        self,
        context: AgentContext,
        screenshot_analysis: ScreenshotAnalysisResult | None,
        atlassian_analysis: AtlassianIntegrationResult | None,
        requirements_analysis: RequirementsGeneratorResult | None,
        user_flow_analysis: UserFlowResult | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[PRDSection]:
        """Build all PRD sections with enhanced migration-focused content."""
        sections: list[PRDSection] = []
        section_order = 1

        # 1. Overview section (always included)
        sections.append(
            await self._generate_overview_section(
                context, atlassian_analysis, kb_contexts, section_order
            )
        )
        section_order += 1

        # 2. User Interface section (if screenshots available)
        if screenshot_analysis:
            sections.append(
                await self._generate_ui_section(context, screenshot_analysis, section_order)
            )
            section_order += 1

        # 3-8. Requirements-based sections
        if requirements_analysis:
            section_order = await self._add_requirements_sections(
                context, requirements_analysis, kb_contexts, sections, section_order
            )

            # 7. Source Tables & Database Mappings section (from existing PRD docs)
            if requirements_analysis.source_tables or requirements_analysis.database_mappings:
                sections.append(
                    await self._generate_source_tables_section(
                        context, requirements_analysis, section_order
                    )
                )
                section_order += 1

            # 8. Validation Rules section
            if requirements_analysis.validation_rules:
                sections.append(
                    await self._generate_validation_section(
                        context, requirements_analysis, section_order
                    )
                )
                section_order += 1

            # 8. Integration Requirements section (NEW)
            if requirements_analysis.integration_requirements:
                sections.append(
                    await self._generate_integration_section(
                        context, requirements_analysis, section_order
                    )
                )
                section_order += 1

            # 9. Non-Functional Requirements
            sections.append(
                await self._generate_nfr_section(context, requirements_analysis, section_order)
            )
            section_order += 1

            # 10. Business Rules section
            sections.append(
                await self._generate_business_rules_section(
                    context, requirements_analysis, section_order
                )
            )
            section_order += 1

        # 11. User Flows section (if available)
        if user_flow_analysis:
            sections.append(
                await self._generate_user_flow_section(context, user_flow_analysis, section_order)
            )
            section_order += 1

            # 12. Workflow specifications (NEW - from requirements)
            if requirements_analysis and requirements_analysis.workflow_specs:
                sections.append(
                    await self._generate_workflow_section(
                        context, requirements_analysis, section_order
                    )
                )
                section_order += 1

        # 13. Migration Strategy section (always included)
        sections.append(
            await self._generate_migration_section(
                context, requirements_analysis, kb_contexts, section_order
            )
        )

        return sections

    async def _add_requirements_sections(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        kb_contexts: dict[str, list[str]],
        sections: list[PRDSection],
        section_order: int,
    ) -> int:
        """Add all requirements-based sections. Returns updated section_order."""
        if requirements_analysis.business_logic:
            sections.append(
                await self._generate_business_logic_section(
                    context, requirements_analysis, kb_contexts, section_order
                )
            )
            section_order += 1

        if requirements_analysis.api_specifications:
            sections.append(
                await self._generate_api_section(
                    context, requirements_analysis, kb_contexts, section_order
                )
            )
            section_order += 1

        sections.append(
            await self._generate_functional_requirements_section(
                context, requirements_analysis, kb_contexts, section_order
            )
        )
        section_order += 1

        sections.append(
            await self._generate_data_model_section(
                context, requirements_analysis, kb_contexts, section_order
            )
        )
        section_order += 1

        if requirements_analysis.source_tables:
            sections.append(
                await self._generate_source_tables_section(
                    context, requirements_analysis, section_order
                )
            )
            section_order += 1

        if requirements_analysis.integration_requirements:
            sections.append(
                await self._generate_integration_section(
                    context, requirements_analysis, section_order
                )
            )
            section_order += 1

        sections.append(
            await self._generate_nfr_section(context, requirements_analysis, section_order)
        )
        section_order += 1

        sections.append(
            await self._generate_business_rules_section(
                context, requirements_analysis, section_order
            )
        )
        section_order += 1

        return section_order

    def _create_prd_document(
        self,
        context: AgentContext,
        sections: list[PRDSection],
        executive_summary: str,
        appendices: list[dict[str, str]],
        screenshot_analysis: ScreenshotAnalysisResult | None,
        atlassian_analysis: AtlassianIntegrationResult | None,
        requirements_analysis: RequirementsGeneratorResult | None,
    ) -> PRDDocument:
        """Create the PRD document structure."""
        return PRDDocument(
            form_name=context.form_name,
            title=f"Migration PRD: {context.form_name.upper()} Module",
            version="1.0.0",
            created_date=datetime.now().isoformat(),
            author="PRD Agent",
            sections=sections,
            executive_summary=executive_summary,
            appendices=appendices,
            metadata={
                "generation_timestamp": datetime.now().isoformat(),
                "agent_version": "2.0.0",
                "prd_type": "migration",
                "sources": {
                    "screenshots": screenshot_analysis is not None,
                    "jira": atlassian_analysis is not None,
                    "code": requirements_analysis is not None,
                },
                "statistics": {
                    "functional_requirements": (
                        len(requirements_analysis.functional_requirements)
                        if requirements_analysis
                        else 0
                    ),
                    "api_endpoints": (
                        len(requirements_analysis.api_specifications)
                        if requirements_analysis
                        else 0
                    ),
                    "data_entities": (
                        len(requirements_analysis.data_requirements) if requirements_analysis else 0
                    ),
                    "source_tables": (
                        len(requirements_analysis.source_tables) if requirements_analysis else 0
                    ),
                    "database_mappings": (
                        len(requirements_analysis.database_mappings) if requirements_analysis else 0
                    ),
                    "business_logic_items": (
                        len(requirements_analysis.business_logic) if requirements_analysis else 0
                    ),
                    "validation_rules": (
                        len(requirements_analysis.validation_rules) if requirements_analysis else 0
                    ),
                    "integrations": (
                        len(requirements_analysis.integration_requirements)
                        if requirements_analysis
                        else 0
                    ),
                },
            },
        )

    async def _generate_overview_section(
        self,
        context: AgentContext,
        atlassian_analysis: AtlassianIntegrationResult | None,
        kb_contexts: dict[str, list[str]],
        order: int,
    ) -> PRDSection:
        """Generate the overview section with specific module details."""
        jira_context = ""
        if atlassian_analysis:
            jira_context = f"""
Based on Jira analysis:
- Total issues: {atlassian_analysis.total_issues}
- Summary: {atlassian_analysis.summary[:1000]}
"""

        kb_context = self.format_context_for_prompt(
            kb_contexts.get("overview", []) + kb_contexts.get("existing_prd", []),
            max_contexts=5,
        )

        prompt = PRDAggregatorPrompts.overview_section(context.form_name, jira_context, kb_context)

        content = await self.invoke_llm(context, prompt)

        return PRDSection(title=f"{order}. Overview", content=content, order=order)

    async def _generate_ui_section(
        self,
        context: AgentContext,
        screenshot_analysis: ScreenshotAnalysisResult,
        order: int,
    ) -> PRDSection:
        """Generate the user interface section."""
        screen_summary = "\n".join(
            [
                f"- **{s.screen_name}**: {s.purpose}"
                for s in screenshot_analysis.screen_analyses[:10]
            ]
        )

        content = f"""## User Interface Analysis

### Screens Analyzed
{len(screenshot_analysis.screen_analyses)} screens were analyzed for the {context.form_name} module.

### Screen Inventory
{screen_summary}

### UI Component Summary
"""
        for component, count in screenshot_analysis.component_inventory.items():
            content += f"- **{component}**: {count} instances\n"

        content += f"""
### Common UI Patterns
{chr(10).join(["- " + p for p in screenshot_analysis.common_patterns])}

### UI Flow Summary
{screenshot_analysis.ui_flow_summary}

### Modernization Recommendations
{chr(10).join(["- " + r for r in screenshot_analysis.recommendations])}
"""

        return PRDSection(title=f"{order}. User Interface", content=content, order=order)

    async def _generate_business_logic_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        kb_contexts: dict[str, list[str]],
        order: int,
    ) -> PRDSection:
        """Generate the business logic documentation section."""
        content = """## Business Logic Specifications

This section documents the exact business logic extracted from the legacy code.
Each item includes trigger conditions, processing steps, and expected outputs.

### Business Logic Inventory
"""
        for bl in requirements_analysis.business_logic:
            content += f"""
#### {bl.logic_id}: {bl.name}
**Type:** {bl.logic_type}

**Description:** {bl.description}

**Trigger:** {bl.trigger}

**Inputs:**
"""
            for inp in bl.inputs:
                if isinstance(inp, dict):
                    content += f"- `{inp.get('name', 'N/A')}` ({inp.get('type', 'unknown')}): {inp.get('source', 'N/A')}\n"
                elif isinstance(inp, str):
                    # Handle case where input is a string instead of a dict
                    content += f"- {inp}\n"
                else:
                    # Handle other types
                    content += f"- {str(inp)}\n"

            content += "\n**Processing Steps:**\n"
            for i, step in enumerate(bl.steps, 1):
                content += f"{i}. {step}\n"

            if bl.conditions:
                content += "\n**Conditional Logic:**\n"
                for cond in bl.conditions:
                    if isinstance(cond, dict):
                        content += f"- IF `{cond.get('condition', '')}` THEN {cond.get('true_action', '')} ELSE {cond.get('false_action', '')}\n"
                    elif isinstance(cond, str):
                        # Handle case where condition is a string instead of a dict
                        content += f"- {cond}\n"
                    else:
                        # Handle other types
                        content += f"- {str(cond)}\n"

            content += "\n**Outputs:**\n"
            for out in bl.outputs:
                if isinstance(out, dict):
                    content += f"- `{out.get('name', 'N/A')}` ({out.get('type', 'unknown')}): {out.get('destination', 'N/A')}\n"
                elif isinstance(out, str):
                    # Handle case where output is a string instead of a dict
                    content += f"- {out}\n"
                else:
                    # Handle other types
                    content += f"- {str(out)}\n"

            if bl.source_location:
                content += f"\n**Source Reference:** `{bl.source_location}`\n"

            content += SECTION_SEPARATOR

        return PRDSection(title=f"{order}. Business Logic", content=content, order=order)

    async def _generate_api_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        kb_contexts: dict[str, list[str]],
        order: int,
    ) -> PRDSection:
        """Generate the API specification section."""
        content = """## API Specifications

Complete API specifications for the module. Each endpoint is documented with
request/response schemas suitable for implementation in any framework.

### API Endpoints Summary

| Method | Path | Description |
|--------|------|-------------|
"""
        for api in requirements_analysis.api_specifications:
            content += f"| {api.http_method} | `{api.path}` | {api.description[:50]}... |\n"

        content += "\n### Detailed API Specifications\n"

        for api in requirements_analysis.api_specifications:
            content += f"""
#### {api.endpoint_name}

**Endpoint:** `{api.http_method} {api.path}`

**Description:** {api.description}

**Request Specification:**
```json
{self._format_json_schema(api.request_spec)}
```

**Response Specification:**
```json
{self._format_json_schema(api.response_spec)}
```

**Business Logic:**
{api.business_logic}

**Source Reference:** `{api.source_method}`

---
"""

        return PRDSection(title=f"{order}. API Specifications", content=content, order=order)

    async def _generate_functional_requirements_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        kb_contexts: dict[str, list[str]],
        order: int,
    ) -> PRDSection:
        """Generate the functional requirements section with detailed logic."""
        content = f"""## Functional Requirements

### Requirements Summary
{requirements_analysis.summary}

### Requirements by Priority

| ID | Title | Priority | Category |
|----|-------|----------|----------|
"""
        for req in requirements_analysis.functional_requirements:
            content += f"| {req.req_id} | {req.title[:40]}... | {req.priority} | {req.category} |\n"

        content += "\n### Detailed Requirements\n"

        for req in requirements_analysis.functional_requirements:
            content += self._format_functional_requirement(req)

        return PRDSection(title=f"{order}. Functional Requirements", content=content, order=order)

    def _format_functional_requirement(self, req) -> str:
        """Format a single functional requirement."""
        content = f"""
#### {req.req_id}: {req.title}
**Priority:** {req.priority} | **Category:** {req.category}

**Description:** {req.description}

**Business Logic:**
{req.business_logic if req.business_logic else "See business logic section for details."}

**User Story:** {req.user_story}

**Acceptance Criteria:**
{chr(10).join(["- " + ac for ac in req.acceptance_criteria])}
"""
        if req.api_specification:
            content += self._format_api_spec_for_req(req.api_specification)
        if req.database_operations:
            content += self._format_database_operations(req.database_operations)
        if req.validation_rules:
            content += f"\n**Validation Rules:**\n{chr(10).join(['- ' + v for v in req.validation_rules])}\n"
        if req.calculations:
            content += (
                f"\n**Calculations:**\n{chr(10).join(['- ' + c for c in req.calculations])}\n"
            )
        if req.source_files:
            content += (
                f"\n**Source References:** {', '.join(['`' + f + '`' for f in req.source_files])}\n"
            )
        content += (
            f"\n**Dependencies:** {', '.join(req.dependencies) if req.dependencies else 'None'}\n"
        )
        content += SECTION_SEPARATOR
        return content

    def _format_api_spec_for_req(self, api_spec: dict) -> str:
        """Format API specification for a requirement."""
        return f"""
**API Contract:**
- Endpoint: `{api_spec.get('method', 'GET')} {api_spec.get('endpoint', 'N/A')}`
- Request: `{api_spec.get('request_body', {})}`
- Response: `{api_spec.get('response', {})}`
"""

    def _format_database_operations(self, operations: list[dict]) -> str:
        """Format database operations."""
        content = "\n**Database Operations:**\n"
        for op in operations:
            content += f"- {op.get('operation', 'QUERY')}: `{op.get('table', 'N/A')}` ({', '.join(op.get('columns', []))})\n"
        return content

    async def _generate_data_model_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        kb_contexts: dict[str, list[str]],
        order: int,
    ) -> PRDSection:
        """Generate the data model section with full schema details."""
        content = """## Data Model

### Entity Relationship Overview

"""
        # Generate Mermaid ER diagram
        if requirements_analysis.data_requirements:
            content += self._generate_mermaid_diagram(requirements_analysis.data_requirements)

        content += "### Entity Specifications\n"

        for entity in requirements_analysis.data_requirements:
            content += self._format_entity_specification(entity)

        return PRDSection(title=f"{order}. Data Model", content=content, order=order)

    def _generate_mermaid_diagram(self, data_requirements: list) -> str:
        """Generate Mermaid ER diagram from data requirements."""
        content = "```mermaid\nerDiagram\n"
        for entity in data_requirements[:10]:
            entity_name = entity.entity_name.replace(" ", "_")
            content += f"    {entity_name} {{\n"
            for field in entity.fields[:10]:
                # Handle both dict and string cases
                if isinstance(field, dict):
                    field_type = str(field.get("type", "string")).replace(" ", "_")
                    field_name = str(field.get("name", "field")).replace(" ", "_")
                else:
                    field_type = "string"
                    field_name = str(field).replace(" ", "_")
                content += f"        {field_type} {field_name}\n"
            content += "    }\n"

        # Add relationships
        for entity in data_requirements:
            entity_name = entity.entity_name.replace(" ", "_")
            for rel in entity.relationships:
                content += self._format_relationship(entity_name, rel)

        content += "```\n\n"
        return content

    def _format_relationship(self, entity_name: str, rel: dict) -> str:
        """Format a single relationship for Mermaid diagram."""
        rel_type = rel.get("type", "ONE_TO_MANY")
        target = str(rel.get("target", "")).replace(" ", "_")
        if not target:
            return ""
        if "MANY_TO_MANY" in rel_type:
            return f'    {entity_name} }}o--o{{ {target} : ""\n'
        if "ONE_TO_MANY" in rel_type:
            return f'    {entity_name} ||--o{{ {target} : ""\n'
        return f'    {entity_name} }}o--|| {target} : ""\n'

    def _format_entity_specification(self, entity) -> str:
        """Format entity specification."""
        content = f"""
#### {entity.entity_name}

**Description:** {entity.description}

**Source Table:** `{entity.source_table or 'N/A'}`
**Source Class:** `{entity.source_class or 'N/A'}`

**Schema:**
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
"""
        for field in entity.fields:
            # Handle both dict and string cases
            if isinstance(field, dict):
                constraints = (
                    ", ".join(field.get("constraints", [])) if field.get("constraints") else "—"
                )
                content += f"| `{field.get('name', '')}` | {field.get('type', '')} | {constraints} | {field.get('description', '')} |\n"
            else:
                # Handle case where field is a string or other type
                content += f"| `{str(field)}` | — | — | — |\n"

        if entity.primary_key:
            content += (
                f"\n**Primary Key:** {', '.join(['`' + k + '`' for k in entity.primary_key])}\n"
            )
        if entity.foreign_keys:
            content += self._format_entity_foreign_keys(entity.foreign_keys)
        if entity.indexes:
            content += self._format_entity_indexes(entity.indexes)
        if entity.relationships:
            content += self._format_entity_relationships(entity.relationships)
        if entity.business_rules:
            content += f"\n**Business Rules:**\n{chr(10).join(['- ' + r for r in entity.business_rules])}\n"
        if entity.sample_queries:
            content += self._format_entity_sample_queries(entity.sample_queries)
        content += SECTION_SEPARATOR
        return content

    def _format_entity_foreign_keys(self, foreign_keys: list) -> str:
        """Format foreign keys for entity."""
        content = "\n**Foreign Keys:**\n"
        for fk in foreign_keys:
            if isinstance(fk, dict):
                content += (
                    f"- `{', '.join(fk.get('columns', []))}` → {fk.get('references', 'N/A')}\n"
                )
            else:
                content += f"- {str(fk)}\n"
        return content

    def _format_entity_indexes(self, indexes: list) -> str:
        """Format indexes for entity."""
        content = "\n**Indexes:**\n"
        for idx in indexes:
            if isinstance(idx, dict):
                unique = "UNIQUE " if idx.get("unique") else ""
                content += (
                    f"- `{idx.get('name', 'idx')}`: {unique}({', '.join(idx.get('columns', []))})\n"
                )
            else:
                content += f"- {str(idx)}\n"
        return content

    def _format_entity_relationships(self, relationships: list) -> str:
        """Format relationships for entity."""
        content = "\n**Relationships:**\n"
        for rel in relationships:
            if isinstance(rel, dict):
                content += f"- {rel.get('type', 'RELATED_TO')} `{rel.get('target', 'N/A')}` via `{rel.get('join_column', 'N/A')}`\n"
            else:
                content += f"- {str(rel)}\n"
        return content

    def _format_entity_sample_queries(self, sample_queries: list) -> str:
        """Format sample queries for entity."""
        content = "\n**Sample Queries:**\n"
        for q in sample_queries[:3]:
            if isinstance(q, dict):
                content += f"\n*{q.get('purpose', 'Query')}:*\n```sql\n{q.get('sql', '')}\n```\n"
            else:
                content += f"\n*Query:*\n```sql\n{str(q)}\n```\n"
        return content

    async def _generate_source_tables_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        order: int,
    ) -> PRDSection:
        """Generate the source tables and database mappings section."""
        content = """## Source Tables & Database Mappings

Complete database schema documentation extracted from existing PRD documentation.
This section provides the exact table structures needed for migration.

"""
        # Source Tables
        if requirements_analysis.source_tables:
            content += "### Database Source Tables\n\n"

            for table in requirements_analysis.source_tables:
                content += self._format_source_table(table)

        # Database Mappings
        if requirements_analysis.database_mappings:
            content += self._format_database_mappings(requirements_analysis.database_mappings)

        return PRDSection(
            title=f"{order}. Source Tables & Database Mappings", content=content, order=order
        )

    def _format_source_table(self, table) -> str:
        """Format source table specification."""
        content = f"""#### {table.table_name}

**Type:** {table.table_type.upper()}

**Description:** {table.description}

**Schema:**
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
"""
        for col in table.columns:
            # Handle both dict and string cases
            if isinstance(col, dict):
                constraints = (
                    ", ".join(col.get("constraints", [])) if col.get("constraints") else "—"
                )
                content += f"| `{col.get('column_name', '')}` | {col.get('data_type', '')} | {constraints} | {col.get('description', '')} |\n"
            else:
                # Handle case where col is a string or other type
                content += f"| `{str(col)}` | — | — | — |\n"

        if table.primary_key:
            content += (
                f"\n**Primary Key:** {', '.join(['`' + pk + '`' for pk in table.primary_key])}\n"
            )
        if table.foreign_keys:
            content += self._format_table_foreign_keys(table.foreign_keys)
        if table.indexes:
            content += self._format_table_indexes(table.indexes)
        if table.stored_procedures:
            content += self._format_table_stored_procedures(table.stored_procedures)
        content += SECTION_SEPARATOR
        return content

    def _format_table_foreign_keys(self, foreign_keys: list) -> str:
        """Format foreign keys for table."""
        content = "\n**Foreign Keys:**\n"
        for fk in foreign_keys:
            content += self._format_foreign_key(fk)
        return content

    def _format_table_indexes(self, indexes: list) -> str:
        """Format indexes for table."""
        content = "\n**Indexes:**\n"
        for idx in indexes:
            if isinstance(idx, dict):
                unique = "UNIQUE " if idx.get("unique") else ""
                content += (
                    f"- `{idx.get('name', 'idx')}`: {unique}({', '.join(idx.get('columns', []))})\n"
                )
            else:
                content += f"- {str(idx)}\n"
        return content

    def _format_table_stored_procedures(self, stored_procedures: list) -> str:
        """Format stored procedures for table."""
        content = "\n**Stored Procedures:**\n"
        for proc in stored_procedures:
            content += self._format_stored_procedure(proc)
        return content

    def _format_foreign_key(self, fk: dict) -> str:
        """Format foreign key specification."""
        if not isinstance(fk, dict):
            return f"- {str(fk)}\n"
        cols = ", ".join(fk.get("columns", []))
        refs_table = fk.get("references_table", "N/A")
        refs_cols = ", ".join(fk.get("references_columns", []))
        on_delete = fk.get("on_delete", "")
        content = f"- `{cols}` → `{refs_table}({refs_cols})`"
        if on_delete:
            content += f" ON DELETE {on_delete}"
        content += "\n"
        return content

    def _format_stored_procedure(self, proc: dict) -> str:
        """Format stored procedure specification."""
        if not isinstance(proc, dict):
            return f"\n##### Procedure\n{str(proc)}\n"
        content = f"\n##### `{proc.get('name', 'procedure')}`\n"
        content += f"**Description:** {proc.get('description', '')}\n"
        if proc.get("parameters"):
            content += "\n**Parameters:**\n"
            for param in proc.get("parameters", []):
                # Handle both dict and string cases
                if isinstance(param, dict):
                    content += f"- `{param.get('name', '')}` ({param.get('type', '')}) - {param.get('direction', 'IN')}\n"
                else:
                    content += f"- {str(param)}\n"
        if proc.get("returns"):
            content += f"\n**Returns:** {proc.get('returns', '')}\n"
        return content

    def _format_database_mappings(self, mappings: list) -> str:
        """Format database mappings."""
        content = "\n### Entity-to-Table Mappings\n\n"
        content += "Mappings between Java entity classes and database tables.\n\n"

        for mapping in mappings:
            content += f"""#### {mapping.entity_class} → {mapping.table_name}

**Field Mappings:**
| Java Field | Java Type | Column Name | Column Type | Annotations |
|------------|-----------|-------------|-------------|-------------|
"""
            for fm in mapping.field_mappings:
                # Handle both dict and string cases
                if isinstance(fm, dict):
                    annotations = (
                        ", ".join(fm.get("annotations", [])) if fm.get("annotations") else "—"
                    )
                    content += f"| `{fm.get('java_field', '')}` | {fm.get('java_type', '')} | `{fm.get('column_name', '')}` | {fm.get('column_type', '')} | {annotations} |\n"
                else:
                    # Handle case where fm is a string or other type
                    content += f"| `{str(fm)}` | — | — | — | — |\n"

            if mapping.relationships:
                content += self._format_mapping_relationships(mapping.relationships)
            if mapping.queries:
                content += self._format_mapping_queries(mapping.queries)
            content += SECTION_SEPARATOR
        return content

    def _format_mapping_relationships(self, relationships: list) -> str:
        """Format relationships for mapping."""
        content = "\n**Relationships:**\n"
        for rel in relationships:
            if isinstance(rel, dict):
                content += f"- {rel.get('type', 'RELATED_TO')} `{rel.get('target_entity', '')}` (Table: `{rel.get('target_table', '')}`) via `{rel.get('join_column', '')}`\n"
            else:
                content += f"- {str(rel)}\n"
        return content

    def _format_mapping_queries(self, queries: list) -> str:
        """Format queries for mapping."""
        content = "\n**Common Queries:**\n"
        for query in queries[:5]:
            if isinstance(query, dict):
                content += f"\n*{query.get('name', 'query')}* ({query.get('type', 'SELECT')}):\n"
                content += f"```sql\n{query.get('sql_or_jpql', '')}\n```\n"
                if query.get("purpose"):
                    content += f"*Purpose: {query.get('purpose')}*\n"
            else:
                content += f"\n*Query:*\n```sql\n{str(query)}\n```\n"
        return content

    async def _generate_validation_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        order: int,
    ) -> PRDSection:
        """Generate the validation rules section."""
        content = """## Validation Rules

All validation rules extracted from the legacy code. Each rule includes
the exact condition and error message for implementation.

### Validation Rules by Entity

"""
        # Group by entity
        by_entity: dict[str, list] = {}
        for rule in requirements_analysis.validation_rules:
            entity = rule.entity or "General"
            if entity not in by_entity:
                by_entity[entity] = []
            by_entity[entity].append(rule)

        for entity, rules in by_entity.items():
            content += f"#### {entity}\n\n"
            content += "| ID | Field | Type | Condition | Error Message |\n"
            content += "|----| ------|------|-----------|---------------|\n"
            for rule in rules:
                condition = (
                    rule.condition[:40] + "..." if len(rule.condition) > 40 else rule.condition
                )
                msg = (
                    rule.error_message[:30] + "..."
                    if len(rule.error_message) > 30
                    else rule.error_message
                )
                content += f"| {rule.rule_id} | `{rule.field}` | {rule.rule_type} | `{condition}` | {msg} |\n"
            content += "\n"

        content += "### Detailed Validation Specifications\n"

        for rule in requirements_analysis.validation_rules:
            content += f"""
#### {rule.rule_id}: {rule.field}

**Entity:** {rule.entity}
**Type:** {rule.rule_type}
**When Applied:** {rule.when_applied}

**Condition:**
```
{rule.condition}
```

**Error Message:** {rule.error_message}

**Description:** {rule.description}

**Source Reference:** `{rule.source_location}`

---
"""

        return PRDSection(title=f"{order}. Validation Rules", content=content, order=order)

    async def _generate_integration_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        order: int,
    ) -> PRDSection:
        """Generate the integration requirements section."""
        content = """## External Integrations

All external system integrations required for this module.

### Integration Summary

| ID | System | Type | Direction | Purpose |
|----|--------|------|-----------|---------|
"""
        for integ in requirements_analysis.integration_requirements:
            content += f"| {integ.integration_id} | {integ.external_system} | {integ.integration_type} | {integ.direction} | {integ.purpose[:30]}... |\n"

        content += "\n### Detailed Integration Specifications\n"

        for integ in requirements_analysis.integration_requirements:
            content += f"""
#### {integ.integration_id}: {integ.name}

**External System:** {integ.external_system}
**Type:** {integ.integration_type}
**Direction:** {integ.direction}

**Purpose:** {integ.purpose}

**Connection Specification:**
```json
{self._format_json_schema(integ.specification)}
```

**Data Mapping:**
"""
            for mapping in integ.data_mapping:
                # Handle both dict and string cases
                if isinstance(mapping, dict):
                    content += f"- `{mapping.get('source_field', 'N/A')}` → `{mapping.get('target_field', 'N/A')}`"
                    if mapping.get("transformation"):
                        content += f" (transform: {mapping.get('transformation')})"
                else:
                    content += f"- {mapping}"
                content += "\n"

            if integ.error_handling:
                # Handle both dict and string cases
                if isinstance(integ.error_handling, dict):
                    content += f"""
**Error Handling:**
- Retry Policy: {integ.error_handling.get('retry_policy', 'N/A')}
- Fallback: {integ.error_handling.get('fallback', 'N/A')}
- Alerts: {integ.error_handling.get('alerts', 'N/A')}
"""
                else:
                    content += f"""
**Error Handling:**
{integ.error_handling}
"""

            if integ.source_files:
                content += f"\n**Source References:** {', '.join(['`' + f + '`' for f in integ.source_files])}\n"

            content += SECTION_SEPARATOR

        return PRDSection(title=f"{order}. External Integrations", content=content, order=order)

    async def _generate_nfr_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        order: int,
    ) -> PRDSection:
        """Generate the non-functional requirements section."""
        content = """## Non-Functional Requirements

"""
        for req in requirements_analysis.non_functional_requirements:
            content += f"""### {req.req_id}: {req.title}

**Category:** {req.category} | **Priority:** {req.priority}

**Description:** {req.description}

**Current Implementation:** {req.current_implementation}

**Metric:** {req.metric}
**Target Value:** {req.target_value}
**Measurement Method:** {req.measurement_method}

**Migration Consideration:** {req.migration_consideration}

---

"""

        return PRDSection(
            title=f"{order}. Non-Functional Requirements", content=content, order=order
        )

    async def _generate_business_rules_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        order: int,
    ) -> PRDSection:
        """Generate the business rules section."""
        content = f"""## Business Rules

### Extracted Business Rules
{chr(10).join(["- " + r for r in requirements_analysis.business_rules])}

### Assumptions
{chr(10).join(["- " + a for a in requirements_analysis.assumptions]) if requirements_analysis.assumptions else "No assumptions documented."}

### Out of Scope
{chr(10).join(["- " + o for o in requirements_analysis.out_of_scope]) if requirements_analysis.out_of_scope else "No items explicitly out of scope."}
"""

        return PRDSection(title=f"{order}. Business Rules", content=content, order=order)

    async def _generate_user_flow_section(
        self,
        context: AgentContext,
        user_flow_analysis: UserFlowResult,
        order: int,
    ) -> PRDSection:
        """Generate the user flow section."""
        content = f"""## User Flows

### Primary Actors
{chr(10).join(["- " + a for a in user_flow_analysis.primary_actors])}

### Entry Points
{chr(10).join(["- " + e for e in user_flow_analysis.entry_points])}

### Exit Points
{chr(10).join(["- " + e for e in user_flow_analysis.exit_points])}

### User Journey Map
{user_flow_analysis.user_journey_map}

### Detailed User Flows

"""
        for flow in user_flow_analysis.user_flows:
            content += f"""### {flow.flow_id}: {flow.name}

**Description:** {flow.description}

**Actor:** {flow.actor}

**Estimated Time:** {flow.estimated_time}

**Preconditions:**
{chr(10).join(["- " + p for p in flow.preconditions])}

**Steps:**
"""
            for step in flow.steps:
                content += f"""
**Step {step.step_number}: {step.action}**
- Screen: {step.screen}
- Input: {", ".join(step.input_data) if step.input_data else "None"}
- Expected Result: {step.expected_result}
"""
                if step.alternative_paths:
                    content += f"- Alternatives: {', '.join(step.alternative_paths)}\n"

            content += f"""
**Postconditions:**
{chr(10).join(["- " + p for p in flow.postconditions])}

**Success Criteria:** {flow.success_criteria}

---

"""

        # Add flow diagram
        content += f"""### Flow Diagram

```mermaid
{user_flow_analysis.flow_diagram_mermaid}
```

### Cross-Module Flows
{chr(10).join(["- " + f for f in user_flow_analysis.cross_module_flows])}
"""

        return PRDSection(title=f"{order}. User Flows", content=content, order=order)

    async def _generate_workflow_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult,
        order: int,
    ) -> PRDSection:
        """Generate the workflow specifications section."""
        content = """## Workflow Specifications

State machines and approval workflows in the module.

"""
        for wf in requirements_analysis.workflow_specs:
            content += f"""### {wf.workflow_id}: {wf.name}

**Entity:** {wf.entity}

**Description:** {wf.description}

**State Diagram:**
```mermaid
stateDiagram-v2
"""
            content += self._format_workflow_diagram(wf)
            content += "```\n\n"
            content += self._format_workflow_states(wf.states)
            content += self._format_workflow_transitions(wf.transitions)
            if wf.source_location:
                content += f"\n**Source Reference:** `{wf.source_location}`\n"

            content += SECTION_SEPARATOR

        return PRDSection(title=f"{order}. Workflow Specifications", content=content, order=order)

    def _format_workflow_diagram(self, wf) -> str:
        """Format workflow state diagram."""
        content = ""
        for state in wf.states:
            if isinstance(state, dict):
                content += f"    {state.get('id', 'state')}: {state.get('name', 'State')}\n"
            else:
                content += f"    {str(state)}: State\n"
        if wf.initial_state:
            content += f"    [*] --> {wf.initial_state}\n"
        for trans in wf.transitions:
            if isinstance(trans, dict):
                from_state = trans.get("from", "start")
                to_state = trans.get("to", "end")
                trigger = trans.get("trigger", "action")
            else:
                from_state = "start"
                to_state = "end"
                trigger = str(trans)
            content += f"    {from_state} --> {to_state}: {trigger}\n"
        for term in wf.terminal_states:
            content += f"    {term} --> [*]\n"
        return content

    def _format_workflow_states(self, states: list) -> str:
        """Format workflow states."""
        content = "**States:**\n"
        for state in states:
            if isinstance(state, dict):
                content += f"- **{state.get('id', 'state')}** ({state.get('name', '')}): {state.get('description', '')}\n"
            else:
                content += f"- **{str(state)}**\n"
        return content

    def _format_workflow_transitions(self, transitions: list) -> str:
        """Format workflow transitions."""
        content = "\n**Transitions:**\n"
        content += "| From | To | Trigger | Conditions | Actions |\n"
        content += "|------|-----|---------|------------|--------|\n"
        for trans in transitions:
            if isinstance(trans, dict):
                conditions = ", ".join(trans.get("guard_conditions", []))[:30] or "—"
                actions = ", ".join(trans.get("actions", []))[:30] or "—"
                content += f"| {trans.get('from', '')} | {trans.get('to', '')} | {trans.get('trigger', '')} | {conditions} | {actions} |\n"
            else:
                content += f"| — | — | {str(trans)} | — | — |\n"
        return content

    async def _generate_migration_section(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult | None,
        kb_contexts: dict[str, list[str]],
        order: int,
    ) -> PRDSection:
        """Generate the migration strategy section."""
        # Assess complexity
        complexity = self._assess_complexity(requirements_analysis)

        # Get technical details
        tech_details = ""
        if requirements_analysis:
            tech_details = f"""
- Functional Requirements: {len(requirements_analysis.functional_requirements)}
- API Endpoints: {len(requirements_analysis.api_specifications)}
- Data Entities: {len(requirements_analysis.data_requirements)}
- Business Logic Items: {len(requirements_analysis.business_logic)}
- Integrations: {len(requirements_analysis.integration_requirements)}
- Validation Rules: {len(requirements_analysis.validation_rules)}
- Workflows: {len(requirements_analysis.workflow_specs)}
"""

        kb_context = self.format_context_for_prompt(
            kb_contexts.get("existing_prd", []), max_contexts=3
        )

        prompt = PRDAggregatorPrompts.migration_strategy_section(
            context.form_name, complexity, f"{tech_details}\n\nEXISTING PRD:\n{kb_context}"
        )

        content = await self.invoke_llm(context, prompt)

        return PRDSection(title=f"{order}. Migration Strategy", content=content, order=order)

    async def _generate_executive_summary(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult | None,
        kb_contexts: dict[str, list[str]],
    ) -> str:
        """Generate the executive summary with metrics."""
        req_count = (
            len(requirements_analysis.functional_requirements) if requirements_analysis else 0
        )
        api_count = len(requirements_analysis.api_specifications) if requirements_analysis else 0
        entity_count = len(requirements_analysis.data_requirements) if requirements_analysis else 0
        integration_count = (
            len(requirements_analysis.integration_requirements) if requirements_analysis else 0
        )
        complexity = self._assess_complexity(requirements_analysis)

        # Include rich KB context for the executive summary
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("existing_prd", [])
            + kb_contexts.get("business_logic", [])
            + kb_contexts.get("source_tables", []),
            max_contexts=10,
        )

        prompt = PRDAggregatorPrompts.executive_summary(
            context.form_name,
            req_count,
            api_count,
            entity_count,
            integration_count,
            complexity,
            kb_context,
        )

        return await self.invoke_llm(context, prompt)

    def _assess_complexity(self, requirements_analysis: RequirementsGeneratorResult | None) -> str:
        """Assess migration complexity based on requirements."""
        if not requirements_analysis:
            return "MEDIUM"

        score = 0
        score += len(requirements_analysis.functional_requirements) * 2
        score += len(requirements_analysis.api_specifications) * 3
        score += len(requirements_analysis.data_requirements) * 2
        score += len(requirements_analysis.integration_requirements) * 5
        score += len(requirements_analysis.workflow_specs) * 4
        score += len(requirements_analysis.validation_rules)

        if score < 30:
            return "LOW"
        elif score < 80:
            return "MEDIUM"
        elif score < 150:
            return "HIGH"
        else:
            return "VERY HIGH"

    def _generate_appendices(
        self,
        screenshot_analysis: ScreenshotAnalysisResult | None,
        requirements_analysis: RequirementsGeneratorResult | None,
        user_flow_analysis: UserFlowResult | None,
    ) -> list[dict[str, str]]:
        """Generate appendix content with code references."""
        appendices = []

        # Appendix A: Code References
        if requirements_analysis and requirements_analysis.code_references:
            code_refs = "| Category | Source Files |\n|----------|-------------|\n"
            for category, files in requirements_analysis.code_references.items():
                code_refs += f"| {category} | {', '.join(['`' + f + '`' for f in files[:5]])} |\n"

            appendices.append({"title": "Appendix A: Source Code References", "content": code_refs})

        # Appendix B: Glossary
        appendices.append(
            {
                "title": "Appendix B: Glossary",
                "content": "Key terms and definitions used in this document.",
            }
        )

        # Appendix C: Change Log
        appendices.append(
            {
                "title": "Appendix C: Change Log",
                "content": "| Version | Date | Author | Changes |\n|---------|------|--------|---------|",
            }
        )

        return appendices

    def _generate_markdown(self, prd: PRDDocument) -> str:
        """Generate the complete markdown document."""
        md = f"""# {prd.title}

**Version:** {prd.version}
**Created:** {prd.created_date}
**Author:** {prd.author}
**PRD Type:** Migration Specification

---

## Executive Summary

{prd.executive_summary}

---

## Document Statistics

| Metric | Count |
|--------|-------|
"""
        if "statistics" in prd.metadata:
            stats = prd.metadata["statistics"]
            for key, value in stats.items():
                display_key = key.replace("_", " ").title()
                md += f"| {display_key} | {value} |\n"

        md += """
---

## Table of Contents

"""
        # Generate TOC
        for section in prd.sections:
            anchor = section.title.lower().replace(" ", "-").replace(".", "")
            md += f"- [{section.title}](#{anchor})\n"

        md += f"{SECTION_SEPARATOR}\n"

        # Add sections
        for section in prd.sections:
            md += f"# {section.title}\n\n{section.content}\n{SECTION_SEPARATOR}\n"

        # Add appendices
        md += "# Appendices\n\n"
        for appendix in prd.appendices:
            md += f"## {appendix['title']}\n\n{appendix['content']}\n\n"

        return md

    def _format_json_schema(self, schema: dict[str, Any]) -> str:
        """Format a dictionary as a readable JSON schema."""
        import json

        if not schema:
            return "{}"
        try:
            return json.dumps(schema, indent=2)
        except (TypeError, ValueError):
            return str(schema)
