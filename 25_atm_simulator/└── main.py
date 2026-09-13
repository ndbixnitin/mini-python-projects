# ==========================================
# Day 25 - ATM Simulator
# ==========================================

print("======================================")
print("             ATM SIMULATOR")
print("======================================")

correct_pin = "1234"
balance = 5000.0
attempts = 3

# PIN Verification
while attempts > 0:

    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("PIN verified successfully! ✅")
        break

    attempts -= 1
    print("Incorrect PIN! ❌")
    print("Attempts remaining:", attempts)

if attempts == 0:
    print("Too many incorrect attempts. Access denied.")
else:

    while True:

        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nYour current balance is: ₹", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Please enter a valid amount.")
            else:
                balance += amount
                print("Money deposited successfully! ✅")
                print("Updated balance: ₹", balance)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Please enter a valid amount.")
            elif amount > balance:
                print("Insufficient balance! ❌")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Updated balance: ₹", balance)

        elif choice == "4":
            print("\nThank you for using ATM Simulator!")
            break

        else:
            print("Invalid choice! Please try again.")

print("======================================")
print("          PROGRAM COMPLETED!")
print("======================================")
