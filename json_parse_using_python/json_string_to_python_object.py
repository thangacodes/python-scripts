import json
user_info = '{ "name":"Thangadurai","age":34,"birth_place":"Salem","work":"Walmart","designation":"SE-II"}'

## load method - help us to convert json string to Python Object
result = json.loads(user_info)
print(f'The employee name is: {result["name"]}')
print(f'The employee age is: {result["age"]}')
print(f'The employee native_place is: {result["birth_place"]}')
print(f'The employee is working at : {result["work"]}')
print(f'The employee designation is: {result["designation"]}')

##Takeaway: When we use f-string in json string, we should use in the print statment with single_quote(') not double_quote(").
