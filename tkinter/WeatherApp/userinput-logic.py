letters = ["a","b","c","d","e","f"]
userinput = input("please enter the english letters that you like: ")
print(f"User entered the values are: {userinput}")
if any (x in userinput.lower() for x in letters):
  print("letters present")
else:
  print("letters not present")
