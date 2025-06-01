import boto3

# Variable declaration
profile     = "vault_admin"
region      = "ap-south-1"
table_names = ["unni", "thangam"]

# Create session and DynamoDB resource
session = boto3.Session(profile_name=profile, region_name=region)
dynamodb = session.resource("dynamodb")

for table in table_names:
    print(f"Initiating deletion of table called: {table}...")
    table_obj = dynamodb.Table(table)

    try:
        response = table_obj.delete()
        print(f"Waiting for table {table} to be deleted...")
        table_obj.wait_until_not_exists()
        print(f"Table {table} is now deleted!\n")
    except Exception as e:
        print(f"Error deleting table {table}: {e}\n")

