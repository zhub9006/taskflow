# TaskFlow Documentation

Welcome to the **TaskFlow** documentation — your guide to building, using, and extending the app.

---

## Getting Started

- [Installation & Setup](#installation--setup)
- [Quick Start Guide](#quick-start-guide)
- [Project Structure](#project-structure)

---

## Installation & Setup

```bash
git clone https://github.com/zhub9006/taskflow.git
cd taskflow
poetry install
```

## Quick Start Guide

```bash
# Add a task
taskflow add "Write documentation" --priority high --tag docs --due 2024-12-31

# List all tasks
taskflow list

# Complete a task
taskflow done 1

# View task details
taskflow show 1

# Delete a task
taskflow delete 1
```

## Project Structure

| Directory | Purpose |
|---|---|
| `src/taskflow/` | Main application package (src-layout) |
| `src/taskflow/cli.py` | CLI commands (Typer + Rich) |
| `src/taskflow/models.py` | Data models (Pydantic) |
| `src/taskflow/core.py` | Business logic (TaskManager) |
| `src/taskflow/storage.py` | Persistence layer (JSON) |
| `src/taskflow/config.py` | App configuration |
| `tests/` | Test suite (pytest) |
| `docs/` | Documentation |

---

## Architecture

TaskFlow follows a **layered architecture** pattern:

1. **CLI Layer** (`cli.py`) — User-facing commands via Typer
2. **Business Logic Layer** (`core.py`) — TaskManager orchestrates operations
3. **Data Layer** (`models.py` + `storage.py`) — Pydantic models + JSON persistence

This separation makes it easy to swap out any layer (e.g., replace JSON with SQLite, or add a web API).

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.
