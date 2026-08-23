# ==========================================
# Day 6 - Multiplication Table Generator
# ==========================================

print("======================================")
print("      MULTIPLICATION TABLE")
print("======================================")

# Take a number from the user
number = int(input("Enter a number: "))

print("\n----- Multiplication Table -----")

# Generate multiplication table
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

print("======================================")
print("       Program Completed!")
print("======================================")
