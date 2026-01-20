"""Prompts for User Flow Agent."""


class UserFlowPrompts:
    """Prompts used by the UserFlowAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for user flow analysis."""
        return f"""You are a UX analyst specializing in documenting user journeys and workflows.
Your task is to analyze and document user flows for the "{form_name}" module.

When documenting user flows:
1. Identify all user types (actors) who interact with the module
2. Map entry and exit points
3. Document step-by-step workflows
4. Note decision points and alternative paths
5. Identify error handling and edge cases
6. Create clear flow diagrams

User flows should be:
- Complete and accurate
- Easy to understand for developers
- Suitable for testing scenarios
- Traceable to requirements

This documentation will guide the UX design of the modernized application."""

    @staticmethod
    def identify_actors(form_name: str, context_text: str) -> str:
        """Prompt for identifying user types/actors."""
        return f"""Based on the context for "{form_name}":

{context_text}

Identify all user types who interact with this module.
For each user type, include:
- Role name
- Brief description of their responsibilities
- Primary use cases

List each actor on a new line in format:
Actor Name: Brief description"""

    @staticmethod
    def flow_boundaries(form_name: str, screen_info: str) -> str:
        """Prompt for identifying entry and exit points."""
        return f"""Based on the UI analysis for "{form_name}":

{screen_info}

Identify:

ENTRY POINTS:
- How users navigate to this module
- Starting screens or actions

EXIT POINTS:
- How users complete tasks
- Navigation to other modules
- Cancel/close actions

Format as two sections: ENTRY POINTS and EXIT POINTS."""

    @staticmethod
    def generate_flows(form_name: str, actors: str, entry_points: str, context_text: str) -> str:
        """Prompt for generating detailed user flows."""
        return f"""Generate detailed user flows for "{form_name}".

Actors: {actors}
Entry points: {entry_points}

Context:
{context_text}

For each major workflow, respond in JSON array format:
[
    {{
        "name": "Flow name",
        "description": "What this flow accomplishes",
        "actor": "Primary actor",
        "preconditions": ["Condition 1", "Condition 2"],
        "postconditions": ["Result 1"],
        "steps": [
            {{
                "action": "What user does",
                "screen": "Screen name",
                "input_data": ["data entered"],
                "expected_result": "What happens",
                "alternative_paths": ["alternative if applicable"]
            }}
        ],
        "success_criteria": "How to know flow succeeded",
        "estimated_time": "Approximate time to complete"
    }}
]

Generate 3-5 key user flows."""

    @staticmethod
    def journey_map(form_name: str, flow_summaries: str) -> str:
        """Prompt for generating user journey map."""
        return f"""Create a user journey map for "{form_name}":

Documented flows:
{flow_summaries}

Describe the overall user journey including:
1. Touchpoints and interactions
2. User emotions/pain points
3. Opportunities for improvement
4. Critical moments in the journey

Provide a comprehensive journey map in prose format."""

    @staticmethod
    def flow_diagram(form_name: str, flow_name: str, steps_text: str) -> str:
        """Prompt for generating Mermaid flowchart."""
        return f"""Create a Mermaid flowchart for "{flow_name}":

Steps:
{steps_text}

Generate a valid Mermaid flowchart diagram showing:
- Start and end points
- Decision points
- Main flow and alternatives
- Keep it clean and readable

Output only the Mermaid code starting with "flowchart TD"."""
