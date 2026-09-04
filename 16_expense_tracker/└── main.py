# ==========================================
# Day 16 - Simple Expense Tracker
# ==========================================

expenses = []

print("======================================")
print("         SIMPLE EXPENSE TRACKER")
print("======================================")

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully! ✅")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\n----- Expense List -----")

            for expense in expenses:
                print(expense["name"], ":", expense["amount"])

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("\nTotal Expense:", total)

    elif choice == "4":
        print("\nThank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
