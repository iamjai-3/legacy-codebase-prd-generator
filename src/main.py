"""
Main entry point for PRD Agent.

This module provides the primary entry point for running the PRD Agent CLI.
PRD generation is done through Temporal workflows for reliability and scalability.
"""

import sys

from src.cli.commands import app
from src.utils.logging_config import setup_logging


def run_cli() -> None:
    """Run the PRD Agent CLI application."""
    setup_logging()
    app()


def main() -> None:
    """Main entry point."""
    if len(sys.argv) > 1:
        run_cli()
    else:
        print("PRD Agent - AI-powered PRD Generation for Legacy Code Migration")
        print("\nUsage:")
        print("  prd-agent generate -f <form_name> --output ./output")
        print("  prd-agent list-collections")
        print("  prd-agent search -f <form_name> -q <query>")
        print("  prd-agent create-minio-folders")
        print("  prd-agent --help")
        print("\nFor more information, run: prd-agent --help")


if __name__ == "__main__":
    main()
