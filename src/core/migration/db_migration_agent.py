"""
Database Migration Agent.

Specialized agent for database schema analysis and Entity Framework Core generation.
Generates entities, repositories, and migration scripts.
"""

from pathlib import Path

from src.core.agentic.agentic_base import AgenticAgent, AgenticConfig
from src.core.agentic.tool_registry import ToolParameter
from src.prompts.loader import load_prompt
from src.tools import code_tools, database_tools, file_tools, minio_tools
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class DatabaseMigrationAgent(AgenticAgent):
    """
    Specialized agent for database migration tasks.

    Generates Entity Framework Core entities, repositories,
    and DbContext from legacy database schema.
    """

    def __init__(
        self,
        form_name: str,
        output_dir: Path,
        config: AgenticConfig | None = None,
    ) -> None:
        """
        Initialize the database migration agent.

        Args:
            form_name: Name of the form
            output_dir: Output directory for generated entities
            config: Optional agent configuration
        """
        self.form_name = form_name
        self.output_dir = Path(output_dir)

        if config is None:
            config = AgenticConfig()
        config.working_directory = self.output_dir

        super().__init__(
            name="DatabaseMigrationAgent",
            system_prompt=load_prompt("database_migration/system_prompt"),
            config=config,
        )

    def _register_default_tools(self) -> None:
        """Register database-specific tools."""
        # Database tools
        self.tool_registry.register(
            name="get_database_schema",
            description="Get the database schema information.",
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
                    description="Specific table name",
                    required=False,
                ),
            ],
            function=lambda **kwargs: database_tools.get_table_mappings(
                self.form_name,
                kwargs.get("table_name"),
            ),
        )

        self.tool_registry.register(
            name="get_entity_definition",
            description="Get the definition of a specific entity from legacy code.",
            parameters=[
                ToolParameter(
                    name="entity_name",
                    type="string",
                    description="Name of the entity to find",
                    required=True,
                ),
            ],
            function=lambda **kwargs: database_tools.get_entity_definition(
                self.form_name,
                kwargs["entity_name"],
            ),
        )

        self.tool_registry.register(
            name="get_db_prd",
            description="Get global database PRD documentation.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_db_prd(),
        )

        self.tool_registry.register(
            name="search_codebase",
            description="Search for related code in the knowledge base.",
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Search query",
                    required=True,
                ),
            ],
            function=lambda **kwargs: code_tools.search_codebase(
                self.form_name,
                kwargs["query"],
            ),
        )

        # File tools
        self.tool_registry.register(
            name="write_file",
            description="Write generated entity/repository to a file.",
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description="File path to write",
                    required=True,
                ),
                ToolParameter(
                    name="content",
                    type="string",
                    description="File content",
                    required=True,
                ),
            ],
            function=lambda **kwargs: file_tools.write_file(
                str(self.output_dir),
                kwargs["filepath"],
                kwargs["content"],
            ),
        )

        self.tool_registry.register(
            name="get_files_info",
            description="List files in a directory.",
            parameters=[
                ToolParameter(
                    name="directory",
                    type="string",
                    description="Directory to list",
                    required=False,
                    default=".",
                ),
            ],
            function=lambda **kwargs: file_tools.get_files_info(
                str(self.output_dir),
                kwargs.get("directory", "."),
            ),
        )

    async def generate_entities(self) -> str:
        """
        Generate EF Core entities from the database schema.

        Returns:
            Summary of generated entities
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)

        prompt = load_prompt("database_migration/generate_entities", form_name=self.form_name)

        return await self.send_message(prompt)
