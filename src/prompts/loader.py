"""
Prompt loader utility.

Reads prompt templates from .txt files under src/prompts/txt/ and formats
them with provided keyword arguments.  Templates use Python str.format()
syntax: {variable_name} for interpolation, {{ / }} for literal braces.

Loaded file contents are cached so each file is read from disk only once.
"""

from functools import lru_cache
from pathlib import Path

_PROMPTS_DIR = Path(__file__).parent / "txt"


@lru_cache(maxsize=128)
def _read_prompt_file(relative_path: str) -> str:
    """Read and cache a prompt .txt file."""
    full_path = _PROMPTS_DIR / f"{relative_path}.txt"
    if not full_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {full_path}")
    return full_path.read_text(encoding="utf-8").rstrip("\n")


def load_prompt(name: str, **kwargs: object) -> str:
    """
    Load a prompt template by name and format with provided variables.

    Args:
        name: Slash-separated path relative to txt/ without .txt extension
              (e.g. "migration/system_prompt").
        **kwargs: Variables to interpolate into the template.

    Returns:
        The formatted prompt string.

    Raises:
        FileNotFoundError: If the .txt file does not exist.
        KeyError: If a required placeholder is missing from kwargs.
    """
    template = _read_prompt_file(name)
    if kwargs:
        return template.format(**kwargs)
    return template
