"""
Agentic AI Coding System.

This module provides an AI coding agent that works like Antigravity IDE,
using Anthropic Claude for reasoning and tool calling, and OpenAI for embeddings.

The agentic system can:
- Read and analyze legacy codebases
- Generate modern code (backend/.NET, frontend/React)
- Ensure 100% parity with documentation and legacy business logic
"""

from src.agentic.agentic_base import AgenticAgent, AgenticConfig
from src.agentic.agent_runner import AgentRunner
from src.agentic.message_history import MessageHistory, Message, MessageRole
from src.agentic.tool_registry import ToolRegistry, Tool


# Lazy getters to avoid circular imports
def get_migration_orchestrator():
    """Get the MigrationOrchestrator class."""
    from src.agentic.migration.migration_orchestrator import MigrationOrchestrator
    return MigrationOrchestrator


def get_db_migration_agent():
    """Get the DatabaseMigrationAgent class."""
    from src.agentic.migration.db_migration_agent import DatabaseMigrationAgent
    return DatabaseMigrationAgent


def get_ui_migration_agent():
    """Get the UIMigrationAgent class."""
    from src.agentic.migration.ui_migration_agent import UIMigrationAgent
    return UIMigrationAgent


def get_code_generation_agent():
    """Get the CodeGenerationAgent class."""
    from src.agentic.migration.code_generation_agent import CodeGenerationAgent
    return CodeGenerationAgent


__all__ = [
    # Core components
    "AgenticAgent",
    "AgenticConfig",
    "AgentRunner",
    "MessageHistory",
    "Message",
    "MessageRole",
    "ToolRegistry",
    "Tool",
    # Migration agent getters
    "get_migration_orchestrator",
    "get_db_migration_agent",
    "get_ui_migration_agent",
    "get_code_generation_agent",
]

