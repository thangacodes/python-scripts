import requests
import json
import time

response       = requests.get('https://jsonplaceholder.typicode.com/users/5')
response_json  = json.loads(response.text)
#finding_street = response_json['address']['geo']['lat']
finding_company = response_json['company']['name']
print(f"Company name is: {finding_company}")
time.sleep(2)
finding_company = response_json['phone']
print(f"Phone number is: {finding_company}")
time.sleep(2)
finding_company = response_json['username']
print(f"User name is: {finding_company}")
