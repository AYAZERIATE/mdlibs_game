"""File I/O helpers for JSON and plain-text persistence."""

import json


def load_json(filename: str, default=None):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default if default is not None else {}


def save_json(filename: str, data) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_text(filename: str, content: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)