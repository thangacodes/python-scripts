import time
import datetime
import boto3
import rich
from rich import print

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
