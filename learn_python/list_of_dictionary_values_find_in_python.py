print(f"This is going to be list of dictionary in python to find out specific application details....\n")
print("###############################################################################################\n")

app_vm_spec = [
    { 
        "Name":"WebServer",
        "Instance_type": "t3.large",
        "Instance_id": "Instance-001",
        "Owner": "web_Ops",
        "Creation_date": "02-12-2023",
        "Cost_centre": "1000453"
     },
    {
        "Name": "Jboss-Server",
        "Instance_type": "t3.xlarge",
        "Instance_id": "Instance-002",
        "Owner": "Web_Ops",
        "Creation_date": "02-12-2023",
        "Cost_centre": "1000453"
    },
    {
        "Name": "DOTNET-APPBACKEND",
        "Instance_type": "t3.2xlarge",
        "Instance_id": "Instance-003",
        "Owner": "MS_DBA",
        "Creation_date": "02-12-2023",
        "Cost_centre": "1000453"
    },
    {
        "Name": "APP-BACKEND",
        "Instance_type": "m5.xlarge",
        "Instance_id": "Instance-004",
        "Owner": "Oracle_DBA",
        "Creation_date": "02-12-2023",
        "Cost_centre": "1000453"
    }
]

print(f"Apache Web details are: \n")
print(f"Apache WebServer Name Is: {app_vm_spec[0]['Name']}")
print(f"Apache WebServer Instance Type Is: {app_vm_spec[0]['Instance_type']}")
print(f"Apache WebServer Instance Id Is: {app_vm_spec[0]['Instance_id']}")
print(f"Project Cost Centre Is: {app_vm_spec[0]['Cost_centre']}\n")
print(f"MSSQL DB details are: \n")
print(f"MSSQL DB Name is: {app_vm_spec[2]['Name']}")
print(f"MSSQL DB Instance Type is: {app_vm_spec[2]['Instance_type']}")
print(f"MSSQL DB Instance Id is: {app_vm_spec[2]['Instance_id']}")
print(f"Project Cost Centre is: {app_vm_spec[2]['Cost_centre']}\n")

print(f"The takeaway from this program is below...\n")

print(f" If you wanted to fetch some details about list of Dictionary in python please use single quote in the square bracket to find out the string value ['key:value']")

## Denotes - "\n" - To give space between two lines in Python, you can use the newline character.

