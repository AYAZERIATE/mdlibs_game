"""Builds the full success dashboard (level 10) out of a User and a
saved quote, and persists it to JSON."""

from models.user import User
from utils import date_utils, file_utils, quote_utils, validation


class DashboardService:
    def build(self) -> dict:
        user = User(
            name=input("Your name: ").strip(),
            main_goal=input("Your main goal: ").strip(),
            why=input("Why this goal matters: ").strip(),
        )

        print("\nList up to 3 supporting goals (press Enter to skip/finish):")
        while len(user.supporting_goals) < 3:
            g = input(f"  Supporting goal #{len(user.supporting_goals) + 1}: ").strip()
            if g == "":
                break
            user.supporting_goals.append(g)

        user.daily_habit = input("\nOne daily habit that supports this goal: ").strip()

        target_date = validation.get_valid_date("Target date (YYYY-MM-DD): ")
        days_left = date_utils.days_between(target_date)
        quote = quote_utils.get_random_quote()

        dashboard = {
            **user.to_dict(),
            "target_date": str(target_date),
            "days_left": days_left,
            "motivation_quote": quote,
            "created": str(date_utils.today()),
        }

        self._print(dashboard, days_left, quote)

        filename = f"{user.slug}_dashboard.json"
        file_utils.save_json(filename, dashboard)
        print(f"\n Dashboard saved to '{filename}'.")
        print("You can reload this file anytime to revisit your plan.")

        return dashboard

    @staticmethod
    def _print(dashboard: dict, days_left: int, quote: str) -> None:
        print("\n══════════════════════════════")
        print("      SUCCESS DASHBOARD")
        print("══════════════════════════════")
        print(f"Name:          {dashboard['name']}")
        print(f"Main goal:     {dashboard['main_goal']}")
        print(f"Why:           {dashboard['why']}")
        if dashboard["supporting_goals"]:
            print("Supporting goals:")
            for g in dashboard["supporting_goals"]:
                print(f"   - {g}")
        print(f"Daily habit:   {dashboard['daily_habit']}")
        print(f"Target date:   {dashboard['target_date']} ({days_left} day(s) left)")
        print(f'Quote:         "{quote}"')