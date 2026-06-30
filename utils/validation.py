"""Reusable input-validation helpers."""

import datetime


def get_valid_integer(prompt: str) -> int:
    """Keep asking until the user enters a whole number."""
    while True:
        raw = input(prompt)
        if raw.isdigit():
            return int(raw)
        print("Please enter a whole number.")


def get_valid_date(prompt: str) -> datetime.date:
    """Keep asking until the user enters a date as YYYY-MM-DD."""
    while True:
        raw = input(prompt).strip()
        try:
            return datetime.datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError:
            print("That date format wasn't recognized. Please use YYYY-MM-DD, e.g. 2026-12-31.")


def get_yes_no(prompt: str) -> bool:
    """Keep asking until the user answers y/n, returns True for yes."""
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")