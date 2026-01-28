"""
Temporal activities for PRD generation workflow.

Activities are organized into modules by function:
- extraction: Code, screenshot, and existing PRD extraction from MinIO
- analysis: Screenshot, database, requirements, and user flow analysis
- aggregation: PRD document aggregation
- storage: Vector storage and file saving
"""

from src.workflows.activities.aggregation import aggregate_prd_activity
from src.workflows.activities.analysis import (
    analyze_database_activity,
    analyze_screenshots_activity,
    analyze_user_flows_activity,
    generate_requirements_activity,
)
from src.workflows.activities.extraction import (
    extract_code_activity,
    extract_existing_prd_activity,
    extract_screenshots_activity,
)
from src.workflows.activities.storage import (
    ensure_minio_folders_activity,
    save_prd_activity,
    store_analysis_results_activity,
    store_vectors_activity,
)

__all__ = [
    # Extraction
    "extract_code_activity",
    "extract_screenshots_activity",
    "extract_existing_prd_activity",
    # Analysis
    "analyze_screenshots_activity",
    "analyze_database_activity",
    "generate_requirements_activity",
    "analyze_user_flows_activity",
    # Aggregation
    "aggregate_prd_activity",
    # Storage
    "ensure_minio_folders_activity",
    "store_vectors_activity",
    "store_analysis_results_activity",
    "save_prd_activity",
]
