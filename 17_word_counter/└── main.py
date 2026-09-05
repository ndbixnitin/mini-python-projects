# ==========================================
# Day 17 - Word Counter
# ==========================================

print("======================================")
print("           WORD COUNTER")
print("======================================")

# Taking text from user
text = input("\nEnter a sentence or paragraph: ")

# Count characters
characters = len(text)

# Count words
words = len(text.split())

# Count sentences
sentences = text.count(".") + text.count("!") + text.count("?")

# Display result
print("\n======================================")
print("              RESULT")
print("======================================")

print("Total Characters:", characters)
print("Total Words     :", words)
print("Total Sentences :", sentences)

print("======================================")
print("       Program Completed!")
print("======================================")
