import boto3
import os
import time
import json
import requests

## variables substituting
keyname = 'ssh_dev.pem'
region_name = 'ap-south-1'
key_location = '/tmp/'

## printing the variables that we substituted
print(f"The key_name is: {keyname}")
print(f"The region is: {region_name}")
print(f"The keypair location is: {key_location}")
key_path = f"{key_location}{keyname}"
print(f"The keyfile saved location is: {key_path}")

## Create an EC2 client for the specified region
ec2 = boto3.client('ec2', region_name=region_name)

## Create a Keypair
response = ec2.create_key_pair(KeyName=keyname)

## Save the private key to a file (you can change the path as needed)
print(f"The private keypath is: {key_path}")
with open(key_path, 'w') as key_file:
    key_file.write(response['KeyMaterial'])

#print(response) // To see entire JSON_PAYLOAD response

print(f"The SSH_KEY is: {response['KeyName']} created.")
print(f"The KEYPAIR_ID is: {response['KeyPairId']}.")
print(f"The REQUEST_ID is: {response['ResponseMetadata']['RequestId']}.")
print(f"The HTTP RESPONSE_CODE is: {response['ResponseMetadata']['HTTPStatusCode']}.")
print(f"The HTTP REQUEST_ID is: {response['ResponseMetadata']['RequestId']}.")
print(f"The KEYPAIR created DATE is: {response['ResponseMetadata']['HTTPHeaders']['date']}.")

