import boto3

# Variables
profile = "vault_admin"
region = "ap-south-1"
bucket_name = "unni-2025-s3-ddb"

# Create session and resource
session = boto3.Session(profile_name=profile, region_name=region)
s3 = session.resource("s3")
bucket = s3.Bucket(bucket_name)

# Delete all objects in the bucket first
print(f"Deleting all objects in bucket '{bucket_name}'...")
bucket.objects.delete()

# Now delete the bucket
print(f"Deleting the bucket '{bucket_name}'...")
bucket.delete()
print("")
print(f"S3 Bucket '{bucket_name}' has been deleted successfully!")
