import boto3
from datetime import datetime
from rich import print

# Get current date
todaysdate = datetime.today()
date = todaysdate.strftime("%m-%d-%Y")

# Print script execution information
print(f"[bold green] The script is executed on: {date} [/bold green]")
print(f"[bold yellow] Get Information related to AWS EC2 using Python Boto3 [/bold yellow]")

try:
    # Initialize EC2 client
    client = boto3.client("ec2")

    # Describe instances with filter for instances in 'stopped' state
    response = client.describe_instances(
        Filters=[
            {"Name": "instance-state-name", "Values": ["stopped"]}
        ]
    )

    # Print instance details including tags
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            image_id = instance['ImageId']
            public_ip = instance.get('PublicIpAddress', 'N/A')  # Handle cases where PublicIpAddress is None

            # Get instance tags
            tags = instance.get('Tags', [])
            tag_str = ', '.join([f"{tag['Key']}={tag['Value']}" for tag in tags])

            print(f"[bold blue] Instance ID: {instance_id} [/bold blue]")
            print(f"[bold blue] Image ID: {image_id} [/bold blue]")
            print(f"[bold blue] Public IP Address: {public_ip} [/bold blue]")
            print(f"[bold blue] Instance Tags: {tags} [/bold blue]")
            print(f"[bold blue] Instance Tags: {tag_str} [/bold blue]")

except Exception as e:
    print(f"[bold red] Error: {str(e)} [/bold red]")

## Please note:
        #) With this boto3 python script, we can easily find out which instances are powered off in AWS.
        #) To find all the EC2 instances that are powered on and running, simply modify the filter section where key value is running.
        #) When you want to find out all the EC2 instances in a region, you can either use the instance state running or stopped in the key values map 
        #) OR you can use tag key values like environment or costcenter.
