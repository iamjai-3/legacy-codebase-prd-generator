"""
Agentic Base Class.

Provides the foundation for agentic AI agents with tool calling capabilities,
working directory boundaries, and integration with OpenAI or Anthropic.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.config.settings import LLMProvider, get_settings
from src.core.agentic.message_history import MessageHistory
from src.core.agentic.tool_registry import ToolRegistry
from src.utils.logging_config import get_logger


@dataclass
class AgenticConfig:
    """Configuration for agentic agent execution."""

    # Working directory boundary for file operations
    working_directory: Path = field(default_factory=lambda: Path.cwd())

    # Maximum iterations for the agent loop
    max_iterations: int = 50

    # Model configuration (set dynamically based on provider)
    model: str = ""
    max_tokens: int = 16384
    temperature: float = 0.0

    # Verbose mode for debugging
    verbose: bool = False

    # Stop sequences
    stop_sequences: list[str] = field(default_factory=list)

    # Tools that must be called at least once before the agent can finish.
    # If the LLM tries to stop without having called these, the runner
    # will automatically inject a continuation prompt and keep going.
    required_tools: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Ensure working_directory is a Path and set default model."""
        if isinstance(self.working_directory, str):
            self.working_directory = Path(self.working_directory)
        # Model is set dynamically in AgenticAgent.__init__ if not specified


class AgenticAgent:
    """
    Base class for agentic AI agents.

    Provides core functionality for:
    - LLM integration with tool calling (OpenAI or Anthropic)
    - Working directory boundaries for security
    - Message history management
    - Tool registration and execution

    Subclasses should register their tools and define their system prompt.
    """

    def __init__(
        self,
        name: str,
        system_prompt: str,
        config: AgenticConfig | None = None,
    ) -> None:
        """
        Initialize the agentic agent.

        Args:
            name: Name of the agent
            system_prompt: System prompt defining agent behavior
            config: Agent configuration (uses defaults if not provided)
        """
        self.name = name
        self.config = config or AgenticConfig()
        self.settings = get_settings()
        self.logger = get_logger(name, agent=name)

        # Determine LLM provider
        self.provider = self.settings.llm.provider

        # Set default model based on provider if not specified
        if not self.config.model:
            if self.provider == LLMProvider.ANTHROPIC:
                self.config.model = self.settings.anthropic.model
            else:
                self.config.model = self.settings.openai.model

        # Initialize client (lazy)
        self._client: Any = None

        # Initialize message history with system prompt
        self.message_history = MessageHistory(system_prompt=system_prompt)

        # Initialize tool registry
        self.tool_registry = ToolRegistry()

        # Register default tools
        self._register_default_tools()

    @property
    def client(self) -> Any:
        """Get or create the LLM client based on configured provider."""
        if self._client is None:
            if self.provider == LLMProvider.ANTHROPIC:
                from anthropic import Anthropic

                self._client = Anthropic(api_key=self.settings.anthropic.api_key)
            else:
                from openai import OpenAI

                self._client = OpenAI(api_key=self.settings.openai.api_key)
        return self._client

    @property
    def working_directory(self) -> Path:
        """Get the working directory boundary."""
        return self.config.working_directory

    def _register_default_tools(self) -> None:
        """Register default tools. Override in subclasses to add more tools."""
        pass

    def validate_path(self, path: str | Path) -> tuple[bool, Path, str]:
        """
        Validate that a path is within the working directory boundary.

        Args:
            path: Path to validate (relative or absolute)

        Returns:
            Tuple of (is_valid, resolved_path, error_message)
        """
        try:
            # Convert to Path and resolve
            if isinstance(path, str):
                path = Path(path)

            # Handle relative paths
            if not path.is_absolute():
                full_path = (self.working_directory / path).resolve()
            else:
                full_path = path.resolve()

            # Check if within working directory
            working_abs = self.working_directory.resolve()

            try:
                full_path.relative_to(working_abs)
                return True, full_path, ""
            except ValueError:
                error = f"Path '{path}' is outside the permitted working directory"
                return False, full_path, error

        except Exception as e:
            return False, Path(), f"Invalid path: {str(e)}"

    def add_tool(
        self,
        name: str,
        description: str,
        parameters: list[dict[str, Any]],
        function: callable,
    ) -> None:
        """
        Register a tool with the agent.

        Args:
            name: Tool name
            description: Tool description
            parameters: List of parameter definitions
            function: Python function implementing the tool
        """
        from src.core.agentic.tool_registry import ToolParameter

        params = [
            ToolParameter(
                name=p["name"],
                type=p.get("type", "string"),
                description=p.get("description", ""),
                required=p.get("required", True),
                enum=p.get("enum"),
                default=p.get("default"),
            )
            for p in parameters
        ]

        self.tool_registry.register(
            name=name,
            description=description,
            parameters=params,
            function=function,
        )

    def get_tools_schema(self) -> list[dict[str, Any]]:
        """Get tool schemas for the configured LLM provider."""
        if self.provider == LLMProvider.ANTHROPIC:
            return self.tool_registry.to_anthropic_tools()
        return self.tool_registry.to_openai_tools()

    def execute_tool(self, name: str, arguments: dict[str, Any]) -> str:
        """
        Execute a tool by name.

        Args:
            name: Tool name
            arguments: Tool arguments

        Returns:
            Tool result as string
        """
        if self.config.verbose:
            self.logger.info(f"Executing tool: {name}", arguments=arguments)

        # Inject working_directory for file operations
        if name in ("get_files_info", "get_file_content", "write_file", "find_files"):
            arguments["working_directory"] = str(self.working_directory)

        result = self.tool_registry.execute(name, arguments)

        if self.config.verbose:
            self.logger.debug(f"Tool result: {result[:200]}...")

        return result

    async def send_message(self, user_message: str) -> str:
        """
        Send a message to the agent and get the response.

        This is a single-turn interaction that may involve multiple
        tool calls before returning the final response.

        Args:
            user_message: The user's message

        Returns:
            The assistant's final text response
        """
        # Add user message to history
        self.message_history.add_user_message(user_message)

        # Run the agent loop
        from src.core.agentic.agent_runner import AgentRunner

        runner = AgentRunner(self)
        return await runner.run()

    def reset(self) -> None:
        """Reset the agent's message history."""
        system_prompt = self.message_history.system_prompt
        self.message_history = MessageHistory(system_prompt=system_prompt)
