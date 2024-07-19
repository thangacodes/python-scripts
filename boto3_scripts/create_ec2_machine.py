import boto3
import time
# Define variables for launching an EC2 instance
KEY_PAIR_NAME = "practical"
AMI_ID = "ami-0ec0e125bb6c6e8ec"
SUBNET_ID = "subnet-e9190a81"
SECURITY_GROUP_ID = "subnet-01a3ea7e1f72afd59"
INSTANCE_TYPE = "t2.micro"
REGION = "ap-south-1"
USER_DATA = '''
#!/bin/bash
sudo yum update -y
sudo yum install -y tree
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl status httpd 
'''

# Establish the boto3 resource and client for EC2
ec2_resource = boto3.resource('ec2', region_name= REGION)
ec2_client = boto3.client('ec2', region_name= REGION)

# Define tags correctly formatted as separate dictionaries
tags = [
    {'Key': 'Name', 'Value': 'Apache-Server'},
    {'Key': 'Owner', 'Value': 'Thangadurai.murugan@example.com'},
    {'Key': 'CreationDate', 'Value': '07/19/2024'},
    {'Key': 'Environment', 'Value': 'Development'}
]

# Launch EC2 instance with specified parameters and tags
instances = ec2_resource.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_PAIR_NAME,
    SecurityGroupIds=[SECURITY_GROUP_ID],
    SubnetId=SUBNET_ID,
    UserData=USER_DATA,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': tags
        }
    ]
)

# Print instance details:-
for instance in instances:
    print(f"EC2 instance {instance.id} has been launched and started")
    print(f"Instance state: {instance.state["Name"]}")
    print(f"Instance AMI: {instance.image.id}")
    print(f"Instance platform: {instance.platform}")
    print(f"Instance type: “{instance.instance_type}")
    print(f"Public IPv4 address: {instance.public_ip_address}")
     print(f"Private IPv4 address: {instance.private_ip_address}")
