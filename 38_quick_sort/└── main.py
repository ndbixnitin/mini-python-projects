# ==========================================
# Day 38 - Quick Sort
# ==========================================

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]

    smaller = []
    greater = []

    for number in numbers[:-1]:
        if number <= pivot:
            smaller.append(number)
        else:
            greater.append(number)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


print("======================================")
print("            QUICK SORT")
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

    sorted_numbers = quick_sort(numbers)

    print("Sorted List:  ", sorted_numbers)

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
