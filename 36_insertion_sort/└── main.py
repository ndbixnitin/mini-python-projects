# ==========================================
# Day 36 - Insertion Sort
# ==========================================

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


print("======================================")
print("          INSERTION SORT")
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

    sorted_numbers = insertion_sort(numbers)

    print("Sorted List:  ", sorted_numbers)

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
