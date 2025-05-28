```bash

Project files and folder structure:

tree
.
├── create_bucket.py
├── create_dydb.py
├── delete_dydb.py
├── inject_data_into_ddb_tables.py
├── file_uploade_s3_bucket.py
├── thangam.txt
├── unni.txt
└── view_scan_tables.py

1 directory, 8 files


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



