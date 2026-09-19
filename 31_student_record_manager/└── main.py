# ==========================================
# Day 31 - Student Record Manager
# ==========================================

students = []


def add_student():
    print("\n----- ADD STUDENT -----")

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()
    course = input("Enter course: ").strip()

    if name == "" or roll_number == "" or course == "":
        print("All fields are required! ❌")
        return

    for student in students:
        if student["roll_number"] == roll_number:
            print("Roll number already exists! ❌")
            return

    student = {
        "name": name,
        "roll_number": roll_number,
        "course": course
    }

    students.append(student)

    print("Student added successfully! ✅")


def view_students():
    print("\n----- STUDENT RECORDS -----")

    if len(students) == 0:
        print("No student records available.")
        return

    for number, student in enumerate(students, start=1):
        print(f"\n{number}.")
        print("Name       :", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Course     :", student["course"])


def search_student():
    roll_number = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found! 🔍")
            print("Name       :", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Course     :", student["course"])
            return

    print("Student not found! ❌")


def update_student():
    roll_number = input("Enter roll number to update: ").strip()

    for student in students:

        if student["roll_number"] == roll_number:

            print("\nStudent Found! 🔍")

            new_name = input("Enter new name: ").strip()
            new_course = input("Enter new course: ").strip()

            if new_name != "":
                student["name"] = new_name

            if new_course != "":
                student["course"] = new_course

            print("Student record updated successfully! ✅")
            return

    print("Student not found! ❌")


def delete_student():
    roll_number = input("Enter roll number to delete: ").strip()

    for student in students:

        if student["roll_number"] == roll_number:
            students.remove(student)

            print("Student deleted successfully! 🗑️")
            return

    print("Student not found! ❌")


print("======================================")
print("       STUDENT RECORD MANAGER")
print("======================================")

while True:

    print("\n----- MENU -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Record Manager!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
