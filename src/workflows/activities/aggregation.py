"""Aggregation activities for PRD generation workflow."""

from typing import Any

from temporalio import activity

from src.agents.base_agent import AgentContext
from src.agents.prd_aggregator_agent import PRDAggregatorAgent
from src.utils.data_reconstruction import (
    reconstruct_atlassian_analysis,
    reconstruct_requirements_analysis,
    reconstruct_screenshot_analysis,
    reconstruct_user_flow_analysis,
)
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


@activity.defn
async def aggregate_prd_activity(
    form_name: str,
    screenshot_analysis: dict[str, Any] | None = None,
    jira_analysis: dict[str, Any] | None = None,
    requirements_analysis: dict[str, Any] | None = None,
    user_flow_analysis: dict[str, Any] | None = None,
    database_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Aggregate all analyses into a migration-ready PRD document."""
    logger.info("Starting migration-focused PRD aggregation", form_name=form_name)

    agent = PRDAggregatorAgent()
    context = AgentContext(form_name=form_name)

    # Reconstruct analysis objects from serialized dicts
    result = await agent.analyze(
        context,
        screenshot_analysis=reconstruct_screenshot_analysis(screenshot_analysis, form_name),
        atlassian_analysis=reconstruct_atlassian_analysis(jira_analysis, form_name),
        requirements_analysis=reconstruct_requirements_analysis(requirements_analysis, form_name),
        user_flow_analysis=reconstruct_user_flow_analysis(user_flow_analysis, form_name),
        database_analysis=database_analysis,
    )

    if result.success and result.data:
        return {
            "success": True,
            "form_name": result.data.form_name,
            "markdown_content": result.data.markdown_content,
            "word_count": result.data.word_count,
            "section_count": result.data.section_count,
            "generation_metrics": result.data.generation_metrics,
            "execution_time_ms": result.execution_time_ms,
        }

    return {
        "success": False,
        "error": result.error,
        "execution_time_ms": result.execution_time_ms,
    }
