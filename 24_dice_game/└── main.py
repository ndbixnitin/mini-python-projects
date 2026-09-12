# ==========================================
# Day 24 - Dice Game
# ==========================================

import random


def roll_dice():
    return random.randint(1, 6)


print("======================================")
print("             DICE GAME")
print("======================================")

player_score = 0
computer_score = 0

while True:

    print("\n1. Play Round")
    print("2. View Score")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":

        player_dice = roll_dice()
        computer_dice = roll_dice()

        print("\nYou rolled:", player_dice)
        print("Computer rolled:", computer_dice)

        if player_dice > computer_dice:
            print("You Win this round! 🎉")
            player_score += 1

        elif player_dice < computer_dice:
            print("Computer Wins this round! 🤖")
            computer_score += 1

        else:
            print("This round is a Draw! 🤝")

    elif choice == "2":

        print("\n----- Current Score -----")
        print("You      :", player_score)
        print("Computer :", computer_score)

    elif choice == "3":

        print("\n----- Final Score -----")
        print("You      :", player_score)
        print("Computer :", computer_score)

        if player_score > computer_score:
            print("🏆 You are the winner!")

        elif player_score < computer_score:
            print("🤖 Computer is the winner!")

        else:
            print("🤝 The game is a draw!")

        print("\nThanks for playing!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("          GAME COMPLETED!")
print("======================================")
