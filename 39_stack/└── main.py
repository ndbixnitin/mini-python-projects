# ==========================================
# Day 39 - Stack
# ==========================================

stack = []


def push():
    value = input("Enter value to push: ")
    stack.append(value)
    print("Value added successfully! ✅")


def pop():
    if len(stack) == 0:
        print("Stack is empty! ❌")
    else:
        value = stack.pop()
        print("Removed value:", value)


def peek():
    if len(stack) == 0:
        print("Stack is empty! ❌")
    else:
        print("Top value:", stack[-1])


def display():
    if len(stack) == 0:
        print("Stack is empty! ❌")
    else:
        print("\nStack:", stack)


print("======================================")
print("             STACK")
print("======================================")

while True:

    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        push()

    elif choice == "2":
        pop()

    elif choice == "3":
        peek()

    elif choice == "4":
        display()

    elif choice == "5":
        print("Program closed. 👋")
        break

    else:
        print("Invalid choice! ❌")

print("======================================")
