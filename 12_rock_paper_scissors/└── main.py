# ==========================================
# Day 12 - Rock Paper Scissors Game
# ==========================================

import random

print("======================================")
print("      ROCK PAPER SCISSORS GAME")
print("======================================")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("\nThanks for playing!")
        break

    if choice == "1":
        user_choice = "rock"
    elif choice == "2":
        user_choice = "paper"
    elif choice == "3":
        user_choice = "scissors"
    else:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\nYou chose:", user_choice.capitalize())
    print("Computer chose:", computer_choice.capitalize())

    if user_choice == computer_choice:
        print("It's a Draw! 🤝")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win! 🎉")
        user_score += 1

    else:
        print("Computer Wins! 🤖")
        computer_score += 1

    print("\n----- Score -----")
    print("You:", user_score)
    print("Computer:", computer_score)

print("\n======================================")
print("           FINAL SCORE")
print("======================================")
print("You:", user_score)
print("Computer:", computer_score)
print("======================================")
