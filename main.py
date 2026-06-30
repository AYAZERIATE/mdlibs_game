def level1():
    print("\n📖 Mad Lib Story")
    name = input("Enter your name: ")
    goal = input("Enter your dream goal: ")
    print(f"\n{name} worked hard every day and finally achieved {goal}!")


def level2():
    print("\n✨ Personalized Story")
    name = input("Your name: ")
    career = input("Dream career: ")
    print(f"\nOne day, {name} became a successful {career}.")


def level3():
    print("\n🎯 Multi-Goal List Builder")
    goals = []

    while True:
        goal = input("Enter a goal (or 'q' to finish): ")

        if goal.lower() == "q":
            break

        goals.append(goal)

    print("\nYour Goals:")
    for i, goal in enumerate(goals, start=1):
        print(f"{i}. {goal}")


def level4():
    print("\n📊 Goal Priority Calculator")

    goal = input("Goal name: ")
    importance = int(input("Importance (1-10): "))
    urgency = int(input("Urgency (1-10): "))

    score = importance + urgency

    print(f"\nGoal: {goal}")
    print(f"Priority Score: {score}")


def level5():
    print("\n🎨 Paint Your Own Goals")
    print("Imagine your future success and describe it below:")
    dream = input("Your success vision: ")

    print("\n🌟 Your Dream 🌟")
    print(dream)


def level6():
    print("\n📅 Weekly Habit Tracker")

    habits = []

    for day in range(7):
        habit = input(f"Habit for day {day + 1}: ")
        habits.append(habit)

    print("\nYour Weekly Habits:")
    for habit in habits:
        print("-", habit)


def level7():
    print("\n⏳ Goal Countdown")

    days = int(input("Days until your goal: "))

    print(f"\nOnly {days} days left. Keep going!")


def level8():
    print("\n💾 Save Your Story To A File")

    story = input("Write your success story: ")

    with open("success_story.txt", "w", encoding="utf-8") as file:
        file.write(story)

    print("Story saved successfully!")


def level9():
    print("\n💡 Motivation Quote Generator")

    import random

    quotes = [
        "Success is the sum of small efforts repeated daily.",
        "Dream big. Start small. Act now.",
        "Your future is created by what you do today.",
        "Discipline beats motivation.",
        "Every expert was once a beginner."
    ]

    print("\n" + random.choice(quotes))


def level10():
    print("\n🏆 FULL SUCCESS DASHBOARD")

    name = input("Your name: ")
    goal = input("Main goal: ")
    progress = input("Current progress (%): ")

    print("\n══════════════════════")
    print("SUCCESS DASHBOARD")
    print("══════════════════════")
    print(f"Name     : {name}")
    print(f"Goal     : {goal}")
    print(f"Progress : {progress}%")
    print("══════════════════════")


def main():
    levels = {
        "1": level1,
        "2": level2,
        "3": level3,
        "4": level4,
        "5": level5,
        "6": level6,
        "7": level7,
        "8": level8,
        "9": level9,
        "10": level10,
    }

    while True:
        print("\n══════════════════════════════")
        print("   SUCCESS STORY — LEVEL MENU")
        print("══════════════════════════════")
        print("1.  Mad Lib story")
        print("2.  Personalized story")
        print("3.  Multi-goal list builder")
        print("4.  Goal priority calculator")
        print("5.  Paint your own goals")
        print("6.  Weekly habit tracker")
        print("7.  Goal countdown")
        print("8.  Save your story to a file")
        print("9.  Motivation quote generator")
        print("10. Full success dashboard")
        print("Q.  Quit")

        choice = input("\nChoose a level: ").strip().lower()

        if choice == "q":
            print("Goodbye — keep chasing your goals!")
            break
        elif choice in levels:
            levels[choice]()
        else:
            print("Not a valid option, try again.")


if __name__ == "__main__":
    main()