"""
Base Agent class for all specialized PRD agents.

Provides common functionality for:
- LLM invocation with retry logic
- Vector store context retrieval
- Structured response parsing
- Execution timing and logging
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Generic, TypeVar

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from src.config.settings import get_settings
from src.utils.logging_config import ExecutionTimer, get_logger
from src.utils.serialization import (
    extract_json_array,
    extract_json_object,
    from_dict_list,
    parse_list_response,
)
from src.vector_store.qdrant_manager import QdrantManager

# Type variable for agent output
T = TypeVar("T")


@dataclass
class AgentContext:
    """Context passed to agents during execution."""

    form_name: str
    form_title: str = ""
    description: str = ""
    additional_context: dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentResult(Generic[T]):
    """Result from agent execution."""

    agent_name: str
    success: bool
    data: T | None = None
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    execution_time_ms: float = 0.0


class BaseAgent(ABC, Generic[T]):
    """
    Abstract base class for all PRD generation agents.

    Each specialized agent inherits from this class and implements
    the analyze method to perform its specific analysis task.

    Provides reusable methods for:
    - LLM invocation with vision support
    - JSON/list response parsing
    - Vector store context retrieval
    - Execution result creation
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the base agent.

        Args:
            name: Name of the agent
        """
        self.name = name
        self.settings = get_settings()
        self._llm: ChatOpenAI | None = None
        self._vector_store: QdrantManager | None = None
        self.logger = get_logger(name, agent=name)

    @property
    def llm(self) -> ChatOpenAI:
        """Get or create the LLM instance."""
        if self._llm is None:
            self._llm = ChatOpenAI(
                model=self.settings.openai.model,
                openai_api_key=self.settings.openai.api_key,
                temperature=self.settings.openai.temperature,
                max_tokens=self.settings.openai.max_tokens,
            )
            self.logger.debug("Initialized LLM", model=self.settings.openai.model)
        return self._llm

    @property
    def vector_store(self) -> QdrantManager:
        """Get or create the vector store manager."""
        if self._vector_store is None:
            self._vector_store = QdrantManager()
        return self._vector_store

    @abstractmethod
    def get_system_prompt(self, context: AgentContext) -> str:
        """
        Get the system prompt for this agent.

        Args:
            context: The agent execution context

        Returns:
            System prompt string
        """
        pass

    @abstractmethod
    async def analyze(self, context: AgentContext, **kwargs: Any) -> AgentResult[T]:
        """
        Perform the agent's analysis task.

        Args:
            context: The agent execution context
            **kwargs: Additional keyword arguments specific to the agent

        Returns:
            AgentResult with the analysis output
        """
        pass

    # ========== LLM Invocation Methods ==========

    async def invoke_llm(
        self, context: AgentContext, user_prompt: str, images: list[str] | None = None
    ) -> str:
        """
        Invoke the LLM with system and user prompts.

        Args:
            context: The agent context
            user_prompt: The user message content
            images: Optional list of base64-encoded images for vision

        Returns:
            LLM response as string
        """
        system_prompt = self.get_system_prompt(context)
        messages = [SystemMessage(content=system_prompt)]

        if images:
            # Use vision-capable message format
            content: list[dict[str, Any]] = [{"type": "text", "text": user_prompt}]
            for img in images:
                content.append(
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img}"}}
                )
            messages.append(HumanMessage(content=content))
        else:
            messages.append(HumanMessage(content=user_prompt))

        self.logger.debug(
            "Invoking LLM",
            prompt_length=len(user_prompt),
            has_images=bool(images),
            image_count=len(images) if images else 0,
        )

        response = await self.llm.ainvoke(messages)
        return str(response.content)

    async def invoke_llm_for_json_array(
        self,
        context: AgentContext,
        prompt: str,
        result_class: type[T],
    ) -> list[T]:
        """
        Invoke LLM and parse response as a list of dataclass instances.

        Args:
            context: The agent context
            prompt: The prompt expecting a JSON array response
            result_class: Dataclass type to parse each array item into

        Returns:
            List of parsed dataclass instances
        """
        response = await self.invoke_llm(context, prompt)
        json_data = extract_json_array(response)
        return from_dict_list(json_data, result_class)

    async def invoke_llm_for_json_object(
        self,
        context: AgentContext,
        prompt: str,
    ) -> dict[str, Any]:
        """
        Invoke LLM and parse response as a JSON object.

        Args:
            context: The agent context
            prompt: The prompt expecting a JSON object response

        Returns:
            Parsed dictionary
        """
        response = await self.invoke_llm(context, prompt)
        return extract_json_object(response)

    async def invoke_llm_for_list(
        self,
        context: AgentContext,
        prompt: str,
        prefix: str = "",
    ) -> list[str]:
        """
        Invoke LLM and parse response as a text list.

        Args:
            context: The agent context
            prompt: The prompt expecting a list response
            prefix: Optional prefix to filter lines (e.g., "BR-")

        Returns:
            List of extracted items
        """
        response = await self.invoke_llm(context, prompt)
        return parse_list_response(response, prefix)

    # ========== Vector Store Methods ==========

    def retrieve_context(
        self,
        form_name: str,
        query: str,
        limit: int = 5,
        doc_type: str | None = None,
        chunk_type: str | None = None,
    ) -> list[str]:
        """
        Retrieve relevant context from the vector store.

        Args:
            form_name: Name of the form collection
            query: Search query
            limit: Maximum number of results
            doc_type: Optional document type filter (e.g., "code", "class_definition", "business_logic")
            chunk_type: Optional chunk type filter (e.g., "class_definition", "method_implementation")

        Returns:
            List of relevant context strings
        """
        try:
            filter_metadata = {}
            if doc_type:
                filter_metadata["doc_type"] = doc_type
            if chunk_type:
                filter_metadata["chunk_type"] = chunk_type

            filter_metadata = filter_metadata if filter_metadata else None

            results = self.vector_store.search(
                form_name=form_name,
                query=query,
                limit=limit,
                filter_metadata=filter_metadata,
            )
            return [r.content for r in results]
        except Exception as e:
            self.logger.warning(
                "Failed to retrieve context from vector store",
                error=str(e),
                form_name=form_name,
                query=query[:50],
            )
            return []

    def format_context_for_prompt(self, contexts: list[str], max_contexts: int = 5) -> str:
        """
        Format retrieved contexts for inclusion in a prompt.

        Args:
            contexts: List of context strings
            max_contexts: Maximum number of contexts to include

        Returns:
            Formatted context string
        """
        if not contexts:
            return "No additional context available."

        limited = contexts[:max_contexts]
        formatted = [f"[Context {i}]\n{ctx}\n" for i, ctx in enumerate(limited, 1)]
        return "\n".join(formatted)

    # ========== Result Creation Methods ==========

    def create_success_result(
        self, data: T, timer: ExecutionTimer, **metadata: Any
    ) -> AgentResult[T]:
        """
        Create a successful agent result.

        Args:
            data: The result data
            timer: Execution timer for duration
            **metadata: Additional metadata to include

        Returns:
            AgentResult with success=True
        """
        return AgentResult(
            agent_name=self.name,
            success=True,
            data=data,
            execution_time_ms=timer.elapsed_ms(),
            metadata=metadata,
        )

    def create_error_result(
        self,
        error: str | Exception,
        timer: ExecutionTimer,
    ) -> AgentResult[T]:
        """
        Create a failed agent result.

        Args:
            error: Error message or exception
            timer: Execution timer for duration

        Returns:
            AgentResult with success=False
        """
        error_msg = str(error) if isinstance(error, Exception) else error
        self.logger.error("Agent execution failed", error=error_msg)

        return AgentResult(
            agent_name=self.name,
            success=False,
            error=error_msg,
            execution_time_ms=timer.elapsed_ms(),
        )
