# ==========================================
# Day 42 - Linked List Insertion
# ==========================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Node inserted at beginning! ✅")

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Node inserted at end! ✅")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

        print("Node inserted at end! ✅")

    # Insert at specific position
    def insert_at_position(self, data, position):

        if position < 1:
            print("Position must be 1 or greater! ❌")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)

        current = self.head
        current_position = 1

        while (
            current is not None
            and current_position < position - 1
        ):
            current = current.next
            current_position += 1

        if current is None:
            print("Invalid position! ❌")
            return

        new_node.next = current.next
        current.next = new_node

        print("Node inserted successfully! ✅")

    # Display linked list
    def display(self):

        if self.head is None:
            print("Linked List is empty! ❌")
            return

        current = self.head

        print("\nLinked List:")

        while current is not None:
            print(current.data, end=" → ")
            current = current.next

        print("None")


linked_list = LinkedList()


print("======================================")
print("      LINKED LIST INSERTION")
print("======================================")


while True:

    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Display")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        try:
            value = int(input("Enter value: "))
            linked_list.insert_at_beginning(value)

        except ValueError:
            print("Please enter a valid number! ❌")

    elif choice == "2":

        try:
            value = int(input("Enter value: "))
            linked_list.insert_at_end(value)

        except ValueError:
            print("Please enter a valid number! ❌")

    elif choice == "3":

        try:
            value = int(input("Enter value: "))
            position = int(input("Enter position: "))

            linked_list.insert_at_position(value, position)

        except ValueError:
            print("Please enter valid numbers! ❌")

    elif choice == "4":
        linked_list.display()

    elif choice == "5":
        print("\nProgram closed. 👋")
        break

    else:
        print("Invalid choice! ❌")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
