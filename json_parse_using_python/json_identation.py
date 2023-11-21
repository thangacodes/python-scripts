import json
user = { "name": "Thangadurai", "age": 34, "place":"Bangalore"}

data = json.dumps(user, indent=3)
print(data)
