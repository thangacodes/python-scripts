import subprocess
from datetime import datetime, timedelta
import sys
existing_key         = sys.argv[1]
new_key              = sys.argv[2]
def check_keypair_age(existing_key, new_key):
    aws_cli_command  = "aws ec2 describe-key-pairs --key-names {} --query 'KeyPairs[*].CreateTime' --output text".format(
        existing_key)
    try:
        key_creation_time_str = subprocess.check_output(
            aws_cli_command, shell=True).strip()
        key_creation_time = datetime.strptime(
            key_creation_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        current_date = datetime.utcnow()
        days_difference = (current_date - key_creation_time).days
        if days_difference > 90:
            print("Key {} has been created more than 90 days ago.".format(existing_key))
            print("Since Keypair {} is created long ago, creating new key".format(
                current_key))
            # Corrected syntax to use subprocess and pass new_key
            subprocess.check_output(
                "aws ec2 create-key-pair --key-name {}".format(new_key), shell=True)
            print("New keypair '{}' created.".format(new_key))
        else:
            print("Key {} has been created within the last 90 days.".format(existing_key))
    except subprocess.CalledProcessError as e:
        print("Error executing AWS CLI command: {}".format(e.output))


# Example usage
check_keypair_age(existing_key, new_key)
