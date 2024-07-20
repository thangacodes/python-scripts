import time
import datetime
import boto3
import rich
from rich import print

def online_shop():
    banner = """
    @@@@  Welcome To Thanga's Online Shopping World  @@@@    
    """
    print(f"[bold blue] {banner} [/bold blue]")  # Print the banner message when the function is called
online_shop()
time.sleep(2)
currentDate = datetime.datetime.today()
date = currentDate.strftime("%m-%d-%Y")
print(f"[bold blue] The Script is executed on: {date} [/bold blue]")
print(f"[bold green] Script is to order fruits in online ... [/bold green]")
fruits = ["apple","banana","grape","blackberry","blueberry","pineapple","strawberry","cherry","watermelon"]
userinput = input("Please enter the fruit that you would like to order: ")
print(f"[bold green] The user entered fruit is: {userinput}[/bold green] ")

if userinput in fruits :
    print(f"[bold yellow] Yes, {userinput} is available and you can good to order it. [/bold yellow] ")
else:
    print(f"[bold red] No, {userinput} is not available at this time. Please retry... [/bold red] ")

## Note: We can create a banner-like message in a Python script using ASCII art or text formatting libraries. 

