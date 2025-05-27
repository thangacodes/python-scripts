import os
import time
import subprocess

# Variables
file_name = "test.txt"

# Ask user to enter the path
user_input = input("Please enter the path, where you want to check file: ")

# Build the full file path
file_path = os.path.join(user_input, file_name)

print(f"User entered path is: {user_input}")
time.sleep(1)

# Check if file exists
if os.path.exists(file_path):
    print(f"File found: {file_path}")

    # Use subprocess to search for the string "interview"
    try:
        result = subprocess.run(
            ["grep", "-i", "interview", file_path],
            capture_output=True,
            text=True,
            check=False  # We handle errors manually
        )

        if result.stdout:
            print("Content is found in the file:")
            print(result.stdout)
        else:
            print("The content 'interview' does NOT exist in the file.")

    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print("The file does NOT exist at the specified path.")
