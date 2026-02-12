"""
Prompts module for PRD Agent.

Contains all LLM prompts used by agents, organized by agent type.
Prompt text lives in src/prompts/txt/*.txt and is loaded at runtime
by the ``load_prompt`` helper.
"""

from src.prompts.loader import load_prompt

__all__ = [
    "load_prompt",
]
