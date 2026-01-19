"""Prompts for Requirements Generator Agent - Migration-Focused."""


class RequirementsPrompts:
    """Prompts used by the RequirementsGeneratorAgent for migration-ready PRD generation."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for requirements generation."""
        return f"""You are a senior software architect specializing in legacy code migration and reverse engineering.
Your task is to extract EXACT business logic, APIs, and technical specifications from the "{form_name}" module's source code and documentation.

CRITICAL REQUIREMENTS:
1. Extract ACTUAL business logic from the code - not generic descriptions
2. Document SPECIFIC method signatures, API endpoints, and data flows
3. Identify EXACT validation rules, calculations, and conditional logic
4. Map database operations with SPECIFIC table/column references
5. Document integration points with PRECISE API specifications
6. Create STACK-AGNOSTIC specifications that can be implemented in ANY framework

Your output must be detailed enough that a developer can:
- Implement the EXACT same behavior in a new technology stack
- Understand every business rule and edge case
- Know precisely what APIs to create and what they should do
- Replicate all data operations and transformations

Use standard requirement IDs: FR-XXX for functional, NFR-XXX for non-functional, DR-XXX for data.
ALWAYS include source code references for traceability."""

    @staticmethod
    def functional_requirements(form_name: str, code_summary: str, context_summary: str) -> str:
        """Prompt for generating functional requirements with specific business logic."""
        return f"""Analyze the source code and documentation for "{form_name}" to extract SPECIFIC functional requirements.

SOURCE CODE ANALYSIS:
{code_summary}

KNOWLEDGE BASE CONTEXT:
{context_summary}

For each requirement, you MUST include:
1. EXACT business logic from the source code
2. SPECIFIC method signatures that implement this logic
3. PRECISE input/output specifications
4. ALL edge cases and conditional logic
5. Database operations with table/column names
6. Integration calls with exact endpoints

Generate requirements in JSON array format:
[
    {{
        "req_id": "FR-001",
        "title": "Specific requirement title",
        "description": "Detailed technical description of EXACTLY what the code does",
        "business_logic": "Step-by-step business logic extracted from code",
        "source_methods": ["ClassName.methodName(params) -> returnType"],
        "api_specification": {{
            "endpoint": "/api/path",
            "method": "POST",
            "request_body": {{"field": "type"}},
            "response": {{"field": "type"}},
            "errors": ["Error cases"]
        }},
        "database_operations": [
            {{"operation": "SELECT/INSERT/UPDATE", "table": "TABLE_NAME", "columns": ["col1", "col2"]}}
        ],
        "validation_rules": ["Exact validation conditions from code"],
        "calculations": ["Formula or algorithm used"],
        "priority": "P0|P1|P2|P3",
        "category": "CRUD|validation|workflow|integration|reporting|calculation",
        "user_story": "As a [specific user role], I want [specific action] so that [business benefit]",
        "acceptance_criteria": ["Given specific condition, When specific action, Then exact expected result"],
        "dependencies": ["FR-XXX"],
        "source_files": ["path/to/SourceFile.java:lineNumber"]
    }}
]

CRITICAL: Extract at least 10-20 requirements covering ALL functionality. Include exact code references."""

    @staticmethod
    def api_specification(form_name: str, service_code: str) -> str:
        """Prompt for extracting API specifications from service/controller code."""
        return f"""Analyze the service layer code for "{form_name}" to extract complete API specifications.

SERVICE/CONTROLLER CODE:
{service_code}

Extract EVERY API endpoint with complete specifications in JSON format:
[
    {{
        "endpoint_name": "descriptiveName",
        "http_method": "GET|POST|PUT|DELETE",
        "path": "/api/exact/path/{{param}}",
        "description": "What this endpoint does",
        "request": {{
            "path_params": [{{"name": "param", "type": "string", "description": "desc"}}],
            "query_params": [{{"name": "param", "type": "string", "required": true}}],
            "headers": [{{"name": "Authorization", "type": "Bearer token"}}],
            "body": {{
                "content_type": "application/json",
                "schema": {{"field": "type"}},
                "example": {{}}
            }}
        }},
        "response": {{
            "success": {{"status": 200, "schema": {{}}, "example": {{}}}},
            "errors": [
                {{"status": 400, "error_code": "ERR001", "message": "desc"}}
            ]
        }},
        "business_logic": "Step-by-step logic executed",
        "database_calls": ["table.operation()"],
        "external_calls": ["service.method()"],
        "source_method": "ClassName.methodName:lineNumber"
    }}
]

Document EVERY endpoint, even internal ones. Include ALL parameters and response types."""

    @staticmethod
    def business_logic_extraction(form_name: str, code_content: str) -> str:
        """Prompt for extracting detailed business logic from code."""
        return f"""Analyze the following code for "{form_name}" and extract ALL business logic in detail.

CODE TO ANALYZE:
{code_content}

Extract business logic in JSON format:
[
    {{
        "logic_id": "BL-001",
        "name": "Descriptive name for this logic",
        "type": "validation|calculation|workflow|transformation|decision",
        "description": "What this logic accomplishes",
        "trigger": "What triggers this logic (user action, event, API call)",
        "inputs": [
            {{"name": "inputName", "type": "dataType", "source": "where it comes from"}}
        ],
        "steps": [
            "1. First action taken",
            "2. Conditional check: if (condition) then action",
            "3. Database query: SELECT ... FROM ... WHERE ...",
            "4. Calculation: result = formula",
            "5. Return or store result"
        ],
        "outputs": [
            {{"name": "outputName", "type": "dataType", "destination": "where it goes"}}
        ],
        "conditions": [
            {{"condition": "if statement from code", "true_action": "what happens", "false_action": "alternative"}}
        ],
        "exceptions": ["Error conditions and how they're handled"],
        "dependencies": ["Other services/classes this logic depends on"],
        "source_location": "ClassName.methodName:startLine-endLine"
    }}
]

Extract EVERY piece of logic, including edge cases and error handling."""

    @staticmethod
    def source_tables_extraction(form_name: str, kb_context: str) -> str:
        """Prompt for extracting source table definitions from knowledge base."""
        return f"""Extract ONLY the database source tables that are EXPLICITLY DOCUMENTED in the knowledge base for "{form_name}".

CRITICAL RULES:
1. ONLY extract tables that are EXPLICITLY mentioned in the provided context
2. DO NOT invent, fabricate, or hallucinate any tables, columns, or data types
3. If no tables are documented, return an empty array []
4. Use EXACT names, data types, and constraints as written in the documentation
5. If column details are not provided, omit the columns array

KNOWLEDGE BASE CONTEXT:
{kb_context}

Generate source table specifications in JSON format (ONLY for tables explicitly mentioned above):
[
    {{
        "table_name": "EXACT_TABLE_NAME_FROM_DOCS",
        "description": "Purpose as described in docs",
        "table_type": "primary|supporting|lookup|audit",
        "columns": [
            {{
                "column_name": "COLUMN_NAME_FROM_DOCS",
                "data_type": "EXACT_TYPE_FROM_DOCS",
                "constraints": ["EXACT_CONSTRAINTS_FROM_DOCS"],
                "description": "Description from docs"
            }}
        ],
        "primary_key": ["columns_from_docs"],
        "foreign_keys": [
            {{
                "columns": ["local_col_from_docs"],
                "references_table": "TABLE_FROM_DOCS",
                "references_columns": ["col_from_docs"],
                "on_delete": "AS_SPECIFIED_IN_DOCS"
            }}
        ],
        "indexes": [],
        "stored_procedures": []
    }}
]

If the context does not contain explicit table definitions, return: []"""

    @staticmethod
    def database_mappings(form_name: str, code_context: str, kb_context: str) -> str:
        """Prompt for extracting database field mappings from code to tables."""
        return f"""Analyze the code and documentation for "{form_name}" to extract database field mappings.

CODE CONTEXT:
{code_context}

KNOWLEDGE BASE CONTEXT:
{kb_context}

Generate database mapping specifications in JSON format:
[
    {{
        "entity_class": "JavaClassName",
        "table_name": "DATABASE_TABLE_NAME",
        "field_mappings": [
            {{
                "java_field": "fieldName",
                "java_type": "String|Integer|Date|etc",
                "column_name": "COLUMN_NAME",
                "column_type": "VARCHAR2|NUMBER|etc",
                "annotations": ["@Column", "@Id", "@ManyToOne"],
                "validation": "Validation rules if any"
            }}
        ],
        "relationships": [
            {{
                "type": "ONE_TO_MANY|MANY_TO_ONE|MANY_TO_MANY",
                "target_entity": "OtherClassName",
                "target_table": "OTHER_TABLE",
                "join_column": "FK_COLUMN",
                "fetch_type": "LAZY|EAGER"
            }}
        ],
        "queries": [
            {{
                "name": "findByFleet",
                "type": "SELECT|INSERT|UPDATE|DELETE",
                "sql_or_jpql": "SELECT * FROM TABLE WHERE FLEET = ?",
                "purpose": "What this query does"
            }}
        ]
    }}
]

Include ALL entity-to-table mappings found in the code."""

    @staticmethod
    def data_requirements(form_name: str, model_summary: str, database_context: str) -> str:
        """Prompt for generating comprehensive data requirements."""
        return f"""Extract ONLY data entities that are EXPLICITLY present in the "{form_name}" source code and documentation.

CRITICAL RULES:
1. ONLY extract entities/tables that appear in the provided code or documentation
2. DO NOT invent generic entities (like Customer, Order, Transaction, User) unless they appear in the code
3. Use EXACT class names, table names, and column names from the source
4. For legacy Java Swing applications, focus on:
   - UI component models (TableModels, ComboBox data)
   - Database tables referenced in the code (FLEET_CHAPTER, CHAPTER_ALERT_RATES, etc.)
   - Form field data structures
5. If no entities are documented, return an empty array []

MODEL/ENTITY CODE:
{model_summary}

DATABASE CONTEXT FROM KNOWLEDGE BASE:
{database_context}

Generate data requirements in JSON format (ONLY for entities found in the code):
[
    {{
        "entity_name": "ACTUAL_CLASS_OR_TABLE_NAME",
        "description": "Purpose inferred from code context",
        "source_table": "ACTUAL_TABLE_NAME_FROM_CODE_OR_N/A",
        "source_class": "ACTUAL_CLASS.java",
        "fields": [
            {{
                "name": "ACTUAL_FIELD_NAME",
                "column": "ACTUAL_COLUMN_NAME_OR_N/A",
                "type": "ACTUAL_TYPE_FROM_CODE",
                "java_type": "ACTUAL_JAVA_TYPE",
                "constraints": ["ACTUAL_CONSTRAINTS"],
                "validation": "FROM_CODE_OR_N/A",
                "default": "FROM_CODE_OR_N/A",
                "description": "Inferred from context"
            }}
        ],
        "primary_key": ["ACTUAL_PK_COLUMNS"],
        "foreign_keys": [],
        "indexes": [],
        "relationships": [],
        "business_rules": ["RULES_FROM_CODE"],
        "sample_queries": []
    }}
]

If no data entities are found in the code, return: []"""

    @staticmethod
    def validation_rules(form_name: str, validation_code: str, context_text: str) -> str:
        """Prompt for extracting precise validation rules."""
        return f"""Extract ONLY validation rules that are EXPLICITLY present in the "{form_name}" source code.

CRITICAL RULES:
1. ONLY extract validations that appear in the provided code snippets
2. DO NOT invent generic validations (like email, password, username) unless they appear in the code
3. Use EXACT field names, conditions, and error messages from the code
4. If no validations are found, return an empty array []
5. Include the EXACT source location (file:line) where the validation appears

VALIDATION CODE SNIPPETS:
{validation_code}

CONTEXT FROM KNOWLEDGE BASE:
{context_text}

Generate validation rules in JSON format (ONLY for validations found in the code above):
[
    {{
        "rule_id": "VR-001",
        "field": "EXACT_FIELD_NAME_FROM_CODE",
        "entity": "{form_name}",
        "type": "required|format|range|business|cross-field",
        "condition": "EXACT_CONDITION_FROM_CODE",
        "error_message": "EXACT_MESSAGE_FROM_CODE_OR_N/A",
        "error_code": "CODE_FROM_SOURCE_OR_EMPTY",
        "description": "What this validation checks based on code logic",
        "when_applied": "Inferred from code context",
        "dependencies": ["ACTUAL_DEPENDENCIES_FROM_CODE"],
        "source_location": "ACTUAL_FILE.java:ACTUAL_LINE"
    }}
]

If no validation logic is found in the code, return: []"""

    @staticmethod
    def integration_requirements(form_name: str, integration_code: str, context: str) -> str:
        """Prompt for extracting integration specifications."""
        return f"""Extract ONLY integrations that are EXPLICITLY present in the "{form_name}" source code.

CRITICAL RULES:
1. ONLY document integrations that appear in the provided code (HTTP clients, API calls, database connections, message queues, COBOL calls)
2. DO NOT invent integrations like "Payment Gateway", "CRM", "Email Service" unless they appear in the code
3. For legacy Java Swing applications, look for:
   - COBOL integration via csBlock, paras.send(), etc.
   - Oracle/database calls via JDBC, stored procedures
   - File I/O operations
   - Internal service calls
4. Use EXACT class names, method names, and endpoints from the code
5. If no external integrations are found, return an empty array []

INTEGRATION CODE:
{integration_code}

CONTEXT:
{context}

Generate integration specifications in JSON format (ONLY for integrations found in the code):
[
    {{
        "integration_id": "INT-001",
        "name": "ACTUAL_INTEGRATION_NAME_FROM_CODE",
        "type": "REST_API|SOAP|DATABASE|MESSAGE_QUEUE|FILE|LEGACY_COBOL",
        "direction": "INBOUND|OUTBOUND|BIDIRECTIONAL",
        "external_system": "ACTUAL_SYSTEM_FROM_CODE",
        "purpose": "Purpose inferred from code context",
        "specification": {{
            "protocol": "ACTUAL_PROTOCOL",
            "endpoint": "ACTUAL_ENDPOINT_OR_METHOD",
            "authentication": {{"type": "AS_IN_CODE", "details": "FROM_CODE"}},
            "request_format": "AS_IN_CODE",
            "response_format": "AS_IN_CODE"
        }},
        "data_mapping": [
            {{"source_field": "ACTUAL_FIELD", "target_field": "ACTUAL_FIELD", "transformation": "FROM_CODE"}}
        ],
        "error_handling": {{
            "retry_policy": "AS_IN_CODE_OR_N/A",
            "fallback": "AS_IN_CODE_OR_N/A",
            "alerts": "AS_IN_CODE_OR_N/A"
        }},
        "frequency": "INFERRED_FROM_CODE",
        "source_files": ["ACTUAL_FILE.java"]
    }}
]

If no integrations are found in the code, return: []"""

    @staticmethod
    def workflow_extraction(form_name: str, workflow_code: str) -> str:
        """Prompt for extracting workflow/state machine logic."""
        return f"""Extract workflow and state transition logic from "{form_name}" code.

WORKFLOW CODE:
{workflow_code}

Generate workflow specifications in JSON format:
[
    {{
        "workflow_id": "WF-001",
        "name": "Workflow name",
        "description": "Business purpose",
        "entity": "Entity this workflow applies to",
        "states": [
            {{"id": "STATE_1", "name": "Display name", "description": "What this state means"}}
        ],
        "transitions": [
            {{
                "from": "STATE_1",
                "to": "STATE_2",
                "trigger": "What causes this transition",
                "guard_conditions": ["Conditions that must be true"],
                "actions": ["Actions performed during transition"],
                "permissions": ["Roles that can perform this"]
            }}
        ],
        "initial_state": "STATE_1",
        "terminal_states": ["STATE_N"],
        "business_rules": ["Rules governing this workflow"],
        "source_location": "ClassName.methodName"
    }}
]

Include all state machines and approval workflows."""

    @staticmethod
    def non_functional_requirements(form_name: str, code_context: str) -> str:
        """Prompt for generating specific non-functional requirements."""
        return f"""Generate non-functional requirements for "{form_name}" based on code analysis.

CODE PATTERNS OBSERVED:
{code_context}

Generate NFRs with specific, measurable targets in JSON format:
[
    {{
        "req_id": "NFR-001",
        "category": "performance|security|usability|reliability|scalability|maintainability",
        "title": "Specific requirement title",
        "description": "Detailed requirement",
        "current_implementation": "How legacy code handles this",
        "metric": "Specific measurable metric",
        "target_value": "Specific target (e.g., '<200ms', '99.9% uptime')",
        "measurement_method": "How to measure this",
        "migration_consideration": "What to consider when migrating",
        "priority": "Critical|High|Medium|Low"
    }}
]

Generate 8-12 NFRs based on observed patterns in the legacy code."""

    @staticmethod
    def summary(
        form_name: str,
        categories: str,
        high_priority: str,
        req_count: int,
        nfr_count: int,
        data_count: int,
    ) -> str:
        """Prompt for generating requirements summary."""
        return f"""Create a comprehensive technical summary for "{form_name}" migration:

STATISTICS:
- Total functional requirements: {req_count}
- Non-functional requirements: {nfr_count}
- Data entities: {data_count}
- Key functional areas: {categories}
- High priority requirements: {high_priority}

Write a 3-4 paragraph technical summary that includes:
1. Overview of the module's core business functionality
2. Key technical components and their interactions
3. Critical integration points and dependencies
4. Migration complexity assessment and recommendations

This summary should help technical leads understand the scope and plan the migration."""
