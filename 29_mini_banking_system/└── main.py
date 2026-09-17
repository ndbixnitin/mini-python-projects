# ==========================================
# Day 29 - Mini Banking System
# ==========================================

accounts = {}


def create_account():
    print("\n----- CREATE ACCOUNT -----")

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:
        print("Account already exists! ❌")
        return

    name = input("Enter account holder name: ").strip()

    try:
        initial_balance = float(input("Enter initial deposit: "))
    except ValueError:
        print("Please enter a valid amount! ❌")
        return

    if initial_balance < 0:
        print("Initial deposit cannot be negative! ❌")
        return

    accounts[account_number] = {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }

    accounts[account_number]["transactions"].append(
        f"Account created with deposit: ₹{initial_balance:.2f}"
    )

    print("Account created successfully! ✅")


def login():
    print("\n----- LOGIN -----")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found! ❌")
        return

    account = accounts[account_number]

    print(f"\nWelcome, {account['name']}! 👋")

    while True:

        print("\n----- ACCOUNT MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":

            print(f"\nCurrent Balance: ₹{account['balance']:.2f}")

        elif choice == "2":

            try:
                amount = float(input("Enter deposit amount: "))
            except ValueError:
                print("Please enter a valid amount! ❌")
                continue

            if amount <= 0:
                print("Amount must be greater than zero! ❌")
            else:
                account["balance"] += amount

                account["transactions"].append(
                    f"Deposited: ₹{amount:.2f}"
                )

                print("Money deposited successfully! ✅")
                print(f"New Balance: ₹{account['balance']:.2f}")

        elif choice == "3":

            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("Please enter a valid amount! ❌")
                continue

            if amount <= 0:
                print("Amount must be greater than zero! ❌")

            elif amount > account["balance"]:
                print("Insufficient balance! ❌")

            else:
                account["balance"] -= amount

                account["transactions"].append(
                    f"Withdrawn: ₹{amount:.2f}"
                )

                print("Money withdrawn successfully! ✅")
                print(f"New Balance: ₹{account['balance']:.2f}")

        elif choice == "4":

            print("\n----- TRANSACTION HISTORY -----")

            if len(account["transactions"]) == 0:
                print("No transactions available.")

            else:
                for number, transaction in enumerate(
                    account["transactions"], start=1
                ):
                    print(f"{number}. {transaction}")

        elif choice == "5":

            print("\nLogged out successfully! 👋")
            break

        else:
            print("Invalid choice! Please try again.")


print("======================================")
print("         MINI BANKING SYSTEM")
print("======================================")

while True:

    print("\n----- MAIN MENU -----")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        create_account()

    elif choice == "2":
        login()

    elif choice == "3":
        print("\nThank you for using Mini Banking System!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
