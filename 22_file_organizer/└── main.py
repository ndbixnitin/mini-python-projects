# ==========================================
# Day 22 - File Organizer
# ==========================================

import os
import shutil

print("======================================")
print("          FILE ORGANIZER")
print("======================================")

# Folder to organize
folder_path = input("Enter folder path: ")

# Check if folder exists
if not os.path.isdir(folder_path):
    print("Folder not found! ❌")
else:

    # File categories
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Music": [".mp3", ".wav"]
    }

    # Create category folders
    for category in categories:
        category_path = os.path.join(folder_path, category)

        if not os.path.exists(category_path):
            os.mkdir(category_path)

    # Organize files
    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file_name)[1].lower()

        moved = False

        # Find matching category
        for category, extensions in categories.items():

            if file_extension in extensions:

                destination = os.path.join(folder_path, category, file_name)

                shutil.move(file_path, destination)

                print(f"Moved: {file_name} -> {category}")
                moved = True
                break

        # Files that don't match any category
        if not moved:
            print(f"Skipped: {file_name}")

    print("\n======================================")
    print("       FILES ORGANIZED SUCCESSFULLY!")
    print("======================================")
