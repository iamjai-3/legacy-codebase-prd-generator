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
        Generate .NET backend code using MULTI-PASS approach.

        Pass 1: Data Layer (Entities, Configurations, DbContext, Repositories)
        Pass 2: Business Layer (Services, Validators, DTOs)
        Pass 3: API Layer (Controllers, Middleware, Program.cs)

        This ensures complete generation of all layers.
        """
        self.logger.info("Starting multi-pass backend generation")

        # Build comprehensive context for all passes
        dependencies_context = self._build_backend_context(kb_contexts)

        all_files = []

        # ============ PASS 1: DATA LAYER ============
        self.logger.info("Pass 1: Generating Data Layer (Entities, Configurations, DbContext)")
        data_layer_prompt = self._build_data_layer_prompt(context, json_spec, dependencies_context)
        data_layer_response = await self.invoke_llm(context, data_layer_prompt)
        data_layer_files, _, _ = parse_llm_code_response(data_layer_response)
        all_files.extend(data_layer_files)
        self.logger.info(f"Pass 1 complete: {len(data_layer_files)} files generated")

        # ============ PASS 2: BUSINESS LAYER ============
        self.logger.info("Pass 2: Generating Business Layer (Services, Validators, DTOs)")
        business_layer_prompt = self._build_business_layer_prompt(
            context, json_spec, dependencies_context, data_layer_files
        )
        business_layer_response = await self.invoke_llm(context, business_layer_prompt)
        business_layer_files, _, _ = parse_llm_code_response(business_layer_response)
        all_files.extend(business_layer_files)
        self.logger.info(f"Pass 2 complete: {len(business_layer_files)} files generated")

        # ============ PASS 3: API LAYER ============
        self.logger.info("Pass 3: Generating API Layer (Controllers, Program.cs)")
        api_layer_prompt = self._build_api_layer_prompt(
            context, json_spec, dependencies_context, data_layer_files, business_layer_files
        )
        api_layer_response = await self.invoke_llm(context, api_layer_prompt)
        api_layer_files, documentation, swagger_json = parse_llm_code_response(api_layer_response)
        all_files.extend(api_layer_files)
        self.logger.info(f"Pass 3 complete: {len(api_layer_files)} files generated")

        # Combine all files into final response format
        self.logger.info(f"Multi-pass backend generation complete: {len(all_files)} total files")

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

    def _build_data_layer_prompt(
        self, context: AgentContext, json_spec: str, dependencies_context: str
    ) -> str:
        """Build prompt for Data Layer generation."""
        project_name = self._get_project_name(context.form_name)

        return f"""You are migrating "{context.form_name}" to .NET 8. Generate the DATA LAYER only.

=== JSON SPECIFICATION ===
{json_spec}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files for the Data Layer with this EXACT structure:

{project_name}.Data/
├── Entities/
│   └── [Entity].cs              # One file per entity with ALL fields
├── Configurations/
│   └── [Entity]Configuration.cs # EF Core configurations with constraints
├── Context/
│   └── {project_name}DbContext.cs  # DbContext with all DbSets
└── Repositories/
    ├── Interfaces/
    │   └── I[Entity]Repository.cs
    └── Implementations/
        └── [Entity]Repository.cs

REQUIREMENTS:
1. Extract ALL entities from the legacy code and JSON spec
2. Include ALL fields with correct types (string, int, decimal, DateTime, etc.)
3. Add proper data annotations ([Key], [MaxLength], [Required], [Column])
4. Configure relationships (foreign keys, navigation properties)
5. Repositories must have async CRUD methods

Output each file with:
```csharp:{project_name}.Data/[folder]/[filename].cs
// file content
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

        return f"""You are migrating "{context.form_name}" to .NET 8. Generate the BUSINESS LAYER only.

=== JSON SPECIFICATION ===
{json_spec}

=== ENTITIES CREATED IN DATA LAYER ===
{entities_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files for the Business Layer with this EXACT structure:

{project_name}.Business/
├── DTOs/
│   └── [Entity]/
│       ├── [Entity]ReadDto.cs
│       ├── [Entity]CreateDto.cs
│       └── [Entity]UpdateDto.cs
├── Services/
│   ├── Interfaces/
│   │   └── I[Entity]Service.cs
│   └── Implementations/
│       └── [Entity]Service.cs
├── Validators/
│   └── [Entity]Validator.cs
└── Mappings/
    └── MappingProfile.cs         # AutoMapper profile

REQUIREMENTS:
1. Create DTOs for ALL entities (Read, Create, Update variants)
2. Services must implement ALL business logic from legacy code:
   - GetAll, GetById, Create, Update, Delete
   - Custom methods (SaveChanges, ValidateExists, etc.)
3. Include ALL validation rules from legacy code
4. Services must use repositories via dependency injection
5. Map ALL legacy methods like doUsingSave(), doesExist() to service methods

CRITICAL: Extract ALL business logic from the knowledge base. Every legacy method must have a corresponding service method.

Output each file with:
```csharp:{project_name}.Business/[folder]/[filename].cs
// file content
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

=== JSON SPECIFICATION ===
{json_spec}

=== SERVICES CREATED IN BUSINESS LAYER ===
{services_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files for the API Layer with this EXACT structure:

{project_name}.API/
├── Controllers/
│   └── [Entity]Controller.cs     # One controller per entity
├── Program.cs                    # Full startup with DI
├── appsettings.json
└── appsettings.Development.json

{project_name}.Common/
├── Exceptions/
│   └── NotFoundException.cs
└── Models/
    ├── ApiResponse.cs
    └── PagedResult.cs

REQUIREMENTS:
1. Controllers must have ALL endpoints from functional requirements:
   - GET /api/[entity] - Get all
   - GET /api/[entity]/{{id}} - Get by ID
   - POST /api/[entity] - Create
   - PUT /api/[entity]/{{id}} - Update
   - DELETE /api/[entity]/{{id}} - Delete
   - Custom endpoints for legacy actions (validate, save-changes, etc.)
2. Use [ApiController] and [Route("api/[controller]")]
3. Include proper error handling with try-catch
4. Return ApiResponse<T> for consistent responses
5. Program.cs must register ALL services, repositories, DbContext
6. Include Swagger/OpenAPI configuration

Also generate a Swagger/OpenAPI specification between:
===SWAGGER_START===
{{json swagger spec}}
===SWAGGER_END===

Output each file with:
```csharp:{project_name}.API/[folder]/[filename].cs
// file content
```"""

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
        self.logger.info("Starting multi-pass frontend generation")

        # Build comprehensive context for all passes
        dependencies_context = self._build_frontend_context(kb_contexts)
        swagger_str = json.dumps(swagger_json, indent=2) if swagger_json else "{}"

        all_files = []

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

Generate COMPLETE files for Types & Schemas with this EXACT structure:

src/
├── types/
│   ├── index.ts                  # Export all types
│   ├── fleet.ts                  # Fleet-related types
│   ├── chapter.ts                # Chapter-related types
│   └── api.ts                    # API response types
└── schemas/
    ├── index.ts                  # Export all schemas
    ├── fleet.schema.ts           # Zod schemas for fleet
    └── chapter.schema.ts         # Zod schemas for chapter

REQUIREMENTS:
1. Create TypeScript interfaces for ALL entities from backend
2. Match field names EXACTLY with backend DTOs
3. Include all field types (string, number, boolean, Date, etc.)
4. Create Zod schemas for form validation
5. Export everything properly for use in components

Output each file with:
```typescript:src/[folder]/[filename].ts
// file content
```"""

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

Generate COMPLETE files for API Hooks with this EXACT structure:

src/
├── hooks/
│   └── api/
│       ├── index.ts              # Export all hooks
│       ├── useFleets.ts          # Fleet CRUD hooks
│       ├── useChapters.ts        # Chapter CRUD hooks
│       └── useChapterAlertRates.ts  # Alert rate hooks
├── lib/
│   └── api.ts                    # Axios instance configuration
└── services/
    └── api/
        ├── fleetService.ts       # Fleet API calls
        ├── chapterService.ts     # Chapter API calls
        └── chapterAlertRateService.ts  # Alert rate API calls

REQUIREMENTS:
1. Use TanStack Query (React Query) for data fetching
2. Create hooks for ALL CRUD operations:
   - useQuery for GET operations
   - useMutation for POST/PUT/DELETE
3. Include proper TypeScript types
4. Handle loading, error, and success states
5. Match ALL endpoints from the Swagger spec

Output each file with:
```typescript:src/[folder]/[filename].ts
// file content
```"""

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

=== JSON SPECIFICATION ===
{json_spec}

=== BACKEND API (Swagger) ===
{swagger_str}

=== KNOWLEDGE BASE CONTEXT ===
{dependencies_context}

Generate COMPLETE files for ALL screens from the PRD/knowledge base with this structure:

src/
├── components/
│   ├── ui/                       # shadcn/ui components (assume installed)
│   ├── [feature]/                # One folder per major feature/entity
│   │   ├── [Feature]SelectionScreen/
│   │   │   ├── index.tsx
│   │   │   ├── [Feature]SelectionForm.tsx
│   │   │   └── [Feature]SelectionList.tsx
│   │   └── [Feature]ManagementScreen/
│   │       ├── index.tsx
│   │       ├── [Feature]ManagementForm.tsx
│   │       └── [Feature]ManagementTable.tsx
│   └── common/
│       ├── DataChangeWarningDialog.tsx
│       └── ConfirmationDialog.tsx
├── pages/
│   ├── index.tsx                 # Home/Dashboard
│   └── [feature]/
│       ├── index.tsx             # Feature list
│       └── [id].tsx              # Feature detail
└── App.tsx                       # Main app with routing

REQUIREMENTS:
1. Create ALL screens mentioned in the PRD and knowledge base:
   - Selection screens for each entity with dropdowns
   - Management screens with forms and tables for CRUD
   - Warning/confirmation dialogs
   - Search screens if mentioned in PRD
2. Use shadcn/ui components (Button, Card, Form, Input, Select, Table, Dialog)
3. Use react-hook-form with zodResolver for forms
4. Use TanStack Query hooks for data fetching
5. Include proper loading and error states
6. Match ALL UI elements from legacy screenshots in knowledge base
7. Generate screens for ALL entities/features from the backend API

IMPORTANT: Extract screen names and features from the knowledge base context above.
Do NOT hardcode - use whatever entities and features are described in the legacy code and PRD.

Output each file with:
```tsx:src/[folder]/[filename].tsx
// file content
```"""
