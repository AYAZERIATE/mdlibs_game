def get_random_quote():
    """Return a single random motivational quote."""
    import random
    return random.choice(QUOTES)
 
 
def level9():
    print("\n--- Level 9 ---")
    print("Motivation Quote Generator\n")
 
    while True:
        print(f"💬 \"{get_random_quote()}\"\n")
        again = input("Want another quote? (y/n): ").strip().lower()
        if again != "y":
            break
 
    print("\nKeep that quote in mind as you work toward your goals.")