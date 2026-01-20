"""
SQL DDL Parser for extracting table structures from SQL files.
Parses CREATE TABLE statements to extract columns, types, and constraints.
"""

import re
from dataclasses import dataclass, field
from typing import Any

# Constants
PRIMARY_KEY_CONSTRAINT = "PRIMARY KEY"


@dataclass
class SQLColumn:
    """Represents a column in a SQL table."""

    name: str
    data_type: str
    constraints: list[str] = field(default_factory=list)
    is_primary_key: bool = False
    is_not_null: bool = False
    description: str = ""


@dataclass
class SQLForeignKey:
    """Represents a foreign key constraint."""

    columns: list[str]
    references_table: str
    references_columns: list[str]
    on_delete: str = ""
    on_update: str = ""


@dataclass
class SQLIndex:
    """Represents a database index."""

    name: str
    columns: list[str]
    is_unique: bool = False


@dataclass
class ParsedTable:
    """Represents a parsed SQL table definition."""

    table_name: str
    columns: list[SQLColumn] = field(default_factory=list)
    primary_key: list[str] = field(default_factory=list)
    foreign_keys: list[SQLForeignKey] = field(default_factory=list)
    indexes: list[SQLIndex] = field(default_factory=list)
    grants: list[str] = field(default_factory=list)
    source_file: str = ""
    raw_ddl: str = ""


class SQLDDLParser:
    """Parser for Oracle/SQL DDL statements."""

    def __init__(self) -> None:
        """Initialize the SQL DDL parser."""
        pass

    def parse_create_table(self, sql_content: str, source_file: str = "") -> list[ParsedTable]:
        """
        Parse CREATE TABLE statements from SQL content.

        Args:
            sql_content: Raw SQL content
            source_file: Source file path for reference

        Returns:
            List of ParsedTable objects
        """
        tables = []

        # Find all CREATE TABLE statements (Oracle style)
        create_pattern = r'CREATE\s+TABLE\s+"?(\w+)"?\s*\(\s*(.*?)\s*\)\s*;'
        matches = re.findall(create_pattern, sql_content, re.IGNORECASE | re.DOTALL)

        for table_name, columns_str in matches:
            parsed_table = self._parse_table_definition(
                table_name, columns_str, sql_content, source_file
            )
            if parsed_table:
                tables.append(parsed_table)

        return tables

    def _process_column_definition(
        self, col_def: str, columns: list, primary_key: list[str], foreign_keys: list
    ) -> bool:
        """Process a single column definition. Returns True if processed, False otherwise."""
        if col_def.upper().startswith(PRIMARY_KEY_CONSTRAINT):
            self._extract_primary_key(col_def, primary_key)
            return True
        if col_def.upper().startswith("FOREIGN KEY"):
            fk = self._parse_foreign_key(col_def)
            if fk:
                foreign_keys.append(fk)
            return True
        if col_def.upper().startswith("CONSTRAINT"):
            return True
        column = self._parse_column(col_def)
        if column:
            columns.append(column)
            if column.is_primary_key:
                primary_key.append(column.name)
        return False

    def _extract_primary_key(self, col_def: str, primary_key: list[str]) -> None:
        """Extract primary key columns from definition."""
        pk_match = re.search(r"PRIMARY\s+KEY\s*\(([^)]+)\)", col_def, re.IGNORECASE)
        if pk_match:
            pk_cols = [c.strip().strip('"') for c in pk_match.group(1).split(",")]
            primary_key.extend(pk_cols)

    def _parse_table_definition(
        self, table_name: str, columns_str: str, full_sql: str, source_file: str
    ) -> ParsedTable:
        """Parse a single table definition."""
        columns = []
        primary_key = []
        foreign_keys = []

        # Split by commas, but handle nested parentheses
        column_defs = self._split_column_definitions(columns_str)

        for col_def in column_defs:
            col_def = col_def.strip()
            if not col_def:
                continue

            if self._process_column_definition(col_def, columns, primary_key, foreign_keys):
                continue

        # Parse GRANT statements
        grants = self._parse_grants(full_sql, table_name)

        # Extract raw DDL for this table
        ddl_pattern = rf'CREATE\s+TABLE\s+"?{re.escape(table_name)}"?\s*\([^;]+\);'
        ddl_match = re.search(ddl_pattern, full_sql, re.IGNORECASE | re.DOTALL)
        raw_ddl = ddl_match.group(0) if ddl_match else ""

        return ParsedTable(
            table_name=table_name,
            columns=columns,
            primary_key=primary_key,
            foreign_keys=foreign_keys,
            indexes=[],  # Indexes are typically in separate statements
            grants=grants,
            source_file=source_file,
            raw_ddl=raw_ddl,
        )

    def _split_column_definitions(self, columns_str: str) -> list[str]:
        """Split column definitions handling nested parentheses."""
        result = []
        current = ""
        paren_depth = 0

        for char in columns_str:
            if char == "(":
                paren_depth += 1
                current += char
            elif char == ")":
                paren_depth -= 1
                current += char
            elif char == "," and paren_depth == 0:
                if current.strip():
                    result.append(current.strip())
                current = ""
            else:
                current += char

        if current.strip():
            result.append(current.strip())

        return result

    def _parse_column(self, col_def: str) -> SQLColumn | None:
        """Parse a single column definition."""
        # Match: "COLUMN_NAME" TYPE(size) [constraints]
        # or: COLUMN_NAME TYPE(size) [constraints]
        pattern = r'"?(\w+)"?\s+(\w+(?:\([^)]+\))?)(?:\s+(.+))?'
        match = re.match(pattern, col_def.strip(), re.IGNORECASE)

        if not match:
            return None

        col_name = match.group(1)
        data_type = match.group(2).upper()
        constraints_str = match.group(3) or ""

        # Parse constraints
        constraints = []
        is_pk = False
        is_not_null = False

        if PRIMARY_KEY_CONSTRAINT in constraints_str.upper():
            is_pk = True
            constraints.append(PRIMARY_KEY_CONSTRAINT)

        if "NOT NULL" in constraints_str.upper():
            is_not_null = True
            constraints.append("NOT NULL")

        if "UNIQUE" in constraints_str.upper():
            constraints.append("UNIQUE")

        if "DEFAULT" in constraints_str.upper():
            default_match = re.search(r"DEFAULT\s+(\S+)", constraints_str, re.IGNORECASE)
            if default_match:
                constraints.append(f"DEFAULT {default_match.group(1)}")

        # Check for foreign key references
        if "REFERENCES" in constraints_str.upper():
            ref_match = re.search(r"REFERENCES\s+(\w+)\s*\((\w+)\)", constraints_str, re.IGNORECASE)
            if ref_match:
                constraints.append(f"FK to {ref_match.group(1)}")

        return SQLColumn(
            name=col_name,
            data_type=data_type,
            constraints=constraints,
            is_primary_key=is_pk,
            is_not_null=is_not_null,
        )

    def _parse_foreign_key(self, fk_def: str) -> SQLForeignKey | None:
        """Parse a foreign key constraint definition."""
        # FOREIGN KEY (col) REFERENCES table(col)
        pattern = r"FOREIGN\s+KEY\s*\(([^)]+)\)\s*REFERENCES\s+(\w+)\s*\(([^)]+)\)"
        match = re.search(pattern, fk_def, re.IGNORECASE)

        if not match:
            return None

        columns = [c.strip().strip('"') for c in match.group(1).split(",")]
        ref_table = match.group(2)
        ref_columns = [c.strip().strip('"') for c in match.group(3).split(",")]

        # Parse ON DELETE/UPDATE
        on_delete = ""
        on_update = ""
        if "ON DELETE" in fk_def.upper():
            del_match = re.search(r"ON\s+DELETE\s+(\w+)", fk_def, re.IGNORECASE)
            if del_match:
                on_delete = del_match.group(1).upper()

        if "ON UPDATE" in fk_def.upper():
            upd_match = re.search(r"ON\s+UPDATE\s+(\w+)", fk_def, re.IGNORECASE)
            if upd_match:
                on_update = upd_match.group(1).upper()

        return SQLForeignKey(
            columns=columns,
            references_table=ref_table,
            references_columns=ref_columns,
            on_delete=on_delete,
            on_update=on_update,
        )

    def _parse_grants(self, sql_content: str, table_name: str) -> list[str]:
        """Parse GRANT statements for a table."""
        grants = []
        grant_pattern = rf'GRANT\s+(\w+)\s+ON\s+"?{re.escape(table_name)}"?\s+TO\s+"?(\w+)"?'
        matches = re.findall(grant_pattern, sql_content, re.IGNORECASE)

        for permission, grantee in matches:
            grants.append(f"{permission} TO {grantee}")

        return grants

    def parse_java_code_for_tables(self, java_content: str) -> dict[str, Any]:
        """
        Extract table and column references from Java code.

        Args:
            java_content: Java source code

        Returns:
            Dictionary with extracted table/column references
        """
        result = {
            "tables": set(),
            "columns": [],
            "sql_queries": [],
            "data_access_patterns": [],
        }

        # Find SQL strings in Java
        sql_patterns = [
            r'(?:"|\'|""")([^"\']*(?:SELECT|INSERT|UPDATE|DELETE|FROM|INTO|WHERE)[^"\']*?)(?:"|\'|""")',
            r'\.(?:executeQuery|executeUpdate|prepareStatement)\s*\(\s*["\']([^"\']+)',
        ]

        for pattern in sql_patterns:
            matches = re.findall(pattern, java_content, re.IGNORECASE)
            for match in matches:
                result["sql_queries"].append(match.strip())

                # Extract table names from SQL
                table_match = re.findall(r"(?:FROM|INTO|UPDATE|JOIN)\s+(\w+)", match, re.IGNORECASE)
                result["tables"].update(table_match)

        # Find field code references (legacy system pattern)
        field_patterns = [
            r"setDataList\s*\(\s*new\s+String\[\]\[\]\s*\{\s*\{([^}]+)\}",
            r'"([A-Z]{4,})"',  # Field codes like "LEEKFL", "LEEKCH"
        ]

        for pattern in field_patterns:
            matches = re.findall(pattern, java_content)
            for match in matches:
                if pattern.startswith('"'):
                    result["columns"].append(match)
                else:
                    cols = [c.strip().strip('"') for c in match.split(",")]
                    result["columns"].extend(cols)

        result["tables"] = list(result["tables"])
        result["columns"] = list(set(result["columns"]))

        return result


def parse_sql_files(code_files: list[Any]) -> list[ParsedTable]:
    """
    Parse all SQL files from a list of code files.

    Args:
        code_files: List of CodeFile objects

    Returns:
        List of ParsedTable objects
    """
    parser = SQLDDLParser()
    all_tables = []

    for cf in code_files:
        if hasattr(cf, "language") and cf.language == "sql":
            tables = parser.parse_create_table(cf.content, cf.path)
            all_tables.extend(tables)

    return all_tables


def extract_table_references_from_java(code_files: list[Any]) -> dict[str, Any]:
    """
    Extract table and SQL references from Java code files.

    Args:
        code_files: List of CodeFile objects

    Returns:
        Dictionary with extracted references
    """
    parser = SQLDDLParser()
    combined = {"tables": set(), "columns": [], "sql_queries": [], "data_access_patterns": []}

    for cf in code_files:
        if hasattr(cf, "language") and cf.language == "java":
            refs = parser.parse_java_code_for_tables(cf.content)
            combined["tables"].update(refs["tables"])
            combined["columns"].extend(refs["columns"])
            combined["sql_queries"].extend(refs["sql_queries"])

    combined["tables"] = list(combined["tables"])
    combined["columns"] = list(set(combined["columns"]))

    return combined


def tables_to_markdown(tables: list[ParsedTable]) -> str:
    """
    Convert parsed tables to Markdown documentation.

    Args:
        tables: List of ParsedTable objects

    Returns:
        Markdown string
    """
    if not tables:
        return "No tables found in source code."

    lines = ["## Database Tables\n"]

    for table in tables:
        _append_table_markdown(table, lines)

    return "\n".join(lines)


def _append_table_markdown(table: ParsedTable, lines: list[str]) -> None:
    """Append markdown for a single table."""
    lines.append(f"### {table.table_name}")
    lines.append(f"\n**Source:** `{table.source_file}`\n")
    _append_table_columns(table, lines)
    _append_table_keys(table, lines)
    _append_table_grants(table, lines)
    lines.append("\n---\n")


def _append_table_columns(table: ParsedTable, lines: list[str]) -> None:
    """Append columns table to markdown."""
    lines.append("| Column | Type | Constraints |")
    lines.append("|--------|------|-------------|")
    for col in table.columns:
        constraints = ", ".join(col.constraints) if col.constraints else "—"
        lines.append(f"| `{col.name}` | {col.data_type} | {constraints} |")


def _append_table_keys(table: ParsedTable, lines: list[str]) -> None:
    """Append primary and foreign keys to markdown."""
    if table.primary_key:
        lines.append(f"\n**Primary Key:** `{', '.join(table.primary_key)}`")
    if table.foreign_keys:
        lines.append("\n**Foreign Keys:**")
        for fk in table.foreign_keys:
            lines.append(
                f"- `{', '.join(fk.columns)}` → `{fk.references_table}({', '.join(fk.references_columns)})`"
            )


def _append_table_grants(table: ParsedTable, lines: list[str]) -> None:
    """Append grants to markdown."""
    if table.grants:
        lines.append(f"\n**Grants:** {', '.join(table.grants)}")
