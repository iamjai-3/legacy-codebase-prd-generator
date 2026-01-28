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
        analyze_database_activity,
        analyze_screenshots_activity,
        analyze_user_flows_activity,
        ensure_minio_folders_activity,
        extract_code_activity,
        extract_existing_prd_activity,
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
    minio_bucket: str | None = None
    minio_prefix: str | None = None
    output_dir: str = "./output"
    recreate_vector_collection: bool = False
    skip_screenshots: bool = False
    db_doc_path: str | None = None
    skip_database_analysis: bool = False


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

    This workflow creates a combined knowledge base from:
    - Legacy code (for existing implementation details)
    - Screenshots (for UI context)
    - Existing PRD documents (for business logic and app flow)

    Workflow Steps:
    1. Extract data from all sources (code, screenshots, existing PRDs) from MinIO
    2. Store all extracted data as vectors in unified knowledge base
    3. Run analysis agents (screenshot) - parallel
    4. Generate requirements using knowledge base
    5. Analyze user flows using knowledge base
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

    def _result_if_success(self, result: dict[str, Any] | None) -> dict[str, Any] | None:
        """Return result dict if successful, None otherwise."""
        if result is None:
            return None
        return result if result.get("success") else None

    def _build_agent_results(
        self,
        screenshot: dict[str, Any],
        requirements: dict[str, Any],
        user_flow: dict[str, Any],
        existing_prd: dict[str, Any],
        database: dict[str, Any],
    ) -> dict[str, bool]:
        """Build agent results summary."""
        return {
            "screenshot_analysis": screenshot.get("success", False),
            "requirements_analysis": requirements.get("success", False),
            "user_flow_analysis": user_flow.get("success", False),
            "existing_prd_extraction": existing_prd.get("success", False),
            "database_analysis": database.get("success", False),
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

        # Ensure MinIO folder structure exists for this form (non-blocking)
        await self._ensure_minio_folders(input)

        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=1),
            maximum_interval=timedelta(minutes=5),
            maximum_attempts=3,
            backoff_coefficient=2.0,
        )

        opts = {"start_to_close_timeout": timedelta(minutes=30), "retry_policy": retry_policy}
        long_opts = {"start_to_close_timeout": timedelta(minutes=60), "retry_policy": retry_policy}

        try:
            # Phase 1: Data Extraction (code, screenshots, existing PRDs from MinIO)
            extraction = await self._extract_data(input, opts)

            # Phase 2: Vector Storage (creates unified knowledge base)
            vector_result = await self._store_vectors(input, extraction, opts)

            # Phase 3: Initial Analysis
            analysis = await self._run_initial_analysis(input, extraction, long_opts)

            # Phase 4: Requirements Generation
            requirements_analysis = await self._generate_requirements(
                input, extraction, analysis, long_opts
            )

            # Phase 5: User Flow Analysis
            user_flow_analysis = await self._analyze_user_flows(
                input, extraction, analysis, long_opts
            )

            # Phase 5.5: Store Analysis Results (database analysis not yet available)
            await self._store_analysis_results(
                input, analysis, requirements_analysis, user_flow_analysis, None, opts
            )

            # Phase 5.9: Database Analysis (form-specific, runs just before PRD aggregation)
            database_analysis = await self._analyze_database(input, opts)

            # Phase 6 & 7: Aggregate and Save PRD
            return await self._finalize_prd(
                input,
                extraction,
                analysis,
                requirements_analysis,
                user_flow_analysis,
                database_analysis,
                vector_result,
                long_opts,
                opts,
            )

        except Exception as e:
            workflow.logger.error(f"Workflow failed: {str(e)}")
            return PRDGenerationOutput(form_name=input.form_name, success=False, error=str(e))

    async def _ensure_minio_folders(self, input: PRDGenerationInput) -> None:
        """Ensure MinIO folder structure exists for the form (verifies bucket exists first)."""
        try:
            # Verify bucket exists and create folders if missing (throws error if bucket missing)
            result = await workflow.execute_activity(
                ensure_minio_folders_activity,
                args=[input.form_name, None],  # form_name, bucket (None = use default "metadatas")
                start_to_close_timeout=timedelta(seconds=30),
            )
            if result.get("success"):
                workflow.logger.info(
                    f"MinIO folder structure ensured for {input.form_name}: {result.get('form_folders', {})}"
                )
            else:
                # Bucket doesn't exist - this is critical, workflow should fail
                error = result.get("error", "Unknown error")
                workflow.logger.error(f"MinIO folder setup failed for {input.form_name}: {error}")
                raise ValueError(f"MinIO setup failed: {error}")
        except ValueError:
            # Re-raise ValueError (bucket doesn't exist) to terminate workflow
            raise
        except Exception as e:
            workflow.logger.error(f"Could not ensure MinIO folders for {input.form_name}: {str(e)}")
            raise  # Re-raise to fail workflow

    async def _extract_data(
        self, input: PRDGenerationInput, opts: dict[str, Any]
    ) -> dict[str, dict[str, Any]]:
        """Phase 1: Extract data from all sources including existing PRDs."""
        workflow.logger.info("Phase 1: Extracting data from all sources")

        # Code extraction - always run (will use MinIO if no local path provided)
        code_data = await workflow.execute_activity(
            extract_code_activity,
            args=[
                input.form_name,
                input.zip_path,
                input.code_directory,
            ],
            **opts,
        )

        screenshot_data = self._empty_result("screenshots")
        if not input.skip_screenshots:
            # Always use metadatas bucket (default), don't pass bucket parameter
            screenshot_data = await workflow.execute_activity(
                extract_screenshots_activity,
                args=[input.form_name, None, None],  # bucket=None uses default "metadatas"
                **opts,
            )

        # Extract existing PRD documents from MinIO (business logic, app flow, requirements)
        existing_prd_data = await workflow.execute_activity(
            extract_existing_prd_activity,
            args=[input.form_name],  # Only MinIO, no local fallback
            **opts,
        )

        workflow.logger.info(
            f"Extraction complete - Code: {code_data.get('file_count', 0)}, "
            f"Screenshots: {screenshot_data.get('screenshot_count', 0)}, "
            f"Existing PRD docs: {existing_prd_data.get('document_count', 0)}"
        )

        return {
            "code": code_data,
            "screenshots": screenshot_data,
            "existing_prd": existing_prd_data,
        }

    async def _store_vectors(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> dict[str, Any]:
        """Phase 2: Store extracted data as vectors to create unified knowledge base."""
        workflow.logger.info("Phase 2: Creating unified knowledge base (vector storage)")

        result = await workflow.execute_activity(
            store_vectors_activity,
            args=[
                input.form_name,
                extraction["code"],
                extraction["screenshots"],
                extraction["existing_prd"],  # Include existing PRD documents
                input.recreate_vector_collection,
                extraction["code"].get(
                    "extract_dir"
                ),  # Pass extract directory to read file content
            ],
            **opts,
        )

        workflow.logger.info(
            f"Knowledge base created - Collection: {result.get('collection_name')}, "
            f"Total vectors: {result.get('total_vectors_added', 0)}"
        )
        return result

    async def _analyze_database(
        self, input: PRDGenerationInput, opts: dict[str, Any]
    ) -> dict[str, Any]:
        """Phase 5.9: Analyze form-specific database table mappings (runs just before PRD aggregation)."""
        workflow.logger.info("Phase 5.9: Analyzing form-specific database table mappings")

        if input.skip_database_analysis:
            workflow.logger.info("Skipping database analysis")
            return {
                "success": False,
                "skipped": True,
                "tables_analyzed": 0,
                "relationships_mapped": 0,
                "vectors_stored": 0,
            }

        try:
            # Database analysis agent will handle MinIO/local lookup automatically
            # Pass None to let it determine the path (MinIO first, then local)
            form_specific_path = None
            if not input.db_doc_path:
                # Agent will try MinIO: FORMS/{FORM_NAME}/FORM_DOCS/{FORM_NAME}_SourceTables.md
                # Then fallback to local: src/PRDs/{FORM_NAME}/FORM_DOCS/{FORM_NAME}_SourceTables.md
                workflow.logger.info(
                    f"Database analysis will auto-detect source tables file for {input.form_name}"
                )

            result = await workflow.execute_activity(
                analyze_database_activity,
                args=[
                    input.form_name,
                    str(form_specific_path) if form_specific_path else input.db_doc_path,
                ],
                **opts,
            )

            workflow.logger.info(
                f"Database analysis complete - Tables: {result.get('tables_analyzed', 0)}, "
                f"Relationships: {result.get('relationships_mapped', 0)}, "
                f"Vectors: {result.get('vectors_stored', 0)}"
            )

            return result
        except Exception as e:
            workflow.logger.warning(f"Database analysis failed: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "tables_analyzed": 0,
                "relationships_mapped": 0,
                "vectors_stored": 0,
            }

    async def _run_initial_analysis(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        """Phase 3: Run screenshot analysis."""
        workflow.logger.info("Phase 3: Running initial analysis agents")

        screenshot_analysis = self._empty_result("screenshot_analysis")
        if not input.skip_screenshots and extraction["screenshots"].get("screenshot_count", 0) > 0:
            screenshot_analysis = await workflow.execute_activity(
                analyze_screenshots_activity,
                args=[input.form_name, extraction["screenshots"]],
                **opts,
            )

        return {"screenshot": screenshot_analysis}

    async def _generate_requirements(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        analysis: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> dict[str, Any]:
        """Phase 4: Generate requirements."""
        workflow.logger.info("Phase 4: Generating requirements")

        screenshot_context = self._get_if_success(analysis["screenshot"], "ui_flow_summary")

        return await workflow.execute_activity(
            generate_requirements_activity,
            args=[input.form_name, extraction["code"], None, screenshot_context],  # No Jira context
            **opts,
        )

    async def _analyze_user_flows(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        analysis: dict[str, dict[str, Any]],
        opts: dict[str, Any],
    ) -> dict[str, Any]:
        """Phase 5: Analyze user flows using the knowledge base."""
        workflow.logger.info("Phase 5: Analyzing user flows")

        user_flow_analysis = await workflow.execute_activity(
            analyze_user_flows_activity,
            args=[
                input.form_name,
                self._result_if_success(analysis["screenshot"]),
                extraction["code"],
            ],
            **opts,
        )

        return user_flow_analysis

    async def _store_analysis_results(
        self,
        input: PRDGenerationInput,
        analysis: dict[str, dict[str, Any]],
        requirements: dict[str, Any],
        user_flow: dict[str, Any],
        database_analysis: dict[str, Any],
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
                self._result_if_success(user_flow),
                self._result_if_success(database_analysis),
            ],
            **opts,
        )

    async def _finalize_prd(
        self,
        input: PRDGenerationInput,
        extraction: dict[str, dict[str, Any]],
        analysis: dict[str, dict[str, Any]],
        requirements: dict[str, Any],
        user_flow: dict[str, Any],
        database_analysis: dict[str, Any],
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
                self._result_if_success(requirements),
                self._result_if_success(user_flow),
                self._result_if_success(database_analysis),
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
            requirements,
            user_flow,
            extraction["existing_prd"],
            database_analysis,
        )

        return self._build_success_output(
            input, prd_result, save_result, vector_result, agent_results
        )
