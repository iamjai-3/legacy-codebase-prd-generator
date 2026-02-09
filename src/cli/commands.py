"""
CLI commands for PRD Agent.

Usage:
    prd-agent generate --form-name le01 --zip-path ./code.zip
    prd-agent list-collections
    prd-agent search --form-name le01 --query "validation rules"
"""

import asyncio
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from temporalio.client import Client

from src.config.settings import get_settings

settings = get_settings()
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
    zip_path: str | None = typer.Option(
        None,
        "--zip-path",
        "-z",
        help="Path to code ZIP file (if not provided, loads from MinIO LEGACY_CODEBASE/)",
    ),
    code_dir: str | None = typer.Option(
        None,
        "--code-dir",
        "-c",
        help="Path to code directory (if not provided, loads from MinIO LEGACY_CODEBASE/)",
    ),
    output_dir: str = typer.Option("./output", "--output", "-o", help="Output directory"),
    minio_bucket: str | None = typer.Option(None, "--bucket", "-b", help="MinIO bucket name"),
):
    """
    Generate a PRD for a legacy form/module.

    Dependencies are automatically loaded from MinIO:
    FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/{FORM_NAME}_dependencies.txt

    Legacy codebase is automatically loaded from MinIO if -z/-c not provided:
    LEGACY_CODEBASE/*.zip

    Example:
        # Using local ZIP file
        prd-agent generate -f le11 -z ./code.zip -o ./output

        # Using MinIO (no -z or -c needed)
        prd-agent generate -f le11 -o ./output
    """
    console.print(
        Panel.fit(
            f"[bold blue]PRD Agent[/bold blue] - Generating PRD for [green]{form_name}[/green]",
            border_style="blue",
        )
    )

    asyncio.run(
        _run_workflow_generation(
            form_name=form_name,
            zip_path=zip_path,
            code_dir=code_dir,
            minio_bucket=minio_bucket,
            output_dir=output_dir,
        )
    )


async def _run_workflow_generation(
    form_name: str,
    zip_path: str | None,
    code_dir: str | None,
    minio_bucket: str | None,
    output_dir: str,
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
                minio_bucket=minio_bucket,
                output_dir=output_dir,
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
    delete_minio: bool = typer.Option(
        True, "--delete-minio/--no-delete-minio", help="Also delete MinIO form data"
    ),
    bucket: str = typer.Option(
        None, "--bucket", "-b", help="MinIO bucket name (defaults to configured bucket)"
    ),
):
    """
    Delete a vector collection and optionally MinIO form data.

    Deletes:
    - Qdrant vector collection for the form
    - MinIO form data (FORMS/{FORM_NAME}/*) if --delete-minio is set
    """
    if not confirm:
        confirm_msg = f"Are you sure you want to delete the collection for '{form_name}'?"
        if delete_minio:
            confirm_msg += "\nThis will also delete all MinIO data for this form."
        confirm = typer.confirm(confirm_msg)
        if not confirm:
            console.print("[yellow]Cancelled.[/yellow]")
            return

    qdrant = QdrantManager()
    success = qdrant.delete_collection(form_name)

    if success:
        console.print(f"[green]✓[/green] Collection for '{form_name}' deleted.")
    else:
        console.print("[red]✗[/red] Failed to delete collection.")

    # Delete MinIO form data if requested
    if delete_minio:
        from src.utils.minio_sync import MinioSync

        try:
            sync = MinioSync(bucket=bucket)
            result = sync.delete_form_data(form_name, bucket=bucket)

            if result.get("success"):
                deleted_count = result.get("deleted_count", 0)
                if deleted_count > 0:
                    console.print(
                        f"[green]✓[/green] MinIO data for '{form_name}' deleted ({deleted_count} objects)."
                    )
                else:
                    console.print(
                        f"[yellow]⚠[/yellow] No MinIO data found for form '{form_name}' in FORMS/{form_name.upper()}/"
                    )
                    console.print(
                        "[dim]Note: If you want to delete the entire bucket, use 'prd-agent delete-bucket'[/dim]"
                    )
            else:
                error = result.get("error", "Unknown error")
                console.print(f"[yellow]⚠[/yellow] MinIO deletion warning: {error}")
        except Exception as e:
            console.print(f"[yellow]⚠[/yellow] Failed to delete MinIO data: {str(e)}")


@app.command()
def create_minio_folders(
    bucket: str = typer.Option(
        None, "--bucket", "-b", help="MinIO bucket name (defaults to configured bucket)"
    ),
):
    """
    Create empty folder structure in MinIO bucket.

    Creates:
    - FORMS/ (parent folder for all forms)
    - DB_PRD/
    - EXPORT_CODEBASE_PRD/
    - LEGACY_CODEBASE/

    Files can then be uploaded via MinIO UI.

    Example:
        prd-agent create-minio-folders
    """
    from src.utils.minio_sync import MinioSync

    console.print(
        Panel.fit(
            "[bold blue]MinIO Folder Creation[/bold blue] - Creating folder structure in MinIO",
            border_style="blue",
        )
    )

    try:
        sync = MinioSync(bucket=bucket)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Creating folders in MinIO...", total=None)

            results = sync.create_folder_structure(bucket=bucket)

            progress.update(task, description="Folder creation complete!")

            table = Table(title="Folder Creation Results")
            table.add_column("Folder", style="cyan")
            table.add_column("Status", style="green")

            for folder, created in results.items():
                status = "[green]✓ Created[/green]" if created else "[red]✗ Failed[/red]"
                table.add_row(folder, status)

            console.print("\n[green]✓ Folder structure created![/green]\n")
            console.print(table)
            console.print("\n[yellow]Note:[/yellow] You can now upload files via MinIO UI")

    except Exception as e:
        console.print(f"\n[red]✗ Folder creation failed:[/red] {str(e)}")
        raise typer.Exit(1)


@app.command()
def create_form_folders(
    form_name: str = typer.Argument(..., help="Form name (e.g., LE11, le07)"),
    bucket: str = typer.Option(
        None, "--bucket", "-b", help="MinIO bucket name (defaults to configured bucket)"
    ),
):
    """
    Create folder structure for a specific form in MinIO.

    Creates:
    - FORMS/{FORM_NAME}/FORM_DOCS/
    - FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/
    - FORMS/{FORM_NAME}/UI_SCREENSHOTS/

    Files can then be uploaded via MinIO UI.

    Example:
        prd-agent create-form-folders LE11
    """
    from src.utils.minio_sync import MinioSync

    console.print(
        Panel.fit(
            f"[bold blue]Form Folder Creation[/bold blue] - Creating folders for {form_name.upper()}",
            border_style="blue",
        )
    )

    try:
        sync = MinioSync(bucket=bucket)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task(f"Creating folders for {form_name.upper()}...", total=None)

            results = sync.create_form_folders(form_name, bucket=bucket)

            progress.update(task, description="Folder creation complete!")

            table = Table(title=f"Folder Creation Results for {form_name.upper()}")
            table.add_column("Folder", style="cyan")
            table.add_column("Status", style="green")

            for folder, created in results.items():
                status = "[green]✓ Created[/green]" if created else "[red]✗ Failed[/red]"
                table.add_row(folder, status)

            console.print(f"\n[green]✓ Folders created for {form_name.upper()}![/green]\n")
            console.print(table)
            console.print("\n[yellow]Note:[/yellow] You can now upload files via MinIO UI")

    except Exception as e:
        console.print(f"\n[red]✗ Folder creation failed:[/red] {str(e)}")
        raise typer.Exit(1)


@app.command()
def delete_bucket(
    bucket: str = typer.Option(
        None, "--bucket", "-b", help="MinIO bucket name (defaults to configured bucket)"
    ),
    confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation"),
    force: bool = typer.Option(
        True, "--force/--no-force", help="Delete all objects in bucket before deleting bucket"
    ),
):
    """
    Delete an entire MinIO bucket.

    WARNING: This will delete ALL data in the bucket, including data for all forms!

    Example:
        prd-agent delete-bucket --bucket metadatas --yes
    """
    from src.config.settings import get_settings
    from src.utils.minio_sync import MinioSync

    bucket_name = bucket or get_settings().minio.bucket

    if not confirm:
        confirm_msg = (
            f"[red]WARNING:[/red] This will delete the entire bucket '{bucket_name}' "
            f"and ALL its contents (data for all forms)!\n"
            f"Are you sure you want to continue?"
        )
        if not typer.confirm(confirm_msg):
            console.print("[yellow]Cancelled.[/yellow]")
            return

    try:
        sync = MinioSync(bucket=bucket)
        result = sync.delete_bucket(bucket=bucket, force=force)

        if result.get("success"):
            console.print(f"[green]✓[/green] Bucket '{bucket_name}' deleted successfully.")
        else:
            error = result.get("error", "Unknown error")
            console.print(f"[red]✗[/red] Failed to delete bucket: {error}")
            raise typer.Exit(1)

    except Exception as e:
        console.print(f"[red]✗[/red] Failed to delete bucket: {str(e)}")
        raise typer.Exit(1)


@app.command()
def migrate_agentic(
    form_name: str = typer.Option(
        ..., "--form-name", "-f", help="Name of the form to migrate (e.g., le11, ea01)"
    ),
    output_dir: str = typer.Option(
        "./output/agentic", "--output", "-o", help="Output directory for generated code"
    ),
    prompt: str | None = typer.Option(None, "--prompt", "-p", help="Custom migration prompt"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
):
    """
    Migrate legacy codebase using the agentic AI system.

    This command uses an AI agent that works like Antigravity IDE to:
    1. Read form documentation and dependencies from MinIO
    2. Search the vector knowledge base for business logic
    3. Generate complete .NET backend and React frontend code

    The agent uses the configured LLM provider (OpenAI or Anthropic) for reasoning.

    Example:
        prd-agent migrate-agentic -f le11 -o ./output/agentic
        prd-agent migrate-agentic -f le11 --verbose
    """
    from src.config.settings import LLMProvider
    from src.core.agentic import AgenticConfig
    from src.core.migration import get_migration_orchestrator

    console.print(
        Panel.fit(
            f"[bold blue]Agentic Migration[/bold blue] - Migrating [green]{form_name}[/green]",
            border_style="blue",
        )
    )

    provider = settings.llm.provider
    if provider == LLMProvider.ANTHROPIC:
        provider_label = f"Anthropic Claude ({settings.anthropic.model})"
    else:
        provider_label = f"OpenAI ({settings.openai.model})"

    console.print(f"\n[dim]Using {provider_label} for reasoning[/dim]")
    console.print(f"[dim]Output directory: {output_dir}[/dim]\n")

    async def run_agentic_migration():
        MigrationOrchestrator = get_migration_orchestrator()

        # Configure the agent
        config = AgenticConfig(
            working_directory=Path(output_dir),
            verbose=verbose,
            max_iterations=50,
            required_tools=["write_file"],
        )

        # Create the orchestrator
        orchestrator = MigrationOrchestrator(
            form_name=form_name,
            output_dir=Path(output_dir),
            config=config,
        )

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Running agentic migration...", total=None)

            try:
                result = await orchestrator.migrate(prompt)
                progress.update(task, description="Migration complete!")

            except Exception as e:
                progress.update(task, description="Migration failed!")
                console.print(f"\n[red]✗ Migration error:[/red] {str(e)}")
                raise typer.Exit(1)

        # Display result
        console.print("\n[green]✓ Agentic migration complete![/green]\n")
        console.print(
            Panel(
                result[:2000] + "..." if len(result) > 2000 else result,
                title="Agent Response",
                border_style="green",
            )
        )

        # Show generated files
        output_path = Path(output_dir)
        if output_path.exists():
            table = Table(title="Generated Files")
            table.add_column("Directory", style="cyan")
            table.add_column("Files", style="green")

            for subdir in ["backend", "frontend"]:
                subdir_path = output_path / subdir
                if subdir_path.exists():
                    files = list(subdir_path.rglob("*"))
                    file_count = len([f for f in files if f.is_file()])
                    table.add_row(subdir, str(file_count))

            console.print(table)

    asyncio.run(run_agentic_migration())


@app.command()
def cache_stats():
    """Show cache statistics."""
    import asyncio

    from src.utils.cache_manager import get_cache_manager

    async def get_stats():
        cache = await get_cache_manager()
        stats = await cache.get_stats()

        if not stats.get("enabled"):
            console.print("[yellow]Cache is disabled[/yellow]")
            return

        table = Table(title="Cache Statistics")
        table.add_column("Cache Type", style="cyan")
        table.add_column("Total Entries", style="green")
        table.add_column("Active Entries", style="blue")
        table.add_column("Total Hits", style="yellow")
        table.add_column("Avg Hits", style="magenta")

        for stat in stats.get("by_type", []):
            table.add_row(
                stat["cache_type"],
                str(stat["total_entries"]),
                str(stat["active_entries"]),
                str(stat["total_hits"]),
                f"{stat['avg_hits']:.2f}",
            )

        console.print(table)

    asyncio.run(get_stats())


@app.command()
def cache_clear(
    cache_type: str = typer.Option(
        None, "--type", "-t", help="Cache type to clear (llm_response, vector_search, tool_result)"
    ),
    confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation"),
):
    """Clear cache entries."""
    import asyncio

    from src.utils.cache_manager import CacheType, get_cache_manager

    if not confirm:
        type_msg = f" for type '{cache_type}'" if cache_type else ""
        if not typer.confirm(f"Are you sure you want to clear cache{type_msg}?"):
            console.print("[yellow]Cancelled[/yellow]")
            return

    async def clear_cache():
        cache = await get_cache_manager()

        if cache_type:
            try:
                ct = CacheType(cache_type)
                await cache.clear(ct)
                console.print(f"[green]✓[/green] Cleared {cache_type} cache")
            except ValueError:
                console.print(f"[red]Invalid cache type:[/red] {cache_type}")
                console.print("Valid types: llm_response, vector_search, tool_result")
        else:
            await cache.clear()
            console.print("[green]✓[/green] All cache cleared")

    asyncio.run(clear_cache())


@app.command()
def version():
    """Show version information."""
    from src import __version__

    console.print(f"[bold blue]PRD Agent[/bold blue] v{__version__}")
    console.print("AI-powered PRD Generation for Legacy Code Migration")


if __name__ == "__main__":
    app()
