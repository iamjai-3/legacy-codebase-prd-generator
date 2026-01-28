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
from rich.progress import Progress, SpinnerColumn, TaskID, TextColumn
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
    zip_path: str | None = typer.Option(None, "--zip-path", "-z", help="Path to code ZIP file (if not provided, loads from MinIO LEGACY_CODEBASE/)"),
    code_dir: str | None = typer.Option(None, "--code-dir", "-c", help="Path to code directory (if not provided, loads from MinIO LEGACY_CODEBASE/)"),
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
                        f"[dim]Note: If you want to delete the entire bucket, use 'prd-agent delete-bucket'[/dim]"
                    )
            else:
                error = result.get("error", "Unknown error")
                console.print(f"[yellow]⚠[/yellow] MinIO deletion warning: {error}")
        except Exception as e:
            console.print(f"[yellow]⚠[/yellow] Failed to delete MinIO data: {str(e)}")


@app.command()
def migrate_code(
    form_name: str = typer.Option(
        ..., "--form-name", "-f", help="Name of the form to migrate (e.g., le01, le07)"
    ),
    output_dir: str = typer.Option(
        "./output/migratedCode", "--output", "-o", help="Output directory for zip files"
    ),
):
    """
    Migrate codebase from knowledge base to .NET backend and React frontend.

    Generates complete .NET backend and React frontend applications based on
    the knowledge base context and packages them into separate zip files.
    After code migration, analyzes database table mappings and stores them
    in the knowledge base for enhanced context.

    Example:
        prd-agent migrate-code -f le07 -o ./output/migratedCode
    """
    from src.agents.base_agent import AgentContext
    from src.agents.code_migration_agent import CodeMigrationAgent
    from src.agents.database_analysis_agent import DatabaseAnalysisAgent

    console.print(
        Panel.fit(
            f"[bold blue]Code Migration Agent[/bold blue] - Migrating [green]{form_name}[/green]",
            border_style="blue",
        )
    )

    async def run_migration():
        context = AgentContext(form_name=form_name)
        migration_agent = CodeMigrationAgent()
        db_agent = DatabaseAnalysisAgent()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            # Step 1: Code Migration
            task1 = progress.add_task("Migrating codebase...", total=None)
            migration_result = await migration_agent.analyze(context, output_dir=output_dir)

            if not migration_result.success or not migration_result.data:
                progress.update(task1, description="Migration failed!")
                console.print(f"\n[red]✗ Migration failed:[/red] {migration_result.error}")
                return

            progress.update(task1, description="Code migration complete!")

            # Step 2: Database Analysis
            task2 = progress.add_task("Analyzing database mappings...", total=None)
            db_result = await db_agent.analyze(context, db_doc_path=None)

            if db_result.success and db_result.data:
                progress.update(task2, description="Database analysis complete!")
                console.print("\n[green]✓ Database analysis successful![/green]")
            else:
                progress.update(task2, description="Database analysis failed!")
                console.print(
                    f"\n[yellow]⚠ Database analysis failed:[/yellow] {db_result.error}"
                )

            # Display results
            console.print("\n[green]✓ Migration successful![/green]\n")

            table = Table(title="Migration Results")
            table.add_column("Item", style="cyan")
            table.add_column("Value", style="green")

            table.add_row("Form Name", migration_result.data.form_name)
            table.add_row("Backend Files", str(len(migration_result.data.backend_files)))
            table.add_row("Frontend Files", str(len(migration_result.data.frontend_files)))
            table.add_row("Backend Zip", migration_result.data.backend_zip_path)
            table.add_row("Frontend Zip", migration_result.data.frontend_zip_path)
            table.add_row("Execution Time", f"{migration_result.execution_time_ms:.2f}ms")

            if db_result.success and db_result.data:
                table.add_row("", "")  # Separator
                table.add_row("Database Tables Analyzed", str(db_result.data.tables_analyzed))
                table.add_row("Relationships Mapped", str(db_result.data.relationships_mapped))
                table.add_row("Vectors Stored", str(db_result.data.vectors_stored))

            console.print(table)

    asyncio.run(run_migration())


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
    from src.utils.minio_sync import MinioSync

    from src.config.settings import get_settings

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
def version():
    """Show version information."""
    from src import __version__

    console.print(f"[bold blue]PRD Agent[/bold blue] v{__version__}")
    console.print("AI-powered PRD Generation for Legacy Code Migration")


if __name__ == "__main__":
    app()
