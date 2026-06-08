"""TaskFlow configuration — app settings and defaults."""

from pathlib import Path

# ── Default Paths ────────────────────────────────────────────────────
DEFAULT_STORAGE_DIR = Path.home() / ".taskflow"
DEFAULT_STORAGE_FILE = DEFAULT_STORAGE_DIR / "tasks.json"

# ── App Metadata ────────────────────────────────────────────────────
APP_NAME = "taskflow"
APP_VERSION = "0.1.0"
APP_AUTHOR = "zhub9006"

# ── Display Defaults ────────────────────────────────────────────────
DEFAULT_PRIORITY = "medium"
DEFAULT_STATUS = "todo"