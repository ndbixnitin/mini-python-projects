# ==========================================
# Day 2 - Simple Calculator
# ==========================================

print("======================================")
print("          SIMPLE CALCULATOR")
print("======================================")

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Display results
print("\n----- Results -----")
print("Addition       :", addition)
print("Subtraction    :", subtraction)
print("Multiplication :", multiplication)

# Division
if num2 == 0:
    print("Division       : Cannot divide by zero")
else:
    division = num1 / num2
    print("Division       :", division)

print("======================================")
print("       Calculator Completed!")
print("======================================")
