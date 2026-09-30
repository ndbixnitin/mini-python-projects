# ==========================================
# Day 40 - Queue
# ==========================================

queue = []


def enqueue():
    value = input("Enter value to add: ")

    queue.append(value)

    print("Value added to queue successfully! ✅")


def dequeue():
    if len(queue) == 0:
        print("Queue is empty! ❌")
    else:
        value = queue.pop(0)

        print("Removed value:", value)


def front():
    if len(queue) == 0:
        print("Queue is empty! ❌")
    else:
        print("Front value:", queue[0])


def display():
    if len(queue) == 0:
        print("Queue is empty! ❌")
    else:
        print("\nQueue:", queue)


print("======================================")
print("              QUEUE")
print("======================================")

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        enqueue()

    elif choice == "2":
        dequeue()

    elif choice == "3":
        front()

    elif choice == "4":
        display()

    elif choice == "5":
        print("Program closed. 👋")
        break

    else:
        print("Invalid choice! ❌")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
