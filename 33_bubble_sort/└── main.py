# ==========================================
# Day 33 - Bubble Sort
# ==========================================

def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


print("======================================")
print("           BUBBLE SORT")
print("======================================")

numbers_input = input("Enter numbers separated by spaces: ")

numbers = []

for value in numbers_input.split():
    try:
        numbers.append(int(value))
    except ValueError:
        print("Invalid value ignored:", value)

if len(numbers) == 0:
    print("No valid numbers entered.")
else:
    print("\nOriginal List:", numbers)

    sorted_numbers = bubble_sort(numbers)

    print("Sorted List:  ", sorted_numbers)

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
