# ── TaskFlow Makefile ───────────────────────────────────────────────

.PHONY: install test lint format check-codestyle check-safety mypy cleanup pre-commit-install

# ── Install ─────────────────────────────────────────────────────────
install:
	poetry install

pre-commit-install:
	pre-commit install

# ── Testing ─────────────────────────────────────────────────────────
test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=taskflow --cov-report=term-missing

# ── Linting & Formatting ───────────────────────────────────────────
format:
	poetry run ruff format src tests
	poetry run ruff check --fix src tests

check-codestyle:
	poetry run ruff check src tests
	poetry run ruff format --check src tests

mypy:
	poetry run mypy src/taskflow

check-safety:
	poetry run bandit -r src/taskflow

lint: test check-codestyle mypy check-safety

# ── Cleanup ─────────────────────────────────────────────────────────
cleanup:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf build dist *.egg-info htmlcov .coverage coverage.xml
