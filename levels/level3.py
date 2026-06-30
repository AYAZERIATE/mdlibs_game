import calendar
import json
from datetime import datetime

FILE_NAME = "goals.json"


def load_goals():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_goals(goals):
    with open(FILE_NAME, "w") as file:
        json.dump(goals, file, indent=4)


def show_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print()
    print(calendar.month(year, month))


def add_goal(goals):
    date = input("Enter date (YYYY-MM-DD): ")
    goal = input("Enter your goal: ")

    goals[date] = goal
    save_goals(goals)

    print("\n Goal saved successfully!\n")


def view_goals(goals):
    if not goals:
        print("\nNo goals found.\n")
        return

    print("\n===== MY GOALS =====")

    for date, goal in sorted(goals.items()):
        print(f"{date} → {goal}")

    print()


def delete_goal(goals):
    date = input("Enter the date of the goal to delete: ")

    if date in goals:
        del goals[date]
        save_goals(goals)
        print(" Goal deleted.\n")
    else:
        print("Goal not found.\n")


def level3():
    print("\n--- Level 3 ---")
    print("Manage your own goal calendar")
    print("This level is going to help you improve your goals over time.\n")

    goals = load_goals()

    while True:
        print("=" * 35)
        print("      MY GOAL CALENDAR")
        print("=" * 35)

        print("1. Show Calendar")
        print("2. Add Goal")
        print("3. View Goals")
        print("4. Delete Goal")
        print("5. Today's Date")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_calendar()

        elif choice == "2":
            add_goal(goals)

        elif choice == "3":
            view_goals(goals)

        elif choice == "4":
            delete_goal(goals)

        elif choice == "5":
            today = datetime.now()
            print("\nToday's date:", today.strftime("%A, %d %B %Y"))
            print()

        elif choice == "6":
            print("\nGood luck achieving your goals!")
            break

        else:
            print("\nInvalid option.\n")