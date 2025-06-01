import boto3
import json
# Profile and region declaration
profile = "vault_admin"
region = "ap-south-1"

# Initialize session
session = boto3.Session(profile_name=profile, region_name=region)

# Use the session to get the EC2 resource
ec2 = session.resource("ec2")

# To see returns a list of the attributes and methods
print(dir(ec2)) 
print("")

# List all EC2 instances and their states
for instance in ec2.instances.all():
    print(f"Instance ID: {instance.id}, State: {instance.state['Name']}")
    print("")

# Print instances with private IP
for instance in ec2.instances.all():
    print(f"Instance {instance.id} is now running with private IP: {instance.private_ip_address}")
    print("")

# Print instances and tags in JSON format
for instance in ec2.instances.all():
    tags_json = json.dumps(instance.tags, indent=2) if instance.tags else "No tags"
    print(f"Instance ID: {instance.id}, State: {instance.state['Name']}")
    print(f"Tags:\n{tags_json}\n")
