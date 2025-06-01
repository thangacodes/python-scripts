import boto3

## Variable declaration
profile     = "vault_admin"
region      = "ap-south-1"
bucket_name = "unni-2025-s3-ddb"
print("")

session = boto3.Session(profile_name=profile, region_name=region)
bucket = session.resource("s3")
print("")
print(dir(bucket))
print("")

# Create the bucket
bucket.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region })
print("")
print(f"S3 Bucket called '{bucket_name}' is created successfully!")
