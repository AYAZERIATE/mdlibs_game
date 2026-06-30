"""User model representing a player's profile and success story."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class User:
    name: str
    main_goal: str = ""
    why: str = ""
    supporting_goals: List[str] = field(default_factory=list)
    daily_habit: str = ""

    @property
    def slug(self) -> str:
        """Filesystem-safe version of the user's name, used for filenames."""
        return self.name.lower().replace(" ", "_") or "my"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "main_goal": self.main_goal,
            "why": self.why,
            "supporting_goals": self.supporting_goals,
            "daily_habit": self.daily_habit,
        }