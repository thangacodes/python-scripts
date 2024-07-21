import boto3
import time
import rich
from datetime import datetime
from rich import print


todaysdate = datetime.today()
date = todaysdate.strftime("%m-%d-%Y")
print(f"[bold green] The script is executed on: {date}[/bold green]")
print(f"[bold yellow] Get Information related to AWS EC2 using Python Boto3 [/bold yellow]")

client = boto3.client("ec2")
response = client.describe_instances(
    Filters=[
        {
            "Name": "instance-state-name",
            "Values": [
                'stopped',
            ]
        },
        {
            "Name": "tag:Environment",
            "Values": [
                'Development',
            ]
        },
    ],
)

for i in response['Reservations']:
    for instance in i['Instances']:
        instance_id = instance['InstanceId']
        image_id = instance['ImageId']
        public_ip = instance.get('PublicIpAddress')

        print(f"Instance ID: {instance_id}")
        print(f"Image ID: {image_id}")
        print(f"Public IP Address: {public_ip}")

## Please note:
        #) With this boto3 python script, we can easily find out which instances are powered off in AWS.
        #) To find all the EC2 instances that are powered on and running, simply modify the filter section where key value is running.
        #) When you want to find out all the EC2 instances in a region, you can either use the instance state running or stopped in the key values map 
        #) OR you can use tag key values like environment or costcenter.
