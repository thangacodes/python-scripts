import datetime
from rich import print
import time
print("[italic green] Quiz program [/italic green]")
print("[italic blue] What is today's date in full???[/italic blue]")
currentDate = datetime.datetime.today()
date = currentDate.strftime("%m-%d-%Y")
print(f"[italic green] Today's date, in number is (MM-DD-YYYY): {date}[/italic green]")
time.sleep(2)
print("[italic green] The quiz program will be starting soon! Please be patient!![/italic green]")
name = input("What is your name:?? ")
print(f"[italic green] My name is: {name}[/italic green] ")
age = input("What is your age:?? ")
print(f"[italic green] My age is: {age}[/italic green] ")
marrige_status = input("Do you married:?? ")
if marrige_status == "no":
    print("[italic green] No, I'm not Married [/italic green] ")
elif marrige_status == "yes":
    print("[italic green] Yes, I'm Married [/italic green]")
else:
    print("[italic green] You entered incorrect answers [/italic green] ")
baby_status = input("Do you have kids:?? ")
if baby_status == "yes":
    print("[italic green] Yes, I do have kids [/italic green] ")
elif baby_status == "no":
    print("[italic green] No, I do not have Kids [/italic green] ")
else:
    print("[italic green] You entered incorrect [/italic green] ")
work = input("Are you currently working?? Say, yes or no: ")
if work == "yes":
    print(f"[bold green] Yes, I am working [/bold green] ")
elif work == "no":
    print(f"[bold green] No, I am not working [/bold green]")
else:
    print(f"[bold green] You entered incorrect answer [/bold green] ")
hobbies = input("What is your hobbies:?? ")
print(f"[italic green] My hobbies are: {hobbies}[/italic green] ")

## Note: Firstly, you need to have this pip should be installed/exist on the windows or linux os.
## pip install colorama ==>colorama to print text in different colors and styles
## pip install rich  ==> rich is another Python library that provides extensive formatting options for terminal output.
