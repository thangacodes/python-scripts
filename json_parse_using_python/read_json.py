import json
import os

print("This python script to read the JSON file contents..\n")

# Use the relative path to the file
file_path = os.path.join(os.path.dirname(__file__), 'json_data.json')
print(f"Would like to see the file_path dir: {file_path}")

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
        # Pretty-print JSON with 2 spaces for indentation
        pretty_json = json.dumps(data, indent=2)
        print('Pretty-printed JSON:', pretty_json)
except FileNotFoundError as e:
    print(f"File not found: {file_path}")
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
