# ==========================================
# Day 28 - Quiz Application with Score
# ==========================================

questions = [
    {
        "question": "Which language is used to create this project?",
        "options": ["A. Python", "B. Java", "C. C++", "D. HTML"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type stores multiple values in an ordered collection?",
        "options": ["A. list", "B. int", "C. float", "D. bool"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used to create a comment in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "Which function is used to get the length of a list?",
        "options": ["A. count()", "B. size()", "C. length()", "D. len()"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to create a loop over a sequence?",
        "options": ["A. repeat", "B. for", "C. loop", "D. iterate"],
        "answer": "B"
    },
    {
        "question": "Which file extension is used for Python programs?",
        "options": ["A. .java", "B. .cpp", "C. .py", "D. .js"],
        "answer": "C"
    },
    {
        "question": "Which function converts input into an integer?",
        "options": ["A. str()", "B. float()", "C. int()", "D. number()"],
        "answer": "C"
    }
]


def run_quiz():
    score = 0

    print("\n======================================")
    print("          QUIZ STARTED!")
    print("======================================")

    for number, question in enumerate(questions, start=1):

        print(f"\nQuestion {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == question["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            print("Wrong! ❌")
            print("Correct answer:", question["answer"])

    return score


def show_result(score):
    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n======================================")
    print("             QUIZ RESULT")
    print("======================================")

    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Wrong Answers  :", total_questions - score)
    print("Percentage     :", round(percentage, 2), "%")

    if percentage == 100:
        print("Excellent! Perfect Score! 🏆")
    elif percentage >= 75:
        print("Great Job! 🎉")
    elif percentage >= 50:
        print("Good! Keep Practicing! 👍")
    else:
        print("Keep Learning and Try Again! 💪")

    print("======================================")


print("======================================")
print("       PYTHON QUIZ APPLICATION")
print("======================================")

while True:

    print("\n1. Start Quiz")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        final_score = run_quiz()
        show_result(final_score)

    elif choice == "2":
        print("\nThank you for playing!")
        break

    else:
        print("Invalid choice! Please try again.")

print("======================================")
print("       PROGRAM COMPLETED!")
print("======================================")
