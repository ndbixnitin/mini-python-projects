# ==========================================
# Day 35 - Selection Sort
# ==========================================

def selection_sort(numbers):
    n = len(numbers)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


print("======================================")
print("          SELECTION SORT")
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

    sorted_numbers = selection_sort(numbers)

    print("Sorted List:  ", sorted_numbers)

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
