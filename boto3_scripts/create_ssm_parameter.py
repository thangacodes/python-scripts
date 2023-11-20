import boto3
import os
import time
import sys
import json

param_name = "create_string_param.example.com"
region_name = "ap-south-1"

print(f"Stored param name is {param_name}")
print(f"The region is {region_name}")

ssm_client = boto3.client('ssm', region_name=region_name)
new_string_parameter= ssm_client.put_parameter(
        Name = param_name,
        Type = 'String',
        Overwrite = True,
        Tier = 'Standard',
        Value = 'login1-2')

#print(new_string_parameter) // To see entire JSON_PAYLOAD response

print(f"The string parameter '{param_name}' TIER is: {new_string_parameter['Tier']}.")
print(f"The REQUEST_ID is: {new_string_parameter['ResponseMetadata']['RequestId']}.")
print(f"The HTTP_STATUS_CODE is: {new_string_parameter['ResponseMetadata']['HTTPStatusCode']}.")
print(f" CONNECTION_STATE is: {new_string_parameter['ResponseMetadata']['HTTPHeaders']['connection']}.")

