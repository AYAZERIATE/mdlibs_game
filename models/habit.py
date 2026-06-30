"""Habit model used by the weekly habit tracker (level 6)."""

from dataclasses import dataclass, field
from typing import Dict

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@dataclass
class Habit:
    name: str
    days_completed: Dict[str, bool] = field(
        default_factory=lambda: {day: False for day in DAYS_OF_WEEK}
    )

    def mark_day(self, day: str, completed: bool) -> None:
        if day not in self.days_completed:
            raise ValueError(f"Unknown day: {day}")
        self.days_completed[day] = completed

    @property
    def completed_count(self) -> int:
        return sum(1 for done in self.days_completed.values() if done)

    @property
    def total_days(self) -> int:
        return len(self.days_completed)

    @property
    def completion_percent(self) -> int:
        if self.total_days == 0:
            return 0
        return round((self.completed_count / self.total_days) * 100)

    def summary_lines(self):
        for day, done in self.days_completed.items():
            mark = "✅" if done else "❌"
            yield f"  {day:<10} {mark}"