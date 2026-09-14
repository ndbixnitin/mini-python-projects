# ==========================================
# Day 26 - Library Management System
# ==========================================

books = []


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)

    print("Book added successfully! ✅")


def view_books():
    if len(books) == 0:
        print("No books available.")
        return

    print("\n----- Library Books -----")

    for index, book in enumerate(books, start=1):

        if book["issued"]:
            status = "Issued"
        else:
            status = "Available"

        print(f"{index}. {book['title']} - {book['author']} [{status}]")


def search_book():
    search = input("Enter book title to search: ").lower()

    found = False

    for book in books:

        if search in book["title"].lower():
            print("\nBook Found! 🔍")
            print("Title :", book["title"])
            print("Author:", book["author"])

            if book["issued"]:
                print("Status: Issued")
            else:
                print("Status: Available")

            found = True

    if not found:
        print("Book not found! ❌")


def issue_book():
    title = input("Enter book title to issue: ").lower()

    for book in books:

        if book["title"].lower() == title:

            if book["issued"]:
                print("This book is already issued! ⚠️")
            else:
                book["issued"] = True
                print("Book issued successfully! 📖")

            return

    print("Book not found! ❌")


def return_book():
    title = input("Enter book title to return: ").lower()

    for book in books:

        if book["title"].lower() == title:

            if not book["issued"]:
                print("This book was not issued.")
            else:
                book["issued"] = False
                print("Book returned successfully! 📚")

            return

    print("Book not found! ❌")


print("======================================")
print("      LIBRARY MANAGEMENT SYSTEM")
print("======================================")

while True:

    print("\n----- MENU -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("\nThank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
