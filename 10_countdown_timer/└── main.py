# ==========================================
# Day 10 - Countdown Timer
# ==========================================

import time

print("======================================")
print("          COUNTDOWN TIMER")
print("======================================")

# Take time in seconds from user
total_seconds = int(input("Enter countdown time in seconds: "))

print("\nCountdown Started!\n")

while total_seconds > 0:

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    print(f"{minutes:02}:{seconds:02}")

    time.sleep(1)

    total_seconds -= 1

print("\n======================================")
print("          TIME'S UP! ⏰")
print("======================================")
