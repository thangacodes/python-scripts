import pandas as pd
import os, datetime, socket

# Display runtime and machine info
runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at: {runtime}")
machine_name = socket.gethostname()
print(f"You are running the script on: {machine_name}")

# Sample data
data = {
    'Name': ["john", "dove", "rob", "pope"],
    'Age': [34, 54, 56, 39],
    'City': ["chennai", "mumbai", "bengaluru", "kerala"],
    'Qualification': ["B.E", "B.SC", "M.SC", "B.COM"],
    'Occupation': ["Software Engineer", "Cloud Engineer", "SRE Engineer", "Data Scientist"]
}

# Create DataFrame and add S.No
df = pd.DataFrame(data)
df.insert(0, 'S.No', range(1, len(df) + 1))

# Get filename from user
file_name = input("Please provide the file name as you wish to keep: ").strip()
print(f"User entered the name of the file: {file_name}")

# Ensure .xlsx extension
if not file_name.endswith('.xlsx'):
    file_name += '.xlsx'

# Save to Excel
df.to_excel(file_name, index=False)
print(f"\n Excel file created successfully at: {os.path.join(os.getcwd(), file_name)}")

# Ask if user wants to delete the file
user_input = input("\n Do you want to delete the created file? (Say 'yes or no'): ").strip().lower()

if user_input == "yes":
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f" File {file_name} is deleted successfully.")
    else:
        print("File does not exist.")
elif user_input == "no":
    print(f"file: {file_name} is not deleted.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
