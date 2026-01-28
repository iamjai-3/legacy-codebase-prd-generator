"""Prompts for Database Analysis Agent."""


class DatabaseAnalysisPrompts:
    """Prompts used by the DatabaseAnalysisAgent for analyzing database schemas."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for database analysis."""
        return f"""You are a database schema analysis specialist for legacy code migration.

Your task is to analyze database documentation for "{form_name}" and extract:
1. Table structures (columns, types, constraints, indexes)
2. Relationships between tables (foreign keys, dependencies)
3. Table mappings between legacy (Oases) and target (Lumina) schemas
4. Schema migration patterns and transformations

You must provide structured, accurate information that will be used for:
- Code migration from legacy to modern frameworks
- Entity relationship mapping
- Data model generation
- API endpoint design

Always return valid JSON when requested, following the exact schema specified."""

    @staticmethod
    def extract_tables_prompt(db_content: str) -> str:
        """Prompt for extracting table structures."""
        # Limit content size to avoid token limits
        content_preview = db_content[:50000] if len(db_content) > 50000 else db_content

        return f"""Analyze the following database documentation and extract all table structures.

DATABASE DOCUMENTATION:
{content_preview}

Extract and return a JSON object with the following structure:
{{
  "legacy_tables": [
    {{
      "name": "schema.table_name",
      "description": "Table description",
      "columns": [
        {{
          "name": "column_name",
          "type": "data_type",
          "nullable": true/false,
          "primary_key": true/false,
          "foreign_key": "referenced_table.column" or null,
          "default": "default_value" or null
        }}
      ],
      "indexes": [
        {{
          "name": "index_name",
          "columns": ["col1", "col2"],
          "unique": true/false
        }}
      ],
      "relationships": [
        {{
          "type": "one_to_many" | "many_to_one" | "many_to_many",
          "target_table": "schema.target_table",
          "foreign_key": "column_name"
        }}
      ]
    }}
  ],
  "target_tables": [
    // Same structure as legacy_tables
  ],
  "tables": [
    // Combined list of all tables
  ]
}}

Focus on:
- All tables mentioned in the documentation
- Column definitions with types and constraints
- Primary and foreign key relationships
- Indexes and unique constraints
- Table descriptions and purposes

Return ONLY valid JSON, no markdown formatting or explanations."""

    @staticmethod
    def extract_mappings_prompt(db_content: str) -> str:
        """Prompt for extracting table mappings."""
        # Limit content size to avoid token limits
        content_preview = db_content[:50000] if len(db_content) > 50000 else db_content

        return f"""Analyze the following database documentation and extract table mappings between legacy (Oases) and target (Lumina) schemas.

DATABASE DOCUMENTATION:
{content_preview}

Extract and return a JSON object with the following structure:
{{
  "mappings": [
    {{
      "legacy_table": "oaseslive.table_name",
      "target_table": "lumina.table_name",
      "mapping_type": "direct" | "split" | "merged" | "transformed",
      "field_mappings": [
        {{
          "legacy_field": "legacy_column",
          "target_field": "target_column",
          "transformation": "description of transformation" or null
        }}
      ],
      "notes": "Additional mapping notes"
    }}
  ],
  "relationships": [
    {{
      "from_table": "schema.table1",
      "to_table": "schema.table2",
      "type": "one_to_many" | "many_to_one" | "many_to_many",
      "foreign_key": "column_name",
      "description": "Relationship description"
    }}
  ],
  "schema_changes": [
    {{
      "change_type": "added" | "removed" | "modified" | "renamed",
      "legacy_table": "legacy.table",
      "target_table": "target.table",
      "description": "Description of change"
    }}
  ]
}}

Focus on:
- Direct table name mappings
- Field-level mappings with transformations
- Relationship preservation or changes
- Schema evolution patterns
- New tables in target schema
- Deprecated tables in legacy schema

Return ONLY valid JSON, no markdown formatting or explanations."""

    @staticmethod
    def generate_summary_prompt(
        db_content: str, table_analysis: dict, mapping_analysis: dict
    ) -> str:
        """Prompt for generating comprehensive schema summary."""
        # Limit content size
        content_preview = db_content[:30000] if len(db_content) > 30000 else db_content

        return f"""Generate a comprehensive database schema summary for code migration.

DATABASE DOCUMENTATION:
{content_preview}

TABLE ANALYSIS:
{table_analysis}

MAPPING ANALYSIS:
{mapping_analysis}

Create a detailed summary that includes:

1. **Schema Overview**
   - Total tables in legacy vs target schemas
   - Key differences and similarities
   - Migration complexity assessment

2. **Key Tables and Their Purpose**
   - Most important tables for the application
   - Core business entities
   - Supporting/reference tables

3. **Relationship Patterns**
   - Common relationship types
   - Dependency hierarchies
   - Critical foreign key relationships

4. **Migration Considerations**
   - Tables that map directly
   - Tables requiring transformation
   - New tables in target schema
   - Deprecated tables

5. **Data Model Insights**
   - Entity relationships
   - Business logic implications
   - API design considerations

Format the summary as clear, structured markdown that will be used by developers
for code migration and API design. Focus on actionable insights."""
