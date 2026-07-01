from datetime import datetime

def level11():

    print("=" * 40)
    print("         LEVEL 11")
    print("     Maximize Your Life Goals")
    print("=" * 40)

    goal = input("\n Enter your goal: ")

    current_day = input(" Enter today's date (YYYY-MM-DD): ")
    final_day = input(" Enter your target date (YYYY-MM-DD): ")

    try:
        current_date = datetime.strptime(current_day, "%Y-%m-%d")
        target_date = datetime.strptime(final_day, "%Y-%m-%d")

        remaining_days = (target_date - current_date).days

        print("\n" + "=" * 40)
        print("         GOAL REPORT")
        print("=" * 40)
        print(f" Goal: {goal}")
        print(f" Today: {current_day}")
        print(f" Target Date: {final_day}")

        if remaining_days > 0:
            weeks = remaining_days // 7
            months = remaining_days // 30

            print(f"\n Days Remaining : {remaining_days}")
            print(f" Weeks Remaining: {weeks}")
            print(f" Months Remaining: {months}")

            print("\n Suggested Plan")
            print("- Work on your goal every day.")
            print("- Track your progress every week.")
            print("- Never skip two days in a row.")
            print("- Celebrate small achievements.")

            print("\n Motivation")
            print('"Success is built one day at a time."')

        elif remaining_days == 0:
            print("\n Today is your deadline!")
            print("Give your best effort and finish strong!")

        else:
            print(f"\n Your target date passed {-remaining_days} days ago.")
            print("Don't give up! Set a new target and continue.")

    except ValueError:
        print("\n Invalid date format.")
        print("Example: 2026-12-31")