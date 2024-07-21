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
    ],
)

for i in response['Reservations']:
    for instance in i['Instances']:
        print(f"instance[InstanceId]")
        print(f"instance[ImageId]")
