import json
print("This python script to read the JSON file contents..")
print("\n")
with open('json_data.json', 'r') as file:
    try:
        data = json.load(file)
        # Pretty-print JSON with 2 spaces for indentation
        pretty_json = json.dumps(data, indent=2)
        print('Pretty-printed JSON:', pretty_json)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
