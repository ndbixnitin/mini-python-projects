# ==========================================
# Day 20 - Contact Book
# ==========================================

contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    print("Contact added successfully! ✅")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\n----- Contact List -----")

        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")


def search_contact():
    name = input("Enter name to search: ").lower()

    found = False

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found! ✅")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            found = True
            break

    if not found:
        print("Contact not found! ❌")


def delete_contact():
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully! 🗑️")
            return

    print("Contact not found! ❌")


print("======================================")
print("           CONTACT BOOK")
print("======================================")

while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
