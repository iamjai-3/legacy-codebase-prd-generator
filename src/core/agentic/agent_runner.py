"""
Agent Runner for Agentic AI.

Implements the main agent execution loop that:
1. Sends messages to the LLM (OpenAI or Anthropic) with tool definitions
2. Handles tool_use / tool_calls responses (including parallel tool calls)
3. Executes tools and returns results
4. Loops until task completion or max iterations
"""

import asyncio
import hashlib
import json
from typing import TYPE_CHECKING, Any

from src.config.settings import LLMProvider
from src.core.agentic.message_history import ToolUse
from src.utils.cache_manager import CacheType, get_cache_manager
from src.utils.logging_config import get_logger

if TYPE_CHECKING:
    from src.core.agentic.agentic_base import AgenticAgent


logger = get_logger(__name__)

IDEMPOTENT_TOOLS = {
    "get_migration_playbook",
    "get_all_form_knowledge",
    "get_form_docs",
    "get_dependencies",
    "get_ui_flow_docs",
    "list_export_templates",
    "get_conversion_prompt",
    "get_oracle_to_postgres_mapping",
    "get_database_schema",
    "get_table_mappings",
    "get_db_prd",
    "list_screenshots",
}


class AgentRunner:
    """
    Executes the agentic loop for an agent.

    The runner handles the interaction between the agent and the LLM,
    managing tool calls and building up the conversation history.
    Supports both OpenAI and Anthropic providers transparently.
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
        self._tool_result_cache: dict[str, str] = {}
        self._tool_result_hash_by_key: dict[str, str] = {}
        self._total_input_tokens = 0
        self._total_output_tokens = 0

    # ------------------------------------------------------------------
    # Normalised response wrapper
    # ------------------------------------------------------------------

    class _NormalisedResponse:
        """Provider-agnostic view of an LLM response."""

        __slots__ = ("stop_reason", "text_content", "tool_uses", "input_tokens", "output_tokens")

        def __init__(
            self,
            stop_reason: str,
            text_content: str | None,
            tool_uses: list[ToolUse],
            input_tokens: int,
            output_tokens: int,
        ) -> None:
            self.stop_reason = stop_reason  # "end_turn" | "tool_use"
            self.text_content = text_content
            self.tool_uses = tool_uses
            self.input_tokens = input_tokens
            self.output_tokens = output_tokens

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------

    async def run(self) -> str:
        """
        Run the agent loop until completion.

        Returns:
            The final text response from the agent
        """
        config = self.agent.config

        for self.iteration in range(config.max_iterations):
            if config.max_total_tokens > 0:
                total_tokens = self._total_input_tokens + self._total_output_tokens
                if total_tokens >= config.max_total_tokens:
                    self.logger.warning(
                        "Token budget exceeded",
                        total_tokens=total_tokens,
                        max_total_tokens=config.max_total_tokens,
                    )
                    return "Error: Token budget exceeded before completing the task."

            if config.verbose:
                self.logger.info(f"Iteration {self.iteration + 1}/{config.max_iterations}")

            try:
                nr = await self._call_llm()

                # Check if we have a final text response (no tool use)
                if nr.stop_reason == "end_turn":
                    if nr.text_content:
                        self.agent.message_history.add_assistant_message(content=nr.text_content)
                        self.logger.info(f"Agent completed in {self.iteration + 1} iterations")
                        return nr.text_content

                # Handle tool use
                if nr.stop_reason == "tool_use":
                    await self._handle_tool_use(nr)
                    continue

                # Unexpected stop reason – return any text we got
                if nr.text_content:
                    self.agent.message_history.add_assistant_message(content=nr.text_content)
                    return nr.text_content

                self.logger.warning(f"Unexpected stop reason: {nr.stop_reason}")
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

    # ------------------------------------------------------------------
    # LLM call dispatch
    # ------------------------------------------------------------------

    async def _call_llm(self) -> "_NormalisedResponse":
        """Call the configured LLM provider and return a normalised response."""
        config = self.agent.config

        # Proactive context truncation
        max_context_tokens = config.max_context_tokens
        estimated_tokens = self.agent.message_history.estimated_tokens

        if estimated_tokens > max_context_tokens:
            self.logger.warning(
                "Context too large (%s tokens). Truncating to recent messages.",
                estimated_tokens,
            )
            self.agent.message_history.truncate_to_recent(max_messages=20)

        if self.agent.provider == LLMProvider.OPENAI:
            return await self._call_openai()
        return await self._call_anthropic()

    # ------------------------------------------------------------------
    # Anthropic-specific
    # ------------------------------------------------------------------

    async def _call_anthropic(self) -> "_NormalisedResponse":
        """Make a call to the Anthropic API and return a normalised response."""
        config = self.agent.config
        messages = self.agent.message_history.to_anthropic_messages()
        tools = self.agent.get_tools_schema()

        if config.verbose:
            self.logger.debug(
                "Calling Anthropic",
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

        # Log token usage
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        self._total_input_tokens += input_tokens
        self._total_output_tokens += output_tokens
        self.logger.info(
            "Anthropic usage: input_tokens=%s output_tokens=%s",
            input_tokens,
            output_tokens,
        )

        # Parse content blocks
        tool_uses: list[ToolUse] = []
        text_content: str | None = None
        for block in response.content:
            if block.type == "tool_use":
                tool_uses.append(ToolUse(id=block.id, name=block.name, input=block.input))
            elif block.type == "text":
                text_content = block.text

        # Map Anthropic stop_reason → normalised
        stop_reason = "end_turn" if response.stop_reason == "end_turn" else "tool_use"

        return self._NormalisedResponse(
            stop_reason=stop_reason,
            text_content=text_content,
            tool_uses=tool_uses,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

    # ------------------------------------------------------------------
    # OpenAI-specific
    # ------------------------------------------------------------------

    async def _call_openai(self) -> "_NormalisedResponse":
        """Make a call to the OpenAI API and return a normalised response."""
        config = self.agent.config
        messages = self.agent.message_history.to_openai_messages()
        tools = self.agent.get_tools_schema()

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

        # Log token usage
        input_tokens = response.usage.prompt_tokens if response.usage else 0
        output_tokens = response.usage.completion_tokens if response.usage else 0
        self._total_input_tokens += input_tokens
        self._total_output_tokens += output_tokens
        self.logger.info(
            "OpenAI usage: prompt_tokens=%s completion_tokens=%s",
            input_tokens,
            output_tokens,
        )

        choice = response.choices[0]
        message = choice.message

        # Parse tool calls
        tool_uses: list[ToolUse] = []
        if message.tool_calls:
            for tc in message.tool_calls:
                try:
                    args = json.loads(tc.function.arguments)
                except (json.JSONDecodeError, TypeError):
                    args = {}
                tool_uses.append(ToolUse(id=tc.id, name=tc.function.name, input=args))

        text_content = message.content

        # Map OpenAI finish_reason → normalised
        if choice.finish_reason == "tool_calls" or tool_uses:
            stop_reason = "tool_use"
        else:
            stop_reason = "end_turn"

        return self._NormalisedResponse(
            stop_reason=stop_reason,
            text_content=text_content,
            tool_uses=tool_uses,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

    # ------------------------------------------------------------------
    # Tool execution helpers (shared across providers)
    # ------------------------------------------------------------------

    async def _execute_one_tool(self, tool_use: ToolUse) -> tuple[str, str, bool]:
        """Run a single tool and return (tool_use_id, result, is_error)."""
        if self.agent.config.verbose:
            self.logger.info(f"Calling tool: {tool_use.name}", input=tool_use.input)
        else:
            print(f"  → Calling: {tool_use.name}")
        try:
            result, is_error = await self._execute_tool_with_cache(tool_use)
            if len(result) > self.agent.config.tool_result_max_chars:
                result = (
                    result[: self.agent.config.tool_result_max_chars]
                    + f"\n\n[... truncated {len(result) - self.agent.config.tool_result_max_chars} chars ...]"
                )
        except Exception as e:
            result = f"Error: {str(e)}"
            is_error = True
        if self.agent.config.verbose:
            preview = result[:500] + "..." if len(result) > 500 else result
            self.logger.debug(f"Tool result: {preview}")
        return tool_use.id, result, is_error

    async def _execute_tool_with_cache(self, tool_use: ToolUse) -> tuple[str, bool]:
        """
        Execute tool with idempotent caching and de-duplication.

        Returns:
            Tuple of (result, is_error)
        """
        config = self.agent.config
        cache_key = self._tool_cache_key(tool_use)

        if config.dedupe_tool_results and tool_use.name in IDEMPOTENT_TOOLS:
            cached = self._tool_result_cache.get(cache_key)
            cached_hash = self._tool_result_hash_by_key.get(cache_key)
            if cached is not None:
                if cached.startswith("Error:"):
                    return cached, True
                if cached_hash and self.agent.message_history.has_tool_result_hash(cached_hash):
                    return (
                        f"[Cached result reused for tool '{tool_use.name}' with identical inputs. "
                        "Refer to the earlier tool result in this conversation.]",
                        False,
                    )
                return cached, cached.startswith("Error:")

        if tool_use.name in IDEMPOTENT_TOOLS:
            cached_value = await self._get_persistent_tool_cache(cache_key)
            if cached_value is not None:
                cached_text = str(cached_value)
                cached_hash = self._hash_text(cached_text)
                if self.agent.message_history.has_tool_result_hash(cached_hash):
                    return (
                        f"[Cached result reused for tool '{tool_use.name}' with identical inputs. "
                        "Refer to the earlier tool result in this conversation.]",
                        False,
                    )
                self._tool_result_cache[cache_key] = cached_text
                self._tool_result_hash_by_key[cache_key] = cached_hash
                return cached_text, cached_text.startswith("Error:")

        result = await asyncio.to_thread(
            self.agent.execute_tool, tool_use.name, tool_use.input
        )
        is_error = result.startswith("Error:")

        if config.dedupe_tool_results and tool_use.name in IDEMPOTENT_TOOLS:
            self._tool_result_cache[cache_key] = result
            self._tool_result_hash_by_key[cache_key] = self._hash_text(result)
            await self._set_persistent_tool_cache(cache_key, result)

        return result, is_error

    async def _get_persistent_tool_cache(self, cache_key: str) -> Any | None:
        try:
            cache = await get_cache_manager()
            if not cache.cache_settings.enabled:
                return None
            return await cache.get(cache_key, CacheType.TOOL_RESULT)
        except Exception:
            return None

    async def _set_persistent_tool_cache(self, cache_key: str, value: str) -> None:
        try:
            cache = await get_cache_manager()
            if not cache.cache_settings.enabled:
                return
            await cache.set(
                cache_key,
                value,
                CacheType.TOOL_RESULT,
                ttl=cache.cache_settings.tool_result_ttl,
                metadata={"scope": "agentic_tool"},
            )
        except Exception:
            return

    @staticmethod
    def _tool_cache_key(tool_use: ToolUse) -> str:
        try:
            payload = json.dumps(tool_use.input, sort_keys=True, default=str)
        except (TypeError, ValueError):
            payload = str(tool_use.input)
        return f"{tool_use.name}:{payload}"

    @staticmethod
    def _hash_text(content: str) -> str:
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    # ------------------------------------------------------------------
    # Tool-use handling (provider-agnostic, works on normalised response)
    # ------------------------------------------------------------------

    async def _handle_tool_use(self, nr: "_NormalisedResponse") -> None:
        """
        Handle tool use from a normalised response.

        1. Record the assistant message with tool_use blocks in history
        2. Execute all tools (in parallel)
        3. Record tool results in history
        """
        if not nr.tool_uses:
            if nr.text_content:
                self.agent.message_history.add_assistant_message(content=nr.text_content)
            return

        self.agent.message_history.add_assistant_message_with_tools(
            content=nr.text_content,
            tool_uses=nr.tool_uses,
        )
        tool_results = await asyncio.gather(
            *[self._execute_one_tool(tool_use) for tool_use in nr.tool_uses]
        )
        self.agent.message_history.add_tool_results(tool_results)
