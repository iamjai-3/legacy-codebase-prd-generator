"""
Logging configuration using structlog for structured logging.

Provides:
- Structured logging with context
- Trace context for request tracking
- Execution timing utilities
"""

import logging
import sys
import time
from collections.abc import Generator
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any
from uuid import uuid4

import structlog
from structlog.typing import Processor

from src.config.settings import get_settings

# Context variable for trace ID across async operations
_trace_id: ContextVar[str] = ContextVar("trace_id", default="")


def setup_logging() -> None:
    """Configure structured logging for the application."""
    settings = get_settings()

    # Configure standard logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.log_level.upper()),
    )

    # Define processors for structlog
    shared_processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        _add_trace_id,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt="iso"),
    ]

    if settings.debug:
        # Development: colored console output
        processors: list[Processor] = [
            *shared_processors,
            structlog.dev.ConsoleRenderer(colors=True),
        ]
    else:
        # Production: JSON output
        processors = [
            *shared_processors,
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, settings.log_level.upper())
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )


def _add_trace_id(
    logger: logging.Logger, method_name: str, event_dict: dict[str, Any]
) -> dict[str, Any]:
    """Add trace_id to log events if available."""
    trace_id = _trace_id.get()
    if trace_id:
        event_dict["trace_id"] = trace_id
    return event_dict


def get_logger(name: str | None = None, **initial_context: Any) -> structlog.BoundLogger:
    """
    Get a configured logger instance.

    Args:
        name: Logger name (usually __name__)
        **initial_context: Initial context to bind to the logger

    Returns:
        Configured structlog BoundLogger
    """
    logger = structlog.get_logger(name)
    if initial_context:
        logger = logger.bind(**initial_context)
    return logger


def set_trace_id(trace_id: str | None = None) -> str:
    """
    Set a trace ID for the current context.

    Args:
        trace_id: Optional trace ID (generated if not provided)

    Returns:
        The trace ID that was set
    """
    if trace_id is None:
        trace_id = str(uuid4())[:8]
    _trace_id.set(trace_id)
    return trace_id


def get_trace_id() -> str:
    """Get the current trace ID."""
    return _trace_id.get()


@contextmanager
def trace_context(operation: str, **context: Any) -> Generator[dict[str, Any], None, None]:
    """
    Context manager for tracing operations with timing.

    Usage:
        with trace_context("analyze_screenshots", form_name="le01") as ctx:
            # Do work...
            ctx["screenshots_count"] = 10
        # Automatically logs duration on exit

    Args:
        operation: Name of the operation being traced
        **context: Additional context to log

    Yields:
        A mutable dict for adding context during execution
    """
    logger = get_logger(__name__)
    trace_id = set_trace_id()
    result_context: dict[str, Any] = {"success": True}
    start_time = time.perf_counter()

    logger.info(f"Starting {operation}", operation=operation, trace_id=trace_id, **context)

    try:
        yield result_context
    except Exception as e:
        result_context["success"] = False
        result_context["error"] = str(e)
        raise
    finally:
        duration_ms = (time.perf_counter() - start_time) * 1000
        result_context["duration_ms"] = round(duration_ms, 2)

        log_method = logger.info if result_context.get("success") else logger.error
        log_method(
            f"Completed {operation}",
            operation=operation,
            trace_id=trace_id,
            **context,
            **result_context,
        )


class ExecutionTimer:
    """
    Simple timer for measuring execution duration.

    Usage:
        timer = ExecutionTimer()
        # Do work...
        duration_ms = timer.elapsed_ms()
    """

    def __init__(self) -> None:
        """Start the timer."""
        self._start = time.perf_counter()

    def elapsed_ms(self) -> float:
        """Get elapsed time in milliseconds."""
        return (time.perf_counter() - self._start) * 1000

    def elapsed_seconds(self) -> float:
        """Get elapsed time in seconds."""
        return time.perf_counter() - self._start
