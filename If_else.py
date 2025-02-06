####### This is the If-else conditional check python Script  ######

city = input("Please enter your city: ").lower()  # Convert to lowercase for case-insensitive comparison
a = "chennai"
b = "ooty"
c = "namakkal"

if city == a:
    print("Wow! You are living in the capital of Tamil Nadu.")
    area_name = input("Enter your area name in the city:").lower()  # Also handle case insensitivity for area
    if area_name == "velacheri":
        print("Awesome, you are living near OMR.")

elif city == b:
    print("Oh! You are living in a tourist city.")
    area_name = input("Enter your area name in the city:").lower()
    if area_name == "tirpur":
        print("Awesome, you are living near the place of loom.")

elif city == c:
    print("Marvellous! You are living in a clean city.")
    area_name = input("Enter your area name in the city:").lower()
    if area_name == "salem road":
        print("Awesome, you are living near the road to TKcode.")
else:
    print("The city name you entered is not in our database.")
