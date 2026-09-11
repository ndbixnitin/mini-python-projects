# ==========================================
# Day 23 - Contact Book with JSON
# ==========================================

import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully! ✅")


def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("\n----- Contact List -----")

    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}. {contact['name']}")
        print("   Phone:", contact["phone"])
        print("   Email:", contact["email"])


def search_contact(contacts):
    name = input("Enter name to search: ").lower()

    found = False

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found! ✅")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True
            break

    if not found:
        print("Contact not found! ❌")


def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)

            print("Contact deleted successfully! ✅")
            return

    print("Contact not found! ❌")


contacts = load_contacts()

print("======================================")
print("      CONTACT BOOK WITH JSON")
print("======================================")

while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        delete_contact(contacts)

    elif choice == "5":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
