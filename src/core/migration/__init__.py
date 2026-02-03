"""
Code Migration Agents.

Agentic AI agents for migrating legacy code to modern frameworks.
"""


def get_migration_orchestrator():
    """Get the MigrationOrchestrator class."""
    from src.core.migration.migration_orchestrator import MigrationOrchestrator

    return MigrationOrchestrator


def get_db_migration_agent():
    """Get the DatabaseMigrationAgent class."""
    from src.core.migration.db_migration_agent import DatabaseMigrationAgent

    return DatabaseMigrationAgent


def get_ui_migration_agent():
    """Get the UIMigrationAgent class."""
    from src.core.migration.ui_migration_agent import UIMigrationAgent

    return UIMigrationAgent


def get_code_generation_agent():
    """Get the CodeGenerationAgent class."""
    from src.core.migration.code_generation_agent import CodeGenerationAgent

    return CodeGenerationAgent


__all__ = [
    "get_migration_orchestrator",
    "get_db_migration_agent",
    "get_ui_migration_agent",
    "get_code_generation_agent",
]
