# ==========================================
# Day 5 - Number Guessing Game
# ==========================================

import random

print("======================================")
print("        NUMBER GUESSING GAME")
print("======================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.")

    elif guess > secret_number:
        print("Too High! Try again.")

    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Number of attempts:", attempts)
        break

print("======================================")
print("         GAME COMPLETED!")
print("======================================")
