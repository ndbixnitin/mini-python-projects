# ==========================================
# Day 45 - Doubly Linked List
# ==========================================


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

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
        new_node.prev = current

        print("Node inserted at end! ✅")

    # Display forward
    def display_forward(self):
        if self.head is None:
            print("List is empty! ❌")
            return

        current = self.head

        print("\nForward:")
        while current is not None:
            print(current.data, end=" ⇄ ")
            current = current.next

        print("None")

    # Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty! ❌")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        print("\nBackward:")
        while current is not None:
            print(current.data, end=" ⇄ ")
            current = current.prev

        print("None")


linked_list = DoublyLinkedList()


print("======================================")
print("       DOUBLY LINKED LIST")
print("======================================")


while True:

    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Display Forward")
    print("4. Display Backward")
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

        linked_list.display_forward()

    elif choice == "4":

        linked_list.display_backward()

    elif choice == "5":

        print("\nProgram closed. 👋")
        break

    else:

        print("Invalid choice! ❌")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
