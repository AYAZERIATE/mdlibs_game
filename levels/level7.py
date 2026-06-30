def level7():
    print("\n--- Level 7 ---")
    print("Goal Countdown\n")
 
    import datetime
 
    goal = input("Enter your goal: ").strip()
 
    while True:
        date_str = input("Enter your target date (YYYY-MM-DD): ").strip()
        try:
            target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("That date format wasn't recognized. Please use YYYY-MM-DD, e.g. 2026-12-31.")
 
    today = datetime.date.today()
    days_left = (target_date - today).days
 
    print(f"\n--- Countdown to: {goal} ---")
    if days_left > 0:
        weeks_left = days_left // 7
        print(f"Target date: {target_date}")
        print(f"Days remaining: {days_left} (~{weeks_left} weeks)")
        print("Every day between now and then is a chance to move closer.")
    elif days_left == 0:
        print("Today is the day! Make it count.")
    else:
        print(f"That date was {abs(days_left)} day(s) ago.")
        print("Consider setting a new target date and trying again — it's never too late to restart.")