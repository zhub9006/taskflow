"""TaskFlow storage — persistence layer (JSON backend)."""

import json
from pathlib import Path
from typing import Optional

from taskflow.models import Task

DEFAULT_STORAGE_PATH = Path.home() / ".taskflow" / "tasks.json"


class Storage:
    """JSON-file-based task storage."""

    def __init__(self, path: Optional[Path] = None) -> None:
        self.path = path or DEFAULT_STORAGE_PATH
        self._ensure_storage_file()

    def _ensure_storage_file(self) -> None:
        """Create the storage file and directory if they don't exist."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def load_all(self) -> list[Task]:
        """Load all tasks from the JSON file."""
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [Task.model_validate(task) for task in data]

    def load(self, task_id: int) -> Optional[Task]:
        """Load a single task by ID."""
        tasks = self.load_all()
        for task in tasks:
            if task.id == task_id:
                return task
        return None

    def save(self, task: Task) -> None:
        """Save (or update) a task in the JSON file."""
        tasks = self.load_all()
        # Update existing or append new
        for i, existing in enumerate(tasks):
            if existing.id == task.id:
                tasks[i] = task
                break
        else:
            tasks.append(task)
        self._write_all(tasks)

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID. Returns True if found & deleted."""
        tasks = self.load_all()
        new_tasks = [t for t in tasks if t.id != task_id]
        if len(new_tasks) == len(tasks):
            return False
        self._write_all(new_tasks)
        return True

    def next_id(self) -> int:
        """Return the next available task ID."""
        tasks = self.load_all()
        if not tasks:
            return 1
        return max(t.id for t in tasks) + 1

    def _write_all(self, tasks: list[Task]) -> None:
        """Write the full task list to the JSON file."""
        data = [t.model_dump_safe() for t in tasks]
        self.path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
        )