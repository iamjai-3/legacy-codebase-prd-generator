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
from src.utils.sql_parser import (
    SQLDDLParser,
    extract_table_references_from_java,
    parse_sql_files,
)
from src.utils.business_logic_extractor import extract_business_logic_summary


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
    assumptions: list[str] = field(default_factory=list)
    out_of_scope: list[str] = field(default_factory=list)
    summary: str = ""
    code_references: dict[str, list[str]] = field(default_factory=dict)  # category -> list of source files
    detailed_business_rules: list[dict[str, Any]] = field(default_factory=list)  # Detailed BRs with conditions


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

            # Extract source tables from SQL files AND existing PRD documentation
            source_tables = await self._extract_source_tables(context, kb_contexts, code_files)

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
            
            # Extract detailed business rules with conditions
            detailed_business_rules = await self._extract_detailed_business_rules(
                context, code_files, kb_contexts
            )

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
                detailed_business_rules=detailed_business_rules,
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
        """Retrieve multiple types of context from the knowledge base.

        Uses targeted queries for legacy Java Swing/COBOL applications.
        Enhanced with specific queries for DTOs, validation functions, and fleet operations.
        """
        contexts = {}

        # Targeted queries for legacy Java desktop applications
        queries = {
            # Code-specific queries
            "business_logic": f"{form_name} class method if else switch save action business logic",
            "api_endpoints": f"{form_name} service method public void return parameter",
            "database": "CREATE TABLE FLEET CHAPTER column VARCHAR NUMBER CHAR sql ddl",
            "integration": f"{form_name} cobol paras send csBlock Oracle GROracleMaster",
            "validation": f"{form_name} validate check required enabled setEnabled error",
            "workflow": f"{form_name} state status save cancel reset action button click",
            # Documentation queries
            "existing_prd": f"{form_name} SourceTables Description Prompt Requirements",
            "source_tables": "CHAPTER_ALERT_RATES FLEET_CHAPTER CHAPTERS FLEET column schema",
            "database_mapping": f"{form_name} table column field setData getData combo dropdown",
            # UI-specific queries
            "ui_components": f"{form_name} JPanel JButton JTable combo dropdown form field",
            # NEW: Enhanced queries for complete extraction
            "dto_models": f"{form_name} SubchaptersDTO ChapterDTO class fields properties getters setters",
            "validation_functions": f"{form_name} doesChapterRecordExist doesSubChapterRecordExist validation check exists",
            "configuration_checks": f"{form_name} usingSubChapters usingRepDefs configuration check flag",
            "fleet_operations": f"{form_name} fleet parameter chapter subchapter fleet-specific",
            "alert_rate_management": f"{form_name} alertLimit alertLimitLandings alertLimitDays removalAlertRate",
            "field_mappings": f"{form_name} field code mapping WCHAPT W2CHSB WFLEET setData getData",
        }

        for key, query in queries.items():
            try:
                # Use metadata filtering for specific document types
                doc_type_filter = None
                chunk_type_filter = None
                if key in ["dto_models", "validation_functions", "configuration_checks"]:
                    doc_type_filter = "code"
                    chunk_type_filter = "class_definition"
                elif key in ["business_logic", "fleet_operations", "alert_rate_management"]:
                    doc_type_filter = "code"
                    chunk_type_filter = "business_logic"
                
                # Increase limit for complex modules (10-15 instead of 5)
                limit = 15 if key in ["dto_models", "source_tables", "database_mapping", "business_logic"] else 10
                
                results = self.retrieve_context(
                    form_name, 
                    query, 
                    limit=limit,
                    doc_type=doc_type_filter,
                    chunk_type=chunk_type_filter
                )
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
        """Extract detailed business logic from source code.
        
        Uses a combination of:
        1. Structured pattern extraction (validation rules, field mappings, etc.)
        2. LLM-based analysis for complex business logic
        """
        # Get relevant code snippets
        logic_code = self._extract_logic_code(code_files)
        
        # ENHANCEMENT: Add structured business logic extraction
        structured_logic = ""
        if code_files:
            # Prioritize main form files
            main_form_files = [cf for cf in code_files 
                              if any(p in cf.path.lower() for p in ["options/le", "cschapter", "support.java"])]
            
            for cf in main_form_files[:5]:
                extracted = extract_business_logic_summary(cf.content, cf.path)
                if extracted and "No business logic" not in extracted:
                    structured_logic += f"\n\n### Extracted from {cf.path}\n{extracted}"
            
            if structured_logic:
                self.logger.info(
                    f"Extracted structured business logic from {len(main_form_files)} main files",
                    form_name=context.form_name,
                )
        
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("existing_prd", []),
            max_contexts=5,
        )

        # Combine all sources for LLM analysis
        combined_context = f"{logic_code}\n\n## STRUCTURED EXTRACTION:{structured_logic}\n\nKNOWLEDGE BASE:\n{kb_context}"
        
        prompt = RequirementsPrompts.business_logic_extraction(
            context.form_name, combined_context
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
        """Generate comprehensive data model requirements with complete field extraction."""
        model_files = self._get_model_files(code_files)
        model_summary = self._build_model_summary(model_files)
        db_context = self.format_context_for_prompt(kb_contexts.get("database", []), max_contexts=8)
        
        # Extract DTO code for complete field extraction
        dto_code = self._extract_dto_code(model_files)
        
        # Get normalized schema from knowledge base
        normalized_schema_context = self.format_context_for_prompt(
            kb_contexts.get("source_tables", []) + kb_contexts.get("database", []),
            max_contexts=10
        )
        
        # Try to find normalized schema SQL
        normalized_schema = self._extract_normalized_schema(normalized_schema_context)
        
        # Use enhanced prompt if we have DTO code and normalized schema
        if dto_code and normalized_schema:
            prompt = RequirementsPrompts.data_requirements_complete(
                context.form_name, dto_code, normalized_schema, model_summary
            )
        else:
            # Fallback to standard prompt
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
    
    def _extract_dto_code(self, model_files: list[CodeFile]) -> str:
        """Extract DTO class code for complete field extraction."""
        if not model_files:
            return ""
        
        dto_files = [cf for cf in model_files if "DTO" in cf.path or "dto" in cf.path.lower()]
        
        if not dto_files:
            return ""
        
        # Combine DTO file contents
        dto_code_parts = []
        for dto_file in dto_files[:5]:  # Limit to 5 DTO files
            dto_code_parts.append(f"// File: {dto_file.path}\n{dto_file.content[:8000]}")
        
        return "\n\n".join(dto_code_parts)
    
    def _extract_normalized_schema(self, context: str) -> str:
        """Extract normalized schema SQL from context."""
        # Look for CREATE TABLE statements
        import re
        create_table_pattern = r'CREATE TABLE[^;]+;'
        matches = re.findall(create_table_pattern, context, re.IGNORECASE | re.DOTALL)
        
        if matches:
            return "\n\n".join(matches[:10])  # Limit to 10 tables
        
        return ""

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
        code_files: list[CodeFile] | None = None,
    ) -> list[SourceTable]:
        """Extract source table definitions from SQL files and knowledge base.

        This method prioritizes ACTUAL SQL DDL from code files over LLM-generated content.
        """
        source_tables: list[SourceTable] = []

        # PRIORITY 1: Parse actual SQL DDL files from code
        if code_files:
            # Log file types for debugging
            sql_files = [cf for cf in code_files if cf.path.lower().endswith('.sql')]
            java_files = [cf for cf in code_files if cf.path.lower().endswith('.java')]
            
            self.logger.info(
                f"Source tables extraction: total={len(code_files)}, sql_files={len(sql_files)}, java_files={len(java_files)}",
                form_name=context.form_name,
            )
            
            # Log SQL file paths for debugging
            if sql_files:
                self.logger.info(
                    f"SQL files found: {[cf.path for cf in sql_files[:10]]}",
                    form_name=context.form_name,
                )
            
            parsed_tables = parse_sql_files(code_files)
            self.logger.info(
                f"Parsed {len(parsed_tables)} tables from SQL files: {[pt.table_name for pt in parsed_tables]}",
                form_name=context.form_name,
            )

            for pt in parsed_tables:
                columns = [
                    {
                        "column_name": col.name,
                        "data_type": col.data_type,
                        "constraints": col.constraints,
                        "is_primary_key": col.is_primary_key,
                        "is_not_null": col.is_not_null,
                    }
                    for col in pt.columns
                ]

                foreign_keys = [
                    {
                        "columns": fk.columns,
                        "references_table": fk.references_table,
                        "references_columns": fk.references_columns,
                        "on_delete": fk.on_delete,
                    }
                    for fk in pt.foreign_keys
                ]

                source_tables.append(
                    SourceTable(
                        table_name=pt.table_name,
                        description=f"Table from {pt.source_file}",
                        table_type="primary" if pt.primary_key else "supporting",
                        columns=columns,
                        primary_key=pt.primary_key,
                        foreign_keys=foreign_keys,
                        indexes=[
                            {"name": idx.name, "columns": idx.columns, "unique": idx.is_unique}
                            for idx in pt.indexes
                        ],
                        stored_procedures=[],
                    )
                )

        # PRIORITY 2: Extract table references from existing PRD documentation
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("source_tables", []) + kb_contexts.get("existing_prd", []),
            max_contexts=10,
        )

        if kb_context.strip() and "SourceTables" in kb_context:
            # Only use LLM if we have actual PRD documentation with table info
            prompt = RequirementsPrompts.source_tables_extraction(context.form_name, kb_context)
            data = extract_json_array(await self.invoke_llm(context, prompt))

            # Add tables from PRD docs that weren't found in SQL files
            existing_names = {t.table_name.upper() for t in source_tables}
            for r in data:
                table_name = r.get("table_name", "")
                if table_name.upper() not in existing_names:
                    source_tables.append(
                        SourceTable(
                            table_name=table_name,
                            description=r.get("description", ""),
                            table_type=r.get("table_type", "supporting"),
                            columns=r.get("columns", []),
                            primary_key=r.get("primary_key", []),
                            foreign_keys=r.get("foreign_keys", []),
                            indexes=r.get("indexes", []),
                            stored_procedures=r.get("stored_procedures", []),
                        )
                    )

        self.logger.info(
            f"Total source tables extracted: {len(source_tables)}",
            form_name=context.form_name,
        )

        return source_tables

    async def _extract_database_mappings(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[DatabaseMapping]:
        """Extract entity-to-table mappings from code.

        Uses SQL parser to extract ACTUAL table references from Java code.
        """
        mappings: list[DatabaseMapping] = []

        # PRIORITY 1: Extract actual table/column references from Java code
        if code_files:
            java_refs = extract_table_references_from_java(code_files)

            self.logger.info(
                f"Extracted {len(java_refs['tables'])} table refs, "
                f"{len(java_refs['columns'])} field codes from Java",
                form_name=context.form_name,
            )

            # Group by main Java files (options files)
            main_files = [cf for cf in code_files if cf.file_type in ["source", "form_definition"]]

            for cf in main_files:
                if cf.language != "java":
                    continue

                # Extract references from this specific file
                parser = SQLDDLParser()
                file_refs = parser.parse_java_code_for_tables(cf.content)

                if file_refs["tables"] or file_refs["columns"]:
                    # Build field mappings from extracted field codes
                    field_mappings = []
                    for col in file_refs["columns"]:
                        field_mappings.append(
                            {
                                "java_field": col,
                                "java_type": "String",  # Default, would need annotation parsing
                                "column_name": col,
                                "column_type": "VARCHAR2",  # Default
                                "annotations": [],
                                "validation": "",
                            }
                        )

                    # Build queries from extracted SQL
                    queries = []
                    for sql in file_refs["sql_queries"]:
                        query_type = "SELECT"
                        if "INSERT" in sql.upper():
                            query_type = "INSERT"
                        elif "UPDATE" in sql.upper():
                            query_type = "UPDATE"
                        elif "DELETE" in sql.upper():
                            query_type = "DELETE"

                        queries.append(
                            {
                                "name": f"{query_type.lower()}Query",
                                "type": query_type,
                                "sql_or_jpql": sql[:200],  # Truncate long queries
                                "purpose": f"Extracted from {cf.path}",
                            }
                        )

                    if field_mappings or queries:
                        mappings.append(
                            DatabaseMapping(
                                entity_class=(
                                    cf.classes[0]
                                    if cf.classes
                                    else cf.path.split("/")[-1].replace(".java", "")
                                ),
                                table_name=(
                                    ", ".join(file_refs["tables"]) if file_refs["tables"] else "N/A"
                                ),
                                field_mappings=field_mappings,
                                relationships=[],
                                queries=queries,
                            )
                        )

        # PRIORITY 2: Use LLM only if we have good context and few mappings
        if len(mappings) < 2:
            model_code = self._get_model_code(code_files)
            kb_context = self.format_context_for_prompt(
                kb_contexts.get("database_mapping", []) + kb_contexts.get("database", []),
                max_contexts=8,
            )

            if model_code != self.NO_CODE_AVAILABLE:
                prompt = RequirementsPrompts.database_mappings(
                    context.form_name, model_code, kb_context
                )
                data = extract_json_array(await self.invoke_llm(context, prompt))

                # Only add LLM-generated mappings that reference actual code
                for r in data:
                    if r.get("entity_class") and r.get("table_name"):
                        mappings.append(
                            DatabaseMapping(
                                entity_class=r.get("entity_class", ""),
                                table_name=r.get("table_name", ""),
                                field_mappings=r.get("field_mappings", []),
                                relationships=r.get("relationships", []),
                                queries=r.get("queries", []),
                            )
                        )

        return mappings

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
- Fleet-specific validation rules
- Configuration flag behavior (usingSubChapters, usingRepDefs)
- Subchapter configuration requirements

Be SPECIFIC - include actual values, field names, and conditions from the source."""

        return await self.invoke_llm_for_list(context, prompt, prefix="BR-")
    
    async def _extract_detailed_business_rules(
        self, 
        context: AgentContext, 
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]]
    ) -> list[dict[str, Any]]:
        """Extract business rules with full descriptions and conditions."""
        if not code_files:
            return []
        
        # Extract business logic from code
        business_logic_code = self._extract_logic_code(code_files)
        
        # Get context from knowledge base
        kb_context = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + 
            kb_contexts.get("validation_functions", []) +
            kb_contexts.get("configuration_checks", []),
            max_contexts=10
        )
        
        prompt = f"""Extract detailed business rules from the code for "{context.form_name}".

CODE:
{business_logic_code}

KNOWLEDGE BASE:
{kb_context}

For each business rule, provide:
1. Rule ID (BR-XXX)
2. Title
3. Detailed description with exact conditions
4. Trigger conditions
5. Actions taken
6. Source location (file:line)

Return as JSON array:
[
    {{
        "rule_id": "BR-001",
        "title": "Chapter Code Existence Validation",
        "description": "Before creating a subchapter, the system must verify that the parent chapter exists using doesChapterRecordExist()",
        "condition": "doesChapterRecordExist(chapter) returns false",
        "action": "Show error message and prevent subchapter creation",
        "trigger": "User attempts to create subchapter",
        "source_location": "csChapterSupport.java:129-152"
    }}
]

Extract ALL business rules including:
- Validation functions (doesChapterRecordExist, doesSubChapterRecordExist)
- Configuration checks (usingSubChapters, usingRepDefs)
- Fleet-specific rules
- Alert rate validations
- Field dependency rules"""

        data = extract_json_array(await self.invoke_llm(context, prompt))
        return data

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
        """Extract code snippets containing business logic.
        
        Prioritizes main form files and includes more content for accurate extraction.
        """
        if not code_files:
            return "No code available."

        logic_keywords = [
            "if ", "else", "switch", "case", "calculate", "validate", "process",
            "save", "update", "delete", "insert", "setData", "getData",
            "actionPerformed", "setEnabled", "setMandatory", "showMessage", "setInfo"
        ]
        
        # Prioritize main form and support files
        priority_patterns = ["options/le", "csChapter", "Support.java", "Service.java"]
        
        priority_files = []
        other_files = []
        
        for cf in code_files:
            if cf.content and any(kw in cf.content.lower() for kw in logic_keywords):
                # Check if this is a priority file (main form or support class)
                is_priority = any(p.lower() in cf.path.lower() for p in priority_patterns)
                if is_priority:
                    priority_files.append(cf)
                else:
                    other_files.append(cf)
        
        # Combine with priority files first
        all_files = priority_files + other_files
        
        snippets = []
        for cf in all_files[:20]:  # Increased from 5 to 20 files
            snippets.append(f"// File: {cf.path}\n{cf.content[:8000]}")  # Increased from 1500 to 8000 chars

        return "\n\n".join(snippets) if snippets else "No logic code found."

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

        # Enhanced keywords to capture Java Swing validation patterns
        keywords = [
            "validate", "validation", "required", "pattern", "check", "error",
            "setMandatory", "isMandated", "showMessage", "setInfo", "JOptionPane",
            "parseInt", "parseDouble", "format", "must be", "cannot be", "invalid",
            "alertLimit", "exclusion", "equals", "trim().equals"
        ]
        
        # Prioritize main form files
        priority_patterns = ["options/le", "Support.java", "Combo.java"]
        priority_files = []
        other_files = []
        
        for cf in code_files:
            if cf.content and any(kw in cf.content.lower() for kw in keywords):
                is_priority = any(p.lower() in cf.path.lower() for p in priority_patterns)
                if is_priority:
                    priority_files.append(cf)
                else:
                    other_files.append(cf)
        
        all_files = priority_files + other_files
        snippets = []
        
        for cf in all_files[:15]:  # Increased from 5 to 15
            snippets.append(f"// File: {cf.path}\n{cf.content[:6000]}")  # Increased from 1500 to 6000

        return "\n\n".join(snippets) if snippets else "No validation code found."

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

    async def _generate_validation_config_requirements(
        self,
        context: AgentContext,
        code_files: list[CodeFile] | None,
        kb_contexts: dict[str, list[str]],
    ) -> list[FunctionalRequirement]:
        """Generate functional requirements for validation functions and configuration checks."""
        validation_code = self._extract_validation_code(code_files)
        config_context = self.format_context_for_prompt(
            kb_contexts.get("validation_functions", []) + 
            kb_contexts.get("configuration_checks", []),
            max_contexts=8
        )
        
        prompt = f"""Extract validation and configuration functional requirements from the code for "{context.form_name}".

CODE:
{validation_code}

CONTEXT:
{config_context}

Generate functional requirements for:
1. Validation functions (doesChapterRecordExist, doesSubChapterRecordExist)
2. Configuration checks (usingSubChapters, usingRepDefs)
3. Fleet-specific validation
4. Alert rate management

Return as JSON array:
[
    {{
        "req_id": "FR-011",
        "title": "Validate Chapter Exists",
        "description": "System must validate that a chapter record exists before allowing operations that reference it",
        "priority": "P0",
        "category": "validation",
        "business_logic": "Call doesChapterRecordExist(chapter). If returns false, show error and prevent operation",
        "source_methods": ["csChapterSupport.doesChapterRecordExist(String chapter)"],
        "api_specification": {{}},
        "database_operations": [{{"operation": "SELECT", "table": "CHAPTERS", "columns": ["CHAPTER"]}}],
        "validation_rules": ["Chapter code must exist in CHAPTERS table"],
        "calculations": [],
        "user_story": "As a user, I want the system to validate chapter existence so that invalid references are prevented",
        "acceptance_criteria": [
            "Given invalid chapter code, When operation is attempted, Then error is shown",
            "Given valid chapter code, When operation is attempted, Then operation proceeds"
        ],
        "dependencies": [],
        "source_files": ["csChapterSupport.java:129-152"]
    }}
]

Include ALL validation and configuration functions found in the code."""

        data = extract_json_array(await self.invoke_llm(context, prompt))
        
        return [
            FunctionalRequirement(
                req_id=r.get("req_id", f"FR-{i+11:03d}"),
                title=r.get("title", ""),
                description=r.get("description", ""),
                priority=r.get("priority", "P1"),
                category=r.get("category", "validation"),
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
    
    def _compile_code_references(self, code_files: list[CodeFile] | None) -> dict[str, list[str]]:
        """Compile code references by category with line numbers."""
        if not code_files:
            return {}

        references: dict[str, list[str]] = {}
        for cf in code_files:
            category = cf.file_type
            if category not in references:
                references[category] = []
            # Include path with potential line number info
            references[category].append(cf.path)

        return references
