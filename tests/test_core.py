"""Tests for TaskFlow core business logic."""

from taskflow.core import TaskManager
from taskflow.models import TaskStatus


def test_create_task(task_manager: TaskManager) -> None:
    """Test that a task can be created and persisted."""
    task = task_manager.create_task(title="Buy groceries")
    assert task.id == 1
    assert task.title == "Buy groceries"
    assert task.status == TaskStatus.TODO


def test_create_task_with_priority(task_manager: TaskManager) -> None:
    """Test creating a task with a specific priority."""
    task = task_manager.create_task(title="Important meeting", priority="high")
    assert task.priority.value == "high"


def test_list_tasks(task_manager: TaskManager) -> None:
    """Test listing all tasks."""
    task_manager.create_task(title="Task A")
    task_manager.create_task(title="Task B")
    tasks = task_manager.list_tasks()
    assert len(tasks) == 2


def test_complete_task(task_manager: TaskManager) -> None:
    """Test marking a task as done."""
    task = task_manager.create_task(title="Write tests")
    completed = task_manager.complete_task(task.id)
    assert completed is not None
    assert completed.status == TaskStatus.DONE


def test_delete_task(task_manager: TaskManager) -> None:
    """Test deleting a task."""
    task = task_manager.create_task(title="Remove me")
    result = task_manager.delete_task(task.id)
    assert result is True
    assert task_manager.list_tasks() == []


def test_delete_nonexistent_task(task_manager: TaskManager) -> None:
    """Test deleting a task that doesn't exist."""
    result = task_manager.delete_task(999)
    assert result is False


def test_get_task_by_id(task_manager: TaskManager) -> None:
    """Test retrieving a single task by ID."""
    task = task_manager.create_task(title="Find me")
    found = task_manager.get_task(task.id)
    assert found is not None
    assert found.title == "Find me"


def test_get_nonexistent_task(task_manager: TaskManager) -> None:
    """Test retrieving a task that doesn't exist."""
    found = task_manager.get_task(999)
    assert found is None