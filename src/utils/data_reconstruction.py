"""
Data reconstruction utilities for Temporal activities.

Handles converting serialized dictionaries back to dataclass instances
after Temporal workflow serialization/deserialization.
"""

from typing import Any

from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def reconstruct_screenshot_analysis(data: dict[str, Any] | None, form_name: str) -> Any:
    """
    Reconstruct ScreenshotAnalysisResult from serialized dict.

    Args:
        data: Serialized screenshot analysis data
        form_name: Form name for the result

    Returns:
        ScreenshotAnalysisResult or None
    """
    if not data or not data.get("success"):
        return None

    from src.agents.screenshot_analysis_agent import (
        ScreenAnalysis,
        ScreenshotAnalysisResult,
        UIElement,
    )

    screen_analyses = []
    for sa_dict in data.get("screen_analyses", []):
        ui_elements = [
            UIElement(
                element_type=elem.get("element_type", "unknown"),
                label=elem.get("label", ""),
                description=elem.get("description", ""),
                location=elem.get("location", ""),
                interactions=elem.get("interactions", []),
            )
            for elem in sa_dict.get("ui_elements", [])
        ]
        screen_analyses.append(
            ScreenAnalysis(
                screen_name=sa_dict.get("screen_name", ""),
                screen_type=sa_dict.get("screen_type", "general"),
                purpose=sa_dict.get("purpose", ""),
                ui_elements=ui_elements,
                layout_description=sa_dict.get("layout_description", ""),
                user_actions=sa_dict.get("user_actions", []),
                data_displayed=sa_dict.get("data_displayed", []),
                validation_rules=sa_dict.get("validation_rules", []),
                accessibility_notes=sa_dict.get("accessibility_notes", []),
            )
        )

    return ScreenshotAnalysisResult(
        form_name=form_name,
        total_screens=data.get("total_screens", 0),
        screen_analyses=screen_analyses,
        ui_flow_summary=data.get("ui_flow_summary", ""),
        common_patterns=data.get("common_patterns", []),
        component_inventory=data.get("component_inventory", {}),
        recommendations=data.get("recommendations", []),
    )


def reconstruct_requirements_analysis(data: dict[str, Any] | None, form_name: str) -> Any:
    """
    Reconstruct RequirementsGeneratorResult from serialized dict.

    Args:
        data: Serialized requirements analysis data
        form_name: Form name for the result

    Returns:
        RequirementsGeneratorResult or None
    """
    if not data or not data.get("success"):
        return None

    from src.agents.requirements_generator_agent import (
        APISpecification,
        BusinessLogic,
        DatabaseMapping,
        DataRequirement,
        FunctionalRequirement,
        IntegrationRequirement,
        NonFunctionalRequirement,
        RequirementsGeneratorResult,
        SourceTable,
        ValidationRule,
        WorkflowSpec,
    )

    # Reconstruct functional requirements with enhanced fields
    func_reqs = [
        FunctionalRequirement(
            req_id=req.get("req_id", ""),
            title=req.get("title", ""),
            description=req.get("description", ""),
            priority=req.get("priority", "P2"),
            category=req.get("category", ""),
            business_logic=req.get("business_logic", ""),
            source_methods=req.get("source_methods", []),
            api_specification=req.get("api_specification", {}),
            database_operations=req.get("database_operations", []),
            validation_rules=req.get("validation_rules", []),
            calculations=req.get("calculations", []),
            user_story=req.get("user_story", ""),
            acceptance_criteria=req.get("acceptance_criteria", []),
            dependencies=req.get("dependencies", []),
            source_files=req.get("source_files", []),
        )
        for req in data.get("functional_requirements", [])
    ]

    # Reconstruct non-functional requirements with enhanced fields
    non_func_reqs = [
        NonFunctionalRequirement(
            req_id=req.get("req_id", ""),
            category=req.get("category", ""),
            title=req.get("title", ""),
            description=req.get("description", ""),
            current_implementation=req.get("current_implementation", ""),
            metric=req.get("metric", ""),
            target_value=req.get("target_value", ""),
            measurement_method=req.get("measurement_method", ""),
            migration_consideration=req.get("migration_consideration", ""),
            priority=req.get("priority", "Medium"),
        )
        for req in data.get("non_functional_requirements", [])
    ]

    # Reconstruct data requirements with enhanced fields
    data_reqs = [
        DataRequirement(
            entity_name=req.get("entity_name", ""),
            description=req.get("description", ""),
            source_table=req.get("source_table", ""),
            source_class=req.get("source_class", ""),
            fields=req.get("fields", []),
            primary_key=req.get("primary_key", []),
            foreign_keys=req.get("foreign_keys", []),
            indexes=req.get("indexes", []),
            relationships=req.get("relationships", []),
            business_rules=req.get("business_rules", []),
            sample_queries=req.get("sample_queries", []),
        )
        for req in data.get("data_requirements", [])
    ]

    # Reconstruct API specifications
    api_specs = [
        APISpecification(
            endpoint_name=api.get("endpoint_name", ""),
            http_method=api.get("http_method", "GET"),
            path=api.get("path", ""),
            description=api.get("description", ""),
            request_spec=api.get("request_spec", {}),
            response_spec=api.get("response_spec", {}),
            business_logic=api.get("business_logic", ""),
            source_method=api.get("source_method", ""),
        )
        for api in data.get("api_specifications", [])
    ]

    # Reconstruct business logic
    business_logic = [
        BusinessLogic(
            logic_id=bl.get("logic_id", ""),
            name=bl.get("name", ""),
            logic_type=bl.get("logic_type", ""),
            description=bl.get("description", ""),
            trigger=bl.get("trigger", ""),
            steps=bl.get("steps", []),
            inputs=bl.get("inputs", []),
            outputs=bl.get("outputs", []),
            conditions=bl.get("conditions", []),
            source_location=bl.get("source_location", ""),
        )
        for bl in data.get("business_logic", [])
    ]

    # Reconstruct integration requirements
    integration_reqs = [
        IntegrationRequirement(
            integration_id=integ.get("integration_id", ""),
            name=integ.get("name", ""),
            integration_type=integ.get("integration_type", ""),
            direction=integ.get("direction", ""),
            external_system=integ.get("external_system", ""),
            purpose=integ.get("purpose", ""),
            specification=integ.get("specification", {}),
            data_mapping=integ.get("data_mapping", []),
            error_handling=integ.get("error_handling", {}),
            source_files=integ.get("source_files", []),
        )
        for integ in data.get("integration_requirements", [])
    ]

    # Reconstruct validation rules
    validation_rules = [
        ValidationRule(
            rule_id=vr.get("rule_id", ""),
            field=vr.get("field", ""),
            entity=vr.get("entity", ""),
            rule_type=vr.get("rule_type", ""),
            condition=vr.get("condition", ""),
            error_message=vr.get("error_message", ""),
            description=vr.get("description", ""),
            when_applied=vr.get("when_applied", ""),
            source_location=vr.get("source_location", ""),
        )
        for vr in data.get("validation_rules", [])
    ]

    # Reconstruct workflow specs
    workflow_specs = [
        WorkflowSpec(
            workflow_id=wf.get("workflow_id", ""),
            name=wf.get("name", ""),
            description=wf.get("description", ""),
            entity=wf.get("entity", ""),
            states=wf.get("states", []),
            transitions=wf.get("transitions", []),
            initial_state=wf.get("initial_state", ""),
            terminal_states=wf.get("terminal_states", []),
            source_location=wf.get("source_location", ""),
        )
        for wf in data.get("workflow_specs", [])
    ]

    # Reconstruct source tables
    source_tables = [
        SourceTable(
            table_name=st.get("table_name", ""),
            description=st.get("description", ""),
            table_type=st.get("table_type", "primary"),
            columns=st.get("columns", []),
            primary_key=st.get("primary_key", []),
            foreign_keys=st.get("foreign_keys", []),
            indexes=st.get("indexes", []),
            stored_procedures=st.get("stored_procedures", []),
        )
        for st in data.get("source_tables", [])
    ]

    # Reconstruct database mappings
    database_mappings = [
        DatabaseMapping(
            entity_class=dm.get("entity_class", ""),
            table_name=dm.get("table_name", ""),
            field_mappings=dm.get("field_mappings", []),
            relationships=dm.get("relationships", []),
            queries=dm.get("queries", []),
        )
        for dm in data.get("database_mappings", [])
    ]

    return RequirementsGeneratorResult(
        form_name=form_name,
        functional_requirements=func_reqs,
        non_functional_requirements=non_func_reqs,
        data_requirements=data_reqs,
        api_specifications=api_specs,
        business_logic=business_logic,
        integration_requirements=integration_reqs,
        validation_rules=validation_rules,
        workflow_specs=workflow_specs,
        source_tables=source_tables,
        database_mappings=database_mappings,
        business_rules=data.get("business_rules", []),
        assumptions=data.get("assumptions", []),
        out_of_scope=data.get("out_of_scope", []),
        summary=data.get("summary", ""),
        code_references=data.get("code_references", {}),
    )


def reconstruct_user_flow_analysis(data: dict[str, Any] | None, form_name: str) -> Any:
    """
    Reconstruct UserFlowResult from serialized dict.

    Args:
        data: Serialized user flow analysis data
        form_name: Form name for the result

    Returns:
        UserFlowResult or None
    """
    if not data or not data.get("success"):
        return None

    from src.agents.user_flow_agent import (
        UserFlow,
        UserFlowResult,
        UserFlowStep,
    )

    user_flows = []
    for flow_dict in data.get("user_flows", []):
        steps = [
            UserFlowStep(
                step_number=step.get("step_number", 0),
                action=step.get("action", ""),
                screen=step.get("screen", ""),
                input_data=step.get("input_data", []),
                expected_result=step.get("expected_result", ""),
                alternative_paths=step.get("alternative_paths", []),
                error_scenarios=step.get("error_scenarios", []),
            )
            for step in flow_dict.get("steps", [])
        ]
        user_flows.append(
            UserFlow(
                flow_id=flow_dict.get("flow_id", ""),
                name=flow_dict.get("name", ""),
                description=flow_dict.get("description", ""),
                actor=flow_dict.get("actor", ""),
                preconditions=flow_dict.get("preconditions", []),
                steps=steps,
                postconditions=flow_dict.get("postconditions", []),
                success_criteria=flow_dict.get("success_criteria", ""),
                estimated_time=flow_dict.get("estimated_time", ""),
            )
        )

    return UserFlowResult(
        form_name=form_name,
        user_flows=user_flows,
        primary_actors=data.get("primary_actors", []),
        entry_points=data.get("entry_points", []),
        exit_points=data.get("exit_points", []),
        user_journey_map=data.get("user_journey_map", ""),
        flow_diagram_mermaid=data.get("flow_diagram_mermaid", ""),
    )


def reconstruct_code_files(data: dict[str, Any] | None) -> list:
    """
    Reconstruct CodeFile objects from serialized dict.

    Args:
        data: Serialized code data

    Returns:
        List of CodeFile objects
    """
    if not data:
        return []

    from src.extractors.code_extractor import CodeFile

    # Try to reconstruct from raw_files first (for backward compatibility)
    raw_files = data.get("raw_files", [])
    code_files = []

    if raw_files:
        # Use raw_files if available (legacy mode)
        for file_data in raw_files:
            if isinstance(file_data, CodeFile):
                code_files.append(file_data)
            elif isinstance(file_data, dict):
                code_files.append(
                    CodeFile(
                        path=file_data.get("path", ""),
                        content=file_data.get("content", ""),
                        language=file_data.get("language", "unknown"),
                        file_type=file_data.get("file_type", "source"),
                        classes=file_data.get("classes", []),
                        methods=file_data.get("methods", []),
                        imports=file_data.get("imports", []),
                        dependencies=file_data.get("dependencies", []),
                        line_count=file_data.get("line_count", 0),
                    )
                )
    else:
        # Reconstruct from metadata in files array (no full content)
        # This is used when raw_files is omitted to avoid Temporal size limits
        for file_info in data.get("files", []):
            code_files.append(
                CodeFile(
                    path=file_info.get("path", ""),
                    content="",  # Content not available - agents should use vector store
                    language=file_info.get("language", "unknown"),
                    file_type=file_info.get("file_type", "source"),
                    classes=file_info.get("classes", []),
                    methods=file_info.get("methods", []),
                    imports=file_info.get("imports", []),
                    dependencies=[],  # Not available in metadata
                    line_count=file_info.get("line_count", 0),
                )
            )

    return code_files


def reconstruct_screenshots(data: dict[str, Any] | None, form_name: str) -> list:
    """
    Reconstruct Screenshot objects from serialized dict.

    Args:
        data: Serialized screenshot data
        form_name: Form name for context

    Returns:
        List of Screenshot objects
    """
    if not data:
        return []

    from src.extractors.minio_extractor import Screenshot

    raw_screenshots = data.get("raw_screenshots", [])
    screenshots = []
    minio_extractor = None  # Lazy initialization

    for item in raw_screenshots:
        if isinstance(item, Screenshot):
            screenshots.append(item)
            continue

        if not isinstance(item, dict):
            continue

        # Handle image_data serialization
        image_data = _restore_image_data(item, minio_extractor, form_name)

        screenshots.append(
            Screenshot(
                object_name=item.get("object_name", ""),
                bucket=item.get("bucket", ""),
                form_name=item.get("form_name", form_name),
                screen_type=item.get("screen_type", "general"),
                image_data=image_data,
                content_type=item.get("content_type", "image/png"),
                size=len(image_data) if image_data else item.get("size", 0),
                metadata=item.get("metadata", {}),
            )
        )

    return screenshots


def _restore_image_data(item: dict[str, Any], minio_extractor: Any, form_name: str) -> bytes:
    """
    Restore image data from various serialization formats.

    Args:
        item: Screenshot dict
        minio_extractor: Optional MinioExtractor instance
        form_name: Form name for logging

    Returns:
        Image data as bytes
    """
    import base64

    from src.extractors.minio_extractor import MinioExtractor

    image_data = item.get("image_data", b"")

    # Handle list of integers
    if isinstance(image_data, list):
        return bytes(image_data)

    # Handle base64 string
    if isinstance(image_data, str):
        try:
            return base64.b64decode(image_data)
        except Exception:
            pass

    # Handle bytes
    if isinstance(image_data, bytes) and len(image_data) > 0:
        return image_data

    # Fetch from Minio as fallback
    try:
        bucket = item.get("bucket", "")
        object_name = item.get("object_name", "")
        if bucket and object_name:
            if minio_extractor is None:
                minio_extractor = MinioExtractor()
            screenshot_obj = minio_extractor.get_screenshot(bucket, object_name)
            if screenshot_obj and screenshot_obj.image_data:
                logger.debug(
                    "Fetched image from Minio",
                    form_name=form_name,
                    object_name=object_name,
                    size=len(screenshot_obj.image_data),
                )
                return screenshot_obj.image_data
    except Exception as e:
        logger.warning(
            "Failed to fetch image from Minio",
            form_name=form_name,
            object_name=item.get("object_name", ""),
            error=str(e),
        )

    return b""
