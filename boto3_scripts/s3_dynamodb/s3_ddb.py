import boto3

# Variable declaration
profile = "vault_admin"
region  = "ap-south-1"
bucket  = "gitops-demo-bucket-tf"

# Files to upload
files_to_upload = ["thangam.txt", "unni.txt"]

# Create a session using the specified profile
session = boto3.Session(profile_name=profile, region_name=region)
s3 = session.client('s3')

# Upload each file
for file_name in files_to_upload:
    try:
        print(f"Uploading {file_name} to s3://{bucket}/{file_name}...")
        s3.upload_file(file_name, bucket, file_name)
        print(f"The file: {file_name} is uploaded successfully.\n")
    except Exception as error:
        print(f"Error uploading {file_name}: {error}")
