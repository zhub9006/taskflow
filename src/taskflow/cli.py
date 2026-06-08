"""TaskFlow CLI — command-line interface powered by Typer + Rich."""

from typing import Annotated, Optional

import typer
from rich import print
from rich.table import Table

from taskflow.core import TaskManager

app = typer.Typer(
    name="taskflow",
    help="✅ TaskFlow — organize, prioritize, and track your tasks with ease.",
    rich_markup_mode="rich",
)

manager = TaskManager()


@app.command()
def add(
    title: Annotated[str, typer.Argument(help="Title of the task")],
    priority: Annotated[str, typer.Option(help="Priority: low | medium | high")] = "medium",
    tag: Annotated[Optional[str], typer.Option(help="Tag for categorization")] = None,
    due: Annotated[Optional[str], typer.Option(help="Due date (YYYY-MM-DD)")] = None,
) -> None:
    """Add a new task."""
    task = manager.create_task(title=title, priority=priority, tag=tag, due=due)
    print(f"[green]✓[/green] Task #{task.id} created: {task.title}")


@app.command()
def list() -> None:
    """List all tasks."""
    tasks = manager.list_tasks()
    if not tasks:
        print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title="📋 TaskFlow — All Tasks")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="white")
    table.add_column("Priority", style="magenta")
    table.add_column("Tag", style="green")
    table.add_column("Due", style="yellow")
    table.add_column("Status", style="bold")

    for task in tasks:
        status_icon = "✅" if task.status == "done" else "⏳"
        table.add_row(
            str(task.id),
            task.title,
            task.priority,
            task.tag or "—",
            str(task.due) if task.due else "—",
            status_icon,
        )

    print(table)


@app.command()
def done(
    task_id: Annotated[int, typer.Argument(help="ID of the task to complete")],
) -> None:
    """Mark a task as done."""
    manager.complete_task(task_id)
    print(f"[green]✓[/green] Task #{task_id} completed!")


@app.command()
def show(
    task_id: Annotated[int, typer.Argument(help="ID of the task to show")],
) -> None:
    """Show details for a specific task."""
    task = manager.get_task(task_id)
    if task is None:
        print(f"[red]✗[/red] Task #{task_id} not found.")
        raise typer.Exit(code=1)
    print(task)


@app.command()
def delete(
    task_id: Annotated[int, typer.Argument(help="ID of the task to delete")],
) -> None:
    """Delete a task."""
    manager.delete_task(task_id)
    print(f"[red]✗[/red] Task #{task_id} deleted.")