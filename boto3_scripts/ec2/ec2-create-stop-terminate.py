# Functions like create, stop, start, terminate

import boto3
import datetime
import time
from botocore.exceptions import ClientError 

# Variable declaration
profile      = "vault_admin"
region       = "ap-south-1"
instance_id  = "i-00b3xxxxxxxxxxxx"
ami          = "ami-0af9569868786b23a"
sgp          = ["sg-0fb1052b65xxxxxx"]
pvtsubnet    = "subnet-01a3ea7e1f72afd59"

# Execution timestamp
exec_time = datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')
print(f"The Script executed at: {exec_time}")
time.sleep(2)

# Initialise a session with the given profile and region
session = boto3.Session(profile_name=profile, region_name=region)
ec2 = session.resource('ec2')

option = input("What operation would you like to perform (create/stop/start/terminate)? ").lower()
print(f"User chosen option: {option}")

try:
    if option == "create":
        print("Creating an EC2 instance...")
        instances = ec2.create_instances(
            ImageId=ami,
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            SecurityGroupIds=sgp,
            SubnetId=pvtsubnet
        )
        instance = instances[0]
        print(f"Created instance ID: {instance.id}")
        print("Waiting for instance to enter 'running' state...")
        instance.wait_until_running()
        print("Instance is now running.")
        
    elif option == "stop":
        print(f"Stopping instance {instance_id}...")
        instance = ec2.Instance(instance_id)
        response = instance.stop()
        print(f"Stop response: {response}")
        print("Waiting for instance to stop...")
        instance.wait_until_stopped()
        print("Instance is now stopped.")

    elif option == "start":
        print(f"Starting instance {instance_id}...")
        instance = ec2.Instance(instance_id)
        response = instance.start()
        print(f"Start response: {response}")
        print("Waiting for instance to run...")
        instance.wait_until_running()
        print("Instance is now running.")

    elif option == "terminate":
        print(f"Terminating instance {instance_id}...")
        instance = ec2.Instance(instance_id)
        response = instance.terminate()
        print(f"Terminate response: {response}")
        print("Waiting for instance to terminate...")
        instance.wait_until_terminated()
        print("Instance has been terminated.")

    else:
        print("Invalid option chosen. Please choose from create/stop/start/terminate.")

except ClientError as error:
    print(f"An error occurred: {error}")
