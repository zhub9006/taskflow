# TaskFlow ✅

> A modern Python task management app — organize, prioritize, and track your tasks with ease.

---

## Features

- 🗂️ **Create, update, and delete tasks** with rich metadata
- 🏷️ **Categorize** tasks with tags and projects
- ⏰ **Due dates & priorities** to stay on track
- 💾 **Persistent storage** (JSON-based, swappable backend)
- 🖥️ **Beautiful CLI** powered by [Typer](https://typer.tiangolo.com/) + [Rich](https://rich.readthedocs.io/)
- ✅ **Well-tested** with pytest and full type-checking via mypy

---

## Quick Start

### Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/zhub9006/taskflow.git
cd taskflow

# Install dependencies with Poetry
poetry install

# Or with pip
pip install -e ".[dev]"
```

### Usage

```bash
# Add a new task
taskflow add "Write project documentation" --priority high --tag docs

# List all tasks
taskflow list

# Complete a task
taskflow done 1

# Show task details
taskflow show 1
```

---

## Project Structure

```
taskflow/
├── .github/                # CI/CD workflows & issue/PR templates
│   └── workflows/
│       └── ci.yml
├── docs/                   # Documentation
│   └── index.md
├── src/
│   └── taskflow/           # Main package (src-layout)
│       ├── __init__.py     # Package metadata
│       ├── __main__.py     # `python -m taskflow` entry point
│       ├── cli.py          # CLI commands (Typer)
│       ├── models.py       # Data models (dataclasses / Pydantic)
│       ├── core.py         # Business logic
│       ├── storage.py      # Persistence layer
│       └── config.py       # Configuration management
├── tests/                  # Test suite
│   ├── conftest.py         # Shared pytest fixtures
│   ├── test_core.py
│   ├── test_models.py
│   └── test_cli.py
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile                # Common dev commands
├── pyproject.toml          # Project config (PEP 621)
└── README.md
```

---

## Development

### Setup

```bash
# Install dev dependencies
make install

# Install pre-commit hooks
make pre-commit-install
```

### Common Commands

| Command              | Description                          |
| -------------------- | ------------------------------------ |
| `make test`          | Run the test suite                   |
| `make lint`          | Run all linters (ruff, mypy, pytest) |
| `make format`        | Auto-format code (ruff)              |
| `make check-safety`  | Run security checks (bandit)         |
| `make cleanup`       | Remove caches and build artifacts    |

---

## Tech Stack

| Tool          | Purpose                        |
| ------------- | ------------------------------ |
| Poetry        | Dependency management          |
| Typer + Rich  | CLI framework & formatting     |
| Pydantic      | Data validation & models       |
| pytest        | Testing                        |
| Ruff          | Linting & formatting           |
| mypy          | Static type checking           |
| pre-commit    | Git hook automation            |
| Bandit        | Security linting               |

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
