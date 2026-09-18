# ==========================================
# Day 30 - Personal Expense Manager
# ==========================================

import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\n----- ADD EXPENSE -----")

    title = input("Enter expense name: ").strip()
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid amount! ❌")
        return

    if title == "" or category == "":
        print("Expense name and category cannot be empty! ❌")
        return

    if amount <= 0:
        print("Amount must be greater than zero! ❌")
        return

    expense = {
        "title": title,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully! ✅")


def view_expenses(expenses):
    print("\n----- ALL EXPENSES -----")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def total_expense(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense: ₹{total:.2f}")


def category_expenses(expenses):
    category = input("Enter category: ").strip().lower()

    found = False
    total = 0

    print(f"\n----- {category.upper()} EXPENSES -----")

    for number, expense in enumerate(expenses, start=1):

        if expense["category"].lower() == category:
            print(
                f"{number}. {expense['title']} - "
                f"₹{expense['amount']:.2f}"
            )

            total += expense["amount"]
            found = True

    if not found:
        print("No expenses found in this category.")
    else:
        print(f"\nCategory Total: ₹{total:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)

    if len(expenses) == 0:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number! ❌")
        return

    if 1 <= number <= len(expenses):

        removed = expenses.pop(number - 1)
        save_expenses(expenses)

        print(
            f"'{removed['title']}' deleted successfully! 🗑️"
        )

    else:
        print("Invalid expense number! ❌")


expenses = load_expenses()

print("======================================")
print("       PERSONAL EXPENSE MANAGER")
print("======================================")

while True:

    print("\n----- MENU -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Expenses")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_expense(expenses)

    elif choice == "4":
        category_expenses(expenses)

    elif choice == "5":
        delete_expense(expenses)

    elif choice == "6":
        print("\nThank you for using Personal Expense Manager!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       DAY 30 COMPLETED! 🎉")
print("======================================")
