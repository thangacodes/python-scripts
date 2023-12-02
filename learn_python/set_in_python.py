numbers = [1,1,2,3,4]
first = set(numbers)
print(first)
second = {1,5}

print(first | second) # | ->denotes union
print(first & second) # & ->denotes intersection
print(first - second) # - ->denotes difference
print(first ^ second) # ^ ->denotes symmatric difference

if 1 in first:
    print("yes")
else:
    print("not exist")
