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
    parse_llm_code_response,
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

            # 6. Create Directory Structures and Write Files
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

                # 7. Create Zip Archives
                output_path = Path(output_dir)
                ensure_directory(output_path)

                backend_zip_path = output_path / f"{context.form_name}_backend.zip"
                frontend_zip_path = output_path / f"{context.form_name}_frontend.zip"

                if backend_files:
                    create_zip_archive(backend_dir, backend_zip_path)
                if frontend_files:
                    create_zip_archive(frontend_dir, frontend_zip_path)

                # 8. Create Result
                result = CodeMigrationResult(
                    form_name=context.form_name,
                    backend_files=backend_files,
                    frontend_files=frontend_files,
                    backend_zip_path=str(backend_zip_path),
                    frontend_zip_path=str(frontend_zip_path),
                    documentation=f"{backend_doc}\n\n{frontend_doc}".strip(),
                    swagger_json=swagger_json,
                )

                self.logger.info(
                    "Code migration complete",
                    form_name=context.form_name,
                    backend_files=len(backend_files),
                    frontend_files=len(frontend_files),
                    backend_zip=str(backend_zip_path),
                    frontend_zip=str(frontend_zip_path),
                    duration_ms=timer.elapsed_ms(),
                )

                return self.create_success_result(result, timer)

        except Exception as e:
            self.logger.error("Code migration failed", error=str(e), form_name=context.form_name)
            return self.create_error_result(e, timer)

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
        """Generate .NET backend code using LLM with FULL knowledge base context."""
        # Build COMPREHENSIVE dependencies context from ALL sources
        dependencies_parts = []

        # Add ALL data model context (increased limits)
        data_model = self.format_context_for_prompt(
            kb_contexts.get("data_model", [])
            + kb_contexts.get("database", [])
            + kb_contexts.get("all_classes", []),
            max_contexts=25,
        )
        if data_model and data_model != "No additional context available.":
            dependencies_parts.append(f"=== DATA MODELS & DATABASE SCHEMA ===\n{data_model}")

        # Add ALL business logic context (CRITICAL for migration)
        business_logic = self.format_context_for_prompt(
            kb_contexts.get("business_logic", [])
            + kb_contexts.get("method_implementations", [])
            + kb_contexts.get("all_methods", []),
            max_contexts=30,
        )
        if business_logic and business_logic != "No additional context available.":
            dependencies_parts.append(f"=== BUSINESS LOGIC & METHODS ===\n{business_logic}")

        # Add ALL form docs context
        form_docs = self.format_context_for_prompt(
            kb_contexts.get("form_docs", []) + kb_contexts.get("all_docs", []), max_contexts=20
        )
        if form_docs and form_docs != "No additional context available.":
            dependencies_parts.append(f"=== FORM DOCUMENTATION & REQUIREMENTS ===\n{form_docs}")

        # Add ALL SQL files context
        sql_context = self.format_context_for_prompt(
            kb_contexts.get("sql_files", []), max_contexts=15
        )
        if sql_context and sql_context != "No additional context available.":
            dependencies_parts.append(f"=== SQL SCHEMAS & QUERIES ===\n{sql_context}")

        # Add source code context
        source_code = self.format_context_for_prompt(
            kb_contexts.get("source_code", []) + kb_contexts.get("all_code", []), max_contexts=20
        )
        if source_code and source_code != "No additional context available.":
            dependencies_parts.append(f"=== LEGACY SOURCE CODE ===\n{source_code}")

        dependencies_context = (
            "\n\n".join(dependencies_parts) if dependencies_parts else "No additional context."
        )

        prompt = CodeMigrationPrompts.backend_conversion_prompt(
            json_str=json_spec, dependencies=dependencies_context
        )

        response = await self.invoke_llm(context, prompt)
        return response

    async def _generate_frontend_code(
        self,
        context: AgentContext,
        json_spec: str,
        swagger_json: dict[str, Any] | None,
        kb_contexts: dict[str, list[str]],
    ) -> str:
        """Generate React frontend code using LLM with FULL knowledge base context."""
        # Build COMPREHENSIVE dependencies context from ALL sources
        dependencies_parts = []

        # Add ALL UI context
        ui_context = self.format_context_for_prompt(
            kb_contexts.get("ui_context", []) + kb_contexts.get("form_definitions", []),
            max_contexts=20,
        )
        if ui_context and ui_context != "No additional context available.":
            dependencies_parts.append(f"=== UI SCREENS & COMPONENTS ===\n{ui_context}")

        # Add ALL data model context
        data_model = self.format_context_for_prompt(
            kb_contexts.get("data_model", []) + kb_contexts.get("all_classes", []), max_contexts=20
        )
        if data_model and data_model != "No additional context available.":
            dependencies_parts.append(f"=== DATA MODELS & TYPES ===\n{data_model}")

        # Add ALL form docs context
        form_docs = self.format_context_for_prompt(
            kb_contexts.get("form_docs", []) + kb_contexts.get("all_docs", []), max_contexts=20
        )
        if form_docs and form_docs != "No additional context available.":
            dependencies_parts.append(f"=== FORM DOCUMENTATION & REQUIREMENTS ===\n{form_docs}")

        # Add ALL business logic for validations
        business_logic = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("method_implementations", []),
            max_contexts=20,
        )
        if business_logic and business_logic != "No additional context available.":
            dependencies_parts.append(f"=== BUSINESS LOGIC & VALIDATIONS ===\n{business_logic}")

        dependencies_context = (
            "\n\n".join(dependencies_parts) if dependencies_parts else "No additional context."
        )

        swagger_str = json.dumps(swagger_json, indent=2) if swagger_json else "{}"

        prompt = CodeMigrationPrompts.frontend_conversion_prompt(
            json_str=json_spec, swagger_json=swagger_str, dependencies=dependencies_context
        )

        response = await self.invoke_llm(context, prompt)
        return response
