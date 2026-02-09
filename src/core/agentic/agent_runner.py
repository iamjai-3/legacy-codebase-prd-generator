"""
Agent Runner for Agentic AI.

Implements the main agent execution loop that:
1. Sends messages to the LLM (OpenAI or Anthropic) with tool definitions
2. Handles tool_use responses (including parallel tool calls)
3. Executes tools and returns results
4. Loops until task completion or max iterations
"""

import asyncio
import json
from typing import TYPE_CHECKING, Any

from src.config.settings import LLMProvider
from src.core.agentic.message_history import ToolUse
from src.utils.logging_config import get_logger

if TYPE_CHECKING:
    from src.core.agentic.agentic_base import AgenticAgent


logger = get_logger(__name__)


class AgentRunner:
    """
    Executes the agentic loop for an agent.

    The runner handles the interaction between the agent and the LLM,
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
        # Track which tools have been called during this run
        self._called_tools: set[str] = set()

    def _required_tools_satisfied(self) -> bool:
        """Check if all required tools have been called at least once."""
        required = self.agent.config.required_tools
        if not required:
            return True
        return all(tool in self._called_tools for tool in required)

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
                response = await self._call_llm()

                # Dispatch to the appropriate provider handler
                if self.agent.provider == LLMProvider.ANTHROPIC:
                    result = await self._handle_anthropic_response(response)
                else:
                    result = await self._handle_openai_response(response)

                if result is not None:
                    return result

                # Continue to next iteration (tool calls were handled)
                continue

            except Exception as e:
                self.logger.error(f"Agent execution error: {e}")
                return f"Error: {str(e)}"

        # Max iterations reached
        self.logger.warning(
            f"Reached maximum iterations ({config.max_iterations}). "
            "Agent may not have completed the task."
        )
        return "Error: Maximum iterations reached without completing the task."

    async def _call_llm(self) -> Any:
        """
        Make a call to the configured LLM API.

        Returns:
            The API response
        """
        config = self.agent.config

        # Check token estimate and truncate if needed
        max_context_tokens = 180000  # Leave headroom for response
        estimated_tokens = self.agent.message_history.estimated_tokens

        if estimated_tokens > max_context_tokens:
            self.logger.warning(f"Context too large ({estimated_tokens} tokens). Truncating...")
            self.agent.message_history.truncate_to_recent(max_messages=10)

        tools = self.agent.get_tools_schema()

        if self.agent.provider == LLMProvider.ANTHROPIC:
            return await self._call_anthropic(config, tools)
        else:
            return await self._call_openai(config, tools)

    async def _call_anthropic(self, config: Any, tools: list[dict[str, Any]]) -> Any:
        """Make a call to Anthropic Claude API."""
        messages = self.agent.message_history.to_anthropic_messages()

        if config.verbose:
            self.logger.debug(
                "Calling Anthropic Claude",
                message_count=len(messages),
                tool_count=len(tools),
            )

        response = await asyncio.to_thread(
            self.agent.client.messages.create,
            model=config.model,
            max_tokens=config.max_tokens,
            system=self.agent.message_history.get_system_prompt(),
            messages=messages,
            tools=tools if tools else None,
        )

        if config.verbose:
            self.logger.debug(
                "Anthropic response",
                stop_reason=response.stop_reason,
                usage_input=response.usage.input_tokens,
                usage_output=response.usage.output_tokens,
            )

        return response

    async def _call_openai(self, config: Any, tools: list[dict[str, Any]]) -> Any:
        """Make a call to OpenAI API."""
        messages = self.agent.message_history.to_openai_messages()

        if config.verbose:
            self.logger.debug(
                "Calling OpenAI",
                message_count=len(messages),
                tool_count=len(tools),
            )

        kwargs: dict[str, Any] = {
            "model": config.model,
            "max_tokens": config.max_tokens,
            "messages": messages,
        }
        if tools:
            kwargs["tools"] = tools

        response = await asyncio.to_thread(
            self.agent.client.chat.completions.create,
            **kwargs,
        )

        if config.verbose:
            self.logger.debug(
                "OpenAI response",
                finish_reason=response.choices[0].finish_reason if response.choices else None,
                usage_prompt=response.usage.prompt_tokens if response.usage else None,
                usage_completion=response.usage.completion_tokens if response.usage else None,
            )

        return response

    # ========== Anthropic Response Handling ==========

    async def _handle_anthropic_response(self, response: Any) -> str | None:
        """
        Handle Anthropic API response.

        Returns:
            Final text if complete, None if tool calls were handled and we should continue.
        """
        # Check if we have a final text response (no tool use)
        if response.stop_reason == "end_turn":
            text_content = self._extract_anthropic_text(response)
            if text_content:
                # Check required tools before finishing
                if not self._required_tools_satisfied():
                    return self._inject_continuation(text_content)
                self.logger.info(f"Agent completed in {self.iteration + 1} iterations")
                return text_content

        # Handle tool use
        if response.stop_reason == "tool_use":
            await self._handle_anthropic_tool_use(response)
            return None

        # Unexpected stop reason
        text_content = self._extract_anthropic_text(response)
        if text_content:
            return text_content

        self.logger.warning(f"Unexpected stop reason: {response.stop_reason}")
        return "Error: Unexpected response from Anthropic."

    async def _handle_anthropic_tool_use(self, response: Any) -> None:
        """Handle tool use requests from Anthropic Claude."""
        tool_uses: list[ToolUse] = []
        text_content = None

        for block in response.content:
            if block.type == "tool_use":
                tool_uses.append(
                    ToolUse(
                        id=block.id,
                        name=block.name,
                        input=block.input,
                    )
                )
            elif block.type == "text":
                text_content = block.text

        if not tool_uses:
            if text_content:
                self.agent.message_history.add_assistant_message(content=text_content)
            return

        # Add assistant message with ALL tool_use blocks
        self.agent.message_history.add_assistant_message_with_tools(
            content=text_content,
            tool_uses=tool_uses,
        )

        # Execute all tools and collect results
        tool_results = await self._execute_tools(tool_uses)

        # Add ALL tool results in ONE user message
        self.agent.message_history.add_tool_results(tool_results)

    def _extract_anthropic_text(self, response: Any) -> str:
        """Extract text content from Anthropic's response."""
        has_tool_use = any(block.type == "tool_use" for block in response.content)

        for block in response.content:
            if block.type == "text":
                if not has_tool_use:
                    self.agent.message_history.add_assistant_message(content=block.text)
                return block.text
        return ""

    # ========== OpenAI Response Handling ==========

    async def _handle_openai_response(self, response: Any) -> str | None:
        """
        Handle OpenAI API response.

        Returns:
            Final text if complete, None if tool calls were handled and we should continue.
        """
        if not response.choices:
            return "Error: Empty response from OpenAI."

        choice = response.choices[0]
        message = choice.message

        # Check if we have a final text response (no tool calls)
        if choice.finish_reason == "stop":
            text_content = message.content or ""
            # Check required tools before finishing — if not satisfied,
            # treat this as an intermediate response and keep going.
            if not self._required_tools_satisfied():
                return self._inject_continuation(text_content)
            if text_content:
                self.agent.message_history.add_assistant_message(content=text_content)
                self.logger.info(f"Agent completed in {self.iteration + 1} iterations")
            return text_content

        # Handle tool calls
        if choice.finish_reason == "tool_calls":
            await self._handle_openai_tool_calls(message)
            return None

        # Unexpected finish reason
        text_content = message.content or ""
        if text_content:
            self.agent.message_history.add_assistant_message(content=text_content)
            return text_content

        self.logger.warning(f"Unexpected finish reason: {choice.finish_reason}")
        return "Error: Unexpected response from OpenAI."

    async def _handle_openai_tool_calls(self, message: Any) -> None:
        """Handle tool call requests from OpenAI."""
        tool_calls = message.tool_calls
        if not tool_calls:
            if message.content:
                self.agent.message_history.add_assistant_message(content=message.content)
            return

        # Convert OpenAI tool calls to our ToolUse format
        tool_uses: list[ToolUse] = []
        for tc in tool_calls:
            try:
                arguments = json.loads(tc.function.arguments)
            except json.JSONDecodeError:
                arguments = {}

            tool_uses.append(
                ToolUse(
                    id=tc.id,
                    name=tc.function.name,
                    input=arguments,
                )
            )

        text_content = message.content

        # Add assistant message with tool calls
        self.agent.message_history.add_assistant_message_with_tools(
            content=text_content,
            tool_uses=tool_uses,
        )

        # Execute all tools and collect results
        tool_results = await self._execute_tools(tool_uses)

        # Add tool results
        self.agent.message_history.add_tool_results(tool_results)

    # ========== Shared ==========

    def _inject_continuation(self, text_content: str) -> None:
        """
        Handle an intermediate text response when required tools haven't been called.

        Adds the model's text to history and injects a user message telling it
        to continue using the outstanding tools. Returns None so the loop continues.
        """
        missing = [t for t in self.agent.config.required_tools if t not in self._called_tools]
        self.logger.info(f"Required tools not yet called: {missing}. Continuing agent loop.")

        # Add the model's intermediate text to history
        self.agent.message_history.add_assistant_message(content=text_content)

        # Inject a user-level continuation prompt
        self.agent.message_history.add_user_message(
            "Continue. You have not called the required tools yet "
            f"({', '.join(missing)}). Proceed with the remaining steps now."
        )
        return None

    async def _execute_tools(self, tool_uses: list[ToolUse]) -> list[tuple[str, str, bool]]:
        """
        Execute a list of tool calls and return results.

        Args:
            tool_uses: List of tool use requests

        Returns:
            List of (tool_use_id, result_content, is_error) tuples
        """
        tool_results: list[tuple[str, str, bool]] = []
        max_result_size = 20000  # Limit each tool result to ~5K tokens

        for tool_use in tool_uses:
            # Track the tool call
            self._called_tools.add(tool_use.name)

            if self.agent.config.verbose:
                self.logger.info(f"Calling tool: {tool_use.name}", input=tool_use.input)
            else:
                print(f"  → Calling: {tool_use.name}")

            try:
                result = self.agent.execute_tool(tool_use.name, tool_use.input)
                is_error = result.startswith("Error:")

                # Truncate large results to prevent context overflow
                if len(result) > max_result_size:
                    result = (
                        result[:max_result_size]
                        + f"\n\n[... truncated {len(result) - max_result_size} chars ...]"
                    )

            except Exception as e:
                result = f"Error: {str(e)}"
                is_error = True

            tool_results.append((tool_use.id, result, is_error))

            if self.agent.config.verbose:
                preview = result[:500] + "..." if len(result) > 500 else result
                self.logger.debug(f"Tool result: {preview}")

        return tool_results
