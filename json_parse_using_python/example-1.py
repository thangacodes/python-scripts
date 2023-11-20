import requests
import json
import time

response       = requests.get('https://jsonplaceholder.typicode.com/users/5')
response_json  = json.loads(response.text)
#finding_street = response_json['address']['geo']['lat']
finding_company = response_json['company']['name']
print(finding_company)
