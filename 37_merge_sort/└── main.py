# ==========================================
# Day 37 - Merge Sort
# ==========================================

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("======================================")
print("            MERGE SORT")
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

    sorted_numbers = merge_sort(numbers)

    print("Sorted List:  ", sorted_numbers)

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
