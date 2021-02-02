####### This is the If-else conditional check python Script  ######

city = input("Please enter your city:")
a = "chennai"
b = "ooty"
c = "namakkal"

if (city == "chennai"):
    print("Wow! you are living in the capital of tamil nadu")
    area_name = input("Enter your area name in the city :")
    if (area_name == "velacheri"):
        print("awesome, you are living near to OMR")

elif (city==b):
    print("Oh! you are living in tourist city")
    area_name = input("Enter your area name in the city :")
    if (area_name == "tirpur"):
        print("awesome, you are living near to place of loom")

elif (city==c):
    print("Marvellous! you are living in the clean city")
    area_name = input("Enter your area name in the city :")
    if (area_name == "salem road"):
        print("awesome, you are living towards to road of TKcode")
else: 
    print("You entered city name is not in our database")
