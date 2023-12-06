import boto3
import os
import time
import boto3
import json
import requests
  
## variables substituting
keyname       = "td.pem"
region_name   = "ap-south-1"
key_location  = "/home/ec2-user/td.pem"
param_name    = "demo.aws.example.privatekey"

## Create an EC2 client for the specified region
ec2 = boto3.client('ec2', region_name=region_name)

## Create a Keypair
response = ec2.create_key_pair(KeyName=keyname)

## Save the private key to a file (you can change the path as needed)
# print(key_path)
with open(key_location, 'w') as key_file:
    key_file.write(response['KeyMaterial'])
time.sleep(2)
from os import system 
system("cat /home/ec2-user/td.pem")
print("\n")
print(f"The param: {param_name} to be amend with the latest keypair: {keyname} value")
print("*************** JSON PAYLOAD RESPONSE ***************")
print(f"The KEYPAIR_NAME is: {response['KeyName']} created.")
print(f"The KEYPAIR_ID is: {response['KeyPairId']}.")
print(f"The REQUEST_ID is: {response['ResponseMetadata']['RequestId']}.")
print(f"The CLIENT_HTTP_REQUEST_ID is: {response['ResponseMetadata']['RequestId']}.")
print(f"The CLIENT_HTTP_RESPONSE_CODE is: {response['ResponseMetadata']['HTTPStatusCode']}.")
print(f"The KEYPAIR is: {keyname} CREATED_DATE on: {response['ResponseMetadata']['HTTPHeaders']['date']}.")
exit()
