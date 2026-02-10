"""
UI Migration Agent.

Specialized agent for frontend migration from legacy Java Swing to React.
Analyzes screenshots and generates React components.
"""

from pathlib import Path

from src.core.agentic.agentic_base import AgenticAgent, AgenticConfig
from src.core.agentic.tool_registry import ToolParameter
from src.prompts.loader import load_prompt
from src.tools import code_tools, file_tools, minio_tools
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class UIMigrationAgent(AgenticAgent):
    """
    Specialized agent for UI migration tasks.

    Generates React components from legacy Java Swing UI
    based on screenshot analysis.
    """

    def __init__(
        self,
        form_name: str,
        output_dir: Path,
        config: AgenticConfig | None = None,
    ) -> None:
        """
        Initialize the UI migration agent.

        Args:
            form_name: Name of the form
            output_dir: Output directory for generated components
            config: Optional agent configuration
        """
        self.form_name = form_name
        self.output_dir = Path(output_dir)

        if config is None:
            config = AgenticConfig()
        config.working_directory = self.output_dir

        super().__init__(
            name="UIMigrationAgent",
            system_prompt=load_prompt("ui_migration/system_prompt"),
            config=config,
        )

    def _register_default_tools(self) -> None:
        """Register UI-specific tools."""
        # Screenshot tools
        self.tool_registry.register(
            name="list_screenshots",
            description="List available UI screenshots.",
            parameters=[],
            function=lambda **kwargs: minio_tools.list_screenshots(self.form_name),
        )

        self.tool_registry.register(
            name="get_form_docs",
            description="Get form documentation including field descriptions.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_form_docs(self.form_name),
        )

        self.tool_registry.register(
            name="search_codebase",
            description="Search for UI-related code and validation rules.",
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

        self.tool_registry.register(
            name="get_code_context",
            description="Get code context for UI patterns.",
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Topic to get context for",
                    required=True,
                ),
            ],
            function=lambda **kwargs: code_tools.get_code_context(
                self.form_name,
                kwargs["query"],
            ),
        )

        # File tools
        self.tool_registry.register(
            name="write_file",
            description="Write generated component to a file.",
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

    async def generate_components(self) -> str:
        """
        Generate React components from screenshots.

        Returns:
            Summary of generated components
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)

        prompt = load_prompt("ui_migration/generate_components", form_name=self.form_name)

        return await self.send_message(prompt)
