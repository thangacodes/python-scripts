print("This program is to select the instance_type and provision on AWS cloud...")
user_input = input("please enter the EC2 instance type: ")
print(f"You've entered instance type is {user_input}")
if user_input == "t2.micro":
    print("You selected a free tier EC2 instance type..")
elif user_input == "m5.large":
    print("You've selected memory optimized EC2 instance type..")
else:
    print("Your input is totally wrong as we don't any instance type that you feed here...")
