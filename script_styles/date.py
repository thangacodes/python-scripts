import datetime
from rich import print
import time

name = input("What is your name:?? ")
print(f"[italic green]My name is: {name}[/italic green] ")
age = input("What is your age:?? ")
print(f"[italic green] My age is: {age}[/italic green] ")
marrige_status = input("Do you married:?? ")
print(f"[italic green] Yes, I do {marrige_status}[/italic green] ")
baby_status = input("Do you have kids:?? ")
print(f"[italic green]Yes, I do have {baby_status} ")
time.sleep(3)
print("[italic blue]What is today's date??[/italic blue]")
currentDate = datetime.datetime.today()
date = currentDate.strftime("%m-%d-%Y")
print(f"[italic green]Today's date, in number is (MM-DD-YYYY): {date}[/italic green]")


## Note: Firstly, you need to have this pip should be installed/exist on the windows or linux os.
## python.exe -m pip install --upgrade pip   //upgraind the old package installer for python
## pip install colorama ==>colorama to print text in different colors and styles
## pip install rich  ==> rich is another Python library that provides extensive formatting options for terminal output.


