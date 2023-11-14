import time
def birthday(name, age, place):
    print(f"Today is {name} birthday")
    print(f"He is {age} years old")
    print(f"He was born in a place called {place}")
birthday("thangadurai", 34, "chennai")
birthday("Anvika", 1, "Bangalore")
time.sleep(2)

# return = statement used to end a function and send a result back to the caller
def creat_name(first, last):
    first = first.capitalize()
    last  = last.capitalize()
    return first + " " + last
full_name = creat_name("murugan","thangaduri")
print(full_name)
