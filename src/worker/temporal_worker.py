"""
Temporal Worker for PRD Generation.

This module runs the Temporal worker that executes PRD generation workflows.
"""

import asyncio
import signal
import sys

from temporalio.client import Client
from temporalio.worker import Worker

from src.config.settings import get_settings
from src.utils.logging_config import get_logger, setup_logging
from src.workflows.activities import (
    aggregate_prd_activity,
    analyze_database_activity,
    analyze_screenshots_activity,
    analyze_user_flows_activity,
    extract_code_activity,
    extract_existing_prd_activity,
    extract_screenshots_activity,
    generate_requirements_activity,
    save_prd_activity,
    store_analysis_results_activity,
    store_vectors_activity,
    verify_minio_bucket_activity,
)  # noqa: F401 - activities are used at runtime
from src.workflows.prd_generation_workflow import PRDGenerationWorkflow

logger = get_logger(__name__)

# All activities to register
ACTIVITIES = [
    # Setup activities
    verify_minio_bucket_activity,
    # Extraction activities
    extract_code_activity,
    extract_screenshots_activity,
    extract_existing_prd_activity,
    # Analysis activities
    analyze_screenshots_activity,
    analyze_database_activity,
    generate_requirements_activity,
    analyze_user_flows_activity,
    # Aggregation and storage activities
    aggregate_prd_activity,
    store_analysis_results_activity,
    store_vectors_activity,
    save_prd_activity,
]


def create_worker(client: Client, task_queue: str) -> Worker:
    """
    Create a Temporal worker with all activities and workflows.

    Args:
        client: Temporal client
        task_queue: Task queue name

    Returns:
        Configured Worker instance
    """
    return Worker(
        client,
        task_queue=task_queue,
        workflows=[PRDGenerationWorkflow],
        activities=ACTIVITIES,
    )


async def run_worker() -> None:
    """
    Run the Temporal worker.

    Connects to Temporal server and starts processing workflows.
    """
    settings = get_settings()

    logger.info(
        "Starting PRD Agent Worker",
        temporal_address=settings.temporal.address,
        task_queue=settings.temporal.task_queue,
    )

    # Connect to Temporal
    client = await Client.connect(
        settings.temporal.address,
        namespace=settings.temporal.namespace,
    )

    logger.info("Connected to Temporal server")

    # Create and run worker
    worker = create_worker(client, settings.temporal.task_queue)

    # Handle shutdown signals
    shutdown_event = asyncio.Event()

    def signal_handler() -> None:
        logger.info("Shutdown signal received")
        shutdown_event.set()

    # Signal handlers only work on Unix systems
    if sys.platform != "win32":
        try:
            loop = asyncio.get_running_loop()
            for sig in (signal.SIGINT, signal.SIGTERM):
                loop.add_signal_handler(sig, signal_handler)
        except NotImplementedError as e:
            # Fallback for platforms that don't support signal handlers
            logger.warning("Signal handlers not supported on this platform", error=str(e))
        except RuntimeError as e:
            # Fallback for runtime errors (e.g., event loop issues)
            logger.warning("Signal handlers not available", error=str(e))

    # Run worker until shutdown
    logger.info("Worker started, waiting for workflows...")

    try:
        # Start worker in background
        async with worker:
            # Use asyncio.wait_for with a timeout to allow signal handling
            try:
                await asyncio.wait_for(shutdown_event.wait(), timeout=None)
            except asyncio.CancelledError:
                logger.info("Worker cancelled")
                raise
    except KeyboardInterrupt:
        logger.info("Worker interrupted by user")
    except Exception as e:
        logger.error("Worker error", error=str(e), exc_info=True)
        raise

    logger.info("Worker stopped gracefully")


def main() -> None:
    """Main entry point for the worker."""
    setup_logging()

    try:
        asyncio.run(run_worker())
    except KeyboardInterrupt:
        logger.info("Worker interrupted")
        sys.exit(0)
    except Exception as e:
        logger.error("Worker failed to start", error=str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
