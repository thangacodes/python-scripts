import time as t
import math as m
from math import pi as p, sin as s, cos as c

print("........")
script_name = "math is a standard Python module that provides mathematical functions and constants"
print()
print(f"{script_name}")
print("")
print("the π (pi) value is:", p)

user_input = float(input("Enter the number that you wanted to check sin and cos theta: "))
print(f"User entered the number is: {user_input}")
print("the value of sin(theta) is:", s(user_input))
print("the value of cos(theta) is:", c(user_input))

t.sleep(2)
print("to check math module functions and constants..")
print(dir(m))
