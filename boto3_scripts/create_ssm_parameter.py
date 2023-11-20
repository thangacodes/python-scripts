import boto3
import os
import time
import sys
import json
import requests

param_name = "test_string_param_create.example.com"
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
#print(new_string_parameter)

print(f"The string param Tier is: {new_string_parameter['Tier']} and the request_id is: {new_string_parameter['ResponseMetadata']['RequestId']} and http_status_code is: {new_string_parameter['ResponseMetadata']['HTTPStatusCode']} and connection_state is: {new_string_parameter['ResponseMetadata']['HTTPHeaders']['connection']}")


