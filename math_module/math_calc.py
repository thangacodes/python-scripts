import time as t
import math as m
from math import pi as p, sin as s, cos as c

print("India is my country..")
print(".....")
user_input = input("Please enter the name in (string): ")
print(f"My name is: {user_input}")
# Checking input datatype
print(f"user entered input datatype is:", type(user_input))

# Convert input to integer after getting the input
int_number = int(input("Please enter the integer number: "))
print(f"User entered number is: {int_number}")
# Checking input datatype
print(f"user entered input datatype is:",type(int_number))
# Convert input to float after getting the input
float_number = float(input("Please enter the float number: "))
print(f"User entered number is: {float_number}")
# Checking input datatype
print(f"user entered input datatype is:",type(float_number))
print(".....")
t.sleep(3)
def kootal():
    # Get inputs from the user and convert to integers
    a = int(input("Please enter number 1: "))
    b = int(input("Please enter number 2: "))
    return a + b

def kalithal():
    # Get inputs from the user and convert to integers
    a = int(input("Please enter number 1: "))
    b = int(input("Please enter number 2: "))
    return a - b

def vaguthal():
    # Get inputs from the user and convert to integers
    a = int(input("Please enter number 1: "))
    b = int(input("Please enter number 2: "))
    return a / b  # Modulus operation (remainder)

# Call the Python functions to perform addition, subtraction, and modulus
addition = kootal()
subtraction = kalithal()
modulus = vaguthal()

# Results
print(f"Addition of two values is: {addition}")
print(f"Subtraction of two values is: {subtraction}")
print(f"Modulus (remainder) of two values is: {modulus}")
