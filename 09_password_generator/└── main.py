# ==========================================
# Day 9 - Password Generator
# ==========================================

import random
import string

print("======================================")
print("         PASSWORD GENERATOR")
print("======================================")

# Take password length from user
length = int(input("Enter password length: "))

# Characters for password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\n----- Generated Password -----")
print("Password:", password)

print("======================================")
print("       Password Generated!")
print("======================================")
