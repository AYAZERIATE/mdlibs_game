from levels.level1 import level1
from levels.level2 import level2
from levels.level3 import level3
from levels.level4 import level4
from levels.level5 import level5


def main():
    print("=" * 50)
    print(" WELCOME TO PAINT YOUR OWN SUCCESS STORY ")
    print("=" * 50)

    while True:
        print("\nChoose a level:")
        print("1. Level 1 - Story of a Successful Boy")
        print("2. Level 2 - Create Your Success Story")
        print("3. Level 3 - Goal Calendar")
        print("4. Level 4 - Goal Priorities")
        print("5. Level 5 - Paint Your Own Goals")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            level1()

        elif choice == "2":
            level2()

        elif choice == "3":
            level3()

        elif choice == "4":
            level4()

        elif choice == "5":
            level5()

        elif choice == "6":
            print("\n Thank you for using Paint Your Own Success Story!")
            break

        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()