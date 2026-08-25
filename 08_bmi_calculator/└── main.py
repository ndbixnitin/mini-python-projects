# ==========================================
# Day 8 - BMI Calculator
# ==========================================

print("======================================")
print("           BMI CALCULATOR")
print("======================================")

# Taking input from user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Display BMI
print("\n----- Result -----")
print("Your BMI is:", round(bmi, 2))

# Check BMI category
if bmi < 18.5:
    print("Category: Underweight")

elif bmi < 25:
    print("Category: Normal Weight")

elif bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obesity")

print("======================================")
print("       Calculation Completed!")
print("======================================")
