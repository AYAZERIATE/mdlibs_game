import random

QUOTES = [
    "Success isn't about being the best. It's about being better than you were yesterday.",
    "Small, consistent actions create extraordinary results over time.",
    "Dream big, start small, act now.",
    "Every expert was once a beginner.",
    "Your future is created by what you do today, not tomorrow."
]


def get_random_quote():
    return random.choice(QUOTES)


def level9():
    print("\n--- Level 9 ---")
    print("Motivation Quote Generator\n")

    while True:
        print(f" \"{get_random_quote()}\"\n")
        again = input("Want another quote? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nKeep that quote in mind as you work toward your goals.")