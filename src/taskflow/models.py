"""TaskFlow data models — validated with Pydantic."""

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Priority(str, Enum):
    """Task priority levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStatus(str, Enum):
    """Task status values."""

    TODO = "todo"
    DONE = "done"


class Task(BaseModel):
    """A single task with metadata."""

    id: int = Field(description="Unique task identifier")
    title: str = Field(min_length=1, description="Task title")
    priority: Priority = Field(default=Priority.MEDIUM, description="Priority level")
    tag: Optional[str] = Field(default=None, description="Categorization tag")
    due: Optional[date] = Field(default=None, description="Due date")
    status: TaskStatus = Field(default=TaskStatus.TODO, description="Current status")

    @field_validator("priority", mode="before")
    @classmethod
    def normalize_priority(cls, v: str) -> str:
        """Normalize priority input to lowercase."""
        return v.lower()

    def model_dump_safe(self) -> dict:
        """Serialize with date as string for JSON storage."""
        data = self.model_dump()
        if data["due"] is not None:
            data["due"] = str(data["due"])
        return data
