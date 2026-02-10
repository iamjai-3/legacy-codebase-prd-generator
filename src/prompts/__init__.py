"""
Prompts module for PRD Agent.

Contains all LLM prompts used by agents, organized by agent type.
Prompt text lives in src/prompts/txt/*.txt and is loaded at runtime
by the ``load_prompt`` helper.
"""

from src.prompts.loader import load_prompt
from src.prompts.prd_aggregator import PRDAggregatorPrompts
from src.prompts.requirements import RequirementsPrompts
from src.prompts.screenshot_analysis import ScreenshotAnalysisPrompts
from src.prompts.user_flow import UserFlowPrompts

__all__ = [
    "load_prompt",
    "RequirementsPrompts",
    "ScreenshotAnalysisPrompts",
    "UserFlowPrompts",
    "PRDAggregatorPrompts",
]
