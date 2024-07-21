import boto3
from rich import print
from datetime import datetime
import time

# Get Current date
todaysdate = datetime.today()
print(f" [bold red] The script is executed on: {todaysdate} [/bold red] ")
date = todaysdate.strftime("%m-%d-%Y")
print(f" [bold blue] The script is executed on date: {date} [/bold blue] ")

# Initialize a new session with specified region
session = boto3.Session(region_name='ap-south-1')

# Create an EC2 resource object using the session
ec2 = session.resource('ec2')

# Retrieve all volumes in the region
volume_iterate = ec2.volumes.all()

# Iterate over volumes and print their details
for volume in volume_iterate:
    print(f"[italic green] Volume ID: {volume.id} [/italic green]")
    print(f"[italic green] Volume Size: {volume.size} GiB [/italic green]")
    print(f"[italic green] Volume State: {volume.state} [/italic green]")
    print(f"[italic green] Volume Type: {volume.volume_type} [/italic green]")
    print(f"[italic green] Attachments: {volume.attachments} [/italic green]")
    print(f"[italic green] Snapshot ID: {volume.snapshot_id} [/italic green]")
    print(f"[italic green] Availability Zone: {volume.availability_zone} [/italic green]")
    print(f"[italic green] Encrypted: {volume.encrypted} [/italic green]")

## Please note:
        #) It is intended to find out all the information related to ECS instance volumes.
        #) 
