# ==========================================
# Day 21 - Notes Saver
# ==========================================

FILE_NAME = "notes.txt"


def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully! ✅")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.read()

        if notes.strip() == "":
            print("No notes available.")
        else:
            print("\n----- Your Notes -----")
            print(notes)

    except FileNotFoundError:
        print("No notes available.")


print("======================================")
print("           NOTES SAVER")
print("======================================")

while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        print("\nThank you for using Notes Saver!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
