import boto3
import json

# Profile and region declaration
profile = "vault_admin"
region = "ap-south-1"

# Initialize session
session = boto3.Session(profile_name=profile, region_name=region)

# Use the session to get the EC2 resource
ec2 = session.resource("ec2")

print(dir(ec2)) 

# List all EC2 instances and their states
for instance in ec2.instances.all():
    print(f"Instance ID: {instance.id}, State: {instance.state['Name']}")

# Print instances with private IP
for instance in ec2.instances.all():
    print(f"Instance {instance.id} is now running with private IP: {instance.private_ip_address}")

# Print instances and tags in JSON format
for instance in ec2.instances.all():
    tags_json = json.dumps(instance.tags, indent=4) if instance.tags else "No tags"
    print(f"Instance ID: {instance.id}, State: {instance.state['Name']}")
    print(f"Tags:\n{tags_json}\n")

# Terminating the running ec2 instances with the tag name of Environment= "Dev"

confirm = input("Are you sure you want to terminate all running instances with Environment=Dev? (yes/no): ")
if confirm.lower() == "yes":
    filters = [
    {'Name': 'instance-state-name', 'Values': ['running']},
    {'Name': 'tag:Environment', 'Values': ['Dev']}
]

for instance in ec2.instances.filter(Filters=filters):
    print(f"Terminating instance {instance.id} with Environment=Dev tag.")
    instance.terminate()
    print(f"Waiting for instance {instance.id} to terminate...")
    instance.wait_until_terminated()
    print("")
    print(f"Instance {instance.id} has been terminated.")
else:
    print("Termination aborted.")
