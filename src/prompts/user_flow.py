"""Prompts for User Flow Agent."""

from src.prompts.loader import load_prompt


class UserFlowPrompts:
    """Prompts used by the UserFlowAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for user flow analysis."""
        return load_prompt("user_flow/system_prompt", form_name=form_name)

    @staticmethod
    def identify_actors(form_name: str, context_text: str) -> str:
        """Prompt for identifying user types/actors."""
        return load_prompt(
            "user_flow/identify_actors",
            form_name=form_name,
            context_text=context_text,
        )

    @staticmethod
    def flow_boundaries(form_name: str, screen_info: str) -> str:
        """Prompt for identifying entry and exit points."""
        return load_prompt(
            "user_flow/flow_boundaries",
            form_name=form_name,
            screen_info=screen_info,
        )

    @staticmethod
    def generate_flows(form_name: str, actors: str, entry_points: str, context_text: str) -> str:
        """Prompt for generating detailed user flows."""
        return load_prompt(
            "user_flow/generate_flows",
            form_name=form_name,
            actors=actors,
            entry_points=entry_points,
            context_text=context_text,
        )

    @staticmethod
    def journey_map(form_name: str, flow_summaries: str) -> str:
        """Prompt for generating user journey map."""
        return load_prompt(
            "user_flow/journey_map",
            form_name=form_name,
            flow_summaries=flow_summaries,
        )

    @staticmethod
    def flow_diagram(form_name: str, flow_name: str, steps_text: str) -> str:
        """Prompt for generating Mermaid flowchart."""
        return load_prompt(
            "user_flow/flow_diagram",
            form_name=form_name,
            flow_name=flow_name,
            steps_text=steps_text,
        )
