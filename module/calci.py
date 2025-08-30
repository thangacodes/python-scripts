import ops as op

print(f"Module concept in Python..")

# Getting inputs from the user
a = int(input("Please enter number: "))
b = int(input("Please enter number: "))

print("Which operation would you like to perform now: ('addition, subtraction, multiplication')")
chosen_operation = input()
if chosen_operation == "addition":
  c = op.addition(a,b)
  print(f"addition of two number is: {c}")
elif chosen_operation == "subtraction":
  c = op.subtraction(a,b)
  print(f"subtraction of two number is: {c}")
elif chosen_operation == "multiplication":
  c = op.multiplication(a,b)
  print(f"multiplication of two number is: {c}")
else:
  print(f"Invalid operation selected by an user.")
