import boto3
import json
import requests

param_name = "create_string_param.example.com"
region_name = "ap-south-1"

print(f"Going to delete the string param {param_name}")

ssm_client = boto3.client("ssm", region_name=region_name)
delete_response = ssm_client.delete_parameter(Name=param_name)

#print(delete_response) //To see entire JSON_PAYLOAD response

print(f"DELETING the string_param is: {param_name}.")
print(f"The REQUEST_ID is: {delete_response['ResponseMetadata']['RequestId']}.")
print(f"The HTTP RESPONSE_CODE is: {delete_response['ResponseMetadata']['HTTPStatusCode']}.")
