# ==========================================
# Day 19 - To-Do List Manager
# ==========================================

tasks = []

print("======================================")
print("          TO-DO LIST MANAGER")
print("======================================")

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        task = input("Enter your new task: ")
        tasks.append(task)
        print("Task added successfully! ✅")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n----- Your Tasks -----")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available to remove.")
        else:
            print("\n----- Your Tasks -----")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully! ❌")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("\nThank you for using To-Do List Manager!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
