import boto3
session = boto3.Session(profile_name='vault_admin')
print("")
# List all available services
services = session.get_available_services()
print("Available services:", services)
print("")
# List services with resource APIs
resources = session.get_available_resources()
print("Services with resource APIs:", resources)
print("")
# Example: get default region for session
print("Session default region:", session.region_name)
print("")
# Example: create an S3 resource object using the session
s3_resource = session.resource('s3')
for bucket in s3_resource.buckets.all():
    print(bucket.name)
