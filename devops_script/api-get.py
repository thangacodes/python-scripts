import time as t
import datetime as d
import requests
script_execdate = d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Script executed at: {script_execdate}")
endpoint = "https://www.google.com/"
print(f"You are trying to hit: {endpoint}")
t.sleep(2)
try:
    response = requests.get(endpoint)
    if response.status_code == 200:
        print("Request was successful!")
        print(f"Response content (first 200 characters): {response.text[:200]}")
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
