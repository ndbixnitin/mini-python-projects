# ==========================================
# Day 15 - Student Grade Calculator
# ==========================================

print("======================================")
print("      STUDENT GRADE CALCULATOR")
print("======================================")

# Taking marks from user
english = float(input("Enter English marks: "))
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
computer = float(input("Enter Computer marks: "))
hindi = float(input("Enter Hindi marks: "))

# Calculate total and percentage
total = english + maths + science + computer + hindi
percentage = total / 5

# Display result
print("\n======================================")
print("              RESULT")
print("======================================")

print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

print("======================================")
print("       Calculation Completed!")
print("======================================")
