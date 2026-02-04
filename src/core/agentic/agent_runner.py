"""
Agent Runner for Agentic AI.

Implements the main agent execution loop that:
1. Sends messages to Claude with tool definitions
2. Handles tool_use responses (including parallel tool calls)
3. Executes tools and returns results
4. Loops until task completion or max iterations
"""

import asyncio
from typing import TYPE_CHECKING, Any

from src.core.agentic.message_history import ToolUse
from src.utils.logging_config import get_logger

if TYPE_CHECKING:
    from src.core.agentic.agentic_base import AgenticAgent


logger = get_logger(__name__)

TOOL_RESULT_MAX_CHARS = 20000  # Limit each tool result to ~5K tokens


class AgentRunner:
    """
    Executes the agentic loop for an agent.

    The runner handles the interaction between the agent and Claude,
    managing tool calls and building up the conversation history.
    """

    def __init__(self, agent: "AgenticAgent") -> None:
        """
        Initialize the agent runner.

        Args:
            agent: The agentic agent to run
        """
        self.agent = agent
        self.iteration = 0
        self.logger = get_logger(__name__, agent=agent.name)

    async def run(self) -> str:
        """
        Run the agent loop until completion.

        Returns:
            The final text response from the agent
        """
        config = self.agent.config

        for self.iteration in range(config.max_iterations):
            if config.verbose:
                self.logger.info(f"Iteration {self.iteration + 1}/{config.max_iterations}")

            try:
                response = await self._call_claude()

                # Check if we have a final text response (no tool use)
                if response.stop_reason == "end_turn":
                    # Extract text content
                    text_content = self._extract_text_content(response)
                    if text_content:
                        self.logger.info(f"Agent completed in {self.iteration + 1} iterations")
                        return text_content

                # Handle tool use
                if response.stop_reason == "tool_use":
                    self._handle_tool_use(response)
                    continue

                # Unexpected stop reason
                text_content = self._extract_text_content(response)
                if text_content:
                    return text_content

                self.logger.warning(f"Unexpected stop reason: {response.stop_reason}")
                break

            except Exception as e:
                self.logger.error(f"Agent execution error: {e}")
                return f"Error: {str(e)}"

        # Max iterations reached
        self.logger.warning(
            f"Reached maximum iterations ({config.max_iterations}). "
            "Agent may not have completed the task."
        )
        return "Error: Maximum iterations reached without completing the task."

    async def _call_claude(self) -> Any:
        """
        Make a call to Claude API.

        Returns:
            The API response
        """
        config = self.agent.config

        # Check token estimate and truncate if needed (proactive to reduce cost)
        max_context_tokens = 100000
        estimated_tokens = self.agent.message_history.estimated_tokens

        if estimated_tokens > max_context_tokens:
            self.logger.warning(
                "Context too large (%s tokens). Truncating to recent messages.",
                estimated_tokens,
            )
            self.agent.message_history.truncate_to_recent(max_messages=20)

        # Build the API request
        messages = self.agent.message_history.to_anthropic_messages()
        tools = self.agent.get_tools_schema()

        if config.verbose:
            self.logger.debug(
                "Calling Claude",
                message_count=len(messages),
                tool_count=len(tools),
            )

        # Make the API call (synchronous Anthropic client)
        response = await asyncio.to_thread(
            self.agent.client.messages.create,
            model=config.model,
            max_tokens=config.max_tokens,
            system=self.agent.message_history.get_system_prompt(),
            messages=messages,
            tools=tools if tools else None,
        )

        # Always log token usage for cost monitoring
        self.logger.info(
            "Claude usage: input_tokens=%s output_tokens=%s",
            response.usage.input_tokens,
            response.usage.output_tokens,
        )
        if config.verbose:
            self.logger.debug(
                "Claude response",
                stop_reason=response.stop_reason,
                usage_input=response.usage.input_tokens,
                usage_output=response.usage.output_tokens,
            )

        # DON'T add to history here - we handle it in _handle_tool_use
        # to properly group multiple tool calls

        return response

    def _parse_tool_uses_from_response(self, response: Any) -> tuple[list[ToolUse], str | None]:
        """Extract tool_use blocks and optional text from Claude response."""
        tool_uses: list[ToolUse] = []
        text_content = None
        for block in response.content:
            if block.type == "tool_use":
                tool_uses.append(ToolUse(id=block.id, name=block.name, input=block.input))
            elif block.type == "text":
                text_content = block.text
        return tool_uses, text_content

    def _execute_one_tool(self, tool_use: ToolUse) -> tuple[str, str, bool]:
        """Run a single tool and return (tool_use_id, result, is_error)."""
        if self.agent.config.verbose:
            self.logger.info(f"Calling tool: {tool_use.name}", input=tool_use.input)
        else:
            print(f"  → Calling: {tool_use.name}")
        try:
            result = self.agent.execute_tool(tool_use.name, tool_use.input)
            is_error = result.startswith("Error:")
            if len(result) > TOOL_RESULT_MAX_CHARS:
                result = (
                    result[:TOOL_RESULT_MAX_CHARS]
                    + f"\n\n[... truncated {len(result) - TOOL_RESULT_MAX_CHARS} chars ...]"
                )
        except Exception as e:
            result = f"Error: {str(e)}"
            is_error = True
        if self.agent.config.verbose:
            preview = result[:500] + "..." if len(result) > 500 else result
            self.logger.debug(f"Tool result: {preview}")
        return tool_use.id, result, is_error

    def _handle_tool_use(self, response: Any) -> None:
        """
        Handle tool use requests from Claude.

        When Claude returns multiple tool_use blocks, we need to:
        1. Add ONE assistant message with ALL tool_use blocks
        2. Execute all tools
        3. Add ONE user message with ALL tool_result blocks

        Args:
            response: The API response containing tool use
        """
        tool_uses, text_content = self._parse_tool_uses_from_response(response)
        if not tool_uses:
            if text_content:
                self.agent.message_history.add_assistant_message(content=text_content)
            return

        self.agent.message_history.add_assistant_message_with_tools(
            content=text_content,
            tool_uses=tool_uses,
        )
        tool_results = [self._execute_one_tool(tool_use) for tool_use in tool_uses]
        self.agent.message_history.add_tool_results(tool_results)

    def _extract_text_content(self, response: Any) -> str:
        """
        Extract text content from Claude's response.

        Args:
            response: The API response

        Returns:
            Text content or empty string
        """
        # Also add pure text responses to history
        has_tool_use = any(block.type == "tool_use" for block in response.content)

        for block in response.content:
            if block.type == "text":
                # Only add to history if this is a pure text response (no tools)
                if not has_tool_use:
                    self.agent.message_history.add_assistant_message(content=block.text)
                return block.text
        return ""
