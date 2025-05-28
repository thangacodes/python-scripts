import boto3
from botocore.exceptions import ClientError
import logging
try:
    session = boto3.Session(profile_name='vault_admin')
    sts = session.client('sts')
    reply = sts.get_caller_identity()
    print(reply)
except ClientError as error:
    logging.error(f"ClientError: {error}")
except Exception as error:
    logging.error(f"Unexpected error: {error}")
