import datetime
from rich import print
print("[italic blue]What is today's date??[/italic blue]")
print("[italic yellow]The answer is below:[/italic yellow]")
currentDate=datetime.datetime.today()
date=currentDate.strftime("%d-%m-%Y")
print(f"[italic green]Today's date, in number is (MM-DD-YYYY): {date}[/italic green]")


## Note: Firstly, you need to have this pip should be installed/exist on the windows or linux os.
## python.exe -m pip install --upgrade pip   //upgraind the old package installer for python
## pip install colorama ==>colorama to print text in different colors and styles
## pip install rich  ==> rich is another Python library that provides extensive formatting options for terminal output.


