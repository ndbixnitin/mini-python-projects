# ==========================================
# Day 18 - Password Strength Checker
# ==========================================

print("======================================")
print("      PASSWORD STRENGTH CHECKER")
print("======================================")

password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

length = len(password)

print("\n======================================")
print("              RESULT")
print("======================================")

if length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password Strength: Strong ✅")

elif length >= 6 and (has_upper or has_lower) and has_digit:
    print("Password Strength: Medium ⚠️")

else:
    print("Password Strength: Weak ❌")

print("\nPassword Requirements:")
print("- At least 8 characters")
print("- One uppercase letter")
print("- One lowercase letter")
print("- One number")
print("- One special character")

print("======================================")
print("       Program Completed!")
print("======================================")
