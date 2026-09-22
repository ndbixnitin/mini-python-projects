# ==========================================
# Day 34 - Binary Search
# ==========================================

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


print("======================================")
print("          BINARY SEARCH")
print("======================================")

numbers_input = input("Enter sorted numbers separated by spaces: ")

numbers = []

for value in numbers_input.split():
    try:
        numbers.append(int(value))
    except ValueError:
        print("Invalid value ignored:", value)

if len(numbers) == 0:
    print("No valid numbers entered.")
else:
    numbers.sort()

    print("\nSorted List:", numbers)

    try:
        target = int(input("Enter number to search: "))

        result = binary_search(numbers, target)

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
