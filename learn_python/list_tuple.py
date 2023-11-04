import time
print(f"We are going to see the list students in list concept..")
student_names = ["john","peter","ajay","anand","kayal"]
print(type(student_names))
print(len(student_names))
student_names.remove("john")
print(len(student_names))
time.sleep(2)
print("adding a new user to the existing list called student_names...")
student_names.append("Sujay")
print(student_names)
print(f"Newly added user name is:")
time.sleep(2)
print("removing newly added user sujay from the list...")
student_names.remove("Sujay")
print(student_names)
print(f"Removing the newly added user name from the list..")
print(student_names)
for i in student_names:
    print(f"Your good name is: {i}")
time.sleep(2)
print(f"List and tuple append/remove will begin soon....")

