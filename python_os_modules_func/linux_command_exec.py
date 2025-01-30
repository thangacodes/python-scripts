import datetime
import time
import os
import subprocess
def todays_date():
    todays_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Script execution time: {todays_date}")
def cwd():
    current_workdir = os.getcwd()
    print(f"Your present working directory is: {current_workdir}")
    time.sleep(1)
def variables():
    disk_space_usage = "df -h"
    executor         = "whoami"
    host             = "hostname"
    name_resolver    = "nslookup"
    engine           = "www.google.com"
    return disk_space_usage, executor, host, name_resolver, engine

# Execute the psql command
def script_begin():
    disk_space_usage, executor, host, name_resolver,engine = variables()
    user_input = input("Please select what do you want to check: ('disk_space_usage' or 'executor' or 'host' or 'name_resolver')\nDo you want to run command?: ")
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
    elif user_input == "host":
        print(f"User want to check the command 'host': {host}")
        try:
            subprocess.run(host, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(f"Error checking the linux command: {err}")
    elif user_input == "name_resolver":
        print("User want to check the command 'name_resolver'")
        try:
            subprocess.run(f"{name_resolver} {engine}", shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print(f"Error checking the linux command: {err}")
    else:
        print("Please select only 'disk (OR) me'...")
    exit

todays_date()
cwd()
script_begin()
