import datetime
import time
import os
import subprocess
todays_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Script execution time: {todays_date}")
current_workdir = os.getcwd()
print(f"Your present working directory is: {current_workdir}")
time.sleep(1)
disk = (f"df -h")
me   = (f"whoami")

# Execute the psql command
user_input = input("Please select which command you want to run ('disk' or 'me'). Do you want to connect?: ")
print(f"User selected command as: {user_input}")
if user_input == "disk":
    print(f"User want to run the command 'disk': {disk}")
    try:
        subprocess.run(disk, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error checking the linux command: {err}")
elif user_input == "me":
    print(f"User want to run the command 'me': {me}")
    try:
        subprocess.run(me, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        print(f"Error checking the linux command: {err}")
else:
    print("Please select only 'disk (OR) me'...")
exit
