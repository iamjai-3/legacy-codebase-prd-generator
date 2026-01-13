"""Base utilities for prompt management."""


def format_context(context_items: list[str], max_items: int = 5) -> str:
    """Format context items for inclusion in prompts."""
    if not context_items:
        return "No additional context available."
    return "\n".join(context_items[:max_items])
