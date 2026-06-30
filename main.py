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