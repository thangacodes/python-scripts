import boto3

# Variable declaration
profile     = "vault_admin"
region      = "ap-south-1"
table_names = ["unni", "thangam"]

# Create session and DynamoDB resource
session = boto3.Session(profile_name=profile, region_name=region)
dynamodb = session.resource("dynamodb")

for table in table_names:
    print(f"Initiating creation of table called: {table}...")

    tab = dynamodb.create_table(
        TableName=table,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )

    # Wait for the table to be created and active
    print(f"Waiting for table {table} to be created and active...")
    tab.wait_until_exists()
    print(f"Table {table} is now created!\n")
