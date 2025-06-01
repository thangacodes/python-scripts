
import boto3
import requests
import json
import os
import time
## Variables substitutions
bucket_name = "thangadurai-demo-bucket-tf-123"
region      = "ap-south-1"
print(f"The bucket that we are going to create is: {bucket_name}")
print(f"The bucket that we are going to create in mumbai region: {region}")
client      = boto3.client('s3')
response    = client.create_bucket(
    CreateBucketConfiguration={
        'LocationConstraint': region
    },
    Bucket  = bucket_name )
print(response)
time.sleep(2)
print("\n")
print(f"BEAUTIFYING THE JSON PAYLOAD RESPONSE in our way...")
print(f"The S3_LOCATION ENDPOINT is: {response['Location']}")
print(f"The HTTPSTATUSCODE IS: {response['ResponseMetadata']['HTTPStatusCode']}")
print(f"The BUCKET {bucket_name} CREATED_ON: {response['ResponseMetadata']['HTTPHeaders']['date']}")
print("\n")
time.sleep(3)
response = client.get_bucket_acl(
    Bucket = bucket_name
)
print(response)
print("\n")
print(f"PAYLOAD JSON RESPONSE FOR GET_BUCKET_ACL...")
print(f"The S3_BUCKET_ACL IS: {response['Permission']}")