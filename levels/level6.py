def level6():
    print("\n--- Level 6 ---")
    print("Weekly Habit Tracker\n")
 
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    habit = input("What habit are you tracking (e.g. 'coding practice')? ").strip()
 
    tracker = {}
    for day in days:
        answer = input(f"  Did you do '{habit}' on {day}? (y/n): ").strip().lower()
        tracker[day] = answer == "y"
 
    completed = sum(1 for done in tracker.values() if done)
    total = len(days)
    percent = round((completed / total) * 100)
 
    print(f"\n--- {habit.title()} — Weekly Summary ---")
    for day, done in tracker.items():
        mark = "✅" if done else "❌"
        print(f"  {day:<10} {mark}")
 
    print(f"\nYou completed '{habit}' on {completed}/{total} days ({percent}%).")
    if percent >= 80:
        print("Outstanding consistency — that's how success habits are built!")
    elif percent >= 50:
        print("Good progress. A little more consistency will compound fast.")
    else:
        print("Every habit starts small. Try to beat this number next week.")
