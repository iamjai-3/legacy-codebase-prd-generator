"""Database Analysis Agent for extracting and analyzing database table mappings."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.prompts.database_analysis import DatabaseAnalysisPrompts
from src.utils.logging_config import ExecutionTimer, get_logger
from src.utils.serialization import extract_json_object

logger = get_logger(__name__)


@dataclass
class DatabaseAnalysisResult:
    """Result from database analysis agent."""

    form_name: str
    tables_analyzed: int = 0
    relationships_mapped: int = 0
    legacy_tables: list[dict[str, Any]] = field(default_factory=list)
    target_tables: list[dict[str, Any]] = field(default_factory=list)
    table_mappings: list[dict[str, Any]] = field(default_factory=list)
    schema_summary: str = ""
    vectors_stored: int = 0


class DatabaseAnalysisAgent(BaseAgent[DatabaseAnalysisResult]):
    """
    Agent for analyzing database table mappings and relationships.

    Extracts comprehensive database schema information from documentation
    and stores it in the knowledge base for use in code migration.
    """

    def __init__(self) -> None:
        """Initialize the database analysis agent."""
        super().__init__("DatabaseAnalysisAgent")

    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for database analysis."""
        return DatabaseAnalysisPrompts.system_prompt(context.form_name)

    async def analyze(
        self,
        context: AgentContext,
        db_doc_path: str | None = None,
        **kwargs: Any,
    ) -> AgentResult[DatabaseAnalysisResult]:
        """
        Analyze database documentation and extract table mappings.

        Args:
            context: Agent execution context
            db_doc_path: Path to database documentation file (defaults to src/db_doc/Database_DOC.md)

        Returns:
            AgentResult with DatabaseAnalysisResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting database analysis",
            form_name=context.form_name,
            db_doc_path=db_doc_path,
        )

        try:
            # 1. Load form-specific database documentation
            db_content = self._load_database_doc(db_doc_path, context.form_name)

            # 2. Extract form-specific table structures and relationships
            table_analysis = await self._analyze_tables(context, db_content)

            # 3. Extract form-specific table mappings (legacy to target)
            mapping_analysis = await self._analyze_mappings(context, db_content)

            # 4. Generate form-specific schema summary
            schema_summary = await self._generate_schema_summary(
                context, db_content, table_analysis, mapping_analysis
            )

            # 5. Store in vector store
            vectors_stored = self._store_database_context(
                context.form_name,
                table_analysis,
                mapping_analysis,
                schema_summary,
            )

            # 6. Create result
            result = DatabaseAnalysisResult(
                form_name=context.form_name,
                tables_analyzed=len(table_analysis.get("tables", [])),
                relationships_mapped=len(mapping_analysis.get("relationships", [])),
                legacy_tables=table_analysis.get("legacy_tables", []),
                target_tables=table_analysis.get("target_tables", []),
                table_mappings=mapping_analysis.get("mappings", []),
                schema_summary=schema_summary,
                vectors_stored=vectors_stored,
            )

            self.logger.info(
                "Database analysis complete",
                form_name=context.form_name,
                tables_analyzed=result.tables_analyzed,
                relationships_mapped=result.relationships_mapped,
                vectors_stored=vectors_stored,
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            self.logger.error("Database analysis failed", error=str(e), form_name=context.form_name)
            return self.create_error_result(e, timer)

    def _load_database_doc(self, db_doc_path: str | None, form_name: str) -> str:
        """Load form-specific database documentation from MinIO or local file."""
        from src.utils.minio_sync import MinioSync

        form_name_upper = form_name.upper()

        # Try MinIO first: FORMS/{FORM_NAME}/FORM_DOCS/{FORM_NAME}_SourceTables.md
        try:
            minio_sync = MinioSync()
            minio_object_name = f"FORMS/{form_name_upper}/FORM_DOCS/{form_name_upper}_SourceTables.md"
            
            # Check if object exists in MinIO
            if minio_sync.file_exists(minio_object_name):
                content = minio_sync.get_file_text(minio_object_name)
                self.logger.info(
                    "Loaded form-specific source tables from MinIO",
                    object_name=minio_object_name,
                    form_name=form_name,
                )
                return content
        except Exception as e:
            self.logger.debug(f"MinIO lookup failed, trying local: {e}")

        # Fallback to local filesystem
        if db_doc_path is None:
            # Try to find form-specific source tables file first
            # Look for src/PRDs/{FORM_NAME}/FORM_DOCS/{FORM_NAME}_SourceTables.md
            form_specific_path = (
                Path(__file__).parent.parent.parent
                / "PRDs"
                / form_name_upper
                / "FORM_DOCS"
                / f"{form_name_upper}_SourceTables.md"
            )
            
            if form_specific_path.exists():
                db_doc_path = form_specific_path
                self.logger.info(
                    "Found form-specific source tables file (local)",
                    path=str(db_doc_path),
                    form_name=form_name,
                )
            else:
                # Fallback to full database doc
                db_doc_path = Path(__file__).parent.parent / "db_doc" / "Database_DOC.md"
                self.logger.info(
                    "Using full database documentation (form-specific not found)",
                    path=str(db_doc_path),
                    form_name=form_name,
                )

        db_path = Path(db_doc_path)
        if not db_path.exists():
            raise FileNotFoundError(f"Database documentation not found: {db_path}")

        self.logger.info("Loading database documentation", path=str(db_path), form_name=form_name)
        with open(db_path, encoding="utf-8") as f:
            content = f.read()

        self.logger.debug(
            "Database documentation loaded", size=len(content), path=str(db_path), form_name=form_name
        )
        return content

    async def _analyze_tables(self, context: AgentContext, db_content: str) -> dict[str, Any]:
        """Extract form-specific table structures from database documentation."""
        prompt = DatabaseAnalysisPrompts.extract_tables_prompt(db_content, context.form_name)

        response = await self.invoke_llm(context, prompt)

        # Try to extract JSON from response
        try:
            json_data = extract_json_object(response)
            if isinstance(json_data, dict):
                return json_data
        except Exception as e:
            self.logger.warning(f"Failed to parse JSON response: {e}")

        # Fallback: return structured text
        return {
            "tables": [],
            "legacy_tables": [],
            "target_tables": [],
            "raw_analysis": response,
        }

    async def _analyze_mappings(self, context: AgentContext, db_content: str) -> dict[str, Any]:
        """Extract form-specific table mappings between legacy and target schemas."""
        prompt = DatabaseAnalysisPrompts.extract_mappings_prompt(db_content, context.form_name)

        response = await self.invoke_llm(context, prompt)

        # Try to extract JSON from response
        try:
            json_data = extract_json_object(response)
            if isinstance(json_data, dict):
                return json_data
        except Exception as e:
            self.logger.warning(f"Failed to parse JSON response: {e}")

        # Fallback: return structured text
        return {
            "mappings": [],
            "relationships": [],
            "raw_analysis": response,
        }

    async def _generate_schema_summary(
        self,
        context: AgentContext,
        db_content: str,
        table_analysis: dict[str, Any],
        mapping_analysis: dict[str, Any],
    ) -> str:
        """Generate form-specific schema summary."""
        prompt = DatabaseAnalysisPrompts.generate_summary_prompt(
            db_content, table_analysis, mapping_analysis, context.form_name
        )

        response = await self.invoke_llm(context, prompt)
        return response

    def _store_database_context(
        self,
        form_name: str,
        table_analysis: dict[str, Any],
        mapping_analysis: dict[str, Any],
        schema_summary: str,
    ) -> int:
        """Store database context in vector store."""
        total_vectors = 0

        # Store table structures
        total_vectors += self._store_tables(
            form_name, table_analysis.get("legacy_tables", []), "legacy"
        )
        total_vectors += self._store_tables(
            form_name, table_analysis.get("target_tables", []), "target"
        )

        # Store table mappings
        total_vectors += self._store_mappings(form_name, mapping_analysis.get("mappings", []))

        # Store relationships
        total_vectors += self._store_relationships(
            form_name, mapping_analysis.get("relationships", [])
        )

        # Store schema summary
        if schema_summary:
            self.vector_store.add_text(
                form_name=form_name,
                text=schema_summary,
                metadata={
                    "doc_type": "database",
                    "chunk_type": "schema_summary",
                },
            )
            total_vectors += 1

        self.logger.info(
            "Stored database context in vector store",
            form_name=form_name,
            vectors_added=total_vectors,
        )

        return total_vectors

    def _store_tables(self, form_name: str, tables: list[dict[str, Any]], schema: str) -> int:
        """Store table structures in vector store."""
        count = 0
        for table in tables:
            table_text = self._format_table_for_storage(table, schema)
            self.vector_store.add_text(
                form_name=form_name,
                text=table_text,
                metadata={
                    "doc_type": "database",
                    "chunk_type": "table_structure",
                    "schema": schema,
                    "table_name": table.get("name", "unknown"),
                },
            )
            count += 1
        return count

    def _store_mappings(self, form_name: str, mappings: list[dict[str, Any]]) -> int:
        """Store table mappings in vector store."""
        count = 0
        for mapping in mappings:
            mapping_text = self._format_mapping_for_storage(mapping)
            self.vector_store.add_text(
                form_name=form_name,
                text=mapping_text,
                metadata={
                    "doc_type": "database",
                    "chunk_type": "table_mapping",
                    "legacy_table": mapping.get("legacy_table", "unknown"),
                    "target_table": mapping.get("target_table", "unknown"),
                },
            )
            count += 1
        return count

    def _store_relationships(self, form_name: str, relationships: list[dict[str, Any]]) -> int:
        """Store relationships in vector store."""
        count = 0
        for rel in relationships:
            rel_text = self._format_relationship_for_storage(rel)
            self.vector_store.add_text(
                form_name=form_name,
                text=rel_text,
                metadata={
                    "doc_type": "database",
                    "chunk_type": "relationship",
                    "from_table": rel.get("from_table", "unknown"),
                    "to_table": rel.get("to_table", "unknown"),
                },
            )
            count += 1
        return count

    def _format_table_for_storage(self, table: dict[str, Any], schema: str) -> str:
        """Format table information for vector storage."""
        lines = [
            f"Table: {table.get('name', 'unknown')} ({schema} schema)",
            f"Description: {table.get('description', 'N/A')}",
        ]

        lines.extend(self._format_columns(table.get("columns", [])))
        lines.extend(self._format_indexes(table.get("indexes", [])))
        lines.extend(self._format_table_relationships(table.get("relationships", [])))

        return "\n".join(lines)

    def _format_columns(self, columns: list[dict[str, Any]]) -> list[str]:
        """Format column information."""
        if not columns:
            return []
        lines = ["\nColumns:"]
        for col in columns:
            col_info = f"  - {col.get('name', 'unknown')}: {col.get('type', 'unknown')}"
            if col.get("primary_key"):
                col_info += " [PRIMARY KEY]"
            if col.get("foreign_key"):
                col_info += f" [FK -> {col.get('foreign_key')}]"
            if col.get("nullable") is False:
                col_info += " [NOT NULL]"
            lines.append(col_info)
        return lines

    def _format_indexes(self, indexes: list[dict[str, Any]]) -> list[str]:
        """Format index information."""
        if not indexes:
            return []
        lines = ["\nIndexes:"]
        for idx in indexes:
            lines.append(f"  - {idx.get('name', 'unknown')}: {idx.get('columns', [])}")
        return lines

    def _format_table_relationships(self, relationships: list[dict[str, Any]]) -> list[str]:
        """Format table relationship information."""
        if not relationships:
            return []
        lines = ["\nRelationships:"]
        for rel in relationships:
            lines.append(
                f"  - {rel.get('type', 'unknown')} -> {rel.get('target_table', 'unknown')}"
            )
        return lines

    def _format_mapping_for_storage(self, mapping: dict[str, Any]) -> str:
        """Format table mapping for vector storage."""
        lines = [
            f"Table Mapping: {mapping.get('legacy_table', 'unknown')} -> {mapping.get('target_table', 'unknown')}",
            f"Mapping Type: {mapping.get('mapping_type', 'direct')}",
        ]

        if mapping.get("field_mappings"):
            lines.append("\nField Mappings:")
            for field_map in mapping["field_mappings"]:
                lines.append(
                    f"  - {field_map.get('legacy_field', 'unknown')} -> {field_map.get('target_field', 'unknown')}"
                )

        if mapping.get("notes"):
            lines.append(f"\nNotes: {mapping.get('notes')}")

        return "\n".join(lines)

    def _format_relationship_for_storage(self, rel: dict[str, Any]) -> str:
        """Format relationship for vector storage."""
        lines = [
            f"Relationship: {rel.get('from_table', 'unknown')} -> {rel.get('to_table', 'unknown')}",
            f"Type: {rel.get('type', 'unknown')}",
        ]

        if rel.get("foreign_key"):
            lines.append(f"Foreign Key: {rel.get('foreign_key')}")

        if rel.get("description"):
            lines.append(f"Description: {rel.get('description')}")

        return "\n".join(lines)
