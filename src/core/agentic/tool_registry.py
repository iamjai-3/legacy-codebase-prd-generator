"""
Tool Registry for Agentic AI.

Provides tool registration, schema generation for Anthropic function calling,
and tool execution with argument validation.
"""

import inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from src.utils.logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class ToolParameter:
    """Definition of a tool parameter."""

    name: str
    type: str  # "string", "integer", "boolean", "array", "object"
    description: str
    required: bool = True
    enum: list[str] | None = None
    default: Any = None


@dataclass
class Tool:
    """
    Definition of a tool that the agent can use.

    Each tool has a name, description, parameters, and a Python function
    that implements the tool's functionality.
    """

    name: str
    description: str
    parameters: list[ToolParameter] = field(default_factory=list)
    function: Callable[..., str] | None = None

    def _build_parameters_schema(self) -> tuple[dict[str, Any], list[str]]:
        """Build the properties and required list from parameters."""
        properties = {}
        required = []

        for param in self.parameters:
            prop_schema: dict[str, Any] = {
                "type": param.type,
                "description": param.description,
            }

            if param.enum:
                prop_schema["enum"] = param.enum

            properties[param.name] = prop_schema

            if param.required:
                required.append(param.name)

        return properties, required

    def to_anthropic_schema(self) -> dict[str, Any]:
        """
        Convert tool to Anthropic tool schema format.

        Returns:
            Dict compatible with Anthropic tools API
        """
        properties, required = self._build_parameters_schema()

        return {
            "name": self.name,
            "description": self.description,
            "input_schema": {
                "type": "object",
                "properties": properties,
                "required": required,
            },
        }

    def to_openai_schema(self) -> dict[str, Any]:
        """
        Convert tool to OpenAI tool schema format.

        Returns:
            Dict compatible with OpenAI tools API
        """
        properties, required = self._build_parameters_schema()

        schema: dict[str, Any] = {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            },
        }

        return schema

    def validate_arguments(self, arguments: dict[str, Any]) -> tuple[bool, str]:
        """
        Validate arguments against parameter definitions.

        Args:
            arguments: Arguments to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check required parameters
        for param in self.parameters:
            if param.required and param.name not in arguments:
                return False, f"Missing required parameter: {param.name}"

            if param.name in arguments and param.enum:
                if arguments[param.name] not in param.enum:
                    return False, f"Invalid value for {param.name}. Must be one of: {param.enum}"

        return True, ""

    def execute(self, **kwargs: Any) -> str:
        """
        Execute the tool with given arguments.

        Args:
            **kwargs: Tool arguments

        Returns:
            Tool result as string
        """
        if self.function is None:
            return f"Error: Tool '{self.name}' has no implementation"

        # Validate arguments
        is_valid, error = self.validate_arguments(kwargs)
        if not is_valid:
            return f"Error: {error}"

        try:
            result = self.function(**kwargs)
            return str(result) if result is not None else "Success"
        except Exception as e:
            logger.error(f"Tool execution failed: {self.name}", error=str(e))
            return f"Error executing {self.name}: {str(e)}"


class ToolRegistry:
    """
    Registry for managing available tools.

    Provides tool registration, lookup, and schema generation for
    Anthropic function calling.
    """

    def __init__(self) -> None:
        """Initialize the tool registry."""
        self._tools: dict[str, Tool] = {}
        self.logger = get_logger(__name__)

    @property
    def tools(self) -> list[Tool]:
        """Get all registered tools."""
        return list(self._tools.values())

    @property
    def tool_names(self) -> list[str]:
        """Get names of all registered tools."""
        return list(self._tools.keys())

    def register(
        self,
        name: str,
        description: str,
        parameters: list[ToolParameter] | None = None,
        function: Callable[..., str] | None = None,
    ) -> Tool:
        """
        Register a new tool.

        Args:
            name: Unique tool name
            description: Tool description for the LLM
            parameters: List of parameter definitions
            function: Python function implementing the tool

        Returns:
            The registered Tool
        """
        if name in self._tools:
            self.logger.warning(f"Overwriting existing tool: {name}")

        tool = Tool(
            name=name,
            description=description,
            parameters=parameters or [],
            function=function,
        )
        self._tools[name] = tool

        self.logger.debug(f"Registered tool: {name}", param_count=len(tool.parameters))
        return tool

    def register_from_function(
        self,
        function: Callable[..., str],
        name: str | None = None,
        description: str | None = None,
    ) -> Tool:
        """
        Register a tool from a Python function using introspection.

        Args:
            function: Python function to register
            name: Optional override for tool name
            description: Optional override for description

        Returns:
            The registered Tool
        """
        tool_name = name or function.__name__
        tool_description = description or (function.__doc__ or "No description available")

        # Extract parameters from function signature
        sig = inspect.signature(function)
        parameters = []

        for param_name, param in sig.parameters.items():
            if param_name in ("self", "cls", "working_directory"):
                continue

            # Determine type from annotation
            param_type = "string"
            if param.annotation != inspect.Parameter.empty:
                if param.annotation == int:
                    param_type = "integer"
                elif param.annotation == bool:
                    param_type = "boolean"
                elif param.annotation == list:
                    param_type = "array"
                elif param.annotation == dict:
                    param_type = "object"

            # Check if required
            required = param.default == inspect.Parameter.empty
            default = None if required else param.default

            parameters.append(
                ToolParameter(
                    name=param_name,
                    type=param_type,
                    description=f"Parameter: {param_name}",
                    required=required,
                    default=default,
                )
            )

        return self.register(
            name=tool_name,
            description=tool_description,
            parameters=parameters,
            function=function,
        )

    def get(self, name: str) -> Tool | None:
        """
        Get a tool by name.

        Args:
            name: Tool name

        Returns:
            Tool if found, None otherwise
        """
        return self._tools.get(name)

    def execute(self, name: str, arguments: dict[str, Any]) -> str:
        """
        Execute a tool by name with given arguments.

        Args:
            name: Tool name
            arguments: Tool arguments

        Returns:
            Tool result as string
        """
        tool = self.get(name)
        if tool is None:
            error_msg = f"Unknown tool: {name}"
            self.logger.error(error_msg)
            return f"Error: {error_msg}"

        self.logger.info(f"Executing tool: {name}", arguments=list(arguments.keys()))
        return tool.execute(**arguments)

    def to_anthropic_tools(self) -> list[dict[str, Any]]:
        """
        Convert all tools to Anthropic API format.

        Returns:
            List of tool schemas for Anthropic messages API
        """
        return [tool.to_anthropic_schema() for tool in self._tools.values()]

    def to_openai_tools(self) -> list[dict[str, Any]]:
        """
        Convert all tools to OpenAI API format.

        Returns:
            List of tool schemas for OpenAI chat completions API
        """
        return [tool.to_openai_schema() for tool in self._tools.values()]

    def unregister(self, name: str) -> bool:
        """
        Remove a tool from the registry.

        Args:
            name: Tool name

        Returns:
            True if tool was removed, False if not found
        """
        if name in self._tools:
            del self._tools[name]
            self.logger.debug(f"Unregistered tool: {name}")
            return True
        return False

    def clear(self) -> None:
        """Remove all tools from the registry."""
        self._tools.clear()
        self.logger.debug("Cleared all tools from registry")
