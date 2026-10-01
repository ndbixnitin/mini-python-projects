# ==========================================
# Day 41 - Singly Linked List
# ==========================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Node added successfully! ✅")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

        print("Node added successfully! ✅")

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

    def search(self, value):
        current = self.head
        position = 1

        while current is not None:

            if current.data == value:
                print("Value found! ✅")
                print("Position:", position)
                return

            current = current.next
            position += 1

        print("Value not found! ❌")

    def delete(self, value):
        if self.head is None:
            print("Linked List is empty! ❌")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted successfully! 🗑️")
            return

        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next
                print("Node deleted successfully! 🗑️")
                return

            current = current.next

        print("Value not found! ❌")


linked_list = LinkedList()


print("======================================")
print("        SINGLY LINKED LIST")
print("======================================")


while True:

    print("\n1. Insert")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        try:
            value = int(input("Enter value: "))
            linked_list.insert_at_end(value)

        except ValueError:
            print("Please enter a valid number! ❌")

    elif choice == "2":
        linked_list.display()

    elif choice == "3":

        try:
            value = int(input("Enter value to search: "))
            linked_list.search(value)

        except ValueError:
            print("Please enter a valid number! ❌")

    elif choice == "4":

        try:
            value = int(input("Enter value to delete: "))
            linked_list.delete(value)

        except ValueError:
            print("Please enter a valid number! ❌")

    elif choice == "5":
        print("\nProgram closed. 👋")
        break

    else:
        print("Invalid choice! ❌")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
