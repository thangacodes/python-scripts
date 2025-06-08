import boto3
import datetime
import time
# Print current time
run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("The script runs at this time:", run_time)
# Variables
aws_region = "ap-south-1"
aws_profile = "vault"
# Create a session using the specified profile
session = boto3.Session(profile_name=aws_profile)
# Create an EC2 client using the session
ec2 = session.client('ec2', region_name=aws_region)
# Describe Elastic IP addresses
describe_ipaddress = ec2.describe_addresses()
print(describe_ipaddress)
time.sleep(2)
# Function to delete unused Elastic IPs
def delete_unused_reserved_ip(ec2_client, addresses):
    for eip in addresses["Addresses"]:
        if "NetworkInterfaceId" not in eip:
            public_ip = eip.get("PublicIp", "Unknown IP")
            print(f"{public_ip} is not associated with any Network Interface ID")
            ec2_client.release_address(AllocationId=eip["AllocationId"])
            print(f"{public_ip} got deleted by the automation")

# Call the function
delete_unused_reserved_ip(ec2, describe_ipaddress)
