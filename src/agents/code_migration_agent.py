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
        """Retrieve comprehensive context from knowledge base."""
        contexts = {}

        queries = {
            "data_model": "data model entity field table column relationship schema primary key foreign key",
            "api_specs": "API endpoint controller service method request response HTTP GET POST PUT DELETE",
            "business_logic": "business logic validation rule calculation workflow process condition",
            "ui_flows": "UI form field component screen user interface input validation",
            "validation": "validation rule required constraint check error message",
            "database": "database table entity field column relationship",
        }

        for key, query in queries.items():
            try:
                # For database queries, use doc_type="database" to get database analysis results
                doc_type = "database" if key == "database" else "code"
                results = self.retrieve_context(form_name, query, limit=10, doc_type=doc_type)
                contexts[key] = results
                self.logger.debug(f"Retrieved {len(results)} contexts for {key}")
            except Exception as e:
                self.logger.warning(f"Failed to retrieve context for {key}: {e}")
                contexts[key] = []

        return contexts

    async def _generate_backend_json_spec(
        self, context: AgentContext, kb_contexts: dict[str, list[str]]
    ) -> str:
        """Generate JSON specification for backend from KB context."""
        # Format context for prompt
        data_context = self.format_context_for_prompt(
            kb_contexts.get("data_model", []) + kb_contexts.get("database", []), max_contexts=15
        )
        api_context = self.format_context_for_prompt(
            kb_contexts.get("api_specs", []), max_contexts=10
        )
        business_context = self.format_context_for_prompt(
            kb_contexts.get("business_logic", []) + kb_contexts.get("validation", []),
            max_contexts=10,
        )

        prompt = f"""Generate a complete JSON specification for the .NET backend migration of "{context.form_name}".

KNOWLEDGE BASE CONTEXT:
{data_context}

API SPECIFICATIONS:
{api_context}

BUSINESS LOGIC:
{business_context}

Create a JSON specification that includes:
1. **Entities**: All data entities with fields, types, constraints, relationships
2. **API Endpoints**: All endpoints with HTTP methods, paths, request/response structures
3. **Validation Rules**: All validation rules with conditions and error messages
4. **Business Logic**: Key business rules and calculations

Return ONLY valid JSON, no markdown formatting or explanations."""

        response = await self.invoke_llm(context, prompt)

        # Try to extract JSON from response
        # Look for JSON in code blocks
        json_pattern = r"```(?:json)?\s*(\{.*?\})\s*```"
        json_match = re.search(json_pattern, response, re.DOTALL)

        if json_match:
            return json_match.group(1)

        # Try to find JSON object directly
        try:
            # Find first { and last }
            start = response.find("{")
            end = response.rfind("}") + 1
            if start >= 0 and end > start:
                json_str = response[start:end]
                # Validate it's JSON
                json.loads(json_str)
                return json_str
        except Exception:
            pass

        # Return as-is if no JSON found (let LLM handle it)
        return response

    async def _generate_frontend_json_spec(
        self,
        context: AgentContext,
        kb_contexts: dict[str, list[str]],
        swagger_json: dict[str, Any] | None,
    ) -> str:
        """Generate JSON specification for frontend from KB context."""
        ui_context = self.format_context_for_prompt(
            kb_contexts.get("ui_flows", []) + kb_contexts.get("validation", []), max_contexts=15
        )
        data_context = self.format_context_for_prompt(
            kb_contexts.get("data_model", []), max_contexts=10
        )

        swagger_info = ""
        if swagger_json:
            swagger_info = f"\n\nSWAGGER/OPENAPI SPEC:\n{json.dumps(swagger_json, indent=2)}"

        prompt = f"""Generate a complete JSON specification for the React frontend migration of "{context.form_name}".

KNOWLEDGE BASE CONTEXT:
{ui_context}

DATA MODEL:
{data_context}
{swagger_info}

Create a JSON specification that includes:
1. **Forms**: All forms with fields, types, validation rules
2. **UI Components**: Component structure and layout
3. **Navigation**: Routes and navigation flows
4. **API Integration**: Endpoints to integrate with

Return ONLY valid JSON, no markdown formatting or explanations."""

        response = await self.invoke_llm(context, prompt)

        # Try to extract JSON from response (same logic as backend)
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
        """Generate .NET backend code using LLM."""
        # Format dependencies from context
        dependencies_context = self.format_context_for_prompt(
            kb_contexts.get("data_model", []) + kb_contexts.get("api_specs", []), max_contexts=5
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
        """Generate React frontend code using LLM."""
        # Format dependencies from context
        dependencies_context = self.format_context_for_prompt(
            kb_contexts.get("ui_flows", []) + kb_contexts.get("data_model", []), max_contexts=5
        )

        swagger_str = json.dumps(swagger_json, indent=2) if swagger_json else "{}"

        prompt = CodeMigrationPrompts.frontend_conversion_prompt(
            json_str=json_spec, swagger_json=swagger_str, dependencies=dependencies_context
        )

        response = await self.invoke_llm(context, prompt)
        return response
