"""
PRD Aggregator Agent for combining all agent outputs into a final PRD document.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from src.agents.atlassian_integration_agent import AtlassianIntegrationResult
from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.agents.requirements_generator_agent import RequirementsGeneratorResult
from src.agents.risk_analysis_agent import RiskAnalysisResult
from src.agents.screenshot_analysis_agent import ScreenshotAnalysisResult
from src.agents.user_flow_agent import UserFlowResult
from src.prompts.prd_aggregator import PRDAggregatorPrompts
from src.utils.logging_config import ExecutionTimer


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
    Agent for aggregating all analysis results into a comprehensive PRD document.
    Combines outputs from all specialized agents into a cohesive document.
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
        risk_analysis: RiskAnalysisResult | None = None,
        **kwargs: Any,
    ) -> AgentResult[PRDAggregatorResult]:
        """
        Aggregate all agent results into a PRD document.

        Args:
            context: Agent execution context
            screenshot_analysis: Results from screenshot analysis
            atlassian_analysis: Results from Atlassian integration
            requirements_analysis: Results from requirements generation
            user_flow_analysis: Results from user flow analysis
            risk_analysis: Results from risk analysis

        Returns:
            AgentResult with PRDAggregatorResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting PRD aggregation",
            form_name=context.form_name,
            has_screenshots=screenshot_analysis is not None,
            has_jira=atlassian_analysis is not None,
            has_requirements=requirements_analysis is not None,
        )

        try:
            # Generate all PRD sections
            sections = await self._build_all_sections(
                context,
                screenshot_analysis,
                atlassian_analysis,
                requirements_analysis,
                user_flow_analysis,
                risk_analysis,
            )

            # Generate executive summary and appendices
            executive_summary = await self._generate_executive_summary(
                context, requirements_analysis, risk_analysis
            )
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
                },
            )

            self.logger.info(
                "PRD generation complete",
                form_name=context.form_name,
                sections=len(sections),
                word_count=result.word_count,
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            return self.create_error_result(e, timer)

    async def _build_all_sections(
        self,
        context: AgentContext,
        screenshot_analysis: ScreenshotAnalysisResult | None,
        atlassian_analysis: AtlassianIntegrationResult | None,
        requirements_analysis: RequirementsGeneratorResult | None,
        user_flow_analysis: UserFlowResult | None,
        risk_analysis: RiskAnalysisResult | None,
    ) -> list[PRDSection]:
        """Build all PRD sections from analysis results."""
        sections: list[PRDSection] = []

        # Always include overview
        sections.append(await self._generate_overview_section(context, atlassian_analysis))

        # Conditional sections based on available analysis
        if screenshot_analysis:
            sections.append(await self._generate_ui_section(context, screenshot_analysis))

        if requirements_analysis:
            sections.append(
                await self._generate_functional_requirements_section(context, requirements_analysis)
            )
            sections.append(await self._generate_nfr_section(context, requirements_analysis))
            sections.append(await self._generate_data_model_section(context, requirements_analysis))
            sections.append(
                await self._generate_business_rules_section(context, requirements_analysis)
            )

        if user_flow_analysis:
            sections.append(await self._generate_user_flow_section(context, user_flow_analysis))

        if risk_analysis:
            sections.append(await self._generate_risk_section(context, risk_analysis))

        # Always include migration strategy
        sections.append(await self._generate_migration_section(context, risk_analysis))

        return sections

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
            title=f"Product Requirements Document: {context.form_name.upper()} Module Migration",
            version="1.0.0",
            created_date=datetime.now().isoformat(),
            author="PRD Agent",
            sections=sections,
            executive_summary=executive_summary,
            appendices=appendices,
            metadata={
                "generation_timestamp": datetime.now().isoformat(),
                "agent_version": "1.0.0",
                "sources": {
                    "screenshots": screenshot_analysis is not None,
                    "jira": atlassian_analysis is not None,
                    "code": requirements_analysis is not None,
                },
            },
        )

    async def _generate_overview_section(
        self, context: AgentContext, atlassian_analysis: AtlassianIntegrationResult | None
    ) -> PRDSection:
        """Generate the overview section."""
        jira_context = ""
        if atlassian_analysis:
            jira_context = f"""
Based on Jira analysis:
- Total issues: {atlassian_analysis.total_issues}
- Summary: {atlassian_analysis.summary[:500]}
"""

        prompt = f"""Write the Overview section for "{context.form_name}" PRD:

{jira_context}

Include:
1. Purpose and Scope
2. Background
3. Goals and Objectives
4. Target Audience
5. Document Conventions

Write in professional technical documentation style."""

        content = await self.invoke_llm(context, prompt)

        return PRDSection(title="1. Overview", content=content, order=1)

    async def _generate_ui_section(
        self, context: AgentContext, screenshot_analysis: ScreenshotAnalysisResult
    ) -> PRDSection:
        """Generate the user interface section."""
        screen_summary = "\n".join(
            [f"- {s.screen_name}: {s.purpose}" for s in screenshot_analysis.screen_analyses[:10]]
        )

        content = f"""## User Interface Overview

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

        return PRDSection(title="2. User Interface", content=content, order=2)

    async def _generate_functional_requirements_section(
        self, context: AgentContext, requirements_analysis: RequirementsGeneratorResult
    ) -> PRDSection:
        """Generate the functional requirements section."""
        content = f"""## Functional Requirements

### Requirements Summary
{requirements_analysis.summary}

### Detailed Requirements

"""
        for req in requirements_analysis.functional_requirements:
            content += f"""#### {req.req_id}: {req.title}
**Priority:** {req.priority} | **Category:** {req.category}

**Description:** {req.description}

**User Story:** {req.user_story}

**Acceptance Criteria:**
{chr(10).join(["- " + ac for ac in req.acceptance_criteria])}

**Dependencies:** {", ".join(req.dependencies) if req.dependencies else "None"}

---

"""

        return PRDSection(title="3. Functional Requirements", content=content, order=3)

    async def _generate_nfr_section(
        self, context: AgentContext, requirements_analysis: RequirementsGeneratorResult
    ) -> PRDSection:
        """Generate the non-functional requirements section."""
        content = """## Non-Functional Requirements

"""
        for req in requirements_analysis.non_functional_requirements:
            content += f"""### {req.req_id}: {req.category.title()}

**Description:** {req.description}

**Metric:** {req.metric}

**Target Value:** {req.target_value}

**Validation Method:** {req.validation_method}

---

"""

        return PRDSection(title="4. Non-Functional Requirements", content=content, order=4)

    async def _generate_data_model_section(
        self, context: AgentContext, requirements_analysis: RequirementsGeneratorResult
    ) -> PRDSection:
        """Generate the data model section."""
        content = """## Data Model

### Entity Overview

"""
        for entity in requirements_analysis.data_requirements:
            content += f"""### {entity.entity_name}

**Description:** {entity.description}

**Source Table:** {entity.source_table or "N/A"}

**Fields:**
| Field | Type | Required |
|-------|------|----------|
"""
            for field_item in entity.fields:
                content += f"| {field_item.get('name', '')} | {field_item.get('type', '')} | {field_item.get('required', '')} |\n"

            content += f"""
**Relationships:**
{chr(10).join(["- " + r for r in entity.relationships])}

**Constraints:**
{chr(10).join(["- " + c for c in entity.constraints])}

---

"""

        return PRDSection(title="5. Data Model", content=content, order=5)

    async def _generate_user_flow_section(
        self, context: AgentContext, user_flow_analysis: UserFlowResult
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

        return PRDSection(title="6. User Flows", content=content, order=6)

    async def _generate_business_rules_section(
        self, context: AgentContext, requirements_analysis: RequirementsGeneratorResult
    ) -> PRDSection:
        """Generate the business rules section."""
        content = f"""## Business Rules

### Business Rules
{chr(10).join(["- " + r for r in requirements_analysis.business_rules])}

### Validation Rules
{chr(10).join(["- " + r for r in requirements_analysis.validation_rules])}

### Assumptions
{chr(10).join(["- " + a for a in requirements_analysis.assumptions])}

### Out of Scope
{chr(10).join(["- " + o for o in requirements_analysis.out_of_scope])}
"""

        return PRDSection(title="7. Business Rules", content=content, order=7)

    async def _generate_risk_section(
        self, context: AgentContext, risk_analysis: RiskAnalysisResult
    ) -> PRDSection:
        """Generate the risk assessment section."""
        content = f"""## Risk Assessment

### Executive Summary
{risk_analysis.executive_summary}

### Risk Matrix

| Severity | Count |
|----------|-------|
| Critical | {risk_analysis.risk_matrix.critical_count} |
| High | {risk_analysis.risk_matrix.high_count} |
| Medium | {risk_analysis.risk_matrix.medium_count} |
| Low | {risk_analysis.risk_matrix.low_count} |

**Overall Risk Score:** {risk_analysis.risk_matrix.risk_score}/100

### Top Risks
{chr(10).join(["- " + r for r in risk_analysis.top_risks])}

### Detailed Risk Register

"""
        for risk in risk_analysis.risks:
            content += f"""### {risk.risk_id}: {risk.title}

**Category:** {risk.category} | **Severity:** {risk.severity} | **Likelihood:** {risk.likelihood}

**Description:** {risk.description}

**Impact:** {risk.impact}

**Affected Areas:** {", ".join(risk.affected_areas)}

**Mitigation Strategies:**
{chr(10).join(["- " + m for m in risk.mitigation_strategies])}

**Contingency Plan:** {risk.contingency_plan}

**Owner:** {risk.owner} | **Status:** {risk.status}

---

"""

        content += f"""
### Technical Debt Items
{chr(10).join(["- " + t for t in risk_analysis.technical_debt_items])}

### Critical Success Factors
{chr(10).join(["- " + s for s in risk_analysis.success_factors])}
"""

        return PRDSection(title="8. Risk Assessment", content=content, order=8)

    async def _generate_migration_section(
        self, context: AgentContext, risk_analysis: RiskAnalysisResult | None
    ) -> PRDSection:
        """Generate the migration strategy section."""
        complexity = risk_analysis.migration_complexity if risk_analysis else "medium"
        approach = (
            risk_analysis.recommended_approach
            if risk_analysis
            else "Phased migration approach recommended."
        )

        content = f"""## Migration Strategy

### Migration Complexity
**Assessed Complexity Level:** {complexity.upper()}

### Recommended Approach
{approach}

### Migration Phases

#### Phase 1: Preparation
- Environment setup
- Data migration planning
- Team training

#### Phase 2: Development
- Core functionality implementation
- Integration development
- Unit testing

#### Phase 3: Testing
- Integration testing
- User acceptance testing
- Performance testing

#### Phase 4: Deployment
- Staged rollout
- Parallel running (if applicable)
- Full cutover

### Rollback Strategy
Detailed rollback procedures to be defined during implementation planning.
"""

        return PRDSection(title="9. Migration Strategy", content=content, order=9)

    async def _generate_executive_summary(
        self,
        context: AgentContext,
        requirements_analysis: RequirementsGeneratorResult | None,
        risk_analysis: RiskAnalysisResult | None,
    ) -> str:
        """Generate the executive summary."""
        req_count = (
            len(requirements_analysis.functional_requirements) if requirements_analysis else 0
        )
        risk_level = risk_analysis.migration_complexity if risk_analysis else "medium"

        prompt = f"""Write an executive summary for the "{context.form_name}" PRD:

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

        return await self.invoke_llm(context, prompt)

    def _generate_appendices(
        self,
        screenshot_analysis: ScreenshotAnalysisResult | None,
        requirements_analysis: RequirementsGeneratorResult | None,
        user_flow_analysis: UserFlowResult | None,
    ) -> list[dict[str, str]]:
        """Generate appendix content."""
        appendices = []

        # Appendix A: Glossary
        appendices.append(
            {
                "title": "Appendix A: Glossary",
                "content": "Key terms and definitions used in this document.",
            }
        )

        # Appendix B: Reference Materials
        appendices.append(
            {
                "title": "Appendix B: Reference Materials",
                "content": "Source documents and references consulted during analysis.",
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

---

## Executive Summary

{prd.executive_summary}

---

## Table of Contents

"""
        # Generate TOC
        for section in prd.sections:
            md += f"- [{section.title}](#{section.title.lower().replace(' ', '-').replace('.', '')})\n"

        md += "\n---\n\n"

        # Add sections
        for section in prd.sections:
            md += f"# {section.title}\n\n{section.content}\n\n---\n\n"

        # Add appendices
        md += "# Appendices\n\n"
        for appendix in prd.appendices:
            md += f"## {appendix['title']}\n\n{appendix['content']}\n\n"

        return md
