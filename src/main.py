"""
Main entry point for PRD Agent.

This module provides the primary entry points for running the PRD Agent
either as a CLI application or programmatically.
"""

import sys

from src.cli.commands import app
from src.generators.prd_generator import PRDGenerationConfig, PRDGenerator
from src.utils.logging_config import get_logger, setup_logging

logger = get_logger(__name__)


def run_cli() -> None:
    """Run the PRD Agent CLI application."""
    setup_logging()
    app()


async def generate_prd(
    form_name: str,
    zip_path: str | None = None,
    code_directory: str | None = None,
    minio_bucket: str | None = None,
    jira_project: str | None = None,
    output_dir: str = "./output",
    skip_screenshots: bool = False,
    skip_jira: bool = False,
    recreate_vectors: bool = False,
) -> dict:
    """
    Generate a PRD programmatically.

    Args:
        form_name: Name of the form to analyze (e.g., 'le01')
        zip_path: Path to the code ZIP file
        code_directory: Path to the code directory
        minio_bucket: Minio bucket for screenshots
        jira_project: Jira project key
        output_dir: Output directory for PRD
        skip_screenshots: Skip screenshot analysis
        skip_jira: Skip Jira integration
        recreate_vectors: Recreate vector collection

    Returns:
        Dictionary with generation results
    """
    setup_logging()

    config = PRDGenerationConfig(
        form_name=form_name,
        zip_path=zip_path,
        code_directory=code_directory,
        minio_bucket=minio_bucket,
        jira_project_key=jira_project,
        output_dir=output_dir,
        skip_screenshots=skip_screenshots,
        skip_jira=skip_jira,
        recreate_vectors=recreate_vectors,
    )

    generator = PRDGenerator()
    result = await generator.generate(config)

    return {
        "success": result.success,
        "form_name": result.form_name,
        "prd_file": result.prd_file_path,
        "word_count": result.word_count,
        "section_count": result.section_count,
        "execution_time": result.execution_time_seconds,
        "error": result.error,
        "metrics": result.agent_metrics,
    }


def main() -> None:
    """Main entry point."""
    if len(sys.argv) > 1:
        # Run CLI if arguments provided
        run_cli()
    else:
        # Show help
        print("PRD Agent - AI-powered PRD Generation for Legacy Code Migration")
        print("\nUsage:")
        print("  prd-agent generate -f <form_name> -z <zip_path>")
        print("  prd-agent list-collections")
        print("  prd-agent search -f <form_name> -q <query>")
        print("  prd-agent --help")
        print("\nFor more information, run: prd-agent --help")


if __name__ == "__main__":
    main()
