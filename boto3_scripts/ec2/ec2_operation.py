import boto3
import datetime
import time
from botocore.exceptions import ClientError 

# Variable declaration
profile      = "vault_admin"
region       = "ap-south-1"
instance_id  = "i-0bf5218b927310330"

# Execution timestamp
exec_time = datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')
print(f"The Script executed at: {exec_time}")
print("")
time.sleep(2)

# Initialise a session with the given profile and region
session = boto3.Session(profile_name=profile, region_name=region)
ec2     = session.resource('ec2')
print("Will show you all the 'attributes and methods' available on the 'ec2' resource object: ")
print("")
print(dir(ec2))
print("")
print(f"You have hardcoded instance id is: {instance_id}")
instance = ec2.Instance(instance_id)
print(instance)
print("Lists all the 'methods and attributes of the Instance object', which can include: ")
print("")
print(dir(instance))
print("")
print(f"Check the instance that you feed over the input on it's status: ")
current_state = instance.state['Name']
print(f"Current state of the EC2 instance is: {current_state}")
print("")
operation = input("what operation would you like to perform (start/stop/terminate) on the EC2 instance? ").lower()
print(f"User input is: {operation}")
try:
    if operation == "start":
        print(f"You are good to start the EC2 instance and it's id is: {instance_id}")
        instance.start()
        instance.wait_until_running()
        status = instance.state['Name']
        print(f"Instance is successfully started: {instance_id} and it's current state is: {status}")
    elif operation == "stop":
        print(f"You are good to stop the EC2 instance and it's id is: {instance_id}")
        instance.stop()
        instance.wait_until_stopped()
        status = instance.state['Name']
        print(f"Instance is successfully stopped: {instance_id} and it's current state is: {status}")
    elif operation == "terminate":
        print(f"You are good to terminate the EC2 instance and it's id is: {instance_id}")
        instance.terminate()
        instance.wait_until_terminated()
        status = instance.state['Name']
        print(f"Instance is successfully terminated: {instance_id} and it's current state is: {status}")
    else:
        print("You must choose only the 'start' or 'stop' or 'terminate' option.")
except ClientError as e:
    error_code = e.response['Error']['Code']
    error_message = e.response['Error']['Message']
    print(f"ClientError caught: {error_code} - {error_message}")
    print(f"Operation '{operation}' cannot be performed on instance '{instance_id}' in its current state '{current_state}'.")
