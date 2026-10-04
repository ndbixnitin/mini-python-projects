# ==========================================
# Day 43 - Linked List Deletion
# ==========================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Delete from beginning
    def delete_from_beginning(self):

        if self.head is None:
            print("Linked List is empty! ❌")
            return

        deleted_value = self.head.data

        self.head = self.head.next

        print("Deleted value:", deleted_value)
        print("First node deleted successfully! ✅")

    # Delete from end
    def delete_from_end(self):

        if self.head is None:
            print("Linked List is empty! ❌")
            return

        # Only one node
        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None

            print("Deleted value:", deleted_value)
            print("Last node deleted successfully! ✅")
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        deleted_value = current.next.data

        current.next = None

        print("Deleted value:", deleted_value)
        print("Last node deleted successfully! ✅")

    # Delete by value
    def delete_by_value(self, value):

        if self.head is None:
            print("Linked List is empty! ❌")
            return

        # If first node contains the value
        if self.head.data == value:
            self.head = self.head.next

            print("Node deleted successfully! ✅")
            return

        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next

                print("Node deleted successfully! ✅")
                return

            current = current.next

        print("Value not found! ❌")

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
print("       LINKED LIST DELETION")
print("======================================")


while True:

    print("\n1. Add Node")
    print("2. Delete from Beginning")
    print("3. Delete from End")
    print("4. Delete by Value")
    print("5. Display")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        try:
            value = int(input("Enter value: "))

            linked_list.insert_at_end(value)

            print("Node added successfully! ✅")

        except ValueError:
            print("Please enter a valid number! ❌")

    elif choice == "2":

        linked_list.delete_from_beginning()

    elif choice == "3":

        linked_list.delete_from_end()

    elif choice == "4":

        try:
            value = int(input("Enter value to delete: "))

            linked_list.delete_by_value(value)

        except ValueError:
            print("Please enter a valid number! ❌")

    elif choice == "5":

        linked_list.display()

    elif choice == "6":

        print("\nProgram closed. 👋")
        break

    else:

        print("Invalid choice! Please try again. ❌")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
