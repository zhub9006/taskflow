"""TaskFlow core — business logic for task management."""

from datetime import date
from typing import Optional

from taskflow.models import Priority, Task, TaskStatus
from taskflow.storage import Storage


class TaskManager:
    """High-level manager for creating, querying, and updating tasks."""

    def __init__(self, storage: Optional[Storage] = None) -> None:
        self.storage = storage or Storage()

    def create_task(
        self,
        title: str,
        priority: str = "medium",
        tag: Optional[str] = None,
        due: Optional[str] = None,
    ) -> Task:
        """Create a new task and persist it."""
        next_id = self.storage.next_id()
        task = Task(
            id=next_id,
            title=title,
            priority=Priority(priority),
            tag=tag,
            due=date.fromisoformat(due) if due else None,
        )
        self.storage.save(task)
        return task

    def list_tasks(self) -> list[Task]:
        """Return all tasks from storage."""
        return self.storage.load_all()

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a single task by ID."""
        return self.storage.load(task_id)

    def complete_task(self, task_id: int) -> Optional[Task]:
        """Mark a task as done."""
        task = self.storage.load(task_id)
        if task is None:
            return None
        task.status = TaskStatus.DONE
        self.storage.save(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        return self.storage.delete(task_id)