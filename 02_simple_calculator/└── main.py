# ==========================================
# Day 2 - Simple Calculator
# ==========================================

print("======================================")
print("          SIMPLE CALCULATOR")
print("======================================")

# Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Display results
print("\n----- Results -----")
print("Addition       :", addition)
print("Subtraction    :", subtraction)
print("Multiplication :", multiplication)

# Check before division
if num2 != 0:
    division = num1 / num2
    print("Division       :", division)
else:
    print("Division       : Cannot divide by zero")

print("======================================")
print("       Calculator Completed!")
print("======================================")
