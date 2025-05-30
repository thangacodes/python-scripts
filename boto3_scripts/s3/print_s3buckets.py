import time
# Read the file and print each S3 bucket name
file_path = "/home/ec2-user/only_bucket.txt"

try:
    with open(file_path, 'r') as file:
        for line in file:
            bucket_name = line.strip()
            print(f"Available bucket in the eu-west-region: {bucket_name}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
