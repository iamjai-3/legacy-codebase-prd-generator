"""Prompts for Requirements Generator Agent."""


class RequirementsPrompts:
    """Prompts used by the RequirementsGeneratorAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for requirements generation."""
        return f"""You are a senior business analyst specializing in requirements engineering for software modernization.
Your task is to generate comprehensive requirements for the "{form_name}" module migration.

When generating requirements:
1. Derive functional requirements from code analysis and existing behavior
2. Define clear acceptance criteria for each requirement
3. Identify data models and their relationships
4. Specify validation rules and business logic
5. Document integration points and dependencies
6. Define non-functional requirements (performance, security)
7. Note assumptions and out-of-scope items

Requirements should be:
- Clear and unambiguous
- Testable with specific acceptance criteria
- Traceable to source code or documentation
- Prioritized for migration planning

Use standard requirement IDs: FR-XXX for functional, NFR-XXX for non-functional, DR-XXX for data."""

    @staticmethod
    def functional_requirements(form_name: str, code_summary: str, context_summary: str) -> str:
        """Prompt for generating functional requirements."""
        return f"""Based on the code analysis and context for "{form_name}", generate functional requirements.

Code Analysis:
{code_summary}

Additional Context:
{context_summary}

For each requirement, respond in JSON array format:
[
    {{
        "title": "Clear requirement title",
        "description": "Detailed description of what the system should do",
        "priority": "P0|P1|P2|P3",
        "category": "CRUD|validation|workflow|integration|reporting",
        "user_story": "As a [user], I want [action] so that [benefit]",
        "acceptance_criteria": ["criterion 1", "criterion 2"],
        "dependencies": ["dependency 1"],
        "source_references": ["file or doc reference"]
    }}
]

Generate 5-10 key functional requirements."""

    @staticmethod
    def non_functional_requirements(form_name: str) -> str:
        """Prompt for generating non-functional requirements."""
        return f"""Generate non-functional requirements for "{form_name}" covering:

1. Performance (response times, throughput)
2. Security (authentication, authorization, data protection)
3. Usability (accessibility, user experience)
4. Reliability (availability, fault tolerance)
5. Scalability (concurrent users, data volume)

Respond in JSON array format:
[
    {{
        "category": "performance|security|usability|reliability|scalability",
        "description": "Requirement description",
        "metric": "Measurable metric",
        "target_value": "Specific target",
        "validation_method": "How to validate"
    }}
]

Generate 4-6 non-functional requirements."""

    @staticmethod
    def data_requirements(form_name: str, model_summary: str) -> str:
        """Prompt for generating data requirements."""
        return f"""Based on the data models for "{form_name}":

{model_summary}

Generate data requirements in JSON format:
[
    {{
        "entity_name": "Entity name",
        "description": "What this entity represents",
        "source_table": "Original table name if known",
        "fields": [
            {{"name": "field_name", "type": "data_type", "required": "yes/no"}}
        ],
        "relationships": ["Related to EntityX via field"],
        "constraints": ["Business constraint 1"]
    }}
]

Focus on core entities and their relationships."""

    @staticmethod
    def integration_requirements(form_name: str, file_list: str) -> str:
        """Prompt for extracting integration requirements."""
        return f"""Based on these integration-related files: {file_list}

Identify integration requirements for "{form_name}":
- External systems/APIs
- Internal service dependencies
- Data exchange formats
- Authentication requirements

List each integration requirement clearly."""

    @staticmethod
    def validation_rules(form_name: str, validation_snippets: str, context_text: str) -> str:
        """Prompt for extracting validation rules."""
        return f"""Extract validation rules for "{form_name}":

Context from existing documentation:
{context_text}

Code snippets with validation:
{validation_snippets}

List all validation rules in the format:
VR-001: [Field/Entity] - [Rule description]

Include field validations, business rules, and data integrity checks."""

    @staticmethod
    def business_rules(form_name: str, context_text: str) -> str:
        """Prompt for extracting business rules."""
        return f"""From the following context for "{form_name}", extract business rules:

{context_text}

List each business rule in the format:
BR-001: [Rule description]

Focus on:
- Conditional logic
- Calculations
- State transitions
- Access control rules"""

    @staticmethod
    def assumptions_and_scope(form_name: str, req_summary: str) -> str:
        """Prompt for identifying assumptions and out-of-scope items."""
        return f"""Based on these requirements for "{form_name}":

{req_summary}

Identify:

ASSUMPTIONS:
- What we're assuming about the current system
- What we're assuming about user behavior
- Technical assumptions

OUT OF SCOPE:
- Features explicitly not included
- Future enhancements
- External dependencies not addressed

Format as two sections: ASSUMPTIONS and OUT OF SCOPE."""

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
        return f"""Summarize the requirements for "{form_name}" migration:

- Total functional requirements: {req_count}
- Non-functional requirements: {nfr_count}
- Data entities: {data_count}
Key functional areas: {categories}

High priority requirements: {high_priority}

Provide a 2-paragraph executive summary suitable for stakeholders."""
