import boto3
import time
import datetime
import rich
from rich import print

# Print the script execution date
currentDate = datetime.datetime.today()
date = currentDate.strftime("%m-%d-%Y")
print(f"[bold red]The Script gets executed on: {date}[/bold red]")

# Variable declaration for launching EC2 machine
AMI = "ami-0ec0e125bb6c6e8ec"
INSTANCETYPE = "t2.micro"
KEYPAIR = "practical"
SGP = "sg-0fb1052b659369aa8"
SUBNET = "subnet-01a3ea7e1f72afd59"
USER_DATA = '''
#!/bin/bash
sudo yum update -y
sudo yum install -y tree
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl status httpd 
'''
# Define tags correctly formatted as separate dictionaries
tags = [
    {'Key': 'Name', 'Value': 'Apache-Server'},
    {'Key': 'Owner', 'Value': 'Thangadurai.murugan@example.com'},
    {'Key': 'CreationDate', 'Value': '07/19/2024'},
    {'Key': 'Environment', 'Value': 'Development'}
]

client = boto3.client('ec2')
response = client.run_instances(
    ImageId=AMI,
    InstanceType=INSTANCETYPE,
    KeyName=KEYPAIR,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[SGP],
    SubnetId=SUBNET,
    UserData=USER_DATA,
    TagSpecifications=[
    {
        'ResourceType': 'instance',
        'Tags': tags
    }
]
)
time.sleep(60)
for instance in response['Instances']:
    print(f"[bold red]    #################################### [/bold red]")
    print(f"[bold blue]   #################################### [/bold blue]")
    print(f"[bold yellow] #################################### [/bold yellow]")
    print(f"[bold green]The Instance Id is: {instance['InstanceId']}[/bold green]")
    print(f"[bold green]The Launch Time is: {instance['LaunchTime']}[/bold green]")
    print(f"[bold green]The Image Id is: {instance['ImageId']}[/bold green]")
    print(f"[bold green]The Instance Type is: {instance['InstanceType']}[/bold green]")
    print(f"[bold green]The Private IP Address is: {instance['PrivateIpAddress']}[/bold green]")

# Please note: In order to avoid costs, I used the default private subnet in Mumbai region to create and associate the private subnet. If you want to run user-data scripts on the remote machine, it needs to be on the default public subnet or on the subnet which has the route to the Internet Gateway.
