"""Prompts for PRD Aggregator Agent - Migration-Focused PRD Generation."""


class PRDAggregatorPrompts:
    """Prompts for generating migration-ready PRD documents."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for PRD aggregation."""
        return f"""You are a senior software architect creating a MIGRATION-READY Product Requirements Document for "{form_name}".

This PRD will be used by developers to:
1. Understand the EXACT business logic of the legacy system
2. Implement the SAME functionality in a NEW technology stack
3. Know precisely what APIs to create and how they should behave
4. Replicate all data operations, validations, and workflows
5. Maintain feature parity during migration

CRITICAL REQUIREMENTS FOR THIS PRD:
- Include SPECIFIC code references and method signatures
- Document EXACT business rules with conditions and calculations
- Specify COMPLETE API contracts with request/response schemas
- Detail ALL database operations with table/column names
- Describe PRECISE validation logic and error handling
- Map ACTUAL user workflows with exact steps

The PRD must be STACK-AGNOSTIC but TECHNICALLY COMPLETE.
A developer reading this should be able to implement the system in any framework.

Do NOT use generic descriptions like "the system shall..."
Instead, use SPECIFIC descriptions like "when field X equals Y, calculate Z using formula A + B * C"."""

    @staticmethod
    def overview_section(form_name: str, jira_context: str, kb_context: str) -> str:
        """Prompt for generating the overview section with specific details."""
        return f"""Write the Overview section for "{form_name}" PRD based on actual system analysis:

JIRA DOCUMENTATION:
{jira_context}

KNOWLEDGE BASE CONTEXT:
{kb_context}

Include these sections with SPECIFIC details from the source:
1. **Purpose and Scope**: What EXACTLY does this module do? What business process does it support?
2. **Business Context**: Who uses this? What triggers its use? What business value does it provide?
3. **System Context**: How does it fit in the larger system? What does it depend on?
4. **Key Functionality Summary**: List the TOP 5-10 core features with brief descriptions
5. **Migration Objectives**: What needs to be preserved? What can be modernized?

Be SPECIFIC - use actual feature names, user roles, and business terms from the source."""

    @staticmethod
    def business_logic_section(form_name: str, logic_data: str, kb_context: str) -> str:
        """Prompt for generating detailed business logic documentation."""
        return f"""Document ALL business logic for "{form_name}" in a format suitable for migration.

EXTRACTED BUSINESS LOGIC:
{logic_data}

KNOWLEDGE BASE CONTEXT:
{kb_context}

For each piece of business logic, document:
1. **Trigger**: What initiates this logic (user action, event, scheduled task)
2. **Inputs**: All input parameters with types and valid values
3. **Processing Steps**: Step-by-step algorithm in pseudocode
4. **Conditions**: All if/else branches with exact conditions
5. **Calculations**: Formulas with variable names and operators
6. **Outputs**: What is returned or stored, with exact format
7. **Error Cases**: What can go wrong and how it's handled
8. **Source Reference**: Original code location

Format as clear, implementable specifications that a developer can code directly from."""

    @staticmethod
    def api_specification_section(form_name: str, api_data: str, kb_context: str) -> str:
        """Prompt for generating comprehensive API documentation."""
        return f"""Document complete API specifications for "{form_name}" migration.

EXTRACTED API DATA:
{api_data}

KNOWLEDGE BASE CONTEXT:
{kb_context}

For each API endpoint, document in OpenAPI-style format:
1. **Endpoint**: HTTP method + path with path parameters
2. **Description**: What this endpoint does
3. **Authentication**: Required auth method
4. **Request**:
   - Path parameters with types
   - Query parameters with types and defaults
   - Request body schema with all fields, types, and validations
   - Example request
5. **Response**:
   - Success response with schema and example
   - Error responses with codes, messages, and when they occur
6. **Business Logic**: What processing happens between request and response
7. **Database Operations**: What tables are read/written
8. **Side Effects**: Events triggered, notifications sent, etc.

Make this a complete API contract that backend developers can implement."""

    @staticmethod
    def data_model_section(form_name: str, data_requirements: str, kb_context: str) -> str:
        """Prompt for generating detailed data model documentation."""
        return f"""Document the complete data model for "{form_name}" migration.

DATA REQUIREMENTS:
{data_requirements}

KNOWLEDGE BASE CONTEXT:
{kb_context}

For each entity/table, document:
1. **Entity Name**: Business name and technical name
2. **Purpose**: What business concept this represents
3. **Schema**:
   | Column | Type | Constraints | Description |
   |--------|------|-------------|-------------|
4. **Primary Key**: Column(s) that uniquely identify records
5. **Foreign Keys**: Relationships to other tables with referential actions
6. **Indexes**: Performance indexes with included columns
7. **Business Rules**: Data integrity rules not captured in constraints
8. **Sample Queries**: Common query patterns with SQL examples
9. **Data Volume**: Expected row counts and growth rate if known

Include an Entity Relationship Diagram in Mermaid format if multiple entities."""

    @staticmethod
    def functional_requirements_section(
        form_name: str, requirements: str, logic_context: str
    ) -> str:
        """Prompt for enhanced functional requirements with business logic."""
        return f"""Enhance the functional requirements for "{form_name}" with implementation details.

BASE REQUIREMENTS:
{requirements}

BUSINESS LOGIC CONTEXT:
{logic_context}

For each requirement, ensure it includes:
1. **Unique ID**: FR-XXX format
2. **Title**: Clear, action-oriented title
3. **Business Logic**: Exact step-by-step processing (not generic descriptions)
4. **API Contract**: If this involves an API, include method, path, request/response
5. **Database Operations**: Specific tables and operations
6. **Validation Rules**: Exact conditions that must be met
7. **Error Handling**: Specific error cases and responses
8. **Acceptance Criteria**: Testable conditions in Given/When/Then format
9. **Source Reference**: Original code or documentation location

Make each requirement implementable without referring back to legacy code."""

    @staticmethod
    def validation_rules_section(form_name: str, validation_data: str) -> str:
        """Prompt for documenting all validation rules."""
        return f"""Document ALL validation rules for "{form_name}" in implementation-ready format.

EXTRACTED VALIDATION DATA:
{validation_data}

For each validation rule, document:
1. **Rule ID**: VR-XXX format
2. **Field/Entity**: What is being validated
3. **Type**: required | format | range | business | cross-field | async
4. **Condition**: Exact validation expression (e.g., "value != null && value.length >= 3 && value.length <= 50")
5. **Error Message**: Exact user-facing message
6. **Error Code**: API error code if applicable
7. **When Applied**: On change | On blur | On submit | Before save
8. **Dependencies**: Other fields that affect this validation
9. **Implementation Notes**: Any special handling required

Group validations by entity/form for easy reference during implementation."""

    @staticmethod
    def integration_section(form_name: str, integration_data: str) -> str:
        """Prompt for documenting external integrations."""
        return f"""Document ALL external integrations for "{form_name}" migration.

EXTRACTED INTEGRATION DATA:
{integration_data}

For each integration, document:
1. **Integration ID**: INT-XXX format
2. **External System**: Name and purpose of the external system
3. **Direction**: Inbound (we receive) | Outbound (we send) | Bidirectional
4. **Protocol**: REST | SOAP | gRPC | Message Queue | File | Database
5. **Connection Details**: Endpoint pattern, authentication method
6. **Data Contract**:
   - Request/message format with schema
   - Response/reply format with schema
   - Field mappings between systems
7. **Error Handling**: Retry logic, circuit breaker, fallback behavior
8. **Timing**: Real-time | Near real-time | Batch | Scheduled
9. **Dependencies**: What must be in place for this integration to work
10. **Migration Notes**: What changes when moving to new stack

Make integration specs complete enough to implement connectors."""

    @staticmethod
    def workflow_section(form_name: str, workflow_data: str) -> str:
        """Prompt for documenting workflows and state machines."""
        return f"""Document ALL workflows and state machines for "{form_name}".

WORKFLOW DATA:
{workflow_data}

For each workflow, document:
1. **Workflow ID**: WF-XXX format
2. **Name**: Business name for this workflow
3. **Purpose**: What business process this implements
4. **States**: All possible states with descriptions
5. **State Diagram**: Mermaid diagram showing states and transitions
6. **Transitions**:
   | From | To | Trigger | Conditions | Actions | Permissions |
   |------|-----|---------|------------|---------|-------------|
7. **Business Rules**: Rules governing this workflow
8. **Notifications**: What notifications are sent at each step
9. **Audit Trail**: What is logged for compliance/debugging

Include enough detail to implement the workflow engine."""

    @staticmethod
    def executive_summary(
        form_name: str,
        req_count: int,
        api_count: int,
        entity_count: int,
        integration_count: int,
        complexity: str,
        kb_context: str = "",
    ) -> str:
        """Prompt for generating executive summary."""
        return f"""Write an executive summary for the "{form_name}" migration PRD.

ACTUAL MODULE CONTEXT FROM KNOWLEDGE BASE:
{kb_context}

METRICS:
- Functional Requirements: {req_count}
- API Endpoints: {api_count}
- Data Entities: {entity_count}
- External Integrations: {integration_count}
- Assessed Complexity: {complexity}

CRITICAL INSTRUCTIONS:
1. Use ONLY the information from the KNOWLEDGE BASE CONTEXT above
2. Do NOT invent or hallucinate any entities, tables, or features
3. Reference the ACTUAL module name, purpose, and features described in the context
4. Use SPECIFIC business terms from the context (e.g., fleet, ATA chapter, alert rates)

The summary should include (4-5 paragraphs):
1. **Module Overview**: What this SPECIFIC module does based on the context above
2. **Technical Scope**: ACTUAL data entities and tables mentioned in the context
3. **Migration Approach**: Recommended strategy based on complexity
4. **Critical Considerations**: Key risks, dependencies, and success factors
5. **Effort Estimate**: High-level timeline and resource estimate

Write for technical leads and project managers who need to plan the migration."""

    @staticmethod
    def migration_strategy_section(
        form_name: str, complexity: str, tech_details: str
    ) -> str:
        """Prompt for generating migration strategy."""
        return f"""Create a detailed migration strategy for "{form_name}".

COMPLEXITY ASSESSMENT: {complexity}

TECHNICAL DETAILS:
{tech_details}

Include these sections:
1. **Complexity Analysis**: Factors contributing to complexity level
2. **Recommended Approach**: Big bang vs. phased vs. strangler pattern
3. **Migration Phases**:
   - Phase 1: What to migrate first and why
   - Phase 2: Second wave with dependencies on Phase 1
   - Phase 3+: Remaining components
4. **Data Migration Strategy**: How to migrate data with minimal downtime
5. **Integration Cutover**: How to switch integrations to new system
6. **Testing Strategy**: Unit, integration, E2E, UAT approach
7. **Rollback Plan**: How to revert if issues arise
8. **Success Criteria**: How to measure successful migration
9. **Risk Mitigation**: Specific risks and mitigation strategies

Be specific to this module's characteristics, not generic advice."""
