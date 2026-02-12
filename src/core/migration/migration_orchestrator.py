"""
Migration Orchestrator Agent.

The main agentic agent that orchestrates the entire migration workflow.
Coordinates between database, UI, and code generation agents to produce
a complete modern codebase from legacy code and documentation.
"""

from pathlib import Path

from src.core.agentic.agentic_base import AgenticAgent, AgenticConfig
from src.core.agentic.tool_registry import ToolParameter
from src.prompts.loader import load_prompt
from src.tools import (
    code_tools,
    database_knowledge_tool,
    database_tools,
    file_tools,
    minio_tools,
)
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class MigrationOrchestrator(AgenticAgent):
    """
    Orchestrates the complete migration workflow.

    This agent coordinates the migration from legacy Java codebase
    to modern .NET backend and React frontend.
    """

    def __init__(
        self,
        form_name: str,
        output_dir: Path,
        config: AgenticConfig | None = None,
    ) -> None:
        """
        Initialize the migration orchestrator.

        Args:
            form_name: Name of the form to migrate (e.g., 'LE11')
            output_dir: Output directory for generated code
            config: Optional agent configuration
        """
        self.form_name = form_name
        self.output_dir = Path(output_dir)

        # Update config with output directory as working directory
        if config is None:
            config = AgenticConfig()
        config.working_directory = self.output_dir

        super().__init__(
            name="MigrationOrchestrator",
            system_prompt=load_prompt("migration/system_prompt"),
            config=config,
        )

        self.logger.info(
            "Initialized MigrationOrchestrator",
            form_name=form_name,
            output_dir=str(output_dir),
        )

    def _register_default_tools(self) -> None:
        """Register all tools needed for migration."""
        # File tools
        self.tool_registry.register(
            name="get_files_info",
            description="List files and directories with metadata. Use to explore the codebase structure.",
            parameters=[
                ToolParameter(
                    name="directory",
                    type="string",
                    description="Directory to list (relative to output directory). Use '.' for root.",
                    required=False,
                    default=".",
                ),
            ],
            function=lambda **kwargs: file_tools.get_files_info(
                str(self.output_dir), kwargs.get("directory", ".")
            ),
        )

        self.tool_registry.register(
            name="get_file_content",
            description="Read the contents of a file (path relative to output directory).",
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description="Relative path to the file (e.g. 'backend/LE11.Data/Entities/Foo.cs')",
                    required=True,
                ),
            ],
            function=lambda **kwargs: file_tools.get_file_content(
                str(self.output_dir), self._normalize_write_path(kwargs["filepath"])
            ),
        )

        self.tool_registry.register(
            name="write_file",
            description=(
                "Write content to a file. Creates parent directories if needed. "
                "The filepath MUST be relative to the output directory "
                "(e.g. 'backend/LE11.Data/Entities/Foo.cs', NOT 'output/backend/...'). "
                "Do NOT prefix with 'output/' or 'output/agentic/'."
            ),
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description=(
                        "Relative path within the output directory "
                        "(e.g. 'backend/LE11.Data/Entities/SomeEntity.cs'). "
                        "Do NOT include 'output/' prefix."
                    ),
                    required=True,
                ),
                ToolParameter(
                    name="content",
                    type="string",
                    description="Content to write to the file",
                    required=True,
                ),
            ],
            function=lambda **kwargs: file_tools.write_file(
                str(self.output_dir),
                self._normalize_write_path(kwargs["filepath"]),
                kwargs["content"],
            ),
        )

        self.tool_registry.register(
            name="find_files",
            description="Find files matching a pattern.",
            parameters=[
                ToolParameter(
                    name="pattern",
                    type="string",
                    description="Glob pattern to match (e.g., '**/*.cs')",
                    required=True,
                ),
                ToolParameter(
                    name="directory",
                    type="string",
                    description="Directory to search in",
                    required=False,
                    default=".",
                ),
            ],
            function=lambda **kwargs: file_tools.find_files(
                str(self.output_dir),
                kwargs["pattern"],
                kwargs.get("directory", "."),
            ),
        )

        # Code analysis tools
        self.tool_registry.register(
            name="search_codebase",
            description="Search the knowledge base for relevant code, documentation, or business logic.",
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Natural language search query",
                    required=True,
                ),
                ToolParameter(
                    name="limit",
                    type="integer",
                    description="Maximum number of results",
                    required=False,
                    default=10,
                ),
            ],
            function=lambda **kwargs: code_tools.search_codebase(
                self.form_name,
                kwargs["query"],
                kwargs.get("limit", 10),
            ),
        )

        self.tool_registry.register(
            name="get_code_context",
            description="Get relevant code context for a specific topic.",
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Topic to get context for",
                    required=True,
                ),
                ToolParameter(
                    name="doc_type",
                    type="string",
                    description="Type filter: code, business_logic, database, etc.",
                    required=False,
                ),
                ToolParameter(
                    name="limit",
                    type="integer",
                    description="Max number of context chunks (default 3 to reduce tokens)",
                    required=False,
                    default=3,
                ),
            ],
            function=lambda **kwargs: code_tools.get_code_context(
                self.form_name,
                kwargs["query"],
                kwargs.get("doc_type"),
                kwargs.get("limit", 3),
            ),
        )

        # Database tools
        self.tool_registry.register(
            name="get_database_schema",
            description="Get database schema information for the form.",
            parameters=[],
            function=lambda **kwargs: database_tools.get_database_schema(self.form_name),
        )

        self.tool_registry.register(
            name="get_table_mappings",
            description="Get table relationships and mappings.",
            parameters=[
                ToolParameter(
                    name="table_name",
                    type="string",
                    description="Specific table to get mappings for",
                    required=False,
                ),
            ],
            function=lambda **kwargs: database_tools.get_table_mappings(
                self.form_name,
                kwargs.get("table_name"),
            ),
        )

        self.tool_registry.register(
            name="get_business_logic",
            description="Get business logic related to a topic.",
            parameters=[
                ToolParameter(
                    name="topic",
                    type="string",
                    description="Topic to get business logic for",
                    required=True,
                ),
            ],
            function=lambda **kwargs: database_tools.get_business_logic(
                self.form_name,
                kwargs["topic"],
            ),
        )

        # MinIO tools
        self.tool_registry.register(
            name="get_migration_playbook",
            description="Get the detailed migration playbook (knowledge-first steps and rules).",
            parameters=[],
            function=lambda **kwargs: load_prompt("migration/playbook"),
        )

        self.tool_registry.register(
            name="get_form_docs",
            description="Get all form documentation from MinIO.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_form_docs(self.form_name),
        )

        self.tool_registry.register(
            name="get_dependencies",
            description="Get the list of files that belong to this form.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_dependencies(self.form_name),
        )

        self.tool_registry.register(
            name="list_screenshots",
            description="List available UI screenshots for the form.",
            parameters=[],
            function=lambda **kwargs: minio_tools.list_screenshots(self.form_name),
        )

        self.tool_registry.register(
            name="get_db_prd",
            description="Get global database PRD documentation.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_db_prd(),
        )

        self.tool_registry.register(
            name="get_conversion_prompt",
            description="Get the conversion prompt template for backend or frontend.",
            parameters=[
                ToolParameter(
                    name="prompt_type",
                    type="string",
                    description="Type: 'backend' or 'frontend'",
                    required=True,
                    enum=["backend", "frontend"],
                ),
            ],
            function=lambda **kwargs: minio_tools.get_conversion_prompt(kwargs["prompt_type"]),
        )

        # NEW: Enhanced MinIO knowledge tools
        self.tool_registry.register(
            name="get_all_form_knowledge",
            description="Get aggregated knowledge for the form: docs, dependencies, screenshots, DB schema.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_all_form_knowledge(self.form_name),
        )

        self.tool_registry.register(
            name="list_export_templates",
            description="List all available BE/FE export code templates.",
            parameters=[],
            function=lambda **kwargs: minio_tools.list_export_templates(),
        )

        self.tool_registry.register(
            name="get_export_template",
            description="Get a specific export template from EXPORT_CODEBASE_PRD.",
            parameters=[
                ToolParameter(
                    name="template_type",
                    type="string",
                    description="'BE' for backend or 'FE' for frontend",
                    required=True,
                    enum=["BE", "FE"],
                ),
                ToolParameter(
                    name="template_name",
                    type="string",
                    description="Template filename or 'list' to see available templates",
                    required=True,
                ),
            ],
            function=lambda **kwargs: minio_tools.get_export_template(
                kwargs["template_type"],
                kwargs["template_name"],
            ),
        )

        self.tool_registry.register(
            name="get_ui_flow_docs",
            description="Get UI flow documentation for understanding user interactions.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_ui_flow_docs(self.form_name),
        )

        # NEW: Database knowledge tools
        self.tool_registry.register(
            name="search_legacy_schema",
            description="Search for legacy (Oases) table schema and relationships.",
            parameters=[
                ToolParameter(
                    name="table_name",
                    type="string",
                    description="Table name to search for",
                    required=True,
                ),
            ],
            function=lambda **kwargs: database_knowledge_tool.search_legacy_schema(
                kwargs["table_name"]
            ),
        )

        self.tool_registry.register(
            name="search_target_schema",
            description="Search for target (Lumina) table schema and relationships.",
            parameters=[
                ToolParameter(
                    name="table_name",
                    type="string",
                    description="Table name to search for",
                    required=True,
                ),
            ],
            function=lambda **kwargs: database_knowledge_tool.search_target_schema(
                kwargs["table_name"]
            ),
        )

        self.tool_registry.register(
            name="get_oracle_to_postgres_mapping",
            description="Get Oracle to PostgreSQL data type mapping guide.",
            parameters=[],
            function=lambda **kwargs: database_knowledge_tool.get_oracle_to_postgres_mapping(),
        )

        self.tool_registry.register(
            name="get_highly_connected_tables",
            description="Get list of highly connected tables (20+ relationships) - critical for migration.",
            parameters=[],
            function=lambda **kwargs: database_knowledge_tool.get_highly_connected_tables(),
        )

        self.tool_registry.register(
            name="get_table_relationships",
            description="Get relationships for a specific table.",
            parameters=[
                ToolParameter(
                    name="table_name",
                    type="string",
                    description="Table name to get relationships for",
                    required=True,
                ),
            ],
            function=lambda **kwargs: database_knowledge_tool.get_table_relationships(
                kwargs["table_name"]
            ),
        )

    def _normalize_write_path(self, filepath: str) -> str:
        """
        Strip leading directory segments that duplicate the output directory.

        LLMs often include 'output/', 'output/agentic/', or 'agentic/' prefixes
        even though write_file already resolves relative to the output directory.
        This safety net strips those prefixes to avoid nested duplicates.
        """
        # Normalise to forward slashes and strip leading ./
        cleaned = filepath.replace("\\", "/").lstrip("./")

        # Build a list of prefixes that the LLM might incorrectly include.
        # E.g. for output_dir = "output/agentic" → try "output/agentic/", "output/", "agentic/"
        parts = str(self.output_dir).replace("\\", "/").strip("/").split("/")
        prefixes_to_strip: list[str] = []
        # full path prefix: "output/agentic/"
        if len(parts) > 1:
            prefixes_to_strip.append("/".join(parts) + "/")
        # each part individually: "output/", "agentic/"
        for part in parts:
            prefixes_to_strip.append(part + "/")

        # Strip the first matching prefix (only once)
        for prefix in prefixes_to_strip:
            if cleaned.lower().startswith(prefix.lower()):
                cleaned = cleaned[len(prefix) :]
                break

        return cleaned or filepath

    # Maximum number of auto-continuation rounds when the LLM stops early
    _MAX_CONTINUATIONS = 5

    async def migrate(self, prompt: str | None = None) -> str:
        """
        Run the migration process.

        Automatically continues the agent if it stops before generating
        a complete backend + frontend codebase.

        Args:
            prompt: Optional custom prompt to guide the migration

        Returns:
            Migration result summary
        """
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Create output structure
        (self.output_dir / "backend").mkdir(exist_ok=True)
        (self.output_dir / "frontend").mkdir(exist_ok=True)

        # Build the migration prompt
        if prompt:
            migration_prompt = prompt
        else:
            migration_prompt = load_prompt("migration/playbook")

        # --- Initial run ---
        result = await self.send_message(migration_prompt)

        # --- Auto-continuation if the LLM stopped early ---
        for continuation in range(self._MAX_CONTINUATIONS):
            if self._is_migration_complete():
                self.logger.info("Migration output looks complete.")
                break

            missing = self._describe_missing_output()
            self.logger.warning(
                "Migration incomplete after round %s. Missing: %s. Sending continuation.",
                continuation + 1,
                missing,
            )

            continuation_prompt = load_prompt("migration/continuation", missing=missing)
            result = await self.send_message(continuation_prompt)

        return result

    # ------------------------------------------------------------------
    # Completion detection helpers
    # ------------------------------------------------------------------

    def _is_migration_complete(self) -> bool:
        """
        Check whether both backend and frontend directories contain generated files.
        """
        return self._count_files("backend") > 0 and self._count_files("frontend") > 0

    def _count_files(self, subdir: str) -> int:
        """Count code files (non-hidden) in a subdirectory of the output."""
        target = self.output_dir / subdir
        if not target.exists():
            return 0
        return sum(1 for f in target.rglob("*") if f.is_file() and not f.name.startswith("."))

    def _describe_missing_output(self) -> str:
        """Return a human-readable description of what's missing."""
        parts: list[str] = []
        be_count = self._count_files("backend")
        fe_count = self._count_files("frontend")

        if be_count == 0:
            parts.append(
                "backend has NO files (need Entities, Repositories, Services, DTOs, Controllers)"
            )
        else:
            # Check for expected subdirectory patterns
            be_path = self.output_dir / "backend"
            has_services = any(be_path.rglob("*Service*"))
            has_controllers = any(be_path.rglob("*Controller*"))
            has_dtos = any(be_path.rglob("*Dto*")) or any(be_path.rglob("*DTO*"))
            if not has_services:
                parts.append("backend missing Services")
            if not has_controllers:
                parts.append("backend missing Controllers")
            if not has_dtos:
                parts.append("backend missing DTOs")

        if fe_count == 0:
            parts.append("frontend has NO files (need components, pages, services, types)")
        else:
            fe_path = self.output_dir / "frontend"
            has_components = any(fe_path.rglob("*.tsx"))
            has_types = any(fe_path.rglob("*.ts"))
            if not has_components:
                parts.append("frontend missing React components (.tsx)")
            if not has_types:
                parts.append("frontend missing TypeScript types (.ts)")

        return "; ".join(parts) if parts else "unknown gaps"
