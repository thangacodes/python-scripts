import boto3
import subprocess
import os
import time

REGION = "ap-south-1"
TAG_KEY = "Name"
TAG_VALUE_PATTERN = "account-index-dev-app-*"
AWS_PROFILE = "vault_admin"

def get_instances_by_tag(tag_key, tag_value_pattern):
    """Fetch EC2 instances dynamically using a tag filter."""
    # Set AWS_PROFILE environment variable
    os.environ['AWS_PROFILE'] = AWS_PROFILE
    # Initialize the boto3 client
    ec2 = boto3.client("ec2", region_name=REGION)
    
    # Fetch EC2 instances based on tags and state
    response = ec2.describe_instances(
        Filters=[
            {"Name": f"tag:{tag_key}", "Values": [tag_value_pattern]},
            {"Name": "instance-state-name", "Values": ["running", "stopped"]} 
        ]
    )
    # Extract instance IDs from the response
    instance_ids = [
        instance["InstanceId"]
        for reservation in response["Reservations"]
        for instance in reservation["Instances"]
    ]
    return instance_ids

def lambda_handler(event, context):
    instances = get_instances_by_tag(TAG_KEY, TAG_VALUE_PATTERN)
    
    if not instances:
        print("No matching instances found.")
        return
    
    action = event.get("action", "start")
    
    # Set AWS_PROFILE environment variable for the boto3 client
    os.environ['AWS_PROFILE'] = AWS_PROFILE
    ec2 = boto3.client("ec2", region_name=REGION)
    
    if action == "start":
        ec2.start_instances(InstanceIds=instances)
        print(f"Started EC2 instances: {instances}")
    elif action == "stop":
        ec2.stop_instances(InstanceIds=instances)
        print(f"Stopped EC2 instances: {instances}")
    else:
        print(f"Invalid action '{action}' specified. Please use 'start' or 'stop'.")
