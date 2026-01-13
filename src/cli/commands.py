"""
CLI commands for PRD Agent.

Usage:
    prd-agent generate --form-name le01 --zip-path ./code.zip
    prd-agent list-collections
    prd-agent search --form-name le01 --query "validation rules"
"""

import asyncio

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TaskID, TextColumn
from rich.table import Table
from temporalio.client import Client

from src.config.settings import get_settings
from src.utils.logging_config import get_logger, setup_logging
from src.vector_store.qdrant_manager import QdrantManager
from src.workflows.prd_generation_workflow import (
    PRDGenerationInput,
    PRDGenerationWorkflow,
)

app = typer.Typer(
    name="prd-agent",
    help="AI-powered PRD Generation Agent for Legacy Code Migration",
    add_completion=False,
)

console = Console()
logger = get_logger(__name__)


@app.callback()
def main_callback():
    """PRD Agent - Generate comprehensive PRDs from legacy code."""
    setup_logging()


@app.command()
def generate(
    form_name: str = typer.Option(
        ..., "--form-name", "-f", help="Name of the form to analyze (e.g., le01, ea01)"
    ),
    zip_path: str | None = typer.Option(None, "--zip-path", "-z", help="Path to the code ZIP file"),
    code_dir: str | None = typer.Option(
        None, "--code-dir", "-c", help="Path to the code directory"
    ),
    file_mappings: str | None = typer.Option(
        None, "--mappings", "-m", help="Comma-separated file paths to include"
    ),
    dependency_file: str | None = typer.Option(
        None, "--dependency-file", "-d", help="Path to dependency file with file paths to include"
    ),
    minio_bucket: str | None = typer.Option(
        None, "--bucket", "-b", help="Minio bucket for screenshots"
    ),
    jira_project: str | None = typer.Option(None, "--jira-project", "-j", help="Jira project key"),
    output_dir: str = typer.Option("./output", "--output", "-o", help="Output directory for PRD"),
    skip_screenshots: bool = typer.Option(
        False, "--skip-screenshots", help="Skip screenshot analysis"
    ),
    skip_jira: bool = typer.Option(False, "--skip-jira", help="Skip Jira integration"),
    recreate_vectors: bool = typer.Option(
        False, "--recreate-vectors", help="Recreate vector collection"
    ),
    use_workflow: bool = typer.Option(
        True, "--use-workflow/--direct", help="Use Temporal workflow or direct execution"
    ),
):
    """
    Generate a PRD for a legacy form/module.

    Example:
        prd-agent generate -f le01 -z ./code.zip -o ./output
    """
    console.print(
        Panel.fit(
            f"[bold blue]PRD Agent[/bold blue] - Generating PRD for [green]{form_name}[/green]",
            border_style="blue",
        )
    )

    if not zip_path and not code_dir:
        console.print(
            "[yellow]Warning:[/yellow] No code source provided. Will use vector store context only."
        )

    mappings_list = file_mappings.split(",") if file_mappings else None

    if use_workflow:
        asyncio.run(
            _run_workflow_generation(
                form_name=form_name,
                zip_path=zip_path,
                code_dir=code_dir,
                file_mappings=mappings_list,
                dependency_file=dependency_file,
                minio_bucket=minio_bucket,
                jira_project=jira_project,
                output_dir=output_dir,
                skip_screenshots=skip_screenshots,
                skip_jira=skip_jira,
                recreate_vectors=recreate_vectors,
            )
        )
    else:
        asyncio.run(
            _run_direct_generation(
                form_name=form_name,
                zip_path=zip_path,
                code_dir=code_dir,
                file_mappings=mappings_list,
                dependency_file=dependency_file,
                minio_bucket=minio_bucket,
                jira_project=jira_project,
                output_dir=output_dir,
                skip_screenshots=skip_screenshots,
                skip_jira=skip_jira,
                recreate_vectors=recreate_vectors,
            )
        )


async def _run_workflow_generation(
    form_name: str,
    zip_path: str | None,
    code_dir: str | None,
    file_mappings: list[str] | None,
    dependency_file: str | None,
    minio_bucket: str | None,
    jira_project: str | None,
    output_dir: str,
    skip_screenshots: bool,
    skip_jira: bool,
    recreate_vectors: bool,
):
    """Run PRD generation via Temporal workflow."""
    settings = get_settings()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Connecting to Temporal...", total=None)

        try:
            # Connect to Temporal
            client = await Client.connect(settings.temporal.address)

            progress.update(task, description="Starting workflow...")

            # Create workflow input
            workflow_input = PRDGenerationInput(
                form_name=form_name,
                zip_path=zip_path,
                code_directory=code_dir,
                file_mappings=file_mappings,
                dependency_file=dependency_file,
                minio_bucket=minio_bucket,
                jira_project_key=jira_project,
                output_dir=output_dir,
                skip_screenshots=skip_screenshots,
                skip_jira=skip_jira,
                recreate_vector_collection=recreate_vectors,
            )

            # Execute workflow
            result = await client.execute_workflow(
                PRDGenerationWorkflow.run,
                workflow_input,
                id=f"prd-generation-{form_name}-{int(asyncio.get_event_loop().time())}",
                task_queue=settings.temporal.task_queue,
            )

            progress.update(task, description="Workflow complete!")

            if result.success:
                console.print("\n[green]✓[/green] PRD generated successfully!")
                console.print(f"  [blue]File:[/blue] {result.prd_file_path}")
                console.print(f"  [blue]Word count:[/blue] {result.word_count}")
                console.print(f"  [blue]Sections:[/blue] {result.section_count}")
                console.print(f"  [blue]Vector collection:[/blue] {result.vector_collection}")
            else:
                console.print(f"\n[red]✗[/red] PRD generation failed: {result.error}")

        except Exception as e:
            console.print(f"\n[red]Error:[/red] {str(e)}")
            console.print("[yellow]Tip:[/yellow] Make sure Temporal server is running.")
            raise typer.Exit(1)


def _get_successful_data(result):
    """Extract data from result if successful, otherwise return None."""
    if result is None:
        return None
    return result.data if result.success else None


def _extract_code_files(
    zip_path: str | None,
    code_dir: str | None,
    file_mappings: list[str] | None,
    dependency_file: str | None = None,
):
    """Extract code files from zip or directory."""
    from src.extractors.code_extractor import CodeExtractor

    if zip_path:
        return CodeExtractor().extract_from_zip(
            zip_path, file_mappings=file_mappings, dependency_file=dependency_file
        )
    if code_dir:
        return CodeExtractor().extract_from_directory(
            code_dir, file_mappings=file_mappings, dependency_file=dependency_file
        )
    return []


async def _analyze_screenshots(context, form_name: str, minio_bucket: str | None):
    """Analyze screenshots from Minio."""
    from src.agents.screenshot_analysis_agent import ScreenshotAnalysisAgent
    from src.extractors.minio_extractor import MinioExtractor

    screenshots = MinioExtractor().get_form_screenshots(form_name, bucket=minio_bucket)
    if not screenshots:
        return None
    return await ScreenshotAnalysisAgent().analyze(context, screenshots=screenshots)


async def _analyze_jira(context, form_name: str, jira_project: str | None):
    """Analyze Jira issues with error handling."""
    from src.agents.atlassian_integration_agent import AtlassianIntegrationAgent
    from src.extractors.jira_extractor import JiraExtractor

    try:
        issues = JiraExtractor().get_form_issues(form_name, project_key=jira_project)
        if not issues:
            return None
        return await AtlassianIntegrationAgent().analyze(context, issues=issues)
    except Exception as e:
        console.print(f"  [yellow]Jira skipped:[/yellow] {str(e)}")
        return None


def _setup_vector_store(form_name: str, code_files: list, recreate_vectors: bool):
    """Phase 1: Setup vector store and add code documents."""
    from src.extractors.code_extractor import CodeExtractor

    qdrant = QdrantManager()
    qdrant.create_collection(form_name, recreate=recreate_vectors)

    if code_files:
        documents = CodeExtractor().to_documents(code_files, form_name)
        qdrant.add_documents(form_name, documents)

    return qdrant


async def _run_analysis_agents(
    context,
    form_name: str,
    code_files: list,
    minio_bucket: str | None,
    jira_project: str | None,
    skip_screenshots: bool,
    skip_jira: bool,
    progress: Progress,
    task: TaskID,
):
    """Phase 2: Run all analysis agents."""
    from src.agents.requirements_generator_agent import RequirementsGeneratorAgent
    from src.agents.risk_analysis_agent import RiskAnalysisAgent
    from src.agents.user_flow_agent import UserFlowAgent

    screenshot_result = None
    if not skip_screenshots:
        progress.update(task, description="Analyzing screenshots...")
        screenshot_result = await _analyze_screenshots(context, form_name, minio_bucket)

    jira_result = None
    if not skip_jira:
        progress.update(task, description="Analyzing Jira issues...")
        jira_result = await _analyze_jira(context, form_name, jira_project)

    progress.update(task, description="Generating requirements...")
    req_result = await RequirementsGeneratorAgent().analyze(context, code_files=code_files)

    progress.update(task, description="Analyzing user flows...")
    flow_result = await UserFlowAgent().analyze(context)

    progress.update(task, description="Analyzing risks...")
    risk_result = await RiskAnalysisAgent().analyze(context)

    return screenshot_result, jira_result, req_result, flow_result, risk_result


async def _aggregate_and_save_prd(
    context,
    screenshot_result,
    jira_result,
    req_result,
    flow_result,
    risk_result,
    form_name: str,
    output_dir: str,
    progress: Progress,
    task: TaskID,
):
    """Phase 3: Aggregate PRD and save to file."""
    from src.agents.prd_aggregator_agent import PRDAggregatorAgent
    from src.utils.file_utils import ensure_directory

    progress.update(task, description="Generating PRD document...")
    prd_result = await PRDAggregatorAgent().analyze(
        context,
        screenshot_analysis=_get_successful_data(screenshot_result),
        atlassian_analysis=_get_successful_data(jira_result),
        requirements_analysis=_get_successful_data(req_result),
        user_flow_analysis=_get_successful_data(flow_result),
        risk_analysis=_get_successful_data(risk_result),
    )

    if not (prd_result.success and prd_result.data):
        console.print(f"\n[red]✗[/red] PRD generation failed: {prd_result.error}")
        return None

    output_path = ensure_directory(output_dir)
    prd_file = output_path / f"{form_name}_PRD.md"
    prd_file.write_text(prd_result.data.markdown_content, encoding="utf-8")

    console.print("\n[green]✓[/green] PRD generated successfully!")
    console.print(f"  [blue]File:[/blue] {prd_file}")
    console.print(f"  [blue]Word count:[/blue] {prd_result.data.word_count}")
    return prd_file


async def _run_direct_generation(
    form_name: str,
    zip_path: str | None,
    code_dir: str | None,
    file_mappings: list[str] | None,
    dependency_file: str | None,
    minio_bucket: str | None,
    jira_project: str | None,
    output_dir: str,
    skip_screenshots: bool,
    skip_jira: bool,
    recreate_vectors: bool,
):
    """Run PRD generation directly without Temporal."""
    from src.agents.base_agent import AgentContext

    context = AgentContext(form_name=form_name)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Extracting code...", total=None)

        code_files = _extract_code_files(zip_path, code_dir, file_mappings, dependency_file)
        console.print(f"  Extracted {len(code_files)} code files")

        progress.update(task, description="Creating vector collection...")
        _setup_vector_store(form_name, code_files, recreate_vectors)

        results = await _run_analysis_agents(
            context,
            form_name,
            code_files,
            minio_bucket,
            jira_project,
            skip_screenshots,
            skip_jira,
            progress,
            task,
        )
        screenshot_result, jira_result, req_result, flow_result, risk_result = results

        await _aggregate_and_save_prd(
            context,
            screenshot_result,
            jira_result,
            req_result,
            flow_result,
            risk_result,
            form_name,
            output_dir,
            progress,
            task,
        )


@app.command()
def list_collections():
    """List all PRD vector collections in Qdrant."""
    qdrant = QdrantManager()
    collections = qdrant.list_collections()

    if not collections:
        console.print("[yellow]No collections found.[/yellow]")
        return

    table = Table(title="PRD Vector Collections")
    table.add_column("Collection Name", style="cyan")
    table.add_column("Status", style="green")

    for collection in collections:
        stats = qdrant.get_collection_stats(
            collection.replace(f"{qdrant.settings.qdrant.collection_prefix}_", "")
        )
        status = stats.get("status", "unknown") if stats.get("exists", True) else "not found"
        table.add_row(collection, status)

    console.print(table)


@app.command()
def search(
    form_name: str = typer.Option(..., "--form-name", "-f", help="Form name to search in"),
    query: str = typer.Option(..., "--query", "-q", help="Search query"),
    limit: int = typer.Option(5, "--limit", "-l", help="Maximum results"),
    doc_type: str | None = typer.Option(
        None, "--type", "-t", help="Filter by doc type (code, screenshot, jira)"
    ),
):
    """
    Search the vector knowledge base.

    Example:
        prd-agent search -f le01 -q "validation rules" -l 10
    """
    qdrant = QdrantManager()

    filter_metadata = {"doc_type": doc_type} if doc_type else None

    with console.status("Searching..."):
        results = qdrant.search(
            form_name=form_name,
            query=query,
            limit=limit,
            filter_metadata=filter_metadata,
        )

    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return

    console.print(f"\n[green]Found {len(results)} results:[/green]\n")

    for i, result in enumerate(results, 1):
        console.print(
            Panel(
                f"[dim]Score:[/dim] {result.score:.4f}\n"
                f"[dim]Type:[/dim] {result.metadata.get('doc_type', 'unknown')}\n\n"
                f"{result.content[:500]}...",
                title=f"[bold]Result {i}[/bold]",
                border_style="dim",
            )
        )


@app.command()
def stats(
    form_name: str = typer.Option(..., "--form-name", "-f", help="Form name to get stats for"),
):
    """Get statistics for a form's vector collection."""
    qdrant = QdrantManager()
    stats = qdrant.get_collection_stats(form_name)

    if not stats.get("exists", True):
        console.print(f"[yellow]Collection for '{form_name}' not found.[/yellow]")
        return

    table = Table(title=f"Collection Stats: {stats.get('name')}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Vectors Count", str(stats.get("vectors_count", 0)))
    table.add_row("Points Count", str(stats.get("points_count", 0)))
    table.add_row("Status", stats.get("status", "unknown"))

    console.print(table)


@app.command()
def delete_collection(
    form_name: str = typer.Option(..., "--form-name", "-f", help="Form name to delete"),
    confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation"),
):
    """Delete a vector collection."""
    if not confirm:
        confirm = typer.confirm(
            f"Are you sure you want to delete the collection for '{form_name}'?"
        )
        if not confirm:
            console.print("[yellow]Cancelled.[/yellow]")
            return

    qdrant = QdrantManager()
    success = qdrant.delete_collection(form_name)

    if success:
        console.print(f"[green]✓[/green] Collection for '{form_name}' deleted.")
    else:
        console.print("[red]✗[/red] Failed to delete collection.")


@app.command()
def version():
    """Show version information."""
    from src import __version__

    console.print(f"[bold blue]PRD Agent[/bold blue] v{__version__}")
    console.print("AI-powered PRD Generation for Legacy Code Migration")


if __name__ == "__main__":
    app()
