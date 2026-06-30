def level8():
    print("\n--- Level 8 ---")
    print("Save Your Story to a File\n")
 
    name = input("Enter your name: ").strip()
    goal = input("Enter your main goal: ").strip()
    why = input("Why does this goal matter to you? ").strip()
 
    story = (
        f"My name is {name}.\n"
        f"My goal is: {goal}\n"
        f"This matters to me because: {why}\n\n"
        f"I am committing to working toward this goal, one day at a time, "
        f"because I believe in my ability to grow and achieve what I set out to do."
    )
 
    filename = f"{name.lower().replace(' ', '_') or 'my'}_story.txt"
 
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)
 
    print(f"\n--- Preview ---\n{story}\n")
    print(f"Saved to '{filename}'. You can open this file anytime to remind yourself why you started.")