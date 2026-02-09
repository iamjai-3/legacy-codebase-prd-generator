"""
Migration Orchestrator Agent.

The main agentic agent that orchestrates the entire migration workflow.
Coordinates between database, UI, and code generation agents to produce
a complete modern codebase from legacy code and documentation.
"""

from pathlib import Path

from src.core.agentic.agentic_base import AgenticAgent, AgenticConfig
from src.core.agentic.tool_registry import ToolParameter
from src.tools import (
    code_tools,
    database_knowledge_tool,
    database_tools,
    file_tools,
    minio_tools,
)
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


# System prompt for the migration orchestrator - Knowledge-First Approach
MIGRATION_SYSTEM_PROMPT = """You are an expert software migration specialist working like Antigravity IDE.
Your job is to migrate legacy Java codebases to modern .NET backend and React frontend applications.

## CRITICAL: Knowledge-First Approach
You MUST gather ALL knowledge before generating ANY code. This ensures 100% accuracy.

## Your Capabilities
You have access to tools to:
1. **Knowledge Retrieval** - Get complete form knowledge from MinIO
2. **Database Schema** - Access legacy/target schema mappings and Oracle→PostgreSQL mappings
3. **Export Templates** - Use exact output format templates for BE/FE code
4. **Search Codebase** - Find relevant legacy code and business logic
5. **Write Files** - Generate new code files in the output directory using `write_file`

## MANDATORY Migration Process (Execute in Order)

### Step 1: Gather ALL Knowledge First (REQUIRED)
1. `get_all_form_knowledge` - Get complete knowledge for the form
2. `list_export_templates` - See available BE/FE templates
3. `get_conversion_prompt("backend")` - Get .NET output format template
4. `get_conversion_prompt("frontend")` - Get React output format template
5. `get_oracle_to_postgres_mapping` - Understand data type mappings

### Step 2: Understand Database Schema
1. `get_database_schema` - Get form's database schema
2. `search_legacy_schema(table_name)` - Find legacy table relationships
3. `get_highly_connected_tables` - Identify critical tables

### Step 3: Extract Business Logic
1. `search_codebase` - Find legacy code implementing business rules
2. `get_code_context` - Get detailed code for validation, calculations
3. `get_business_logic` - Extract documented business rules

### Step 4: Generate Backend (.NET) FIRST
Using the conversion template format, call `write_file` for each file:
- Generate Entities matching DB schema (use Oracle→PostgreSQL mappings)
- Create Repositories with EF Core patterns
- Implement Services preserving ALL business logic
- Create Controllers with RESTful endpoints

### Step 5: Generate Frontend (React)
Using the conversion template format, call `write_file` for each file:
- Analyze UI screenshots with `list_screenshots`
- Generate React components matching legacy UI
- Implement form validation matching legacy rules
- Create API services to call backend

### Step 6: Verify Output
- Check all business logic preserved
- Verify entity-to-table mappings match schema
- Confirm UI matches screenshots

## Critical Rules
1. **ONLY GENERATE CODE FILES** - NO documentation files (no .md, README, MANIFEST, etc.)
2. **ALWAYS gather knowledge before generating code**
3. **Follow the exact output format from templates**
4. **100% Parity with legacy system behavior**
5. **Use Oracle→PostgreSQL type mappings for entities**
6. **Code comments only** - Add inline comments in code, NOT separate doc files
7. **You MUST call `write_file` to create every output file** - do not finish without writing files

## Output Structure (FROM TEMPLATES)
```
output/
├── backend/
│   ├── {ProjectName}.Data/Entities/
│   ├── {ProjectName}.Data/Repositories/
│   ├── {ProjectName}.Business/Services/
│   ├── {ProjectName}.Business/DTOs/
│   └── {ProjectName}.API/Controllers/
└── frontend/
    ├── components/
    ├── pages/
    ├── services/
    └── types/
```

Be thorough and methodical. The quality of the migration depends on knowledge completeness.
"""


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
            system_prompt=MIGRATION_SYSTEM_PROMPT,
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
            description="Read the contents of a file.",
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description="Path to the file to read",
                    required=True,
                ),
            ],
            function=lambda **kwargs: file_tools.get_file_content(
                str(self.output_dir), kwargs["filepath"]
            ),
        )

        self.tool_registry.register(
            name="write_file",
            description="Write content to a file. Creates parent directories if needed.",
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description="Path to the file to write",
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
                str(self.output_dir), kwargs["filepath"], kwargs["content"]
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
            ],
            function=lambda **kwargs: code_tools.get_code_context(
                self.form_name,
                kwargs["query"],
                kwargs.get("doc_type"),
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

    async def migrate(self, prompt: str | None = None) -> str:
        """
        Run the migration process.

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
            migration_prompt = f"""
# Migration Task: Form '{self.form_name}'

## STEP 1: GATHER ALL KNOWLEDGE FIRST (MANDATORY)

Execute these tools in order before generating ANY code:

1. `get_all_form_knowledge` - Retrieve complete form knowledge
2. `list_export_templates` - See available BE/FE templates
3. `get_conversion_prompt("backend")` - Get .NET output format
4. `get_oracle_to_postgres_mapping` - Get data type mappings

## STEP 2: GENERATE BACKEND CODE

Using the backend conversion template format, call `write_file` to create:
- backend/{self.form_name}.Data/Entities/ - EF Core entities matching DB schema
- backend/{self.form_name}.Data/Repositories/ - Data access layer
- backend/{self.form_name}.Business/Services/ - Business logic
- backend/{self.form_name}.Business/DTOs/ - Data transfer objects
- backend/{self.form_name}.API/Controllers/ - REST endpoints

## STEP 3: GENERATE FRONTEND CODE

Using the frontend conversion template format, call `write_file` to create:
- frontend/components/ - React components matching UI screenshots
- frontend/pages/ - Pages for each form screen
- frontend/services/ - API services to call backend
- frontend/types/ - TypeScript type definitions

## CRITICAL - ONLY CODE FILES:
- Generate ONLY .cs, .tsx, .ts, .json, .csproj files
- NO documentation files (no .md, README, MANIFEST, API docs)
- NO swagger/OpenAPI files
- Put all documentation as inline code comments

## REQUIREMENTS:
- 100% parity with legacy business logic
- Use Oracle→PostgreSQL type mappings for entities
- Follow exact template output structure
- Inline comments only (no separate doc files)

START by calling `get_all_form_knowledge` to gather knowledge, then generate ALL files.
"""

        return await self.send_message(migration_prompt)
