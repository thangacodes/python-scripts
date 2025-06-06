import os
import boto3
import datetime
import time

print("The script was executed on:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
s3  = boto3.client('s3')
sns = boto3.client('sns')
time.sleep(2)
sns_topic_arn='arn:aws:sns:${region}:${account_number}:${sns_topic_name}
def lambda_handler(event, context):
    #Iterate through s3 events records
    for record in event['Records']:
        # Get the bucket and key of the uploaded file in it
        bucket_name = record['s3']['bucket']['name']
        object_key  = record['s3']['object']['key']
        
        # Extract the file extension
        file_extension = os.path.splitext(object_key)[1]
        # list of ransomware file extensions to watch for
        malware_extensions = ['.exe', '.bat', '.dll', '.ps1', '.zip']
        
        # check if the uploaded file has a ransomware extensions
        if file_extension.lower() in malware_extensions:
            print("Malicious file detected: {}".format(object_key))
            
            # Send email notifications though SNS
            message_body = "Malicious file detected in S3 bucket: {}\nFile: {}".format(bucket_name, object_key)
            subject = "[URGENT] Suspicious File Uploaded to S3 bucket - Action Required"
            sns.publish(TopicArn=sns_topic_arn, Message=message_body, Subject=subject)
            print("Email Notification sent..")
        else:
            print("file '{}' is not associated with malware.".format(object_key))
