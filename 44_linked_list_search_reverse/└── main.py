# ==========================================
# Day 44 - Linked List Search & Reverse
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Display linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Search value
    def search(self, value):
        current = self.head
        position = 1

        while current is not None:
            if current.data == value:
                print("Value found!")
                print("Position:", position)
                return

            current = current.next
            position += 1

        print("Value not found!")

    # Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        self.head = previous

        print("Linked List reversed successfully!")


linked_list = LinkedList()


print("======================================")
print("     LINKED LIST SEARCH & REVERSE")
print("======================================")


while True:

    print("\n1. Add Node")
    print("2. Display")
    print("3. Search")
    print("4. Reverse")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            value = int(input("Enter value: "))
            linked_list.insert(value)
            print("Node added successfully!")

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":

        print("\nLinked List:")
        linked_list.display()

    elif choice == "3":

        try:
            value = int(input("Enter value to search: "))
            linked_list.search(value)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":

        linked_list.reverse()

    elif choice == "5":

        print("Program closed!")
        break

    else:

        print("Invalid choice!")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
