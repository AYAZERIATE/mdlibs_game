"""Goal management: the calendar-based tracker (level 3) and the
priority calculator (level 4), backed by the Goal model."""

from models.goal import Goal
from utils import date_utils, file_utils, validation

GOALS_FILE = "goals.json"


class GoalService:
    def __init__(self, filename: str = GOALS_FILE):
        self.filename = filename
        self._goals: dict = file_utils.load_json(self.filename, default={})

    def add_goal(self) -> Goal:
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        description = input("Enter your goal: ").strip()

        goal = Goal(description=description, date=date_str)
        self._goals[date_str] = description
        file_utils.save_json(self.filename, self._goals)

        print("\n Goal saved successfully!\n")
        return goal

    def view_goals(self) -> None:
        if not self._goals:
            print("\nNo goals found.\n")
            return

        print("\n===== MY GOALS =====")
        for date, description in sorted(self._goals.items()):
            print(f"{date} → {description}")
        print()

    def delete_goal(self) -> bool:
        date_str = input("Enter the date of the goal to delete: ").strip()
        if date_str in self._goals:
            del self._goals[date_str]
            file_utils.save_json(self.filename, self._goals)
            print(" Goal deleted.\n")
            return True

        print("Goal not found.\n")
        return False

    def show_calendar(self) -> None:
        year = validation.get_valid_integer("Enter year: ")
        month = validation.get_valid_integer("Enter month (1-12): ")
        date_utils.print_month_calendar(year, month)

    def calculate_priority(self) -> Goal:
        description = input("Enter your goal: ").strip()
        months = validation.get_valid_integer("In how many months do you want to achieve it? ")

        goal = Goal(description=description, months=months)
        goal.calculate_priority()
        return goal