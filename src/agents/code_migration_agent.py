"""Code Migration Agent for generating .NET backend and React frontend from knowledge base."""

import json
import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.prompts.code_migration import CodeMigrationPrompts
from src.utils.code_migration_utils import (
    create_directory_structure,
    create_zip_archive,
    generate_validation_report,
    parse_llm_code_response,
    validate_backend_structure,
    validate_frontend_structure,
)
from src.utils.file_utils import ensure_directory
from src.utils.logging_config import ExecutionTimer, get_logger

logger = get_logger(__name__)


@dataclass
class CodeMigrationResult:
    """Result from code migration agent."""

    form_name: str
    backend_files: list[dict[str, str]] = field(
        default_factory=list
    )  # [{"path": "...", "content": "..."}]
    frontend_files: list[dict[str, str]] = field(default_factory=list)
    backend_zip_path: str = ""
    frontend_zip_path: str = ""
    documentation: str = ""
    swagger_json: dict[str, Any] | None = None
    backend_validation: dict[str, Any] = field(default_factory=dict)
    frontend_validation: dict[str, Any] = field(default_factory=dict)
    validation_report: str = ""


class CodeMigrationAgent(BaseAgent[CodeMigrationResult]):
    """
    Agent for migrating legacy Java Swing codebase to .NET backend and React frontend.

    Retrieves context from knowledge base and generates complete, runnable applications.
    """

    def __init__(self) -> None:
        """Initialize the code migration agent."""
        super().__init__("CodeMigrationAgent")

    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for code migration."""
        return CodeMigrationPrompts.system_prompt(context.form_name)

    async def analyze(
        self,
        context: AgentContext,
        output_dir: str = "./output/migratedCode",
        **kwargs: Any,
    ) -> AgentResult[CodeMigrationResult]:
        """
        Generate .NET backend and React frontend code from knowledge base.

        Args:
            context: Agent execution context
            output_dir: Output directory for zip files

        Returns:
            AgentResult with CodeMigrationResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting code migration",
            form_name=context.form_name,
            output_dir=output_dir,
        )

        try:
            # 1. Retrieve Knowledge Base Context
            kb_contexts = self._retrieve_kb_context(context.form_name)

            # 2. Generate Backend JSON Specification
            backend_json_spec = await self._generate_backend_json_spec(context, kb_contexts)

            # 3. Generate .NET Backend Code
            backend_response = await self._generate_backend_code(
                context, backend_json_spec, kb_contexts
            )
            backend_files, backend_doc, swagger_json = parse_llm_code_response(backend_response)

            # 4. Generate Frontend JSON Specification
            frontend_json_spec = await self._generate_frontend_json_spec(
                context, kb_contexts, swagger_json
            )

            # 5. Generate React Frontend Code
            frontend_response = await self._generate_frontend_code(
                context, frontend_json_spec, swagger_json, kb_contexts
            )
            frontend_files, frontend_doc, _ = parse_llm_code_response(frontend_response)

            # 6. Validate Generated Code Structure
            self.logger.info("Validating generated code structure")

            # Extract entities and screens from generated files (not hardcoded)
            backend_entities = self._extract_entities_from_files(backend_files)
            frontend_screens = self._extract_screens_from_files(frontend_files)

            backend_validation = validate_backend_structure(backend_files, backend_entities)
            frontend_validation = validate_frontend_structure(frontend_files, frontend_screens)

            validation_report = generate_validation_report(
                backend_validation, frontend_validation, context.form_name
            )

            self.logger.info(
                "Validation complete",
                backend_valid=backend_validation["valid"],
                frontend_valid=frontend_validation["valid"],
                backend_issues=len(backend_validation.get("structure_issues", [])),
                frontend_issues=len(frontend_validation.get("structure_issues", [])),
            )

            # 7. Create Directory Structures and Write Files
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)

                # Create backend structure
                backend_dir = temp_path / f"{context.form_name}_backend"
                if backend_files:
                    create_directory_structure(backend_dir, backend_files)

                # Create frontend structure
                frontend_dir = temp_path / f"{context.form_name}_frontend"
                if frontend_files:
                    create_directory_structure(frontend_dir, frontend_files)

                # 8. Create Zip Archives
                output_path = Path(output_dir)
                ensure_directory(output_path)

                backend_zip_path = output_path / f"{context.form_name}_backend.zip"
                frontend_zip_path = output_path / f"{context.form_name}_frontend.zip"

                if backend_files:
                    create_zip_archive(backend_dir, backend_zip_path)
                if frontend_files:
                    create_zip_archive(frontend_dir, frontend_zip_path)

                # Save validation report
                report_path = output_path / f"{context.form_name}_validation_report.md"
                report_path.write_text(validation_report, encoding="utf-8")

                # 9. Create Result
                result = CodeMigrationResult(
                    form_name=context.form_name,
                    backend_files=backend_files,
                    frontend_files=frontend_files,
                    backend_zip_path=str(backend_zip_path),
                    frontend_zip_path=str(frontend_zip_path),
                    documentation=f"{backend_doc}\n\n{frontend_doc}".strip(),
                    swagger_json=swagger_json,
                    backend_validation=backend_validation,
                    frontend_validation=frontend_validation,
                    validation_report=validation_report,
                )

                self.logger.info(
                    "Code migration complete",
                    form_name=context.form_name,
                    backend_files=len(backend_files),
                    frontend_files=len(frontend_files),
                    backend_zip=str(backend_zip_path),
                    frontend_zip=str(frontend_zip_path),
                    backend_valid=backend_validation["valid"],
                    frontend_valid=frontend_validation["valid"],
                    duration_ms=timer.elapsed_ms(),
                )

                return self.create_success_result(result, timer)

        except Exception as e:
            self.logger.error("Code migration failed", error=str(e), form_name=context.form_name)
            return self.create_error_result(e, timer)

    def _extract_entities_from_files(self, files: list[dict[str, str]]) -> list[str]:
        """Extract entity names from generated backend files."""
        entities = []
        for file_info in files:
            path = file_info.get("path", "")
            if "Entities/" in path and path.endswith(".cs"):
                # Extract entity name from path like "[Project].Data/Entities/[Entity].cs"
                entity_name = path.split("/")[-1].replace(".cs", "")
                if entity_name and entity_name not in entities:
                    entities.append(entity_name)

        # No default entities - let validation report missing entities
        return entities

    def _get_project_name(self, form_name: str) -> str:
        """Generate project name from form name (e.g., le11 -> LE11Management)."""
        # Capitalize form name properly
        capitalized = form_name.upper() if len(form_name) <= 4 else form_name.capitalize()
        return f"{capitalized}Management"

    def _extract_screens_from_files(self, files: list[dict[str, str]]) -> list[str]:
        """Extract screen names from generated frontend files."""
        screens = []
        for file_info in files:
            path = file_info.get("path", "")
            # Look for component folders like "src/components/fleet/FleetSelectionScreen/"
            if "components/" in path and "Screen" in path:
                # Extract screen name from path
                parts = path.split("/")
                for part in parts:
                    if "Screen" in part and part not in screens:
                        screen_name = part.replace("Screen", "").replace("/", "")
                        if screen_name:
                            screens.append(screen_name)

        # No default screens - let validation report what's missing
        return list(set(screens))

    def _retrieve_kb_context(self, form_name: str) -> dict[str, list[str]]:
        """
        Retrieve COMPREHENSIVE context from the unified knowledge base.

        This retrieves from ALL sources with MAXIMUM coverage:
        - Legacy code (FULL business logic, methods, data models)
        - Form docs (requirements, app flows, field mappings)
        - DB_PRD (database schemas, table relationships)
        - Screenshots (UI context)
        """
        contexts = {}

        # Define comprehensive queries - using HIGHER limits for full coverage
        query_configs = [
            # CRITICAL: Business Logic Methods - target business_logic doc_type
            {
                "key": "method_implementations",
                "queries": [
                    "METHOD FULL METHOD IMPLEMENTATION",
                    "public private method action doUsing",
                    "save update delete calculate validate",
                ],
                "doc_type": "business_logic",
                "limit": 30,
            },
            # Legacy Code - Full Source Files
            {
                "key": "source_code",
                "queries": [
                    "Java Source Code options adapter service",
                    "FILE CONTENT class method field",
                    "public class extends implements",
                ],
                "doc_type": "code",
                "limit": 25,
            },
            # Data Models & DTOs - get ALL fields
            {
                "key": "data_model",
                "queries": [
                    "class entity DTO field property type",
                    "FILE HEADER Classes fields private String",
                    "getter setter attribute column Integer Boolean",
                ],
                "doc_type": "code",
                "limit": 25,
            },
            # Form Docs - FULL documentation from MinIO
            {
                "key": "form_docs",
                "queries": [
                    "PRD Document CONTENT requirement",
                    "business rule specification field mapping",
                    "Description overview form functional",
                ],
                "doc_type": "existing_prd",
                "limit": 25,
            },
            # Database - Schema & SQL from DB_PRD
            {
                "key": "database",
                "queries": [
                    "DATABASE DOCUMENTATION table column schema",
                    "CREATE TABLE primary key foreign key",
                    "entity relationship mapping constraint",
                ],
                "doc_type": "database",
                "limit": 20,
            },
            # SQL Files from legacy code
            {
                "key": "sql_files",
                "queries": [
                    "SQL DDL Content CREATE TABLE",
                    "INSERT UPDATE DELETE SELECT Language: sql",
                ],
                "doc_type": "code",
                "limit": 15,
            },
            # UI Context from Screenshots
            {
                "key": "ui_context",
                "queries": [
                    "UI Screen Analysis screen form field",
                    "Screenshot Analysis component layout button",
                ],
                "doc_type": "screenshot_analysis",
                "limit": 15,
            },
            # Form Definitions (.form files)
            {
                "key": "form_definitions",
                "queries": [
                    "Form Definition layout component field",
                ],
                "doc_type": "code",
                "limit": 10,
            },
        ]

        for config in query_configs:
            key = config["key"]
            all_results = []

            for query in config["queries"]:
                try:
                    results = self.retrieve_context(
                        form_name,
                        query,
                        limit=config["limit"],
                        doc_type=config.get("doc_type"),
                    )
                    all_results.extend(results)
                except Exception as e:
                    self.logger.warning(
                        f"Failed to retrieve context for {key} with query '{query}': {e}"
                    )

            # Deduplicate results while preserving order (use longer hash)
            seen = set()
            unique_results = []
            for r in all_results:
                r_hash = hash(r[:500]) if len(r) > 500 else hash(r)
                if r_hash not in seen:
                    seen.add(r_hash)
                    unique_results.append(r)

            contexts[key] = unique_results[: config["limit"]]
            self.logger.info(f"Retrieved {len(contexts[key])} unique contexts for {key}")

        # CRITICAL: Also retrieve ALL content without doc_type filters
        comprehensive_queries = [
            ("all_methods", "METHOD public private void String action save update", 35),
            ("all_classes", "class entity DTO extends implements interface field", 30),
            ("all_docs", "PRD Document requirement specification business rule", 25),
            ("all_code", "Java Source Code method class field validation", 30),
        ]

        for key, query, limit in comprehensive_queries:
            try:
                results = self.retrieve_context(form_name, query, limit=limit, doc_type=None)
                contexts[key] = results
                self.logger.info(f"Retrieved {len(results)} comprehensive contexts for {key}")
            except Exception as e:
                self.logger.warning(f"Failed to retrieve comprehensive context for {key}: {e}")
                contexts[key] = []

        # Merge for backward compatibility
        contexts["business_logic"] = (
            contexts.get("method_implementations", []) + contexts.get("all_methods", [])
        )[:40]
        contexts["api_specs"] = contexts.get("source_code", [])[:20]

        # Log total context retrieved
        total_contexts = sum(len(v) for v in contexts.values())
        self.logger.info(f"Total knowledge base contexts retrieved: {total_contexts}")

        return contexts

    async def _generate_backend_json_spec(
        self, context: AgentContext, kb_contexts: dict[str, list[str]]
    ) -> str:
        """Generate JSON specification for backend from comprehensive KB context."""
        # Combine ALL relevant contexts for maximum coverage
        data_model_context = self.format_context_for_prompt(
            kb_contexts.get("data_model", [])
            + kb_contexts.get("database", [])
            + kb_contexts.get("sql_files", []),
            max_contexts=20,
        )

        business_logic_context = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("api_specs", []),
            max_contexts=20,
        )

        form_docs_context = self.format_context_for_prompt(
            kb_contexts.get("form_docs", []) + kb_contexts.get("all_docs", []), max_contexts=15
        )

        all_code_context = self.format_context_for_prompt(
            kb_contexts.get("all_code", []), max_contexts=15
        )

        prompt = f"""You are migrating a legacy Java Swing application "{context.form_name}" to a modern .NET backend.

CRITICAL: You must extract ALL information from the knowledge base below to generate an accurate JSON specification.
The generated code must match 100% with the legacy codebase - every field, every validation, every business rule.

=== LEGACY CODE - DATA MODELS & ENTITIES ===
{data_model_context}

=== LEGACY CODE - BUSINESS LOGIC & METHODS ===
{business_logic_context}

=== FORM DOCUMENTATION & REQUIREMENTS ===
{form_docs_context}

=== ADDITIONAL CODE CONTEXT ===
{all_code_context}

Based on the above knowledge base, generate a COMPLETE JSON specification that includes:

1. **Entities** (extract ALL from the legacy code):
   - Entity name (exactly as in legacy code)
   - ALL fields with exact names, types, and constraints
   - Relationships (foreign keys, one-to-many, many-to-many)
   - Database table mappings

2. **API Endpoints** (based on legacy methods):
   - Map each legacy action/method to a REST endpoint
   - Include exact request/response structures
   - Match field names exactly

3. **Validation Rules** (extract ALL from legacy code):
   - Field-level validations (required, min/max, patterns)
   - Business validations (cross-field, conditional)
   - Error messages (use exact messages from legacy)

4. **Business Logic** (preserve ALL from legacy):
   - Calculations and formulas
   - Conditional logic and workflows
   - Data transformations

Return ONLY valid JSON. The JSON must be comprehensive and match the legacy system exactly.
Do NOT invent fields or logic - extract everything from the knowledge base."""

        response = await self.invoke_llm(context, prompt)

        # Try to extract JSON from response
        json_pattern = r"```(?:json)?\s*(\{.*?\})\s*```"
        json_match = re.search(json_pattern, response, re.DOTALL)

        if json_match:
            return json_match.group(1)

        # Try to find JSON object directly
        try:
            start = response.find("{")
            end = response.rfind("}") + 1
            if start >= 0 and end > start:
                json_str = response[start:end]
                json.loads(json_str)
                return json_str
        except Exception:
            pass

        return response

    async def _generate_frontend_json_spec(
        self,
        context: AgentContext,
        kb_contexts: dict[str, list[str]],
        swagger_json: dict[str, Any] | None,
    ) -> str:
        """Generate JSON specification for frontend from comprehensive KB context."""
        # Combine ALL relevant UI contexts
        ui_context = self.format_context_for_prompt(
            kb_contexts.get("ui_context", []) + kb_contexts.get("form_docs", []), max_contexts=20
        )

        data_model_context = self.format_context_for_prompt(
            kb_contexts.get("data_model", []) + kb_contexts.get("all_code", []), max_contexts=15
        )

        business_logic_context = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []), max_contexts=10
        )

        swagger_info = ""
        if swagger_json:
            swagger_info = (
                f"\n\n=== BACKEND API SPECIFICATION ===\n{json.dumps(swagger_json, indent=2)}"
            )

        prompt = f"""You are migrating a legacy Java Swing application "{context.form_name}" to a modern React frontend.

CRITICAL: You must extract ALL UI information from the knowledge base below to generate an accurate JSON specification.
The generated React app must match 100% with the legacy UI - every form, every field, every validation.

=== LEGACY UI SCREENS & COMPONENTS ===
{ui_context}

=== DATA MODELS & FIELD DEFINITIONS ===
{data_model_context}

=== BUSINESS LOGIC & VALIDATIONS ===
{business_logic_context}
{swagger_info}

Based on the above knowledge base, generate a COMPLETE JSON specification that includes:

1. **Forms** (extract ALL from legacy screens):
   - Form names exactly as in legacy
   - ALL fields with exact names, types, labels
   - Field validations (required, patterns, min/max)
   - Field relationships and dependencies

2. **UI Components** (based on legacy .form files):
   - Component types (text input, dropdown, table, etc.)
   - Layout and positioning
   - Labels and placeholders

3. **Navigation**:
   - Screen flows and transitions
   - Routes for each screen
   - Menu structure

4. **API Integration** (match with backend spec):
   - Endpoints for each form action
   - Request/response field mappings
   - Error handling

5. **Validation Rules** (client-side):
   - Field-level validations
   - Cross-field validations
   - Error messages (exact from legacy)

Return ONLY valid JSON. The JSON must be comprehensive and match the legacy UI exactly.
Do NOT invent fields or UI elements - extract everything from the knowledge base."""

        response = await self.invoke_llm(context, prompt)

        json_pattern = r"```(?:json)?\s*(\{.*?\})\s*```"
        json_match = re.search(json_pattern, response, re.DOTALL)

        if json_match:
            return json_match.group(1)

        try:
            start = response.find("{")
            end = response.rfind("}") + 1
            if start >= 0 and end > start:
                json_str = response[start:end]
                json.loads(json_str)
                return json_str
        except Exception:
            pass

        return response

    async def _generate_backend_code(
        self,
        context: AgentContext,
        json_spec: str,
        kb_contexts: dict[str, list[str]],
    ) -> str:
        """
        Generate .NET backend code using MULTI-PASS approach (4 passes for 100% output).

        Pass 1a: Data Layer core (Entities, Configurations, DbContext)
        Pass 1b: Repositories (Interfaces + Implementations)
        Pass 2: Business Layer (Services, DTOs, Validators, Mappings)
        Pass 3: API Layer (Controllers, Program.cs, appsettings, Common)
        """
        self.logger.info("Starting 4-pass backend generation for 100%% output")

        dependencies_context = self._build_backend_context(kb_contexts)
        all_files = []

        # ============ PASS 1a: ENTITIES, CONFIGURATIONS, DBCONTEXT ============
        self.logger.info("Pass 1a: Data Layer (Entities, Configurations, DbContext)")
        data_core_prompt = self._build_data_core_prompt(context, json_spec, dependencies_context)
        data_core_response = await self.invoke_llm(context, data_core_prompt)
        data_core_files, _, _ = parse_llm_code_response(data_core_response)
        all_files.extend(data_core_files)
        self.logger.info("Pass 1a complete: %s files", len(data_core_files))

        # ============ PASS 1b: REPOSITORIES ============
        self.logger.info("Pass 1b: Repositories (Interfaces + Implementations)")
        repos_prompt = self._build_repositories_prompt(
            context, json_spec, dependencies_context, data_core_files
        )
        repos_response = await self.invoke_llm(context, repos_prompt)
        repos_files, _, _ = parse_llm_code_response(repos_response)
        all_files.extend(repos_files)
        self.logger.info("Pass 1b complete: %s files", len(repos_files))

        data_layer_files = data_core_files + repos_files

        # ============ PASS 2: BUSINESS LAYER ============
        self.logger.info("Pass 2: Business Layer (Services, DTOs, Validators, Mappings)")
        business_layer_prompt = self._build_business_layer_prompt(
            context, json_spec, dependencies_context, data_layer_files
        )
        business_layer_response = await self.invoke_llm(context, business_layer_prompt)
        business_layer_files, _, _ = parse_llm_code_response(business_layer_response)
        all_files.extend(business_layer_files)
        self.logger.info("Pass 2 complete: %s files", len(business_layer_files))

        # ============ PASS 3: API LAYER ============
        self.logger.info("Pass 3: API Layer (Controllers, Program.cs, appsettings, Common)")
        api_layer_prompt = self._build_api_layer_prompt(
            context, json_spec, dependencies_context, data_layer_files, business_layer_files
        )
        api_layer_response = await self.invoke_llm(context, api_layer_prompt)
        api_layer_files, documentation, swagger_json = parse_llm_code_response(api_layer_response)
        all_files.extend(api_layer_files)
        self.logger.info("Pass 3 complete: %s files", len(api_layer_files))

        self.logger.info("Backend generation complete: %s total files", len(all_files))
        return self._format_multipass_response(all_files, documentation, swagger_json)

    def _build_backend_context(self, kb_contexts: dict[str, list[str]]) -> str:
        """Build comprehensive context for backend generation."""
        dependencies_parts = []

        # Data model context
        data_model = self.format_context_for_prompt(
            kb_contexts.get("data_model", [])
            + kb_contexts.get("database", [])
            + kb_contexts.get("all_classes", []),
            max_contexts=30,
        )
        if data_model and data_model != "No additional context available.":
            dependencies_parts.append(f"=== DATA MODELS & DATABASE SCHEMA ===\n{data_model}")

        # Business logic context
        business_logic = self.format_context_for_prompt(
            kb_contexts.get("business_logic", [])
            + kb_contexts.get("method_implementations", [])
            + kb_contexts.get("all_methods", []),
            max_contexts=35,
        )
        if business_logic and business_logic != "No additional context available.":
            dependencies_parts.append(f"=== BUSINESS LOGIC & METHODS ===\n{business_logic}")

        # Form docs context
        form_docs = self.format_context_for_prompt(
            kb_contexts.get("form_docs", []) + kb_contexts.get("all_docs", []), max_contexts=25
        )
        if form_docs and form_docs != "No additional context available.":
            dependencies_parts.append(f"=== FORM DOCUMENTATION & REQUIREMENTS ===\n{form_docs}")

        # SQL files context
        sql_context = self.format_context_for_prompt(
            kb_contexts.get("sql_files", []), max_contexts=20
        )
        if sql_context and sql_context != "No additional context available.":
            dependencies_parts.append(f"=== SQL SCHEMAS & QUERIES ===\n{sql_context}")

        # Source code context
        source_code = self.format_context_for_prompt(
            kb_contexts.get("source_code", []) + kb_contexts.get("all_code", []), max_contexts=25
        )
        if source_code and source_code != "No additional context available.":
            dependencies_parts.append(f"=== LEGACY SOURCE CODE ===\n{source_code}")

        return "\n\n".join(dependencies_parts) if dependencies_parts else "No additional context."

    def _build_data_core_prompt(
        self, context: AgentContext, json_spec: str, dependencies_context: str
    ) -> str:
        """Build prompt for Data Layer core: Entities, Configurations, DbContext only."""
        project_name = self._get_project_name(context.form_name)

        return f"""You are migrating "{context.form_name}" to .NET 8. Generate ONLY the Data Layer CORE (Entities, Configurations, DbContext). You will generate Repositories in a separate step.

MANDATORY: You MUST output EVERY file listed below. Do not skip any entity, configuration, or DbContext.

=== JSON SPECIFICATION ===
{json_spec}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files with this EXACT structure (no Repositories in this step):

{project_name}.Data/
├── Entities/
│   └── [Entity].cs              # ONE FILE PER ENTITY - extract ALL from JSON/legacy
├── Configurations/
│   └── [Entity]Configuration.cs # ONE PER ENTITY - table name, columns, relationships
└── Context/
    └── {project_name}DbContext.cs  # DbContext with DbSet for EVERY entity

REQUIREMENTS:
1. Extract ALL entities from the JSON spec and knowledge base - one .cs file per entity
2. Every entity: ALL fields, correct types, [Key], [MaxLength], [Required], [Column], navigation properties
3. Every configuration: ToTable, HasKey, Property mappings, HasOne/WithMany relationships
4. DbContext: DbSet<Entity> for every entity, OnModelCreating if needed
5. Use exact table/column names from legacy (knowledge base)

Output EACH file in a separate code block:
```csharp:{project_name}.Data/Entities/[EntityName].cs
// full file content
```
```csharp:{project_name}.Data/Configurations/[EntityName]Configuration.cs
// full file content
```
```csharp:{project_name}.Data/Context/{project_name}DbContext.cs
// full file content
```"""

    def _build_repositories_prompt(
        self,
        context: AgentContext,
        json_spec: str,
        dependencies_context: str,
        data_core_files: list[dict[str, str]],
    ) -> str:
        """Build prompt for Repositories only (Interfaces + Implementations)."""
        project_name = self._get_project_name(context.form_name)
        entity_names = []
        for f in data_core_files:
            if "Entities/" in f.get("path", ""):
                name = f["path"].split("/")[-1].replace(".cs", "")
                entity_names.append(name)
        entities_str = ", ".join(entity_names) if entity_names else "every entity from Data layer"

        return f"""You are migrating "{context.form_name}" to .NET 8. Generate ONLY Repositories (Interfaces + Implementations). Entities and DbContext already exist.

MANDATORY: You MUST output ONE interface and ONE implementation per entity. Do not skip any.

=== JSON SPECIFICATION ===
{json_spec}

=== ENTITIES (already created) ===
{entities_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files:

{project_name}.Data/
└── Repositories/
    ├── Interfaces/
    │   └── I[Entity]Repository.cs   # ONE PER ENTITY
    └── Implementations/
        └── [Entity]Repository.cs   # ONE PER ENTITY

REQUIREMENTS:
1. I[Entity]Repository: GetAllAsync, GetByIdAsync (or composite key), AddAsync, UpdateAsync, DeleteAsync, plus any from legacy (ExistsAsync, etc.)
2. [Entity]Repository: Implement interface, inject {project_name}DbContext, use DbSet, async/await
3. Handle composite keys where needed (e.g. FleetChapter: Fleet + Chapter)

Output EACH file:
```csharp:{project_name}.Data/Repositories/Interfaces/I[Entity]Repository.cs
// full content
```
```csharp:{project_name}.Data/Repositories/Implementations/[Entity]Repository.cs
// full content
```"""

    def _build_business_layer_prompt(
        self,
        context: AgentContext,
        json_spec: str,
        dependencies_context: str,
        data_layer_files: list[dict[str, str]],
    ) -> str:
        """Build prompt for Business Layer generation."""
        project_name = self._get_project_name(context.form_name)

        # Summarize data layer for context
        entity_names = []
        for f in data_layer_files:
            if "Entities/" in f.get("path", ""):
                name = f["path"].split("/")[-1].replace(".cs", "")
                entity_names.append(name)

        entities_str = (
            ", ".join(entity_names) if entity_names else "(extract entities from knowledge base)"
        )

        return f"""You are migrating "{context.form_name}" to .NET 8. Generate the BUSINESS LAYER only (DTOs, Services, Validators, Mappings).

MANDATORY: You MUST generate EVERY file below. Do not skip DTOs, Service interfaces, Service implementations, or Validators. Services MUST contain real business logic from the knowledge base.

=== JSON SPECIFICATION ===
{json_spec}

=== ENTITIES CREATED IN DATA LAYER ===
{entities_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files for the Business Layer:

{project_name}.Business/
├── DTOs/
│   └── [Entity]/
│       ├── [Entity]ReadDto.cs
│       ├── [Entity]CreateDto.cs
│       └── [Entity]UpdateDto.cs
├── Services/
│   ├── Interfaces/
│   │   └── I[Entity]Service.cs      # ONE PER ENTITY - all methods from legacy
│   └── Implementations/
│       └── [Entity]Service.cs      # ONE PER ENTITY - FULL implementation
├── Validators/
│   └── [Entity]Validator.cs        # ONE PER ENTITY - FluentValidation
└── Mappings/
    └── MappingProfile.cs           # AutoMapper: Entity <-> DTOs

REQUIREMENTS:
1. DTOs: Read/Create/Update for EVERY entity; match entity fields exactly
2. I[Entity]Service: GetAllAsync, GetByIdAsync, CreateAsync, UpdateAsync, DeleteAsync + every custom method from legacy (SaveChanges, ValidateExists, etc.)
3. [Entity]Service: FULL implementation - inject I[Entity]Repository, implement every method with real logic from knowledge base (validations, calculations, workflows). Do NOT leave methods empty or as stubs.
4. Validators: rules from legacy (Required, MaxLength, custom rules)
5. MappingProfile: CreateMap for each Entity <-> ReadDto/CreateDto/UpdateDto

CRITICAL: Service implementations must contain the actual business logic from the knowledge base (calculations, validations, conditional logic). Extract from METHOD and BUSINESS LOGIC sections.

Output EACH file in its own code block:
```csharp:{project_name}.Business/[folder]/[path].cs
// full file content
```"""

    def _build_api_layer_prompt(
        self,
        context: AgentContext,
        json_spec: str,
        dependencies_context: str,
        data_layer_files: list[dict[str, str]],
        business_layer_files: list[dict[str, str]],
    ) -> str:
        """Build prompt for API Layer generation."""
        project_name = self._get_project_name(context.form_name)

        # Extract service names for DI registration
        service_names = []
        for f in business_layer_files:
            if "Services/Implementations/" in f.get("path", ""):
                name = f["path"].split("/")[-1].replace(".cs", "")
                service_names.append(name)

        services_str = (
            ", ".join(service_names) if service_names else "(extract services from business layer)"
        )

        return f"""You are migrating "{context.form_name}" to .NET 8. Generate the API LAYER only.

MANDATORY: You MUST generate ALL of these files. Do not skip Program.cs, appsettings, Common, or any Controller.

=== JSON SPECIFICATION ===
{json_spec}

=== SERVICES CREATED IN BUSINESS LAYER ===
{services_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files:

{project_name}.API/
├── Controllers/
│   └── [Entity]Controller.cs     # ONE controller PER entity (FleetChaptersController, ChapterController, etc.)
├── Program.cs                    # MANDATORY: WebApplicationBuilder, AddDbContext, AddScoped for ALL repositories and services, AddControllers, Swagger
├── appsettings.json              # MANDATORY: ConnectionStrings, Logging
└── appsettings.Development.json

{project_name}.Common/
├── Exceptions/
│   └── NotFoundException.cs
└── Models/
    ├── ApiResponse.cs            # Generic ApiResponse<T>, Succeed/Fail
    └── PagedResult.cs

REQUIREMENTS:
1. ONE Controller per entity: [Entity]Controller with [Route("api/[controller]")], inject I[Entity]Service
2. Each controller: GET all, GET by id (or composite), POST, PUT, DELETE + custom actions from legacy
3. Program.cs: MUST register DbContext, EVERY I*Repository -> *Repository, EVERY I*Service -> *Service, AddControllers, UseSwagger/UseSwaggerUI
4. appsettings.json: ConnectionStrings:DefaultConnection, Logging
5. Common: ApiResponse<T>, PagedResult<T>, NotFoundException

Also output Swagger JSON between:
===SWAGGER_START===
{{"openapi":"3.0.0", ...}}
===SWAGGER_END===

Output EACH file (Program.cs, appsettings.json, appsettings.Development.json, every Controller, Common files):
```csharp:{project_name}.API/Program.cs
// full content
```
```csharp:{project_name}.API/Controllers/[Entity]Controller.cs
// full content
```
```json:{project_name}.API/appsettings.json
// full content
```
And Common:
```csharp:{project_name}.Common/Models/ApiResponse.cs
// full content
```
etc."""

    def _format_multipass_response(
        self,
        all_files: list[dict[str, str]],
        documentation: str,
        swagger_json: dict[str, Any] | None,
    ) -> str:
        """Format multi-pass results into the expected response format."""
        response_parts = []

        # Add all files
        for file_info in all_files:
            path = file_info.get("path", "")
            content = file_info.get("content", "")
            response_parts.append(f"```csharp:{path}\n{content}\n```")

        # Add documentation if present
        if documentation:
            response_parts.append(
                f"\n===DOCUMENTATION_START===\n{documentation}\n===DOCUMENTATION_END==="
            )

        # Add swagger if present
        if swagger_json:
            swagger_str = json.dumps(swagger_json, indent=2)
            response_parts.append(f"\n===SWAGGER_START===\n{swagger_str}\n===SWAGGER_END===")

        return "\n\n".join(response_parts)

    async def _generate_frontend_code(
        self,
        context: AgentContext,
        json_spec: str,
        swagger_json: dict[str, Any] | None,
        kb_contexts: dict[str, list[str]],
    ) -> str:
        """
        Generate React frontend code using MULTI-PASS approach.

        Pass 1: Types & Schemas (TypeScript types, Zod schemas)
        Pass 2: API Hooks (TanStack Query hooks for all endpoints)
        Pass 3: Components (All screens from PRD)

        This ensures complete generation of all layers.
        """
        self.logger.info("Starting 4-pass frontend generation for valid React app")

        dependencies_context = self._build_frontend_context(kb_contexts)
        swagger_str = json.dumps(swagger_json, indent=2) if swagger_json else "{}"

        all_files = []

        # ============ PASS 0: PROJECT SCAFFOLD (package.json, public/, entry) ============
        self.logger.info("Pass 0: Generating project scaffold (package.json, public/, src/main)")
        scaffold_prompt = self._build_frontend_scaffold_prompt(
            context, json_spec, dependencies_context
        )
        scaffold_response = await self.invoke_llm(context, scaffold_prompt)
        scaffold_files, _, _ = parse_llm_code_response(scaffold_response)
        all_files.extend(scaffold_files)
        self.logger.info("Pass 0 complete: %s files", len(scaffold_files))

        # ============ PASS 1: TYPES & SCHEMAS ============
        self.logger.info("Pass 1: Generating Types & Schemas")
        types_prompt = self._build_frontend_types_prompt(
            context, json_spec, swagger_str, dependencies_context
        )
        types_response = await self.invoke_llm(context, types_prompt)
        types_files, _, _ = parse_llm_code_response(types_response)
        all_files.extend(types_files)
        self.logger.info(f"Pass 1 complete: {len(types_files)} files generated")

        # ============ PASS 2: API HOOKS ============
        self.logger.info("Pass 2: Generating API Hooks")
        hooks_prompt = self._build_frontend_hooks_prompt(
            context, json_spec, swagger_str, dependencies_context
        )
        hooks_response = await self.invoke_llm(context, hooks_prompt)
        hooks_files, _, _ = parse_llm_code_response(hooks_response)
        all_files.extend(hooks_files)
        self.logger.info(f"Pass 2 complete: {len(hooks_files)} files generated")

        # ============ PASS 3: COMPONENTS ============
        self.logger.info("Pass 3: Generating Components")
        components_prompt = self._build_frontend_components_prompt(
            context, json_spec, swagger_str, dependencies_context, types_files
        )
        components_response = await self.invoke_llm(context, components_prompt)
        components_files, documentation, _ = parse_llm_code_response(components_response)
        all_files.extend(components_files)
        self.logger.info(f"Pass 3 complete: {len(components_files)} files generated")

        # Combine all files into final response format
        self.logger.info(f"Multi-pass frontend generation complete: {len(all_files)} total files")

        return self._format_multipass_response(all_files, documentation, None)

    def _build_frontend_context(self, kb_contexts: dict[str, list[str]]) -> str:
        """Build comprehensive context for frontend generation."""
        dependencies_parts = []

        # UI context
        ui_context = self.format_context_for_prompt(
            kb_contexts.get("ui_context", []) + kb_contexts.get("form_definitions", []),
            max_contexts=25,
        )
        if ui_context and ui_context != "No additional context available.":
            dependencies_parts.append(f"=== UI SCREENS & COMPONENTS ===\n{ui_context}")

        # Data model context
        data_model = self.format_context_for_prompt(
            kb_contexts.get("data_model", []) + kb_contexts.get("all_classes", []), max_contexts=25
        )
        if data_model and data_model != "No additional context available.":
            dependencies_parts.append(f"=== DATA MODELS & TYPES ===\n{data_model}")

        # Form docs context
        form_docs = self.format_context_for_prompt(
            kb_contexts.get("form_docs", []) + kb_contexts.get("all_docs", []), max_contexts=25
        )
        if form_docs and form_docs != "No additional context available.":
            dependencies_parts.append(f"=== FORM DOCUMENTATION & REQUIREMENTS ===\n{form_docs}")

        # Business logic for validations
        business_logic = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("method_implementations", []),
            max_contexts=25,
        )
        if business_logic and business_logic != "No additional context available.":
            dependencies_parts.append(f"=== BUSINESS LOGIC & VALIDATIONS ===\n{business_logic}")

        return "\n\n".join(dependencies_parts) if dependencies_parts else "No additional context."

    def _build_frontend_scaffold_prompt(
        self, context: AgentContext, json_spec: str, dependencies_context: str
    ) -> str:
        """Build prompt for React project scaffold - valid runnable app root."""
        return f"""You are creating a React + TypeScript + Vite project for "{context.form_name}". Generate ONLY the project scaffold (root config and entry files).

MANDATORY: You MUST output each of these files. Paths are relative to the project root.

Generate these files (paths relative to project root):

package.json          # name, scripts (dev, build, preview), dependencies: react, react-dom, react-router-dom, @tanstack/react-query, axios, zod, typescript, vite
index.html            # Vite entry: <script type="module" src="/src/main.tsx"></script>
vite.config.ts        # defineConfig, react(), resolve alias @/
tsconfig.json         # compilerOptions for React + strict
tsconfig.node.json    # for Vite config
public/
  index.html          # optional minimal HTML if needed; or use root index.html only
src/
  main.tsx            # createRoot, BrowserRouter, QueryClientProvider, App
  App.tsx             # Routes with placeholder routes (e.g. /, /fleet-chapters)
  vite-env.d.ts       # /// <reference types="vite/client" />

REQUIREMENTS:
1. package.json: "name": "{context.form_name}-frontend", scripts dev/build/preview, all deps with versions
2. src/main.tsx: React 18 createRoot, wrap with QueryClientProvider and BrowserRouter, render <App />
3. src/App.tsx: Basic layout and <Routes><Route path="/" element=... /></Routes>
4. All paths in your output MUST be relative to project root: package.json, index.html, src/main.tsx, etc. (no leading slash, no ..)

Output EACH file with path relative to project root:
```json:package.json
{{ ... }}
```
```html:index.html
<!DOCTYPE html>...
```
```typescript:vite.config.ts
...
```
```typescript:src/main.tsx
...
```
```tsx:src/App.tsx
...
```
etc."""

    def _build_frontend_types_prompt(
        self, context: AgentContext, json_spec: str, swagger_str: str, dependencies_context: str
    ) -> str:
        """Build prompt for Types & Schemas generation."""
        return f"""You are migrating "{context.form_name}" to React TypeScript. Generate TYPES & SCHEMAS only.

=== JSON SPECIFICATION ===
{json_spec}

=== BACKEND API (Swagger) ===
{swagger_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files. Paths MUST be relative to the React project root (e.g. src/types/..., no leading / or ..):

src/
├── types/
│   ├── index.ts                  # Export all types
│   └── [entity].ts               # One file per entity + api.ts
└── schemas/
    ├── index.ts                  # Export all schemas
    └── [entity].schema.ts        # Zod schemas per entity

REQUIREMENTS:
1. TypeScript interfaces for ALL entities from backend; match field names exactly
2. Zod schemas for form validation
3. Paths in code blocks: src/types/index.ts, src/types/fleet.ts, etc. (relative to project root)

Output each file:
```typescript:src/types/index.ts
// content
```
```typescript:src/types/fleet.ts
// content
```
etc."""

    def _build_frontend_hooks_prompt(
        self, context: AgentContext, json_spec: str, swagger_str: str, dependencies_context: str
    ) -> str:
        """Build prompt for API Hooks generation."""
        return f"""You are migrating "{context.form_name}" to React TypeScript. Generate API HOOKS only.

=== JSON SPECIFICATION ===
{json_spec}

=== BACKEND API (Swagger) ===
{swagger_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files. Paths MUST be relative to project root (e.g. src/hooks/api/...):

src/
├── hooks/api/
│   ├── index.ts
│   └── use[Entity].ts            # One hook file per entity/endpoint
├── lib/
│   └── api.ts                    # Axios/fetch base URL and client
└── services/api/
    └── [entity]Service.ts        # API calls per entity

REQUIREMENTS:
1. TanStack Query: useQuery for GET, useMutation for POST/PUT/DELETE
2. One hook file per entity matching Swagger endpoints
3. Paths: src/hooks/api/useFleets.ts, src/lib/api.ts, etc. (relative to project root)

Output each file:
```typescript:src/lib/api.ts
// content
```
```typescript:src/hooks/api/useFleets.ts
// content
```
etc."""

    def _build_frontend_components_prompt(
        self,
        context: AgentContext,
        json_spec: str,
        swagger_str: str,
        dependencies_context: str,
        types_files: list[dict[str, str]],
    ) -> str:
        """Build prompt for Components generation."""
        return f"""You are migrating "{context.form_name}" to React TypeScript. Generate ALL COMPONENTS.

MANDATORY: Paths MUST be relative to the React project root (e.g. src/components/..., src/pages/...). No leading slash, no "..". This ensures the app is written inside the correct project folder.

=== JSON SPECIFICATION ===
{json_spec}

=== BACKEND API (Swagger) ===
{swagger_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files. Structure (all paths relative to project root):

src/
├── components/
│   ├── ui/                       # Button, Card, Form, Input, Select, Table, Dialog
│   ├── [feature]/                # One folder per entity/feature
│   │   ├── [Feature]Screen/
│   │   │   ├── index.tsx
│   │   │   ├── [Feature]Form.tsx
│   │   │   └── [Feature]Table.tsx
│   └── common/
│       └── ConfirmationDialog.tsx
├── pages/
│   ├── index.tsx                 # Home
│   └── [feature]/
│       ├── index.tsx             # List
│       └── [id].tsx              # Detail
└── App.tsx                       # Update with Routes for all screens

REQUIREMENTS:
1. One screen/folder per entity from backend (FleetChapters, Chapter, etc.)
2. Forms with react-hook-form + zodResolver; TanStack Query for data
3. Paths in code blocks: src/components/fleet/FleetScreen/index.tsx, src/pages/fleet-chapters/index.tsx, etc.
4. Update src/App.tsx with <Route path="/fleet-chapters" element=... /> for each feature

Output EACH file with path relative to project root:
```tsx:src/components/fleet/FleetScreen/index.tsx
// content
```
```tsx:src/pages/fleet-chapters/index.tsx
// content
```
etc."""
