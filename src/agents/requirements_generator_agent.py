"""
Requirements Generator Agent for synthesizing migration-ready requirements.

Analyzes code, Jira documentation, screenshots, and existing PRDs to generate
comprehensive functional and non-functional requirements with SPECIFIC business logic,
API specifications, and data models for legacy system migration.
"""

from dataclasses import dataclass, field
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.extractors.code_extractor import CodeFile
from src.prompts.requirements import RequirementsPrompts
from src.utils.logging_config import ExecutionTimer
from src.utils.serialization import extract_json_array


@dataclass
class APISpecification:
    """API endpoint specification for migration."""

    endpoint_name: str
    http_method: str
    path: str
    description: str
    request_spec: dict[str, Any] = field(default_factory=dict)
    response_spec: dict[str, Any] = field(default_factory=dict)
    business_logic: str = ""
    source_method: str = ""


@dataclass
class BusinessLogic:
    """Extracted business logic from source code."""

    logic_id: str
    name: str
    logic_type: str  # validation, calculation, workflow, transformation
    description: str
    trigger: str
    steps: list[str] = field(default_factory=list)
    inputs: list[dict[str, str]] = field(default_factory=list)
    outputs: list[dict[str, str]] = field(default_factory=list)
    conditions: list[dict[str, str]] = field(default_factory=list)
    source_location: str = ""


@dataclass
class FunctionalRequirement:
    """A functional requirement with full migration specification."""

    req_id: str
    title: str
    description: str
    priority: str  # P0, P1, P2, P3
    category: str  # CRUD, validation, workflow, integration, reporting, calculation
    business_logic: str  # Detailed step-by-step logic
    source_methods: list[str] = field(default_factory=list)
    api_specification: dict[str, Any] = field(default_factory=dict)
    database_operations: list[dict[str, Any]] = field(default_factory=list)
    validation_rules: list[str] = field(default_factory=list)
    calculations: list[str] = field(default_factory=list)
    user_story: str = ""
    acceptance_criteria: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    source_files: list[str] = field(default_factory=list)


@dataclass
class NonFunctionalRequirement:
    """A non-functional requirement with migration considerations."""

    req_id: str
    category: str  # performance, security, usability, reliability
    title: str
    description: str
    current_implementation: str
    metric: str
    target_value: str
    measurement_method: str
    migration_consideration: str
    priority: str


@dataclass
class DataRequirement:
    """Data model and storage requirements with full schema."""

    entity_name: str
    description: str
    source_table: str
    source_class: str
    fields: list[dict[str, Any]] = field(default_factory=list)
    primary_key: list[str] = field(default_factory=list)
    foreign_keys: list[dict[str, Any]] = field(default_factory=list)
    indexes: list[dict[str, Any]] = field(default_factory=list)
    relationships: list[dict[str, Any]] = field(default_factory=list)
    business_rules: list[str] = field(default_factory=list)
    sample_queries: list[dict[str, str]] = field(default_factory=list)


@dataclass
class IntegrationRequirement:
    """External system integration specification."""

    integration_id: str
    name: str
    integration_type: str  # REST_API, SOAP, DATABASE, MESSAGE_QUEUE
    direction: str  # INBOUND, OUTBOUND, BIDIRECTIONAL
    external_system: str
    purpose: str
    specification: dict[str, Any] = field(default_factory=dict)
    data_mapping: list[dict[str, str]] = field(default_factory=list)
    error_handling: dict[str, Any] = field(default_factory=dict)
    source_files: list[str] = field(default_factory=list)


@dataclass
class ValidationRule:
    """Validation rule specification."""

    rule_id: str
    field: str
    entity: str
    rule_type: str  # required, format, range, business, cross-field
    condition: str
    error_message: str
    description: str
    when_applied: str
    source_location: str


@dataclass
class WorkflowSpec:
    """Workflow/state machine specification."""

    workflow_id: str
    name: str
    description: str
    entity: str
    states: list[dict[str, str]] = field(default_factory=list)
    transitions: list[dict[str, Any]] = field(default_factory=list)
    initial_state: str = ""
    terminal_states: list[str] = field(default_factory=list)
    source_location: str = ""


@dataclass
class SourceTable:
    """Database source table specification."""

    table_name: str
    description: str
    table_type: str  # primary, supporting, lookup, audit
    columns: list[dict[str, Any]] = field(default_factory=list)
    primary_key: list[str] = field(default_factory=list)
    foreign_keys: list[dict[str, Any]] = field(default_factory=list)
    indexes: list[dict[str, Any]] = field(default_factory=list)
    stored_procedures: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class DatabaseMapping:
    """Entity-to-table mapping specification."""

    entity_class: str
    table_name: str
    field_mappings: list[dict[str, Any]] = field(default_factory=list)
    relationships: list[dict[str, Any]] = field(default_factory=list)
    queries: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class RequirementsGeneratorResult:
    """Complete migration-ready requirements specification."""

    form_name: str
    functional_requirements: list[FunctionalRequirement]
    non_functional_requirements: list[NonFunctionalRequirement]
    data_requirements: list[DataRequirement]
    api_specifications: list[APISpecification]
    business_logic: list[BusinessLogic]
    integration_requirements: list[IntegrationRequirement]
    validation_rules: list[ValidationRule]
    workflow_specs: list[WorkflowSpec]
    source_tables: list[SourceTable]  # Database source tables from PRD docs
    database_mappings: list[DatabaseMapping]  # Entity-to-table mappings
    business_rules: list[str]
    assumptions: list[str]
    out_of_scope: list[str]
    summary: str
    code_references: dict[str, list[str]]  # category -> list of source files


class RequirementsGeneratorAgent(BaseAgent[RequirementsGeneratorResult]):
    """
    Agent for generating comprehensive, migration-ready requirements from
    code analysis, screenshots, Jira documentation, and existing PRDs.
    """

    # Constants for common messages
    NO_CODE_AVAILABLE = "No code available."
    NO_CODE_FOUND = "No code files available for analysis."

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
        Generate migration-ready requirements from multiple input sources.

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
            "Starting migration-focused requirements generation",
            form_name=context.form_name,
            code_files_count=len(code_files) if code_files else 0,
            has_jira_context=jira_context is not None,
        )

        try:
            # Retrieve comprehensive context from knowledge base
            kb_contexts = self._retrieve_comprehensive_context(context.form_name)

            # Extract business logic from code
            business_logic = await self._extract_business_logic(context, code_files, kb_contexts)

            # Generate API specifications
            api_specs = await self._extract_api_specifications(context, code_files, kb_contexts)

            # Generate functional requirements with specific logic
            functional_reqs = await self._generate_functional_requirements(
                context, code_files, kb_contexts, business_logic, api_specs
            )

            # Generate comprehensive data requirements
            data_reqs = await self._generate_data_requirements(context, code_files, kb_contexts)

            # Extract validation rules
            validation_rules = await self._extract_validation_rules(
                context, code_files, kb_contexts
            )

            # Extract workflow specifications
            workflow_specs = await self._extract_workflows(context, code_files, kb_contexts)

            # Extract integration requirements
            integration_reqs = await self._extract_integration_requirements(
                context, code_files, kb_contexts
            )

            # Extract source tables from existing PRD documentation
            source_tables = await self._extract_source_tables(context, kb_contexts)

            # Extract database mappings from code
            database_mappings = await self._extract_database_mappings(
                context, code_files, kb_contexts
            )

            # Generate non-functional requirements
            non_functional_reqs = await self._generate_non_functional_requirements(
                context, code_files, kb_contexts
            )

            # Extract business rules
            business_rules = await self._extract_business_rules(context, kb_contexts)

            # Identify scope boundaries
            assumptions, out_of_scope = await self._identify_assumptions(context, functional_reqs)

            # Generate comprehensive summary
            summary = await self._generate_summary(
                context, functional_reqs, non_functional_reqs, data_reqs, api_specs
            )

            # Compile code references
            code_references = self._compile_code_references(code_files)

            result = RequirementsGeneratorResult(
                form_name=context.form_name,
                functional_requirements=functional_reqs,
                non_functional_requirements=non_functional_reqs,
                data_requirements=data_reqs,
                api_specifications=api_specs,
                business_logic=business_logic,
                integration_requirements=integration_reqs,
                validation_rules=validation_rules,
                workflow_specs=workflow_specs,
                source_tables=source_tables,
                database_mappings=database_mappings,
                business_rules=business_rules,
                assumptions=assumptions,
                out_of_scope=out_of_scope,
                summary=summary,
                code_references=code_references,
            )

            self.logger.info(
                "Migration-focused requirements generation complete",
                form_name=context.form_name,
                functional_count=len(functional_reqs),
                api_count=len(api_specs),
                business_logic_count=len(business_logic),
                data_entities=len(data_reqs),
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            return self.create_error_result(e, timer)

    def _retrieve_comprehensive_context(self, form_name: str) -> dict[str, list[str]]:
        """Retrieve multiple types of context from the knowledge base."""
        contexts = {}

        # Query for different aspects of the system
        queries = {
            "business_logic": "business logic validation rules calculations workflow",
            "api_endpoints": "API endpoint service controller HTTP request response",
            "database": "database table column SQL query insert update select",
            "integration": "integration external system API client service call",
            "validation": "validation validate required field error message",
            "workflow": "workflow state transition approval process status",
            "existing_prd": "PRD requirements specification description functionality",
            "source_tables": "source table schema column primary key foreign key constraint data type",
            "database_mapping": "entity mapping field column annotation relationship join query",
        }

        for key, query in queries.items():
            try:
                results = self.retrieve_context(form_name, query, limit=8)
                contexts[key] = results
                self.logger.debug(f"Retrieved {len(results)} contexts for {key}")
            except Exception as e:
                self.logger.warning(f"Failed to retrieve context for {key}: {e}")
                contexts[key] = []

        return contexts

    async def _extract_business_logic(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[BusinessLogic]:
        """Extract detailed business logic from source code."""
        # Get relevant code snippets
        logic_code = self._extract_logic_code(code_files)
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("existing_prd", []),
            max_contexts=5,
        )

        prompt = RequirementsPrompts.business_logic_extraction(
            context.form_name, f"{logic_code}\n\nKNOWLEDGE BASE:\n{kb_context}"
        )

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            BusinessLogic(
                logic_id=r.get("logic_id", f"BL-{i:03d}"),
                name=r.get("name", ""),
                logic_type=r.get("type", "general"),
                description=r.get("description", ""),
                trigger=r.get("trigger", ""),
                steps=r.get("steps", []),
                inputs=r.get("inputs", []),
                outputs=r.get("outputs", []),
                conditions=r.get("conditions", []),
                source_location=r.get("source_location", ""),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _extract_api_specifications(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[APISpecification]:
        """Extract API specifications from service/controller code."""
        service_code = self._get_service_code(code_files)
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("api_endpoints", []), max_contexts=5
        )

        prompt = RequirementsPrompts.api_specification(
            context.form_name, f"{service_code}\n\nKNOWLEDGE BASE:\n{kb_context}"
        )

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            APISpecification(
                endpoint_name=r.get("endpoint_name", f"endpoint_{i}"),
                http_method=r.get("http_method", "GET"),
                path=r.get("path", ""),
                description=r.get("description", ""),
                request_spec=r.get("request", {}),
                response_spec=r.get("response", {}),
                business_logic=r.get("business_logic", ""),
                source_method=r.get("source_method", ""),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _generate_functional_requirements(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
        business_logic: list[BusinessLogic],
        api_specs: list[APISpecification],
    ) -> list[FunctionalRequirement]:
        """Generate functional requirements with specific business logic."""
        code_summary = self._build_comprehensive_code_summary(code_files, limit=20)

        # Include business logic and API specs in context
        logic_summary = "\n".join(f"- {bl.name}: {bl.description}" for bl in business_logic[:10])
        api_summary = "\n".join(
            f"- {api.http_method} {api.path}: {api.description}" for api in api_specs[:10]
        )

        context_summary = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("existing_prd", []),
            max_contexts=8,
        )

        prompt = RequirementsPrompts.functional_requirements(
            context.form_name,
            f"{code_summary}\n\nBUSINESS LOGIC:\n{logic_summary}\n\nAPI ENDPOINTS:\n{api_summary}",
            context_summary,
        )

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            FunctionalRequirement(
                req_id=r.get("req_id", f"FR-{i:03d}"),
                title=r.get("title", ""),
                description=r.get("description", ""),
                priority=r.get("priority", "P2"),
                category=r.get("category", "CRUD"),
                business_logic=r.get("business_logic", ""),
                source_methods=r.get("source_methods", []),
                api_specification=r.get("api_specification", {}),
                database_operations=r.get("database_operations", []),
                validation_rules=r.get("validation_rules", []),
                calculations=r.get("calculations", []),
                user_story=r.get("user_story", ""),
                acceptance_criteria=r.get("acceptance_criteria", []),
                dependencies=r.get("dependencies", []),
                source_files=r.get("source_files", []),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _generate_data_requirements(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[DataRequirement]:
        """Generate comprehensive data model requirements."""
        model_files = self._get_model_files(code_files)
        model_summary = self._build_model_summary(model_files)
        db_context = self.format_context_for_prompt(kb_contexts.get("database", []), max_contexts=5)

        prompt = RequirementsPrompts.data_requirements(context.form_name, model_summary, db_context)

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            DataRequirement(
                entity_name=r.get("entity_name", "Unknown"),
                description=r.get("description", ""),
                source_table=r.get("source_table", ""),
                source_class=r.get("source_class", ""),
                fields=r.get("fields", []),
                primary_key=r.get("primary_key", []),
                foreign_keys=r.get("foreign_keys", []),
                indexes=r.get("indexes", []),
                relationships=r.get("relationships", []),
                business_rules=r.get("business_rules", []),
                sample_queries=r.get("sample_queries", []),
            )
            for r in data
        ]

    async def _extract_validation_rules(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[ValidationRule]:
        """Extract precise validation rules from code."""
        validation_code = self._extract_validation_code(code_files)
        context_text = self.format_context_for_prompt(
            kb_contexts.get("validation", []), max_contexts=5
        )

        prompt = RequirementsPrompts.validation_rules(
            context.form_name, validation_code, context_text
        )

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            ValidationRule(
                rule_id=r.get("rule_id", f"VR-{i:03d}"),
                field=r.get("field", ""),
                entity=r.get("entity", ""),
                rule_type=r.get("type", "required"),
                condition=r.get("condition", ""),
                error_message=r.get("error_message", ""),
                description=r.get("description", ""),
                when_applied=r.get("when_applied", ""),
                source_location=r.get("source_location", ""),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _extract_workflows(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[WorkflowSpec]:
        """Extract workflow/state machine specifications."""
        workflow_code = self._extract_workflow_code(code_files)
        kb_context = self.format_context_for_prompt(kb_contexts.get("workflow", []), max_contexts=5)

        prompt = RequirementsPrompts.workflow_extraction(
            context.form_name, f"{workflow_code}\n\nKNOWLEDGE BASE:\n{kb_context}"
        )

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            WorkflowSpec(
                workflow_id=r.get("workflow_id", f"WF-{i:03d}"),
                name=r.get("name", ""),
                description=r.get("description", ""),
                entity=r.get("entity", ""),
                states=r.get("states", []),
                transitions=r.get("transitions", []),
                initial_state=r.get("initial_state", ""),
                terminal_states=r.get("terminal_states", []),
                source_location=r.get("source_location", ""),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _extract_integration_requirements(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[IntegrationRequirement]:
        """Extract integration specifications from code."""
        integration_code = self._get_integration_code(code_files)
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("integration", []), max_contexts=5
        )

        prompt = RequirementsPrompts.integration_requirements(
            context.form_name, integration_code, kb_context
        )

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            IntegrationRequirement(
                integration_id=r.get("integration_id", f"INT-{i:03d}"),
                name=r.get("name", ""),
                integration_type=r.get("type", "REST_API"),
                direction=r.get("direction", "OUTBOUND"),
                external_system=r.get("external_system", ""),
                purpose=r.get("purpose", ""),
                specification=r.get("specification", {}),
                data_mapping=r.get("data_mapping", []),
                error_handling=r.get("error_handling", {}),
                source_files=r.get("source_files", []),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _extract_source_tables(
        self,
        context: AgentContext,
        kb_contexts: dict[str, list[str]],
    ) -> list[SourceTable]:
        """Extract source table definitions from knowledge base."""
        # Combine source table context from multiple queries
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("source_tables", [])
            + kb_contexts.get("database", [])
            + kb_contexts.get("existing_prd", []),
            max_contexts=10,
        )

        prompt = RequirementsPrompts.source_tables_extraction(context.form_name, kb_context)

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            SourceTable(
                table_name=r.get("table_name", ""),
                description=r.get("description", ""),
                table_type=r.get("table_type", "primary"),
                columns=r.get("columns", []),
                primary_key=r.get("primary_key", []),
                foreign_keys=r.get("foreign_keys", []),
                indexes=r.get("indexes", []),
                stored_procedures=r.get("stored_procedures", []),
            )
            for r in data
        ]

    async def _extract_database_mappings(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[DatabaseMapping]:
        """Extract entity-to-table mappings from code."""
        model_code = self._get_model_code(code_files)
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("database_mapping", []) + kb_contexts.get("database", []),
            max_contexts=8,
        )

        prompt = RequirementsPrompts.database_mappings(context.form_name, model_code, kb_context)

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            DatabaseMapping(
                entity_class=r.get("entity_class", ""),
                table_name=r.get("table_name", ""),
                field_mappings=r.get("field_mappings", []),
                relationships=r.get("relationships", []),
                queries=r.get("queries", []),
            )
            for r in data
        ]

    def _get_model_code(self, code_files: list[CodeFile] | None) -> str:
        """Get model/entity layer code for database mapping extraction."""
        if not code_files:
            return self.NO_CODE_AVAILABLE

        model_files = [
            cf
            for cf in code_files
            if cf.file_type in ["model", "entity"]
            or any(kw in cf.path.lower() for kw in ["model", "entity", "dto", "domain"])
        ]

        if not model_files:
            return "No model code found."

        return "\n\n".join(f"// File: {cf.path}\n{cf.content[:2000]}" for cf in model_files[:5])

    async def _generate_non_functional_requirements(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[NonFunctionalRequirement]:
        """Generate specific non-functional requirements."""
        code_context = self._analyze_nfr_patterns(code_files)
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("existing_prd", []), max_contexts=3
        )

        prompt = RequirementsPrompts.non_functional_requirements(
            context.form_name, f"{code_context}\n\nEXISTING PRD:\n{kb_context}"
        )

        data = extract_json_array(await self.invoke_llm(context, prompt))

        return [
            NonFunctionalRequirement(
                req_id=r.get("req_id", f"NFR-{i:03d}"),
                category=r.get("category", "performance"),
                title=r.get("title", ""),
                description=r.get("description", ""),
                current_implementation=r.get("current_implementation", ""),
                metric=r.get("metric", ""),
                target_value=r.get("target_value", ""),
                measurement_method=r.get("measurement_method", ""),
                migration_consideration=r.get("migration_consideration", ""),
                priority=r.get("priority", "Medium"),
            )
            for i, r in enumerate(data, 1)
        ]

    async def _extract_business_rules(
        self, context: AgentContext, kb_contexts: dict[str, list[str]]
    ) -> list[str]:
        """Extract business rules from knowledge base context."""
        context_text = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("existing_prd", []),
            max_contexts=8,
        )

        prompt = f"""From the following knowledge base context for "{context.form_name}", extract ALL business rules.

{context_text}

List each business rule in the format:
BR-XXX: [Detailed rule description with specific conditions and actions]

Focus on:
- Conditional logic (if X then Y)
- Calculation formulas
- Access control rules
- State transition rules
- Data integrity rules
- Workflow triggers

Be SPECIFIC - include actual values, field names, and conditions from the source."""

        return await self.invoke_llm_for_list(context, prompt, prefix="BR-")

    async def _identify_assumptions(
        self, context: AgentContext, functional_reqs: list[FunctionalRequirement]
    ) -> tuple[list[str], list[str]]:
        """Identify assumptions and out-of-scope items."""
        req_summary = "\n".join(
            f"- {r.req_id}: {r.title} ({r.category})" for r in functional_reqs[:15]
        )

        prompt = f"""Based on these requirements for "{context.form_name}":

{req_summary}

Identify:

ASSUMPTIONS:
- Technical assumptions about the legacy system
- Data assumptions
- User behavior assumptions
- Integration assumptions

OUT OF SCOPE:
- Features explicitly not included in migration
- Future enhancements
- External dependencies not addressed

Format as two sections: ASSUMPTIONS and OUT OF SCOPE.
Be specific to this module, not generic."""

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
                if item and current_section == "assumptions":
                    assumptions.append(item)
                elif item and current_section == "out_of_scope":
                    out_of_scope.append(item)

        return assumptions, out_of_scope

    async def _generate_summary(
        self,
        context: AgentContext,
        functional_reqs: list[FunctionalRequirement],
        non_functional_reqs: list[NonFunctionalRequirement],
        data_reqs: list[DataRequirement],
        api_specs: list[APISpecification],
    ) -> str:
        """Generate comprehensive requirements summary."""
        categories = ", ".join({r.category for r in functional_reqs}) or "N/A"
        high_priority = [r.title for r in functional_reqs if r.priority == "P0"][:5]

        prompt = RequirementsPrompts.summary(
            context.form_name,
            categories,
            ", ".join(high_priority) or "None identified",
            len(functional_reqs),
            len(non_functional_reqs),
            len(data_reqs),
        )

        return await self.invoke_llm(context, prompt)

    # ========== Code Analysis Helper Methods ==========

    def _build_comprehensive_code_summary(
        self, code_files: list[CodeFile] | None, limit: int = 20
    ) -> str:
        """Build a comprehensive summary of code files including key methods."""
        if not code_files:
            return "No code files available for analysis."

        parts = []
        for cf in code_files[:limit]:
            part = f"\n### File: {cf.path}\n"
            part += f"- Language: {cf.language}, Type: {cf.file_type}\n"
            if cf.classes:
                part += f"- Classes: {', '.join(cf.classes)}\n"
            if cf.methods:
                part += f"- Methods: {', '.join(cf.methods[:10])}\n"
            if cf.content and len(cf.content) < 2000:
                part += f"- Code snippet:\n```{cf.language}\n{cf.content[:1500]}\n```\n"
            parts.append(part)

        return "\n".join(parts)

    def _extract_logic_code(self, code_files: list[CodeFile] | None) -> str:
        """Extract code snippets containing business logic."""
        if not code_files:
            return "No code available."

        logic_keywords = ["if ", "else", "switch", "case", "calculate", "validate", "process"]
        snippets = []

        for cf in code_files:
            if cf.content and any(kw in cf.content.lower() for kw in logic_keywords):
                snippets.append(f"// File: {cf.path}\n{cf.content[:1500]}")

        return "\n\n".join(snippets[:5]) if snippets else "No logic code found."

    def _get_service_code(self, code_files: list[CodeFile] | None) -> str:
        """Get service/controller layer code."""
        if not code_files:
            return "No code available."

        service_files = [
            cf
            for cf in code_files
            if cf.file_type in ["service", "controller", "adapter"]
            or any(kw in cf.path.lower() for kw in ["service", "controller", "api"])
        ]

        if not service_files:
            return "No service code found."

        return "\n\n".join(f"// File: {cf.path}\n{cf.content[:2000]}" for cf in service_files[:5])

    def _get_model_files(self, code_files: list[CodeFile] | None) -> list[CodeFile]:
        """Extract model/entity files from code files."""
        if not code_files:
            return []

        model_files = [
            cf
            for cf in code_files
            if cf.file_type in ["model", "entity"]
            or any(kw in cf.path.lower() for kw in ["model", "entity", "dto", "domain"])
        ]

        if not model_files:
            model_files = [cf for cf in code_files if cf.language == "sql"][:5]

        return model_files

    def _build_model_summary(self, model_files: list[CodeFile]) -> str:
        """Build detailed summary of model files."""
        if not model_files:
            return "No model files found."

        parts = []
        for cf in model_files[:10]:
            part = f"### {cf.path}\n"
            if cf.classes:
                part += f"Classes: {', '.join(cf.classes)}\n"
            if cf.content:
                part += f"```{cf.language}\n{cf.content[:1500]}\n```\n"
            parts.append(part)

        return "\n".join(parts)

    def _extract_validation_code(self, code_files: list[CodeFile] | None) -> str:
        """Extract code snippets containing validation logic."""
        if not code_files:
            return "No code available."

        keywords = ["validate", "validation", "required", "pattern", "check", "error"]
        snippets = []

        for cf in code_files:
            if cf.content and any(kw in cf.content.lower() for kw in keywords):
                snippets.append(f"// File: {cf.path}\n{cf.content[:1500]}")

        return "\n\n".join(snippets[:5]) if snippets else "No validation code found."

    def _extract_workflow_code(self, code_files: list[CodeFile] | None) -> str:
        """Extract workflow/state machine code."""
        if not code_files:
            return "No code available."

        keywords = ["state", "status", "workflow", "transition", "approve", "reject", "process"]
        snippets = []

        for cf in code_files:
            if cf.content and any(kw in cf.content.lower() for kw in keywords):
                snippets.append(f"// File: {cf.path}\n{cf.content[:1500]}")

        return "\n\n".join(snippets[:5]) if snippets else "No workflow code found."

    def _get_integration_code(self, code_files: list[CodeFile] | None) -> str:
        """Get integration-related code."""
        if not code_files:
            return "No code available."

        keywords = ["client", "api", "integration", "http", "rest", "soap", "external"]
        integration_files = [
            cf
            for cf in code_files
            if cf.file_type in ["adapter", "service"]
            or any(kw in cf.path.lower() for kw in keywords)
        ]

        if not integration_files:
            return "No integration code found."

        return "\n\n".join(
            f"// File: {cf.path}\n{cf.content[:1500]}" for cf in integration_files[:5]
        )

    def _analyze_nfr_patterns(self, code_files: list[CodeFile] | None) -> str:
        """Analyze code for NFR-related patterns."""
        if not code_files:
            return "No code available for NFR analysis."

        patterns = {
            "caching": ["cache", "cached", "redis", "memcache"],
            "security": ["auth", "token", "encrypt", "permission", "role"],
            "logging": ["log", "logger", "audit"],
            "error_handling": ["try", "catch", "exception", "error"],
            "performance": ["async", "parallel", "batch", "optimize"],
        }

        findings = []
        for category, keywords in patterns.items():
            matches = []
            for cf in code_files:
                if cf.content and any(kw in cf.content.lower() for kw in keywords):
                    matches.append(cf.path)
            if matches:
                findings.append(f"{category}: Found in {', '.join(matches[:3])}")

        return "\n".join(findings) if findings else "No specific NFR patterns detected."

    def _compile_code_references(self, code_files: list[CodeFile] | None) -> dict[str, list[str]]:
        """Compile code references by category."""
        if not code_files:
            return {}

        references: dict[str, list[str]] = {}
        for cf in code_files:
            category = cf.file_type
            if category not in references:
                references[category] = []
            references[category].append(cf.path)

        return references
