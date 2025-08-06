import secrets
import time, datetime, sys, os, subprocess
print("")
runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at: {runtime}")
time.sleep(1)
print("Script path is:", os.getcwd())
executor_name = subprocess.check_output(['whoami'], stderr=subprocess.STDOUT)
executor_name = executor_name.decode('utf-8').strip()
print(f"script executor name is: {executor_name}")
print("Script to Create an API KEY for run flask application")
api_key = secrets.token_hex(16) 
print(f'Newly generated application API KEY is: "{api_key}"')
