import boto3
import os
import time
## variables substituting
keyname = 'poc-dev.pem'
region_name = 'ap-south-1'
key_location = '/tmp/'
## printing the variables that we substituted
print(f"The key_name is: {keyname}")
print(f"The region is: {region_name}")
print(f"The keypair location is: {key_location}")
key_path = f"{key_location}{keyname}"
print(f"The keyfile saved location is: {key_path}")
time.sleep(5)

# # Create an EC2 client for the specified region
ec2 = boto3.client('ec2', region_name='ap-south-1')

# # Create a key pair
response = ec2.create_key_pair(KeyName=keyname)

# # Save the private key to a file (you can change the path as needed)
key_path = f"{key_location}{keyname}"
print(f"The private key path is: {key_path}")
with open(key_path, 'wb') as key_file:
    key_file.write(response['KeyMaterial'])
print(f"Keypair {keyname} is created in the {region_name} region. Private key is saved to {key_path}")
