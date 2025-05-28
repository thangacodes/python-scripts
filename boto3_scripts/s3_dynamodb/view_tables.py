import boto3
import json

profile = "vault_admin"
region = "ap-south-1"
table_names = ["thangam", "unni"]  # list of tables

session = boto3.Session(profile_name=profile, region_name=region)
dynamodb = session.resource('dynamodb')

for table_name in table_names:
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response.get('Items', [])
    
    print(f"Items in {table_name} table:")
    print(json.dumps(items, indent=2))
    print("\n" + "="*21 + "\n")
