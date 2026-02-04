"""
Database Knowledge Tools for Agentic AI.

Provides tools for accessing database schema mappings and documentation
for accurate code migration from Oracle/Legacy to PostgreSQL/Target.
"""

import re

from src.tools.minio_tools import get_db_prd
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def search_legacy_schema(table_name: str) -> str:
    """
    Search for legacy (Oases) table schema and relationships.

    Args:
        table_name: Table name to search for (partial match supported)

    Returns:
        Schema information for matching tables
    """
    try:
        db_prd = get_db_prd()

        if "Error" in db_prd:
            return f"Database PRD not available: {db_prd}"

        # Search for table in legacy section
        table_lower = table_name.lower()
        lines = db_prd.split("\n")

        matches = []
        in_legacy_section = False

        for i, line in enumerate(lines):
            if "Legacy Schema Relationships" in line:
                in_legacy_section = True
            elif "Target Schema Relationships" in line:
                in_legacy_section = False

            if in_legacy_section and table_lower in line.lower():
                # Get context (5 lines before and after)
                start = max(0, i - 5)
                end = min(len(lines), i + 10)
                context = "\n".join(lines[start:end])
                matches.append(context)

        if matches:
            return f"# Legacy Schema Matches for: {table_name}\n\n" + "\n\n---\n\n".join(
                matches[:5]
            )

        return f"No legacy schema found for table: {table_name}"

    except Exception as e:
        logger.error(f"Error searching legacy schema: {e}")
        return f"Error: {str(e)}"


def search_target_schema(table_name: str) -> str:
    """
    Search for target (Lumina) table schema and relationships.

    Args:
        table_name: Table name to search for (partial match supported)

    Returns:
        Schema information for matching tables
    """
    try:
        db_prd = get_db_prd()

        if "Error" in db_prd:
            return f"Database PRD not available: {db_prd}"

        # Search for table in target section
        table_lower = table_name.lower()
        lines = db_prd.split("\n")

        matches = []
        in_target_section = False

        for i, line in enumerate(lines):
            if "Target Schema Relationships" in line:
                in_target_section = True

            if in_target_section and table_lower in line.lower():
                # Get context
                start = max(0, i - 5)
                end = min(len(lines), i + 10)
                context = "\n".join(lines[start:end])
                matches.append(context)

        if matches:
            return f"# Target Schema Matches for: {table_name}\n\n" + "\n\n---\n\n".join(
                matches[:5]
            )

        return f"No target schema found for table: {table_name}"

    except Exception as e:
        logger.error(f"Error searching target schema: {e}")
        return f"Error: {str(e)}"


def get_schema_comparison() -> str:
    """
    Get summary comparison between legacy and target schemas.

    Returns:
        Schema comparison summary with metrics
    """
    try:
        db_prd = get_db_prd()

        if "Error" in db_prd:
            return f"Database PRD not available: {db_prd}"

        # Extract comparison section
        lines = db_prd.split("\n")
        comparison_lines = []
        in_comparison = False

        for line in lines:
            if "Comparison Summary" in line:
                in_comparison = True
            elif "## Legacy Schema" in line or "## Target Schema" in line:
                if in_comparison:
                    break

            if in_comparison:
                comparison_lines.append(line)

        if comparison_lines:
            return "\n".join(comparison_lines[:30])

        return "Schema comparison summary not found in documentation."

    except Exception as e:
        logger.error(f"Error getting schema comparison: {e}")
        return f"Error: {str(e)}"


def get_table_relationships(table_name: str) -> str:
    """
    Get relationships for a specific table.

    Args:
        table_name: Table name to get relationships for

    Returns:
        Table relationships and foreign key information
    """
    try:
        db_prd = get_db_prd()

        if "Error" in db_prd:
            return f"Database PRD not available: {db_prd}"

        table_lower = table_name.lower()
        lines = db_prd.split("\n")

        # Find table entry with relationships
        relationship_info = []

        for i, line in enumerate(lines):
            if table_lower in line.lower() and "relationship" in line.lower():
                # Extract relationship count
                match = re.search(r"\((\d+)\s*relationship", line)
                if match:
                    count = match.group(1)
                    relationship_info.append(f"- {line.strip()} [{count} relationships]")

        if relationship_info:
            return f"# Relationships for: {table_name}\n\n" + "\n".join(relationship_info)

        # Fallback: search for table mentions
        for i, line in enumerate(lines):
            if table_lower in line.lower():
                return f"Found reference: {line.strip()}"

        return f"No relationship information found for: {table_name}"

    except Exception as e:
        logger.error(f"Error getting table relationships: {e}")
        return f"Error: {str(e)}"


def get_oracle_to_postgres_mapping() -> str:
    """
    Get Oracle to PostgreSQL data type mapping guide.

    Returns:
        Data type mapping reference for migration
    """
    return """# Oracle to PostgreSQL Data Type Mapping

| Oracle Type | PostgreSQL Type | Notes |
|-------------|-----------------|-------|
| VARCHAR2(n) | VARCHAR(n) | Direct mapping |
| CHAR(n) | CHAR(n) | Direct mapping |
| NUMBER | NUMERIC / INTEGER / BIGINT | Use INTEGER for whole numbers |
| NUMBER(p,s) | DECIMAL(p,s) | Exact precision |
| DATE | TIMESTAMP | Oracle DATE includes time |
| TIMESTAMP | TIMESTAMP | Direct mapping |
| CLOB | TEXT | Unlimited length |
| BLOB | BYTEA | Binary data |
| RAW | BYTEA | Binary data |
| LONG | TEXT | Deprecated in Oracle |
| ROWID | No equivalent | Use SERIAL/BIGSERIAL |
| XMLTYPE | XML or JSONB | Prefer JSONB for flexibility |

## Key PostgreSQL Features to Use

1. **SERIAL/BIGSERIAL** - Auto-incrementing primary keys
2. **JSONB** - Flexible schema for metadata fields
3. **TEXT[]** - Array types for tags/lists
4. **UUID** - Globally unique identifiers
5. **TIMESTAMP WITH TIME ZONE** - Timezone-aware dates

## Common Function Mappings

| Oracle | PostgreSQL |
|--------|------------|
| NVL(a,b) | COALESCE(a,b) |
| SYSDATE | CURRENT_TIMESTAMP |
| ROWNUM | LIMIT/OFFSET |
| DECODE | CASE WHEN |
| TO_CHAR | TO_CHAR (similar) |
| || | || or CONCAT() |
"""


def _parse_highly_connected_section(lines: list[str]) -> list[str]:
    """Extract lines from the 'Highly Connected Tables' section until next ##."""
    connected_tables = []
    in_section = False
    for line in lines:
        if "Highly Connected Tables" in line:
            in_section = True
            continue
        if in_section and line.startswith("##"):
            break
        if in_section and line.strip():
            connected_tables.append(line)
    return connected_tables


def _extract_high_rel_tables_from_lines(lines: list[str]) -> list[tuple[str, int]]:
    """Extract (table, relationship_count) from lines matching **table** (N relationship pattern."""
    high_rel_tables = []
    for line in lines:
        match = re.search(r"\*\*([^*]+)\*\*\s*\((\d+)\s*relationship", line)
        if match:
            table = match.group(1)
            count = int(match.group(2))
            if count >= 20:
                high_rel_tables.append((table, count))
    high_rel_tables.sort(key=lambda x: x[1], reverse=True)
    return high_rel_tables


def get_highly_connected_tables() -> str:
    """
    Get list of highly connected tables (many relationships).

    These are critical tables that require careful migration planning.

    Returns:
        List of tables with high relationship counts
    """
    try:
        db_prd = get_db_prd()
        if "Error" in db_prd:
            return f"Database PRD not available: {db_prd}"

        lines = db_prd.split("\n")
        connected_tables = _parse_highly_connected_section(lines)
        if connected_tables:
            return "# Highly Connected Tables\n\n" + "\n".join(connected_tables[:30])

        high_rel_tables = _extract_high_rel_tables_from_lines(lines)
        if high_rel_tables:
            output = ["# Highly Connected Tables (20+ relationships)\n"]
            output.extend(
                f"- **{table}** ({count} relationships)" for table, count in high_rel_tables[:20]
            )
            return "\n".join(output)

        return "No highly connected tables information found."

    except Exception as e:
        logger.error(f"Error getting highly connected tables: {e}")
        return f"Error: {str(e)}"
