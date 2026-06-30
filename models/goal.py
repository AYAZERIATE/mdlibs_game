

from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class Goal:
    description: str
    date: Optional[str] = None       
    months: Optional[int] = None     
    priority: Optional[str] = None   

    def calculate_priority(self) -> str:
        """Derive a priority label from how many months away the goal is."""
        if self.months is None:
            return self.priority or "Unknown"

        if self.months > 4:
            self.priority = "High"
        elif self.months == 4:
            self.priority = "Medium"
        else:
            self.priority = "Low"

        return self.priority

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Goal":
        return Goal(
            description=data.get("description", ""),
            date=data.get("date"),
            months=data.get("months"),
            priority=data.get("priority"),
        )