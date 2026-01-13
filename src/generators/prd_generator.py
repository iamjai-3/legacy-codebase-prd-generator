"""
PRD Generator for creating comprehensive PRD documents.

This module provides a high-level interface for generating PRDs
either through Temporal workflows or direct execution.
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from src.agents.atlassian_integration_agent import (
    AtlassianIntegrationAgent,
    AtlassianIntegrationResult,
)
from src.agents.base_agent import AgentContext, AgentResult
from src.agents.prd_aggregator_agent import PRDAggregatorAgent, PRDAggregatorResult
from src.agents.requirements_generator_agent import (
    RequirementsGeneratorAgent,
    RequirementsGeneratorResult,
)
from src.agents.risk_analysis_agent import RiskAnalysisAgent, RiskAnalysisResult
from src.agents.screenshot_analysis_agent import (
    ScreenshotAnalysisAgent,
    ScreenshotAnalysisResult,
)
from src.agents.user_flow_agent import UserFlowAgent, UserFlowResult
from src.config.settings import get_settings
from src.extractors.code_extractor import CodeExtractor, CodeFile
from src.extractors.jira_extractor import JiraExtractor
from src.extractors.minio_extractor import MinioExtractor
from src.utils.file_utils import ensure_directory, write_json
from src.utils.logging_config import ExecutionTimer, get_logger
from src.vector_store.qdrant_manager import QdrantManager

logger = get_logger(__name__)


@dataclass
class PRDGenerationConfig:
    """Configuration for PRD generation."""

    form_name: str
    zip_path: str | None = None
    code_directory: str | None = None
    file_mappings: list[str] | None = None
    minio_bucket: str | None = None
    minio_prefix: str | None = None
    jira_project_key: str | None = None
    jira_jql: str | None = None
    output_dir: str = "./output"
    recreate_vectors: bool = False
    skip_screenshots: bool = False
    skip_jira: bool = False


@dataclass
class PRDGenerationResult:
    """Result of PRD generation."""

    success: bool
    form_name: str
    prd_file_path: str | None = None
    metadata_file_path: str | None = None
    vector_collection: str | None = None
    word_count: int = 0
    section_count: int = 0
    execution_time_seconds: float = 0.0
    error: str | None = None
    agent_metrics: dict[str, Any] | None = None


class PRDGenerator:
    """
    High-level interface for generating PRDs.

    This class orchestrates all agents to produce comprehensive
    Product Requirements Documents from legacy codebases.
    """

    def __init__(self) -> None:
        """Initialize the PRD generator."""
        self.settings = get_settings()
        self.qdrant = QdrantManager()

    async def generate(self, config: PRDGenerationConfig) -> PRDGenerationResult:
        """
        Generate a PRD for the given configuration.

        Args:
            config: PRD generation configuration

        Returns:
            PRDGenerationResult with the outcome
        """
        timer = ExecutionTimer()
        context = AgentContext(form_name=config.form_name)
        agent_metrics: dict[str, Any] = {}

        logger.info(
            "Starting PRD generation",
            form_name=config.form_name,
            skip_screenshots=config.skip_screenshots,
            skip_jira=config.skip_jira,
        )

        try:
            # Phase 1: Extract and vectorize code
            code_files = await self._extract_code(config)
            agent_metrics["code_files"] = len(code_files)
            agent_metrics["vectors_added"] = self._vectorize_code(config, code_files)

            # Phase 2-3: External data extraction (screenshots and Jira)
            screenshot_result = await self._get_screenshot_analysis(context, config)
            jira_result = await self._get_jira_analysis(context, config)
            agent_metrics["screenshot_analysis"] = screenshot_result is not None
            agent_metrics["jira_analysis"] = jira_result is not None

            # Phase 4-6: Analysis phases
            req_result = await self._generate_requirements(context, code_files)
            flow_result = await self._analyze_user_flows(context, screenshot_result)
            risk_result = await self._analyze_risks(context, req_result)

            agent_metrics.update(
                self._collect_analysis_metrics(req_result, flow_result, risk_result)
            )

            # Phase 7: Aggregate PRD
            prd_result = await self._aggregate_prd(
                context, screenshot_result, jira_result, req_result, flow_result, risk_result
            )

            if not prd_result.success or not prd_result.data:
                return self._create_failure_result(
                    config.form_name, prd_result.error or "PRD aggregation failed", agent_metrics
                )

            # Phase 8: Save PRD
            return await self._finalize_and_save(config, prd_result.data, timer, agent_metrics)

        except Exception as e:
            logger.error(
                "PRD generation failed",
                form_name=config.form_name,
                error=str(e),
            )
            return self._create_failure_result(config.form_name, str(e), agent_metrics)

    def _vectorize_code(self, config: PRDGenerationConfig, code_files: list[CodeFile]) -> int:
        """Create vector collection and add code documents."""
        self.qdrant.create_collection(config.form_name, recreate=config.recreate_vectors)

        if not code_files:
            return 0

        extractor = CodeExtractor()
        documents = extractor.to_documents(code_files, config.form_name)
        return self.qdrant.add_documents(config.form_name, documents)

    async def _get_screenshot_analysis(
        self, context: AgentContext, config: PRDGenerationConfig
    ) -> AgentResult[ScreenshotAnalysisResult] | None:
        """Get screenshot analysis if not skipped."""
        if config.skip_screenshots:
            return None
        return await self._analyze_screenshots(context, config)

    async def _get_jira_analysis(
        self, context: AgentContext, config: PRDGenerationConfig
    ) -> AgentResult[AtlassianIntegrationResult] | None:
        """Get Jira analysis if not skipped."""
        if config.skip_jira:
            return None
        return await self._analyze_jira(context, config)

    def _collect_analysis_metrics(
        self,
        req_result: AgentResult[RequirementsGeneratorResult],
        flow_result: AgentResult[UserFlowResult],
        risk_result: AgentResult[RiskAnalysisResult],
    ) -> dict[str, int]:
        """Collect metrics from analysis results."""
        return {
            "requirements_generated": (
                len(req_result.data.functional_requirements)
                if req_result.success and req_result.data
                else 0
            ),
            "user_flows": (
                len(flow_result.data.user_flows) if flow_result.success and flow_result.data else 0
            ),
            "risks_identified": (
                len(risk_result.data.risks) if risk_result.success and risk_result.data else 0
            ),
        }

    async def _finalize_and_save(
        self,
        config: PRDGenerationConfig,
        prd_data: PRDAggregatorResult,
        timer: ExecutionTimer,
        agent_metrics: dict[str, Any],
    ) -> PRDGenerationResult:
        """Save PRD and create success result."""
        output_path = ensure_directory(config.output_dir)
        prd_file, metadata_file = await self._save_prd(
            config.form_name, prd_data.markdown_content, output_path, agent_metrics
        )

        execution_time = timer.elapsed_seconds()

        logger.info(
            "PRD generation complete",
            form_name=config.form_name,
            prd_file=str(prd_file),
            execution_time_seconds=execution_time,
        )

        return PRDGenerationResult(
            success=True,
            form_name=config.form_name,
            prd_file_path=str(prd_file),
            metadata_file_path=str(metadata_file),
            vector_collection=self.qdrant.get_collection_name(config.form_name),
            word_count=prd_data.word_count,
            section_count=prd_data.section_count,
            execution_time_seconds=execution_time,
            agent_metrics=agent_metrics,
        )

    def _create_failure_result(
        self,
        form_name: str,
        error: str,
        agent_metrics: dict[str, Any],
    ) -> PRDGenerationResult:
        """Create a failure result."""
        return PRDGenerationResult(
            success=False,
            form_name=form_name,
            error=error,
            agent_metrics=agent_metrics,
        )

    def _extract_code(self, config: PRDGenerationConfig) -> list[CodeFile]:
        """Extract code from ZIP or directory."""
        extractor = CodeExtractor()

        if config.zip_path:
            return extractor.extract_from_zip(
                config.zip_path,
                file_mappings=config.file_mappings,
            )
        elif config.code_directory:
            return extractor.extract_from_directory(
                config.code_directory,
                file_mappings=config.file_mappings,
            )
        return []

    async def _analyze_screenshots(
        self,
        context: AgentContext,
        config: PRDGenerationConfig,
    ) -> AgentResult[ScreenshotAnalysisResult] | None:
        """Analyze screenshots from Minio."""
        try:
            extractor = MinioExtractor()
            screenshots = extractor.get_form_screenshots(
                config.form_name,
                bucket=config.minio_bucket,
                prefix=config.minio_prefix,
            )

            if screenshots:
                agent = ScreenshotAnalysisAgent()
                result = await agent.analyze(context, screenshots=screenshots)
                return result if result.success else None

        except Exception as e:
            logger.warning("Screenshot analysis failed", error=str(e))

        return None

    async def _analyze_jira(
        self,
        context: AgentContext,
        config: PRDGenerationConfig,
    ) -> AgentResult[AtlassianIntegrationResult] | None:
        """Analyze Jira issues."""
        try:
            extractor = JiraExtractor()
            issues = extractor.get_form_issues(
                config.form_name,
                project_key=config.jira_project_key,
                additional_jql=config.jira_jql,
            )

            if issues:
                agent = AtlassianIntegrationAgent()
                result = await agent.analyze(context, issues=issues)
                return result if result.success else None

        except Exception as e:
            logger.warning("Jira analysis failed", error=str(e))

        return None

    async def _generate_requirements(
        self,
        context: AgentContext,
        code_files: list[CodeFile],
    ) -> AgentResult[RequirementsGeneratorResult]:
        """Generate requirements from code analysis."""
        agent = RequirementsGeneratorAgent()
        return await agent.analyze(context, code_files=code_files)

    async def _analyze_user_flows(
        self,
        context: AgentContext,
        screenshot_result: AgentResult[ScreenshotAnalysisResult] | None,
    ) -> AgentResult[UserFlowResult]:
        """Analyze user flows."""
        agent = UserFlowAgent()
        screenshot_analysis = (
            screenshot_result.data if screenshot_result and screenshot_result.success else None
        )
        return await agent.analyze(context, screenshot_analysis=screenshot_analysis)

    async def _analyze_risks(
        self,
        context: AgentContext,
        requirements_result: AgentResult[RequirementsGeneratorResult],
    ) -> AgentResult[RiskAnalysisResult]:
        """Analyze migration risks."""
        agent = RiskAnalysisAgent()
        return await agent.analyze(context, requirements_analysis=requirements_result)

    async def _aggregate_prd(
        self,
        context: AgentContext,
        screenshot_result: AgentResult[ScreenshotAnalysisResult] | None,
        jira_result: AgentResult[AtlassianIntegrationResult] | None,
        req_result: AgentResult[RequirementsGeneratorResult],
        flow_result: AgentResult[UserFlowResult],
        risk_result: AgentResult[RiskAnalysisResult],
    ) -> AgentResult[PRDAggregatorResult]:
        """Aggregate all analysis results into PRD."""
        agent = PRDAggregatorAgent()
        return await agent.analyze(
            context,
            screenshot_analysis=screenshot_result.data if screenshot_result else None,
            atlassian_analysis=jira_result.data if jira_result else None,
            requirements_analysis=req_result.data if req_result.success else None,
            user_flow_analysis=flow_result.data if flow_result.success else None,
            risk_analysis=risk_result.data if risk_result.success else None,
        )

    def _save_prd(
        self,
        form_name: str,
        content: str,
        output_path: Path,
        metrics: dict[str, Any],
    ) -> tuple[Path, Path]:
        """Save PRD and metadata files."""
        # Save markdown
        prd_file = output_path / f"{form_name}_PRD.md"
        prd_file.write_text(content, encoding="utf-8")

        # Save metadata
        metadata = {
            "form_name": form_name,
            "generated_at": datetime.now().isoformat(),
            "word_count": len(content.split()),
            "file_path": str(prd_file),
            "metrics": metrics,
        }

        metadata_file = output_path / f"{form_name}_PRD_metadata.json"
        write_json(metadata_file, metadata)

        return prd_file, metadata_file
