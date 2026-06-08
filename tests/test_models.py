"""Tests for TaskFlow data models."""

from datetime import date

from taskflow.models import Priority, Task, TaskStatus


def test_task_creation() -> None:
    """Test basic Task model creation."""
    task = Task(id=1, title="Test task")
    assert task.id == 1
    assert task.title == "Test task"
    assert task.priority == Priority.MEDIUM
    assert task.status == TaskStatus.TODO


def test_task_with_all_fields() -> None:
    """Test Task with all optional fields populated."""
    task = Task(
        id=2,
        title="Full task",
        priority="high",
        tag="work",
        due=date(2024, 12, 31),
        status="done",
    )
    assert task.priority == Priority.HIGH
    assert task.tag == "work"
    assert task.due == date(2024, 12, 31)
    assert task.status == TaskStatus.DONE


def test_priority_normalization() -> None:
    """Test that priority values are normalized to lowercase."""
    task = Task(id=3, title="Mixed case", priority="HIGH")
    assert task.priority == Priority.HIGH


def test_task_title_min_length() -> None:
    """Test that empty titles are rejected."""
    from pydantic import ValidationError

    try:
        Task(id=4, title="")
        assert False, "Should have raised ValidationError"
    except ValidationError:
        pass  # Expected


def test_model_dump_safe() -> None:
    """Test safe serialization for JSON storage."""
    task = Task(id=5, title="Serialize me", due=date(2024, 6, 1))
    data = task.model_dump_safe()
    assert data["due"] == "2024-06-01"