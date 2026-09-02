# ==========================================
# Day 14 - Dice Rolling Simulator
# ==========================================

import random

print("======================================")
print("       DICE ROLLING SIMULATOR")
print("======================================")

while True:

    choice = input("\nPress R to roll the dice or E to exit: ").upper()

    if choice == "R":
        dice = random.randint(1, 6)
        print("You rolled:", dice)

    elif choice == "E":
        print("\nThanks for playing!")
        break

    else:
        print("Invalid choice! Please enter R or E.")

print("======================================")
print("         GAME COMPLETED!")
print("======================================")
