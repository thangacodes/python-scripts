import pandas as pd
import os
import datetime
import socket
import time

runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at: {runtime}")
machine_name = socket.gethostname()
print(f"You are running the script on: {machine_name}")

# Example Data's
data = {
  'Name': ["john", "dove", "rob", "pope"],
  'Age': [34,54,56,39],
  'City': ["chennai", "mumbai", "bengaluru", "kerala"],
  'Qualification': ["B.E", "B.SC", "M.SC", "B.COM"],
  'Occupation': ["Software Engineer", "Cloud Engineer", "SRE Engineer", "Data Scientist"]
}
# Create pandas dataframe
df = pd.DataFrame(data)
# Add S.No column starting from 1
df.insert(0, 'S.No', range(1, len(df) + 1))
# Define file path
file_name = 'sample.xlsx'
# write dataframe to excel
df.to_excel(file_name, index=False)
print(f"Excel file has been created successfully on the path: {os.getcwd()} ")
# Pause for the User Selection ('Yes or No')
time.sleep(10)
user_input = input("Do you like to delete the sample.xlsx file ('Say yes or no')? ")
if user_input.lower() == "yes":
    print("User selected choice as 'yes', hence deleting the file")
    if os.path.exists("sample.xlsx"):
        os.remove("sample.xlsx")
        print("File deleted successfully.")
    else:
        print("File does not exist.")
elif user_input.lower() == "no":
    print("User selected choice as 'no', hence ignoring the deletion of the file")
else:
    print("User has to select only 'yes' or 'no' options.")
