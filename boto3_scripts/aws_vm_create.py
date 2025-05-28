import boto3
import botocore
import time

# Initialize session and EC2 resource
session = boto3.Session(profile_name="vault_admin", region_name="ap-south-1")
ec2 = session.resource('ec2')

# List all EC2 instances
print("Listing existing EC2 instances:")
for instance in ec2.instances.all():
    print(f"Instance ID: {instance.id}, State: {instance.state['Name']}")

# Variables
image_id   = "ami-0af9569868786b23a"
sshkey     = "bastion"
vmspec     = "t2.micro"
sgp        = ["sg-0fb1052b659369aa8"]
subnet_id  = "subnet-01a3ea7e1f72afd59"

# Define tags
tags = [
    {'Key': 'Name', 'Value': 'WebServer'},
    {'Key': 'Environment', 'Value': 'Dev'},
    {'Key': 'Owner', 'Value': 'admin@try-devops.xyz'},
    {'Key': 'PyVersion', 'Value': 'Python 3.13.3'}
]

# Create EC2 instance with Security Group and Tags
print("\nCreating a new EC2 instance with tags...")
instances = ec2.create_instances(
    ImageId=image_id,
    MinCount=1,
    MaxCount=1,
    InstanceType=vmspec,
    KeyName=sshkey,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': tags
        }
    ],
    NetworkInterfaces=[{
    'DeviceIndex': 0,
    'SubnetId': subnet_id,
    'AssociatePublicIpAddress': False,
    'Groups': sgp
    }]
)

# Wait for instance to run
instance = instances[0]
print(f"Instance {instance.id} created, waiting for it to run...")
instance.wait_until_running()

# Reload instance data to get public IP or other updated attributes
instance.load()
print(f"Instance {instance.id} is now running with public IP: {instance.public_ip_address}")
print(f"Instance {instance.id} is now running with public IP: {instance.private_ip_address}")
sg_names = [sg['GroupName'] for sg in instance.security_groups]
print(f"Security Groups attached: {', '.join(sg_names)}")
sg_ids = [sg['GroupId'] for sg in instance.security_groups]
print(f"Security Group IDs associated: {', '.join(sg_ids)}")

#Note: It will create ec2 instance without public ip address.
