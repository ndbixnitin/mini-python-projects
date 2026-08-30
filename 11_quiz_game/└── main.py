# ==========================================
# Day 11 - Quiz Game
# ==========================================

print("======================================")
print("           PYTHON QUIZ GAME")
print("======================================")

questions = [
    {
        "question": "1. What is the extension of a Python file?",
        "options": ["A. .py", "B. .java", "C. .cpp", "D. .html"],
        "answer": "A"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. len()", "D. type()"],
        "answer": "B"
    },
    {
        "question": "3. Which keyword is used for a loop in Python?",
        "options": ["A. repeat", "B. loop", "C. for", "D. next"],
        "answer": "C"
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "5. Which function is used to take input from the user?",
        "options": ["A. print()", "B. get()", "C. input()", "D. scan()"],
        "answer": "C"
    }
]

score = 0

for question in questions:

    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == question["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")
        print("Correct answer is:", question["answer"])

print("\n======================================")
print("             QUIZ RESULT")
print("======================================")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent! 🎉")
elif percentage >= 50:
    print("Good Job! 👍")
else:
    print("Keep Practicing! 💪")

print("======================================")
print("         GAME COMPLETED!")
print("======================================")

