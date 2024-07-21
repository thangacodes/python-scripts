import boto3
from rich import print
from datetime import datetime
import time

# Get Current date
todaysdate = datetime.today()
print(f" [bold red] The script is executed on: {todaysdate} [/bold red] ")
date = todaysdate.strftime("%m-%d-%Y")
print(f" [bold blue] The script is executed on date: {date} [/bold blue] ")


# Create an EC2 resource object using the session
ec2 = boto3.resource(service_name="ec2",region_name="ap-south-1")
for each in ec2.volumes.all():
    print(f" [bold yellow] The ebs volume of all in one form: {each.id, each.state, each.size, each.encrypted, each.tags} [/bold yellow]")
    time.sleep(2)
    print(f"Going to show us each value separately....")
    print(f"[italic green] Volume ID: {each.id} [/italic green]")
    print(f"[italic green] Volume Size: {each.size} GiB [/italic green]")
    print(f"[italic green] Volume State: {each.state} [/italic green]")
    print(f"[italic green] Volume Type: {each.volume_type} [/italic green]")
    print(f"[italic green] Attachments: {each.attachments} [/italic green]")
    print(f"[italic green] Snapshot ID: {each.snapshot_id} [/italic green]")
    print(f"[italic green] Availability Zone: {each.availability_zone} [/italic green]")
    print(f"[italic green] Encrypted: {each.encrypted} [/italic green]")

## Please note:
        #) It is intended to find out all the information related to ECS instance volumes.
        #) 
