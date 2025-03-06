#!/bin/bash
echo "Script to create a venv using python3"
echo "Checking Python installed/available version on MacBook"
python3 --version
VENV_DIR="/Users/td/Desktop/devops_script/vedhu"
if [ -d "$VENV_DIR" ]; then
    echo "Venv directory path is: '$VENV_DIR' already exists. Skipping creation part."
else
    echo "Creating a virtual environment in '$VENV_DIR'"
    python3 -m venv "$VENV_DIR"
    echo "VENV created successfully."
fi
# Activate venv
echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"
echo "venv is activated."

# Install required dependency pip3 library to run python script
pip install --upgrade pip
pip3 install boto3
echo "install request module"
pip3 install requests
echo "python script invoke beginning shortly..."
sleep 2
echo "Using here document  syntax in shell, we input for the command to append in a file.."
cat <<EOF > api_call.py
import time as t
import datetime as d
import requests
script_execdate = d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Script executed at: {script_execdate}")
endpoint = "https://www.google.com/"
print(f"You are trying to hit: {endpoint}")
t.sleep(2)
try:
    response = requests.get(endpoint)
    if response.status_code == 200:
        print("Request was successful!")
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as error:
    print(f"An error occurred: {error}")
EOF
echo ""
echo ""
echo "Executing python3 script to make api call..."
python3 api_call.py
echo "Deactivate the virtual environment"
deactivate

# Define the directory path
DIR_PATH="/Users/murugat/Desktop/adf_val/devops_script"

# List out files in the directory
echo "Listing files in $DIR_PATH"
ls -ltr $DIR_PATH
# Check if 'vedhu' folder exists
if [ -d "$DIR_PATH/vedhu" ]; then
   echo "You are good to delete venv folder called 'vedhu'"
   echo "Removing VENV folder called 'vedhu' since work is over.."
   rm -rf "$DIR_PATH/vedhu"
else
   echo "No folder called 'vedhu'. Hence skipping..."
fi
echo "cross checking file before script exit.."
ls -lrt $DIR_PATH
exit 0
