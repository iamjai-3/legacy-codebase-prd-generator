"""
Message History Management for Agentic AI.

Manages conversation history with role-based messages, token counting,
and serialization for the agentic tool calling loop.
"""

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

    def to_anthropic_message(self) -> dict[str, Any]:
        """
        Convert to Anthropic API message format.

        Returns:
            Dict compatible with Anthropic messages API
        """
        if self.role == MessageRole.SYSTEM:
            # System messages are handled separately in Anthropic
            return {"role": "user", "content": self.content}

        # Handle multiple tool results (from parallel tool calls)
        if self.role == MessageRole.TOOL and self.tool_results:
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

        # Handle single tool result (legacy)
        if self.role == MessageRole.TOOL and self.tool_result:
            return {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": self.tool_result.tool_use_id,
                        "content": (
                            self.tool_result.content
                            if isinstance(self.tool_result.content, str)
                            else str(self.tool_result.content)
                        ),
                        "is_error": self.tool_result.is_error,
                    }
                ],
            }

        # Handle multiple tool uses (parallel tool calls)
        if self.role == MessageRole.ASSISTANT and self.tool_uses:
            content_blocks = []
            # Add text first if present
            if self.content and isinstance(self.content, str) and self.content.strip():
                content_blocks.append({"type": "text", "text": self.content})
            # Add all tool uses
            for tu in self.tool_uses:
                content_blocks.append(
                    {
                        "type": "tool_use",
                        "id": tu.id,
                        "name": tu.name,
                        "input": tu.input,
                    }
                )
            return {
                "role": "assistant",
                "content": content_blocks,
            }

        # Handle single tool use (legacy)
        if self.role == MessageRole.ASSISTANT and self.tool_use:
            content_blocks = []
            if self.content and isinstance(self.content, str) and self.content.strip():
                content_blocks.append({"type": "text", "text": self.content})
            content_blocks.append(
                {
                    "type": "tool_use",
                    "id": self.tool_use.id,
                    "name": self.tool_use.name,
                    "input": self.tool_use.input,
                }
            )
            return {
                "role": "assistant",
                "content": content_blocks,
            }

        return {
            "role": self.role.value,
            "content": self.content,
        }

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
        message = Message(
            role=MessageRole.TOOL,
            content=content,
            tool_result=tool_result,
        )
        self._messages.append(message)
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

        # Combine content for token estimation
        combined_content = "\n".join(r[1] for r in results)

        message = Message(
            role=MessageRole.TOOL,
            content=combined_content,
            tool_results=tool_results,
        )
        self._messages.append(message)
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

    def get_system_prompt(self) -> str:
        """Get the system prompt."""
        return self.system_prompt

    def clear(self) -> None:
        """Clear all messages from history."""
        self._messages.clear()
        self._estimated_tokens = 0

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
