import os
import datetime
import subprocess

# Function to check for Terraform files in a specific directory
def files_checking(directory="/Users/eash/Documents/workout/dynamodb"):
    tf_files_found = False
    try:
        file_list = os.listdir(directory)
        print(f"\nChecking directory: {directory}")
        for file in file_list:
            print(f"Available file: {file}")
            if file.endswith(".tf"):
                tf_files_found = True
        if tf_files_found:
            print("Terraform files found")
        else:
            print("No Terraform files found")
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except Exception as e:
        print(f"An error occurred during file check: {e}")
    return tf_files_found

# Function to execute Terraform commands
def tf_exec(directory="/Users/eash/Documents/workout/dynamodb"):
    try:
        os.chdir(directory)  # Change working directory
        user_input = input("\nEnter Terraform commands to run (e.g., init fmt validate plan): ").strip().lower()
        commands = user_input.split()

        valid_commands = {
            "init": ["terraform", "init"],
            "fmt": ["terraform", "fmt"],
            "validate": ["terraform", "validate"],
            "plan": ["terraform", "plan"],
            "apply": ["terraform", "apply", "auto-approve"],
            "destroy": ["terraform", "destroy", "auto-approve"]
        }
        for cmd in commands:
            if cmd in valid_commands:
                print(f"Running terraform {cmd}...")
                subprocess.run(valid_commands[cmd], check=True)
            else:
                print(f"Invalid command skipped: {cmd}")

    except Exception as error:
        print(f"An error occurred during Terraform execution: {error}")
    finally:
        print("Terraform script execution completed.")
# Main execution block
if __name__ == "__main__":
    try:
        exec_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nScript executed at: {exec_time}")
        print("Script to perform Terraform operations\n")
        tf_dir = "/Users/eash/Documents/workout/dynamodb"
        if files_checking(tf_dir):  # Proceed only if Terraform files exist
            tf_exec(tf_dir)
        else:
            print("Exiting: No .tf files found.")
    except Exception as error:
        print(f"Top-level error: {error}")
