import datetime
import os 
import time
import socket

def print_execution_time():
    print("The script was executed on:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
def print_hostname():
    comp_hostname=socket.gethostname()
    print(f"Script executed on the machine hostname is: {comp_hostname}")
def print_private_ip():
    private_ip = socket.gethostbyname('localhost')
    # Print the private IP address
    print("The private IP address of the MacBook Pro is:", private_ip)
    time.sleep(1)
def print_current_working_dir():
    currentworkingdir=os.getcwd()
    print(f"Current Working Directory: {currentworkingdir}")
    return currentworkingdir
def list_files_in_directory(currentworkingdir):
    listdir_inthe_cwd=os.listdir(currentworkingdir)
    print(f"Get the list of files in the cwd: {listdir_inthe_cwd}")
    for files in listdir_inthe_cwd:
        print(f"File name is: {files}")
def create_directory():
# Create a new directory and check if the directory exists
    user_choice = input("Enter the directory name that you want to create:")
    print(f"User entered input as: {user_choice}")
    if os.path.exists(user_choice):
        print(f"Already there is a folder name called: {user_choice} is exist, hence cannot be created with the same name")
    else:
        try:
        # Create the directory if it does not exist
            os.mkdir(user_choice)
            print(f"Folder {user_choice} creation in progress..")
        except Exception as e:
            print(f"Error: {e}. Please check the current working directory.")
def remove_directory():
# Delete a new directory
# List files and directories in the current working directory before removing
    print("Files and directories in the current working directory: ")
    current_files_and_folders = (os.listdir(os.getcwd()))
    for k in current_files_and_folders:
        print(f"Cross checking available files and folders: {k}")
        time.sleep(3)
    user_input = input("Enter the directory name that you want to remove: ")
    print(f"User entered input as: {user_input}")
    try:
        delete_directory = os.rmdir(user_input)
        print(f"Directory {user_input} is deleted successfully..")
        return delete_directory
    except OSError as e:
        print(f"Error: {e}. The directory does not exist.")
def main():
    print_execution_time()
    print_hostname()
    print_private_ip()
    time.sleep(1)     
    create_directory()
    remove_directory()
if __name__ == "__main__":
    main()
