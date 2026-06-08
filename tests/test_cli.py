"""Tests for TaskFlow CLI commands."""

from typer.testing import CliRunner

from taskflow.cli import app
from taskflow.core import TaskManager
from taskflow.storage import Storage

runner = CliRunner()


def test_cli_add_command(tmp_path) -> None:
    """Test the 'add' CLI command."""
    storage = Storage(path=tmp_path / "tasks.json")
    # Temporarily override the global manager for testing
    import taskflow.cli as cli_module
    original_manager = cli_module.manager
    cli_module.manager = TaskManager(storage=storage)

    result = runner.invoke(app, ["add", "My first task"])
    assert result.exit_code == 0
    assert "Task #1 created" in result.output

    cli_module.manager = original_manager


def test_cli_list_command(tmp_path) -> None:
    """Test the 'list' CLI command."""
    storage = Storage(path=tmp_path / "tasks.json")
    manager = TaskManager(storage=storage)
    manager.create_task(title="List me")

    import taskflow.cli as cli_module
    original_manager = cli_module.manager
    cli_module.manager = manager

    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "List me" in result.output

    cli_module.manager = original_manager