"""
Code Generation Agent.

Specialized agent for backend business logic migration.
Generates .NET services, controllers, and preserves all business rules.
"""

from pathlib import Path

from src.core.agentic.agentic_base import AgenticAgent, AgenticConfig
from src.core.agentic.tool_registry import ToolParameter
from src.prompts.loader import load_prompt
from src.tools import code_tools, database_tools, file_tools, minio_tools
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class CodeGenerationAgent(AgenticAgent):
    """
    Specialized agent for backend code generation.

    Generates .NET Core services and controllers while
    preserving all business logic from legacy Java code.
    """

    def __init__(
        self,
        form_name: str,
        output_dir: Path,
        config: AgenticConfig | None = None,
    ) -> None:
        """
        Initialize the code generation agent.

        Args:
            form_name: Name of the form
            output_dir: Output directory for generated code
            config: Optional agent configuration
        """
        self.form_name = form_name
        self.output_dir = Path(output_dir)

        if config is None:
            config = AgenticConfig()
        config.working_directory = self.output_dir

        super().__init__(
            name="CodeGenerationAgent",
            system_prompt=load_prompt("code_generation/system_prompt"),
            config=config,
        )

    def _register_default_tools(self) -> None:
        """Register code generation tools."""
        # Code analysis tools
        self.tool_registry.register(
            name="search_codebase",
            description="Search for business logic in the legacy codebase.",
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Search query (e.g., 'validation rules', 'calculate total')",
                    required=True,
                ),
                ToolParameter(
                    name="limit",
                    type="integer",
                    description="Maximum results",
                    required=False,
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
            description="Get relevant code context for a topic.",
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
                    description="Filter by doc type: code, business_logic",
                    required=False,
                ),
            ],
            function=lambda **kwargs: code_tools.get_code_context(
                self.form_name,
                kwargs["query"],
                kwargs.get("doc_type"),
            ),
        )

        self.tool_registry.register(
            name="get_business_logic",
            description="Get business logic for a specific topic.",
            parameters=[
                ToolParameter(
                    name="topic",
                    type="string",
                    description="Business logic topic",
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
            description="Get form documentation and requirements.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_form_docs(self.form_name),
        )

        self.tool_registry.register(
            name="get_conversion_prompt",
            description="Get the backend conversion prompt template.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_conversion_prompt("backend"),
        )

        self.tool_registry.register(
            name="get_dependencies",
            description="Get the list of legacy files belonging to this form.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_dependencies(self.form_name),
        )

        # File tools
        self.tool_registry.register(
            name="write_file",
            description="Write generated code to a file.",
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
                ),
            ],
            function=lambda **kwargs: file_tools.get_files_info(
                str(self.output_dir),
                kwargs.get("directory", "."),
            ),
        )

        self.tool_registry.register(
            name="get_file_content",
            description="Read a file's content.",
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description="Path to file",
                    required=True,
                ),
            ],
            function=lambda **kwargs: file_tools.get_file_content(
                str(self.output_dir),
                kwargs["filepath"],
            ),
        )

    async def generate_services(self) -> str:
        """
        Generate .NET services with business logic.

        Returns:
            Summary of generated services
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)

        prompt = load_prompt("code_generation/generate_services", form_name=self.form_name)

        return await self.send_message(prompt)
