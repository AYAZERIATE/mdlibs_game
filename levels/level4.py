def level4():
    print("\n--- Level 4 ---")
    print("Goal Priorities\n")
 
    goal = input("Enter your goal: ")
 
    while True:
        months_raw = input("In how many months do you want to achieve it? ")
        if months_raw.isdigit():
            months = int(months_raw)
            break
        print("Please enter a whole number.")
 
    if months > 4:
        priority = "High"
    elif months == 4:
        priority = "Medium"
    else:
        priority = "Low"
 
    print("\n----- Goal Information -----")
    print(f"Goal: {goal}")
    print(f"Time: {months} months")
    print(f"Priority: {priority}")