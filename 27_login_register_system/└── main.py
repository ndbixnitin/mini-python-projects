# ==========================================
# Day 27 - Login & Register System
# ==========================================

import json
import os

FILE_NAME = "users.json"


def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)


def register(users):
    print("\n----- REGISTER -----")

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if username == "" or password == "":
        print("Username and password cannot be empty! ❌")
        return

    for user in users:
        if user["username"].lower() == username.lower():
            print("Username already exists! ❌")
            return

    if len(password) < 6:
        print("Password must contain at least 6 characters! ❌")
        return

    new_user = {
        "username": username,
        "password": password
    }

    users.append(new_user)
    save_users(users)

    print("Registration successful! ✅")


def login(users):
    print("\n----- LOGIN -----")

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    for user in users:
        if (
            user["username"].lower() == username.lower()
            and user["password"] == password
        ):
            print("\nLogin successful! 🎉")
            print("Welcome,", user["username"])
            return

    print("Invalid username or password! ❌")


users = load_users()

print("======================================")
print("       LOGIN & REGISTER SYSTEM")
print("======================================")

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        register(users)

    elif choice == "2":
        login(users)

    elif choice == "3":
        print("\nThank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
