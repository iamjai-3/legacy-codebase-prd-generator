"""Prompts for Screenshot Analysis Agent."""


class ScreenshotAnalysisPrompts:
    """Prompts used by the ScreenshotAnalysisAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for screenshot analysis."""
        return f"""You are a UI/UX analyst specializing in legacy application modernization.
Your task is to analyze screenshots from the "{form_name}" module to understand its interface and user experience.

When analyzing screenshots:
1. Identify all UI components (buttons, inputs, tables, menus)
2. Understand the screen's purpose and user workflow
3. Note layout patterns and navigation structure
4. Identify data displayed and user interactions
5. Document validation indicators and error states
6. Note accessibility concerns
7. Suggest modernization opportunities

Your analysis will inform the PRD for the modernized application.

Be thorough but concise. Focus on actionable insights for migration."""

    @staticmethod
    def analyze_screenshot(form_name: str) -> str:
        """Prompt for analyzing a single screenshot."""
        return f"""Analyze this screenshot from the "{form_name}" application.

Provide your analysis in JSON format:
{{
    "screen_name": "Descriptive screen name",
    "screen_type": "form|list|detail|dialog|dashboard|report|menu",
    "purpose": "What this screen is used for",
    "layout_description": "Layout structure description",
    "ui_elements": [
        {{
            "element_type": "button|input|table|dropdown|checkbox|etc",
            "label": "Element label or identifier",
            "description": "What this element does",
            "location": "top|bottom|left|right|center",
            "interactions": ["click", "input", "select"]
        }}
    ],
    "user_actions": ["List of actions users can perform"],
    "data_displayed": ["Types of data shown"],
    "validation_rules": ["Visible validation indicators"],
    "accessibility_notes": ["Accessibility observations"]
}}

Be precise and thorough in identifying all UI components."""

    @staticmethod
    def flow_summary(form_name: str, screen_descriptions: str) -> str:
        """Prompt for generating UI flow summary."""
        return f"""Based on these screens from the "{form_name}" module:

{screen_descriptions}

Describe the overall UI flow:
1. How do screens connect to each other?
2. What is the typical user journey?
3. What are the main entry and exit points?
4. Are there any workflow patterns (wizard, list-detail, etc.)?

Provide a 2-3 paragraph summary of the UI flow."""

    @staticmethod
    def recommendations(form_name: str, inventory_str: str) -> str:
        """Prompt for generating modernization recommendations."""
        return f"""Based on the UI analysis of "{form_name}":

Component inventory: {inventory_str}

Provide modernization recommendations:
1. UI/UX improvements
2. Modern component replacements
3. Responsive design considerations
4. Accessibility improvements
5. Performance optimizations

List 5-7 specific, actionable recommendations."""
