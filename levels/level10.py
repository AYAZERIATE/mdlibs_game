print("\n--- Level 10 ---")
print("Full Success Dashboard\n")
print("This combines everything: your story, your goals, a habit, a")
print("countdown, and a saved JSON file you can reload later.\n")
 
import datetime
import json
 
name = input("Your name: ").strip()
main_goal = input("Your main goal: ").strip()
why = input("Why this goal matters: ").strip()
 
goals = []
print("\nList up to 3 supporting goals (press Enter to skip/finish):")
while len(goals) < 3:
        g = input(f"  Supporting goal #{len(goals) + 1}: ").strip()
        if g == "":
            break
        goals.append(g)
 
habit = input("\nOne daily habit that supports this goal: ").strip()
 
while True:
        date_str = input("Target date (YYYY-MM-DD): ").strip()
        try:
            target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Please use the format YYYY-MM-DD.")
 
days_left = (target_date - datetime.date.today()).days
quote = get_random_quote()
 
dashboard = {
        "name": name,
        "main_goal": main_goal,
        "why": why,
        "supporting_goals": goals,
        "daily_habit": habit,
        "target_date": str(target_date),
        "days_left": days_left,
        "motivation_quote": quote,
        "created": str(datetime.date.today()),
    }
 
print("\n══════════════════════════════")
print("      SUCCESS DASHBOARD")
print("══════════════════════════════")
print(f"Name:          {dashboard['name']}")
print(f"Main goal:     {dashboard['main_goal']}")
print(f"Why:           {dashboard['why']}")
if goals:
        print("Supporting goals:")
        for g in goals:
            print(f"   - {g}")
print(f"Daily habit:   {dashboard['daily_habit']}")
print(f"Target date:   {dashboard['target_date']} ({days_left} day(s) left)")
print(f"Quote:         \"{quote}\"")
 
filename = f"{(name.lower().replace(' ', '_') or 'my')}_dashboard.json"
with open(filename, "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2)
 
print(f"\n Dashboard saved to '{filename}'.")
print("You can reload this file anytime to revisit your plan.")