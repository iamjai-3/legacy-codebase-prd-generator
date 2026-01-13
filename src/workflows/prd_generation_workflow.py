"""
Temporal Workflow for PRD Generation.

This workflow orchestrates all agents and activities to generate
a comprehensive PRD from multiple data sources.
"""

from dataclasses import dataclass
from datetime import timedelta
from typing import Any

from temporalio import workflow
from temporalio.common import RetryPolicy

# Import activities (will be available at runtime)
with workflow.unsafe.imports_passed_through():
    from src.workflows.activities import (
        aggregate_prd_activity,
        analyze_jira_activity,
        analyze_risks_activity,
        analyze_screenshots_activity,
        analyze_user_flows_activity,
        extract_code_activity,
        extract_jira_activity,
        extract_screenshots_activity,
        generate_requirements_activity,
        save_prd_activity,
        store_analysis_results_activity,
        store_vectors_activity,
    )  # noqa: F401


@dataclass
class PRDGenerationInput:
    """Input parameters for PRD generation workflow."""

    form_name: str
    zip_path: str | None = None
    code_directory: str | None = None
    file_mappings: list[str] | None = None
    dependency_file: str | None = None
    minio_bucket: str | None = None
    minio_prefix: str | None = None
    jira_project_key: str | None = None
    jira_jql: str | None = None
    output_dir: str = "./output"
    recreate_vector_collection: bool = False
    skip_screenshots: bool = False
    skip_jira: bool = False


@dataclass
class PRDGenerationOutput:
    """Output from PRD generation workflow."""

    form_name: str
    success: bool
    prd_file_path: str | None = None
    vector_collection: str | None = None
    word_count: int = 0
    section_count: int = 0
    execution_time_seconds: float = 0.0
    error: str | None = None
    agent_results: dict[str, Any] | None = None


@workflow.defn
class PRDGenerationWorkflow:
    """
    Temporal workflow that orchestrates the entire PRD generation process.

    Workflow Steps:
    1. Extract data from all sources (code, screenshots, Jira) - parallel
    2. Store extracted data as vectors
    3. Run analysis agents (screenshot, Jira) - parallel
    4. Generate requirements
    5. Analyze user flows and risks - parallel
    6. Aggregate all insights into PRD
    7. Save PRD document
    """

    def _empty_result(self, source: str) -> dict[str, Any]:
        """Return an empty result for skipped sources."""
        return {
            "success": False,
            "skipped": True,
            "source": source,
            "file_count": 0,
            "screenshot_count": 0,
            "issue_count": 0,
        }

    def _get_if_success(self, result: dict[str, Any], key: str, default: Any = None) -> Any:
        """Get a value from result dict only if the result was successful."""
        return result.get(key, default) if result.get("success") else default

    def _result_if_success(self, result: dict[str, Any]) -> dict[str, Any] | None:
        """Return result dict if successful, None otherwise."""
        return result if result.get("success") else None

    def _build_agent_results(
        self,
        screenshot: dict[str, Any],
        jira: dict[str, Any],
        requirements: dict[str, Any],
        user_flow: dict[str, Any],
        risk: dict[str, Any],
    ) -> dict[str, bool]:
        """Build agent results summary."""
        return {
            "screenshot_analysis": screenshot.get("success", False),
            "jira_analysis": jira.get("success", False),
            "requirements_analysis": requirements.get("success", False),
            "user_flow_analysis": user_flow.get("success", False),
            "risk_analysis": risk.get("success", False),
        }

    def _build_success_output(
        self,
        input: PRDGenerationInput,
        prd_result: dict[str, Any],
        save_result: dict[str, Any],
        vector_result: dict[str, Any],
        agent_results: dict[str, bool],
    ) -> PRDGenerationOutput:
        """Build successful output response."""
        metrics = prd_result.get("generation_metrics", {})
        execution_time = metrics.get("execution_time_ms", 0) / 1000

        return PRDGenerationOutput(
            form_name=input.form_name,
            success=True,
            prd_file_path=save_result.get("markdown_file"),
            vector_collection=vector_result.get("collection_name"),
            word_count=prd_result.get("word_count", 0),
            section_count=prd_result.get("section_count", 0),
            execution_time_seconds=execution_time,
            agent_results=agent_results,
        )

    @workflow.run
    async def run(self, input: PRDGenerationInput) -> PRDGenerationOutput:
        """Execute the PRD generation workflow."""
        workflow.logger.info(f"Starting PRD generation for {input.form_name}")

        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=1),
            maximum_interval=timedelta(minutes=5),
            maximum_attempts=3,
            backoff_coefficient=2.0,
        )

        opts = {"start_to_close_timeout": timedelta(minutes=30), "retry_policy": retry_policy}
        long_opts = {"start_to_close_timeout": timedelta(minutes=60), "retry_policy": retry_policy}

        try:
            # Phase 1: Data Extraction
            extraction = await self._extract_data(input, opts)

            # Phase 2: Vector Storage
            vector_result = await self._store_vectors(input, extraction, opts)

            # Phase 3: Initial Analysis
            analysis = await self._run_initial_analysis(input, extraction, long_opts)

            # Phase 4: Requirements Generation
            requirements_analysis = await self._generate_requirements(
                input, extraction, analysis, long_opts
            )

            # Phase 5: Flow and Risk Analysis
            flow_risk = await self._analyze_flows_and_risks(
                input, extraction, analysis, requirements_analysis, long_opts
            )

            # Phase 5.5: Store Analysis Results
            await self._store_analysis_results(
                input, analysis, requirements_analysis, flow_risk, opts
            )

            # Phase 6 & 7: Aggregate and Save PRD
            return await self._finalize_prd(
                input, analysis, requirements_analysis, flow_risk, vector_result, long_opts, opts
            )

        except Exception as e:
            workflow.logger.error(f"Workflow failed: {str(e)}")
            return PRDGenerationOutput(form_name=input.form_name, success=False, error=str(e))

    async def _extract_data(
        self, input: PRDGenerationInput, opts: dict[str, Any]
    ) -> dict[str, dict[str, Any]]:
        """Phase 1: Extract data from all sources."""
        workflow.logger.info("Phase 1: Extracting data from all sources")

        code_data = self._empty_result("code")
        if input.zip_path or input.code_directory:
            code_data = await workflow.execute_activity(
                extract_code_activity,
                args=[
                    input.form_name,
                    input.zip_path,
                    input.code_directory,
                    input.file_mappings,
                    input.dependency_file,
                ],
                **opts,
            )

        screenshot_data = self._empty_result("screenshots")
        if not input.skip_screenshots:
            screenshot_data = await workflow.execute_activity(
                extract_screenshots_activity,
                args=[input.form_name, input.minio_bucket, input.minio_prefix],
                **opts,
            )

        jira_data = self._empty_result("jira")
        if not input.skip_jira:
            jira_data = await workflow.execute_activity(
                extract_jira_activity,
                args=[input.form_name, input.jira_project_key, input.jira_jql],
                **opts,
            )

        workflow.logger.info(
            f"Extraction complete - Code: {code_data.get('file_count', 0)}, "
            f"Screenshots: {screenshot_data.get('screenshot_count', 0)}, "
            f"Jira: {jira_data.get('issue_count', 0)}"
        )

        return {"code": code_data, "screenshots": screenshot_data, "jira": jira_data}

    async def _store_vectors(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> dict[str, Any]:
        """Phase 2: Store extracted data as vectors."""
        workflow.logger.info("Phase 2: Storing data as vectors")

        result = await workflow.execute_activity(
            store_vectors_activity,
            args=[
                input.form_name,
                extraction["code"],
                extraction["screenshots"],
                extraction["jira"],
                input.recreate_vector_collection,
            ],
            **opts,
        )

        workflow.logger.info(
            f"Vector storage complete - Collection: {result.get('collection_name')}, "
            f"Vectors: {result.get('total_vectors_added', 0)}"
        )
        return result

    async def _run_initial_analysis(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        """Phase 3: Run screenshot and Jira analysis."""
        workflow.logger.info("Phase 3: Running initial analysis agents")

        screenshot_analysis = self._empty_result("screenshot_analysis")
        if not input.skip_screenshots and extraction["screenshots"].get("screenshot_count", 0) > 0:
            screenshot_analysis = await workflow.execute_activity(
                analyze_screenshots_activity,
                args=[input.form_name, extraction["screenshots"]],
                **opts,
            )

        jira_analysis = self._empty_result("jira_analysis")
        if not input.skip_jira and extraction["jira"].get("issue_count", 0) > 0:
            jira_analysis = await workflow.execute_activity(
                analyze_jira_activity,
                args=[input.form_name, extraction["jira"]],
                **opts,
            )

        return {"screenshot": screenshot_analysis, "jira": jira_analysis}

    async def _generate_requirements(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        analysis: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> dict[str, Any]:
        """Phase 4: Generate requirements."""
        workflow.logger.info("Phase 4: Generating requirements")

        jira_context = self._get_if_success(analysis["jira"], "summary")
        screenshot_context = self._get_if_success(analysis["screenshot"], "ui_flow_summary")

        return await workflow.execute_activity(
            generate_requirements_activity,
            args=[input.form_name, extraction["code"], jira_context, screenshot_context],
            **opts,
        )

    async def _analyze_flows_and_risks(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        analysis: dict[str, dict[str, Any]],
        requirements: dict[str, Any],
        opts: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        """Phase 5: Analyze user flows and risks in parallel."""
        workflow.logger.info("Phase 5: Analyzing user flows and risks")

        user_flow_task = workflow.execute_activity(
            analyze_user_flows_activity,
            args=[
                input.form_name,
                self._result_if_success(analysis["screenshot"]),
                extraction["code"],
            ],
            **opts,
        )

        risk_task = workflow.execute_activity(
            analyze_risks_activity,
            args=[input.form_name, extraction["code"], self._result_if_success(requirements)],
            **opts,
        )

        user_flow_analysis = await user_flow_task
        risk_analysis = await risk_task

        return {"user_flow": user_flow_analysis, "risk": risk_analysis}

    async def _store_analysis_results(
        self,
        input: PRDGenerationInput,
        analysis: dict[str, dict[str, Any]],
        requirements: dict[str, Any],
        flow_risk: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> None:
        """Phase 5.5: Store analysis results in knowledge base."""
        workflow.logger.info("Phase 5.5: Storing analysis results in knowledge base")

        await workflow.execute_activity(
            store_analysis_results_activity,
            args=[
                input.form_name,
                self._result_if_success(analysis["screenshot"]),
                self._result_if_success(requirements),
                self._result_if_success(flow_risk["user_flow"]),
                self._result_if_success(flow_risk["risk"]),
            ],
            **opts,
        )

    async def _finalize_prd(
        self,
        input: PRDGenerationInput,
        analysis: dict[str, dict[str, Any]],
        requirements: dict[str, Any],
        flow_risk: dict[str, dict[str, Any]],
        vector_result: dict[str, Any],
        long_opts: dict[str, Any],
        opts: dict[str, Any],
    ) -> PRDGenerationOutput:
        """Phase 6 & 7: Aggregate and save PRD."""
        workflow.logger.info("Phase 6: Aggregating PRD document")

        prd_result = await workflow.execute_activity(
            aggregate_prd_activity,
            args=[
                input.form_name,
                self._result_if_success(analysis["screenshot"]),
                self._result_if_success(analysis["jira"]),
                self._result_if_success(requirements),
                self._result_if_success(flow_risk["user_flow"]),
                self._result_if_success(flow_risk["risk"]),
            ],
            **long_opts,
        )

        if not prd_result.get("success"):
            return PRDGenerationOutput(
                form_name=input.form_name,
                success=False,
                error=prd_result.get("error", "PRD aggregation failed"),
            )

        workflow.logger.info("Phase 7: Saving PRD document")

        save_result = await workflow.execute_activity(
            save_prd_activity,
            args=[input.form_name, prd_result.get("markdown_content", ""), input.output_dir],
            **opts,
        )

        workflow.logger.info(f"PRD saved to: {save_result.get('markdown_file')}")

        agent_results = self._build_agent_results(
            analysis["screenshot"],
            analysis["jira"],
            requirements,
            flow_risk["user_flow"],
            flow_risk["risk"],
        )

        return self._build_success_output(
            input, prd_result, save_result, vector_result, agent_results
        )
