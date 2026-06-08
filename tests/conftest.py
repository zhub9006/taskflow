"""Shared pytest fixtures for TaskFlow tests."""

import json
from pathlib import Path
from typing import Generator

import pytest

from taskflow.core import TaskManager
from taskflow.storage import Storage


@pytest.fixture
def tmp_storage(tmp_path: Path) -> Storage:
    """Provide a Storage instance backed by a temporary JSON file."""
    storage_path = tmp_path / "tasks.json"
    storage_path.write_text("[]", encoding="utf-8")
    return Storage(path=storage_path)


@pytest.fixture
def task_manager(tmp_storage: Storage) -> TaskManager:
    """Provide a TaskManager using the temporary storage."""
    return TaskManager(storage=tmp_storage)