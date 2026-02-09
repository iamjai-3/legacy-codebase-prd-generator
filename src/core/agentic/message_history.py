"""
Message History Management for Agentic AI.

Manages conversation history with role-based messages, token counting,
and serialization for the agentic tool calling loop.
"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class MessageRole(str, Enum):
    """Role of a message in the conversation."""

    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
    SYSTEM = "system"


@dataclass
class ToolUse:
    """Represents a tool use request from the assistant."""

    id: str
    name: str
    input: dict[str, Any]


@dataclass
class ToolResult:
    """Represents the result of a tool execution."""

    tool_use_id: str
    content: str
    is_error: bool = False


@dataclass
class Message:
    """A message in the conversation history."""

    role: MessageRole
    content: str | list[dict[str, Any]]
    tool_use: ToolUse | None = None
    tool_uses: list[ToolUse] | None = None  # For multiple parallel tool calls
    tool_result: ToolResult | None = None
    tool_results: list[ToolResult] | None = None  # For multiple tool results
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)

    def _anthropic_tool_result_content(self, tr: ToolResult) -> Any:
        """Normalize tool result content for Anthropic API."""
        return tr.content if isinstance(tr.content, str) else str(tr.content)

    def _anthropic_content_blocks_with_text(self) -> list[dict[str, Any]]:
        """Build content blocks list, prepending text block if present."""
        blocks: list[dict[str, Any]] = []
        if self.content and isinstance(self.content, str) and self.content.strip():
            blocks.append({"type": "text", "text": self.content})
        return blocks

    def to_anthropic_message(self) -> dict[str, Any]:
        """
        Convert to Anthropic API message format.

        Returns:
            Dict compatible with Anthropic messages API
        """
        if self.role == MessageRole.SYSTEM:
            return {"role": "user", "content": self.content}
        if self.role == MessageRole.TOOL and self.tool_results:
            return self._to_anthropic_tool_results_multi()
        if self.role == MessageRole.TOOL and self.tool_result:
            return self._to_anthropic_tool_result_single()
        if self.role == MessageRole.ASSISTANT and self.tool_uses:
            return self._to_anthropic_assistant_tool_uses()
        if self.role == MessageRole.ASSISTANT and self.tool_use:
            return self._to_anthropic_assistant_tool_use()
        return {"role": self.role.value, "content": self.content}

    def _to_anthropic_tool_results_multi(self) -> dict[str, Any]:
        """Anthropic message for multiple tool results (parallel tool calls)."""
        return {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tr.tool_use_id,
                    "content": tr.content,
                    "is_error": tr.is_error,
                }
                for tr in self.tool_results
            ],
        }

    def _to_anthropic_tool_result_single(self) -> dict[str, Any]:
        """Anthropic message for a single tool result (legacy)."""
        return {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": self.tool_result.tool_use_id,
                    "content": self._anthropic_tool_result_content(self.tool_result),
                    "is_error": self.tool_result.is_error,
                }
            ],
        }

    def _to_anthropic_assistant_tool_uses(self) -> dict[str, Any]:
        """Anthropic message for assistant with multiple tool uses (parallel)."""
        content_blocks = self._anthropic_content_blocks_with_text()
        for tu in self.tool_uses:
            content_blocks.append(
                {"type": "tool_use", "id": tu.id, "name": tu.name, "input": tu.input}
            )
        return {"role": "assistant", "content": content_blocks}

    def _to_anthropic_assistant_tool_use(self) -> dict[str, Any]:
        """Anthropic message for assistant with single tool use (legacy)."""
        content_blocks = self._anthropic_content_blocks_with_text()
        content_blocks.append(
            {
                "type": "tool_use",
                "id": self.tool_use.id,
                "name": self.tool_use.name,
                "input": self.tool_use.input,
            }
        )
        return {"role": "assistant", "content": content_blocks}

    # --- OpenAI format methods ---

    def to_openai_messages(self) -> list[dict[str, Any]]:
        """
        Convert to OpenAI API message format.

        OpenAI uses separate 'tool' role messages for each tool result,
        so a single Message may expand into multiple OpenAI messages.

        Returns:
            List of dicts compatible with OpenAI chat completions API
        """
        if self.role == MessageRole.SYSTEM:
            return [{"role": "system", "content": self.content}]

        # Tool results → one message per result with role "tool"
        if self.role == MessageRole.TOOL and self.tool_results:
            return [
                {
                    "role": "tool",
                    "tool_call_id": tr.tool_use_id,
                    "content": tr.content,
                }
                for tr in self.tool_results
            ]
        if self.role == MessageRole.TOOL and self.tool_result:
            return [
                {
                    "role": "tool",
                    "tool_call_id": self.tool_result.tool_use_id,
                    "content": self.tool_result.content,
                }
            ]

        # Assistant with tool uses
        if self.role == MessageRole.ASSISTANT and (self.tool_uses or self.tool_use):
            tool_calls_list = self.tool_uses or ([self.tool_use] if self.tool_use else [])
            msg: dict[str, Any] = {
                "role": "assistant",
                "content": self.content if self.content else None,
                "tool_calls": [
                    {
                        "id": tu.id,
                        "type": "function",
                        "function": {
                            "name": tu.name,
                            "arguments": json.dumps(tu.input),
                        },
                    }
                    for tu in tool_calls_list
                ],
            }
            return [msg]

        # Plain user / assistant message
        return [{"role": self.role.value, "content": self.content}]

    def to_dict(self) -> dict[str, Any]:
        """Serialize message to dictionary for persistence."""
        return {
            "role": self.role.value,
            "content": self.content,
            "tool_use": (
                {
                    "id": self.tool_use.id,
                    "name": self.tool_use.name,
                    "input": self.tool_use.input,
                }
                if self.tool_use
                else None
            ),
            "tool_result": (
                {
                    "tool_use_id": self.tool_result.tool_use_id,
                    "content": self.tool_result.content,
                    "is_error": self.tool_result.is_error,
                }
                if self.tool_result
                else None
            ),
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Message":
        """Deserialize message from dictionary."""
        tool_use = None
        if data.get("tool_use"):
            tool_use = ToolUse(
                id=data["tool_use"]["id"],
                name=data["tool_use"]["name"],
                input=data["tool_use"]["input"],
            )

        tool_result = None
        if data.get("tool_result"):
            tool_result = ToolResult(
                tool_use_id=data["tool_result"]["tool_use_id"],
                content=data["tool_result"]["content"],
                is_error=data["tool_result"].get("is_error", False),
            )

        return cls(
            role=MessageRole(data["role"]),
            content=data["content"],
            tool_use=tool_use,
            tool_result=tool_result,
            timestamp=(
                datetime.fromisoformat(data["timestamp"])
                if data.get("timestamp")
                else datetime.now()
            ),
            metadata=data.get("metadata", {}),
        )


class MessageHistory:
    """
    Manages conversation history for the agentic AI.

    Handles message storage, retrieval, and conversion to Anthropic API format.
    Includes token estimation for context window management.
    """

    def __init__(self, system_prompt: str = "") -> None:
        """
        Initialize message history.

        Args:
            system_prompt: Initial system prompt for the conversation
        """
        self.system_prompt = system_prompt
        self._messages: list[Message] = []
        self._estimated_tokens = 0
        self._tool_result_hashes: set[str] = set()

    @property
    def messages(self) -> list[Message]:
        """Get all messages in the history."""
        return self._messages.copy()

    @property
    def message_count(self) -> int:
        """Get the number of messages."""
        return len(self._messages)

    @property
    def estimated_tokens(self) -> int:
        """Get estimated token count (rough approximation)."""
        return self._estimated_tokens

    def has_tool_result_hash(self, hash_value: str) -> bool:
        """Check if a tool result hash exists in the current history."""
        return hash_value in self._tool_result_hashes

    def add_user_message(self, content: str) -> Message:
        """
        Add a user message to the history.

        Args:
            content: The user's message content

        Returns:
            The created Message
        """
        message = Message(role=MessageRole.USER, content=content)
        self._messages.append(message)
        self._update_token_estimate(content)
        return message

    def add_assistant_message(
        self,
        content: str | None = None,
        tool_use: ToolUse | None = None,
    ) -> Message:
        """
        Add an assistant message to the history.

        Args:
            content: The assistant's text response (optional)
            tool_use: Tool use request if the assistant wants to call a tool

        Returns:
            The created Message
        """
        message = Message(
            role=MessageRole.ASSISTANT,
            content=content or "",
            tool_use=tool_use,
        )
        self._messages.append(message)
        if content:
            self._update_token_estimate(content)
        return message

    def add_tool_result(
        self,
        tool_use_id: str,
        content: str,
        is_error: bool = False,
    ) -> Message:
        """
        Add a tool result message to the history (single tool).

        Args:
            tool_use_id: ID of the tool use request
            content: The tool result content
            is_error: Whether the tool execution failed

        Returns:
            The created Message
        """
        tool_result = ToolResult(
            tool_use_id=tool_use_id,
            content=content,
            is_error=is_error,
        )
        content_hash = self._hash_text(content)
        message = Message(
            role=MessageRole.TOOL,
            content=content,
            tool_result=tool_result,
            metadata={"tool_result_hashes": [content_hash]},
        )
        self._messages.append(message)
        self._tool_result_hashes.add(content_hash)
        self._update_token_estimate(content)
        return message

    def add_assistant_message_with_tools(
        self,
        content: str | None = None,
        tool_uses: list[ToolUse] | None = None,
    ) -> Message:
        """
        Add an assistant message with multiple tool calls.

        Used when Claude requests multiple tools in parallel.

        Args:
            content: Optional text content
            tool_uses: List of tool use requests

        Returns:
            The created Message
        """
        message = Message(
            role=MessageRole.ASSISTANT,
            content=content or "",
            tool_uses=tool_uses or [],
        )
        self._messages.append(message)
        if content:
            self._update_token_estimate(content)
        return message

    def add_tool_results(
        self,
        results: list[tuple[str, str, bool]],
    ) -> Message:
        """
        Add multiple tool results in a single message.

        This is required by Anthropic API when responding to parallel tool calls.

        Args:
            results: List of (tool_use_id, content, is_error) tuples

        Returns:
            The created Message
        """
        tool_results = [
            ToolResult(tool_use_id=tid, content=content, is_error=is_error)
            for tid, content, is_error in results
        ]
        content_hashes = [self._hash_text(content) for _, content, _ in results]

        # Combine content for token estimation
        combined_content = "\n".join(r[1] for r in results)

        message = Message(
            role=MessageRole.TOOL,
            content=combined_content,
            tool_results=tool_results,
            metadata={"tool_result_hashes": content_hashes},
        )
        self._messages.append(message)
        self._tool_result_hashes.update(content_hashes)
        self._update_token_estimate(combined_content)
        return message

    def to_anthropic_messages(self) -> list[dict[str, Any]]:
        """
        Convert history to Anthropic API message format.

        Returns:
            List of messages compatible with Anthropic messages API
        """
        messages = []
        for msg in self._messages:
            if msg.role != MessageRole.SYSTEM:
                messages.append(msg.to_anthropic_message())
        return messages

    def to_openai_messages(self) -> list[dict[str, Any]]:
        """
        Convert history to OpenAI API message format.

        The system prompt is included as the first message.
        Tool results expand into individual messages with role 'tool'.

        Returns:
            List of messages compatible with OpenAI chat completions API
        """
        messages: list[dict[str, Any]] = []
        # System prompt as first message
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        for msg in self._messages:
            if msg.role != MessageRole.SYSTEM:
                messages.extend(msg.to_openai_messages())
        return messages

    def get_system_prompt(self) -> str:
        """Get the system prompt."""
        return self.system_prompt

    def clear(self) -> None:
        """Clear all messages from history."""
        self._messages.clear()
        self._estimated_tokens = 0
        self._tool_result_hashes.clear()

    def truncate_to_recent(self, max_messages: int = 50) -> int:
        """
        Truncate history to most recent messages.

        Args:
            max_messages: Maximum number of messages to keep

        Returns:
            Number of messages removed
        """
        if len(self._messages) <= max_messages:
            return 0

        removed_count = len(self._messages) - max_messages
        self._messages = self._messages[-max_messages:]
        self._recalculate_tokens()
        return removed_count

    def _update_token_estimate(self, content: str) -> None:
        """Update token estimate with new content."""
        # Rough approximation: ~4 characters per token
        self._estimated_tokens += len(content) // 4

    def _recalculate_tokens(self) -> None:
        """Recalculate total token estimate."""
        total = len(self.system_prompt) // 4
        for msg in self._messages:
            if isinstance(msg.content, str):
                total += len(msg.content) // 4
        self._estimated_tokens = total
        self._recalculate_tool_result_hashes()

    def _recalculate_tool_result_hashes(self) -> None:
        """Recalculate tool result hash set from current messages."""
        hashes: set[str] = set()
        for msg in self._messages:
            if msg.metadata:
                hashes.update(msg.metadata.get("tool_result_hashes", []))
        self._tool_result_hashes = hashes

    @staticmethod
    def _hash_text(content: str) -> str:
        """Hash content for de-duplication tracking."""
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def to_dict(self) -> dict[str, Any]:
        """Serialize history to dictionary."""
        return {
            "system_prompt": self.system_prompt,
            "messages": [msg.to_dict() for msg in self._messages],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "MessageHistory":
        """Deserialize history from dictionary."""
        history = cls(system_prompt=data.get("system_prompt", ""))
        for msg_data in data.get("messages", []):
            history._messages.append(Message.from_dict(msg_data))
        history._recalculate_tokens()
        return history
