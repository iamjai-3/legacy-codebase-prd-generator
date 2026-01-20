"""Analysis activities for PRD generation workflow."""

from typing import Any

from temporalio import activity

from src.agents.atlassian_integration_agent import AtlassianIntegrationAgent
from src.agents.base_agent import AgentContext
from src.agents.requirements_generator_agent import RequirementsGeneratorAgent
from src.agents.screenshot_analysis_agent import ScreenshotAnalysisAgent
from src.agents.user_flow_agent import UserFlowAgent
from src.utils.data_reconstruction import reconstruct_code_files, reconstruct_screenshots
from src.utils.logging_config import get_logger
from src.workflows.activities.common import to_dict

logger = get_logger(__name__)


@activity.defn
async def analyze_screenshots_activity(
    form_name: str,
    screenshot_data: dict[str, Any],
) -> dict[str, Any]:
    """Analyze screenshots using the ScreenshotAnalysisAgent."""
    logger.info("Starting screenshot analysis", form_name=form_name)

    agent = ScreenshotAnalysisAgent()
    context = AgentContext(form_name=form_name)
    screenshots = reconstruct_screenshots(screenshot_data, form_name)

    result = await agent.analyze(context, screenshots=screenshots if screenshots else None)

    if result.success and result.data:
        return {
            "success": True,
            "total_screens": result.data.total_screens,
            "screen_analyses": [to_dict(s) for s in result.data.screen_analyses],
            "ui_flow_summary": result.data.ui_flow_summary,
            "common_patterns": result.data.common_patterns,
            "component_inventory": result.data.component_inventory,
            "recommendations": result.data.recommendations,
            "execution_time_ms": result.execution_time_ms,
        }

    return {
        "success": False,
        "error": result.error,
        "execution_time_ms": result.execution_time_ms,
    }


@activity.defn
async def analyze_jira_activity(
    form_name: str,
    jira_data: dict[str, Any],
) -> dict[str, Any]:
    """Analyze Jira issues using the AtlassianIntegrationAgent."""
    logger.info("Starting Jira analysis", form_name=form_name)

    agent = AtlassianIntegrationAgent()
    context = AgentContext(form_name=form_name)
    issues = jira_data.get("raw_issues", [])

    result = await agent.analyze(context, issues=issues)

    if result.success and result.data:
        return {
            "success": True,
            "total_issues": result.data.total_issues,
            "issues_by_type": result.data.issues_by_type,
            "issues_by_status": result.data.issues_by_status,
            "requirements": [to_dict(r) for r in result.data.requirements],
            "business_rules": result.data.business_rules,
            "technical_constraints": result.data.technical_constraints,
            "open_questions": result.data.open_questions,
            "documentation_gaps": result.data.documentation_gaps,
            "summary": result.data.summary,
            "execution_time_ms": result.execution_time_ms,
        }

    return {
        "success": False,
        "error": result.error,
        "execution_time_ms": result.execution_time_ms,
    }


@activity.defn
async def generate_requirements_activity(
    form_name: str,
    code_data: dict[str, Any],
    jira_context: str | None = None,
    screenshot_context: str | None = None,
) -> dict[str, Any]:
    """Generate requirements using the RequirementsGeneratorAgent."""
    logger.info("Starting requirements generation", form_name=form_name)

    agent = RequirementsGeneratorAgent()
    context = AgentContext(form_name=form_name)
    code_files = reconstruct_code_files(code_data)

    result = await agent.analyze(
        context,
        code_files=code_files if code_files else None,
        jira_context=jira_context,
        screenshot_context=screenshot_context,
    )

    if result.success and result.data:
        return {
            "success": True,
            "functional_requirements": [to_dict(r) for r in result.data.functional_requirements],
            "non_functional_requirements": [
                to_dict(r) for r in result.data.non_functional_requirements
            ],
            "data_requirements": [to_dict(r) for r in result.data.data_requirements],
            "integration_requirements": result.data.integration_requirements,
            "validation_rules": result.data.validation_rules,
            "business_rules": result.data.business_rules,
            "assumptions": result.data.assumptions,
            "out_of_scope": result.data.out_of_scope,
            "summary": result.data.summary,
            "execution_time_ms": result.execution_time_ms,
        }

    return {
        "success": False,
        "error": result.error,
        "execution_time_ms": result.execution_time_ms,
    }


@activity.defn
async def analyze_user_flows_activity(
    form_name: str,
    screenshot_analysis: dict[str, Any] | None = None,
    code_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Analyze user flows using the UserFlowAgent."""
    logger.info("Starting user flow analysis", form_name=form_name)

    agent = UserFlowAgent()
    context = AgentContext(form_name=form_name)

    result = await agent.analyze(
        context, screenshot_analysis=screenshot_analysis, code_analysis=code_analysis
    )

    if result.success and result.data:
        return {
            "success": True,
            "user_flows": [to_dict(f) for f in result.data.user_flows],
            "primary_actors": result.data.primary_actors,
            "entry_points": result.data.entry_points,
            "exit_points": result.data.exit_points,
            "user_journey_map": result.data.user_journey_map,
            "flow_diagram_mermaid": result.data.flow_diagram_mermaid,
            "execution_time_ms": result.execution_time_ms,
        }

    return {
        "success": False,
        "error": result.error,
        "execution_time_ms": result.execution_time_ms,
    }
