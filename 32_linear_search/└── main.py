# ==========================================
# Day 32 - Linear Search
# ==========================================

def linear_search(numbers, target):
    for index in range(len(numbers)):

        if numbers[index] == target:
            return index

    return -1


print("======================================")
print("          LINEAR SEARCH")
print("======================================")

# Take numbers from user
numbers_input = input(
    "Enter numbers separated by spaces: "
)

numbers = []

for value in numbers_input.split():
    try:
        numbers.append(int(value))
    except ValueError:
        print("Invalid value ignored:", value)

if len(numbers) == 0:
    print("No valid numbers entered.")
else:

    try:
        target = int(input("Enter number to search: "))

        result = linear_search(numbers, target)

        print("\n----- SEARCH RESULT -----")

        if result == -1:
            print("Number not found! ❌")
        else:
            print("Number found! ✅")
            print("Index:", result)
            print("Position:", result + 1)

    except ValueError:
        print("Please enter a valid number! ❌")


print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
