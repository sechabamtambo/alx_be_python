while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    
    if task and priority in ("high", "medium", "low") and time_bound in ("yes", "no"):
        break
    else:
        print("\nInvalid input. Please try again.\n")

match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"
        
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
    
print("\n Reminder:", reminder)

