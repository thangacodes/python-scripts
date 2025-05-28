import boto3
from botocore.exceptions import ClientError
import logging
import time
try:
    session = boto3.Session(profile_name='vault_admin')
    sts = session.client('sts')
    reply = sts.get_caller_identity()
    print(reply)
    time.sleep(2)
    print("")
    print("Extracting the require data's like arn, account_id, userid, HTTPStatusCode")
    print("")
    print(f"User ID is: {reply['UserId']}")
    print(f"Account ID is: {reply['Account']}")
    print(f"Account ID is: {reply['Arn']}")
    print(f"HTTP Status Code is: {reply['ResponseMetadata']['HTTPStatusCode']}")
except ClientError as error:
    logging.error(f"ClientError: {error}")
except Exception as error:
    logging.error(f"Unexpected error: {error}")


## Note: This script uses the AWS profile named vault_admin, which is explicitly specified during session creation.
