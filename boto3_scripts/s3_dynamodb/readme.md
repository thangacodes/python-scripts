```bash

Project files and folder structure:
.
├── create_bucket.py
├── create_dydb.py
├── delete_bucket.py
├── delete_dydb.py
├── file_uploade_s3_bucket.py
├── inject_data_into_ddb_tables.py
├── readme.md
├── step_function_workflow.png
├── thangam.txt
├── unni.txt
└── view_tables.py

0 directories, 11 files

Here's the hierarchy we need to run the Python script on:

1. Run create_bucket.py
2. Run create_dydb.py
3. Run file_uploade_s3_bucket.py
4. Run inject_data_into_ddb_tables.py
5. Run view_scan_tables.py

Once done with the work, please run the DynamoDB table deletion script:

1.delete_dydb.py

Additionally, please run the S3 bucket deletion script to remove the static S3 bucket we created for this work

1. delete_bucket.py

# Note: We can also view or scan the items inserted into DynamoDB tables using the AWS CLI

aws dynamodb scan --table-name unni --region ap-south-1 --profile vault_admin --output json | jq .
aws dynamodb scan --table-name thangam --region ap-south-1 --profile vault_admin --output json | jq .


# Another method is:

We can architect the entire workflow using AWS Lambda and Step Functions to automate and orchestrate the process in a cloud-native,
serverless way.

Step Function Workflow:

[create_bucket] → [create_dydb] → [file_uploade_s3_bucket] 
→ [inject_data_into_ddb_tables] → [view_tables] 
→ [delete_dydb] → [delete_bucket]

Attached is the entire workflow for the Step Functions.




