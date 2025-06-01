import boto3
import json

# Variable declaration
profile      = "vault_admin"
region       = "ap-south-1"
bucket       = "unni-2025-s3-ddb"
dydb_tables  = ["unni", "thangam"]
files_to_use = ["unni.txt", "thangam.txt"]

# Create boto3 session with profile and region
session = boto3.Session(profile_name=profile, region_name=region)
s3 = session.client('s3')
dynamodb = session.resource('dynamodb')

for file_name in files_to_use:
    table_base = file_name.split(".")[0].lower()
    if table_base not in dydb_tables:
        print(f"Skipping unknown file {file_name}")
        continue
    try:
        print(f"Downloading {file_name} from s3://{bucket}/{file_name}...")
        s3_object = s3.get_object(Bucket=bucket, Key=file_name)
        file_content = s3_object['Body'].read().decode('utf-8')
        data = json.loads(file_content)
    except Exception as e:
        print(f"Error downloading or parsing {file_name}: {e}")
        continue
    users = data.get("users", [])
    if not users:
        print(f"No users found in {file_name}")
        continue
    table = dynamodb.Table(table_base)
    print(f"Inserting users into DynamoDB table: {table_base}")
    for idx, user in enumerate(users, start=1):
        if 'name' not in user:
            print(f"Skipping user without 'name': {user}")
            continue

        user['id'] = str(idx)  # add primary key field if needed

        try:
            table.put_item(Item=user)
            print(f"Inserted user {user['name']} into {table_base}")
        except Exception as error:
            print(f"Failed to insert user {user}: {error}")
