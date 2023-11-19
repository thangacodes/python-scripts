print(f"Going to delete the string param {param_name}")
import boto3
param_name = "cisx.me.example.com"
region_name = "ap-south-1"

ssm_client = boto3.client("ssm", region_name=region_name)
delete_response = ssm_client.delete_parameter(Name=param_name)
print(delete_response)

