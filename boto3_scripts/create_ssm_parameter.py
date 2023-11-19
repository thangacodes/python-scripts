import boto3
import os
import time
import sys
import json

param_name = "cisx.me.example.com"
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
print(f"SSM parameter created with version is: {new_string_parameter['Version']} and Tier is: {new_string_parameter['Tier']}")
