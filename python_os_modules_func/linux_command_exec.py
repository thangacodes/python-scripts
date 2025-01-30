import datetime
import time
import os
import subprocess
todays_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Script execution time: {todays_date}")
current_workdir = os.getcwd()
print(f"Your present working directory is: {current_workdir}")
time.sleep(1)
disk_space_usage = "df -h"
executor         = "whoami"

# Execute the psql command
user_input = input("Please select which command you want to run ('disk' or 'me')\nDo you want to connect?: ")
print(f"User selected command as: {user_input}")
if user_input == "disk_space_usage":
    print(f"User want to check the command 'disk_space_usage': {disk_space_usage}")
    try:
        subprocess.run(disk_space_usage, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error checking the linux command: {err}")
elif user_input == "executor":
    print(f"User want to check the command 'executor': {executor}")
    try:
        subprocess.run(executor, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error checking the linux command: {err}")
else:
    print("Please select only 'disk (OR) me'...")
exit
