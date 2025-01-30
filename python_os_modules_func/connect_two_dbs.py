import datetime
import time
import os
import subprocess
todays_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"Script is executed on: {todays_date}")
time.sleep(1)
print("Python3 script to connect source (OR) dest db")
time.sleep(2)
print("Checking we are at the right place, where our belt config.json file exist..")
time.sleep(4)
current_workdir = os.getcwd()
print(f"You are at the right place: {current_workdir}")
time.sleep(3)
src_db="app1.ap-south-1.rds.amazonaws.com"
dest_db="app2.ap-ap-south-1.rds.amazonaws.com"
db_name="devopsdb"
username="admin"
port="5432"
connect_src_db = (f"psql -h {src_db} -p {port} -U {username} -d {db_name}")
connect_dest_db = (f"psql -h {dest_db} -p {port} -U {username} -d {db_name}")

# Execute the psql command

user_input = input("Please select which db (src_db or dest_db), do you want to connect: ")
print(f"User selected db name as: {user_input}")

if user_input == "src_db":
    print(f"User want to connect 'src_db': {src_db}")
    try:
        subprocess.run(connect_src_db, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to source database: {e}")
elif user_input == "dest_db":
    print(f"User want to connect 'dest_db': {dest_db}")
    try:
        subprocess.run(connect_dest_db, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to source database: {e}")
else:
    print("Please select only 'src_db (OR) dest_db'...")
exit
