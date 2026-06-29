def level4():
   print("Level 4")
print("Goal Priorities\n")

goal = input("Enter your goal: ")
months = int(input("In how many months do you want to achieve it? "))

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