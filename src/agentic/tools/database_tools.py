"""
Database Tools for Agentic AI.

Provides database schema retrieval and table mapping functionality
using the existing knowledge base.
"""

from typing import Any

from src.vector_store.qdrant_manager import QdrantManager
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def get_database_schema(form_name: str) -> str:
    """
    Retrieve database schema information from the knowledge base.
    
    Searches for database documentation, table definitions, and
    schema information relevant to the specified form.
    
    Args:
        form_name: The form name to get schema for
        
    Returns:
        Formatted database schema information
    """
    try:
        manager = QdrantManager()
        
        # Search for database-related content
        results = manager.search(
            form_name=form_name,
            query="database schema table columns entity relationship",
            limit=15,
            filter_metadata={"doc_type": "database"},
        )
        
        if not results:
            # Try without filter
            results = manager.search(
                form_name=form_name,
                query="database schema table definition SQL entity",
                limit=10,
            )
        
        if not results:
            return f"No database schema found for form: {form_name}"
        
        lines = [f"# Database Schema for: {form_name}\n"]
        
        for i, result in enumerate(results, 1):
            source = "unknown"
            if result.metadata:
                source = result.metadata.get("file_path", result.metadata.get("source", "unknown"))
            
            lines.append(f"## Schema {i}")
            lines.append(f"Source: {source}")
            lines.append(f"\n{result.content}\n")
            lines.append("---")
        
        return "\n".join(lines)
        
    except Exception as e:
        logger.error(f"Database schema retrieval error: {e}")
        return f"Error retrieving database schema: {str(e)}"


def get_table_mappings(form_name: str, table_name: str | None = None) -> str:
    """
    Retrieve table mappings and relationships from the knowledge base.
    
    Args:
        form_name: The form name to get mappings for
        table_name: Optional specific table to get mappings for
        
    Returns:
        Formatted table mapping information
    """
    try:
        manager = QdrantManager()
        
        query = f"table mapping relationship foreign key {table_name or ''}"
        
        results = manager.search(
            form_name=form_name,
            query=query.strip(),
            limit=10,
        )
        
        if not results:
            if table_name:
                return f"No mappings found for table: {table_name}"
            return f"No table mappings found for form: {form_name}"
        
        lines = [f"# Table Mappings for: {form_name}"]
        if table_name:
            lines[0] += f" (Table: {table_name})"
        lines.append("")
        
        for i, result in enumerate(results, 1):
            source = "unknown"
            if result.metadata:
                source = result.metadata.get("file_path", result.metadata.get("source", "unknown"))
            
            lines.append(f"## Mapping {i}")
            lines.append(f"Source: {source}")
            lines.append(f"\n{result.content}\n")
            lines.append("---")
        
        return "\n".join(lines)
        
    except Exception as e:
        logger.error(f"Table mapping retrieval error: {e}")
        return f"Error retrieving table mappings: {str(e)}"


def get_entity_definition(form_name: str, entity_name: str) -> str:
    """
    Retrieve the definition of a specific entity/table.
    
    Args:
        form_name: The form name
        entity_name: Name of the entity/table to find
        
    Returns:
        Entity definition and related code
    """
    try:
        manager = QdrantManager()
        
        # Search for the specific entity
        results = manager.search(
            form_name=form_name,
            query=f"{entity_name} class entity table definition columns fields",
            limit=5,
        )
        
        if not results:
            return f"No definition found for entity: {entity_name}"
        
        lines = [f"# Entity Definition: {entity_name}\n"]
        
        for i, result in enumerate(results, 1):
            source = "unknown"
            if result.metadata:
                source = result.metadata.get("file_path", result.metadata.get("source", "unknown"))
            
            lines.append(f"## Source {i}: {source}")
            lines.append(f"\n{result.content}\n")
            lines.append("---")
        
        return "\n".join(lines)
        
    except Exception as e:
        logger.error(f"Entity definition retrieval error: {e}")
        return f"Error retrieving entity definition: {str(e)}"


def get_business_logic(form_name: str, topic: str) -> str:
    """
    Retrieve business logic related to a specific topic.
    
    Args:
        form_name: The form name
        topic: Topic/area to get business logic for
        
    Returns:
        Relevant business logic code and documentation
    """
    try:
        manager = QdrantManager()
        
        # Search for business logic
        results = manager.search(
            form_name=form_name,
            query=f"{topic} business logic validation rule calculation",
            limit=10,
            filter_metadata={"doc_type": "business_logic"},
        )
        
        if not results:
            # Try without filter
            results = manager.search(
                form_name=form_name,
                query=f"{topic} business logic implementation method",
                limit=10,
            )
        
        if not results:
            return f"No business logic found for topic: {topic}"
        
        lines = [f"# Business Logic: {topic}\n"]
        
        for i, result in enumerate(results, 1):
            source = "unknown"
            if result.metadata:
                source = result.metadata.get("file_path", result.metadata.get("source", "unknown"))
            
            lines.append(f"## Logic {i}")
            lines.append(f"Source: {source}")
            lines.append(f"\n{result.content}\n")
            lines.append("---")
        
        return "\n".join(lines)
        
    except Exception as e:
        logger.error(f"Business logic retrieval error: {e}")
        return f"Error retrieving business logic: {str(e)}"
