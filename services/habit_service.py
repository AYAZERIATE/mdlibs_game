"""Weekly habit tracking (level 6)."""

from models.habit import DAYS_OF_WEEK, Habit


class HabitService:
    def track_week(self) -> Habit:
        name = input("What habit are you tracking (e.g. 'coding practice')? ").strip()
        habit = Habit(name=name)

        for day in DAYS_OF_WEEK:
            answer = input(f"  Did you do '{name}' on {day}? (y/n): ").strip().lower()
            habit.mark_day(day, answer == "y")

        return habit

    def print_summary(self, habit: Habit) -> None:
        print(f"\n--- {habit.name.title()} — Weekly Summary ---")
        for line in habit.summary_lines():
            print(line)

        print(
            f"\nYou completed '{habit.name}' on "
            f"{habit.completed_count}/{habit.total_days} days "
            f"({habit.completion_percent}%)."
        )

        if habit.completion_percent >= 80:
            print("Outstanding consistency — that's how success habits are built!")
        elif habit.completion_percent >= 50:
            print("Good progress. A little more consistency will compound fast.")
        else:
            print("Every habit starts small. Try to beat this number next week.")