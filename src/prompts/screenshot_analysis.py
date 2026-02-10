"""Prompts for Screenshot Analysis Agent."""

from src.prompts.loader import load_prompt


class ScreenshotAnalysisPrompts:
    """Prompts used by the ScreenshotAnalysisAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for screenshot analysis."""
        return load_prompt("screenshot_analysis/system_prompt", form_name=form_name)

    @staticmethod
    def analyze_screenshot(form_name: str) -> str:
        """Prompt for analyzing a single screenshot."""
        return load_prompt("screenshot_analysis/analyze_screenshot", form_name=form_name)

    @staticmethod
    def flow_summary(form_name: str, screen_descriptions: str) -> str:
        """Prompt for generating UI flow summary."""
        return load_prompt(
            "screenshot_analysis/flow_summary",
            form_name=form_name,
            screen_descriptions=screen_descriptions,
        )

    @staticmethod
    def recommendations(form_name: str, inventory_str: str) -> str:
        """Prompt for generating modernization recommendations."""
        return load_prompt(
            "screenshot_analysis/recommendations",
            form_name=form_name,
            inventory_str=inventory_str,
        )
