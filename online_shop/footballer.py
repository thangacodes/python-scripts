import datetime
import rich
from rich import print

def playerlist():
    bestfb = ["messi","ronaldo","pogba","neimar","benzima","kaka"]
    user_input = input("Who is your favorite footballer: ")
    print(f"[bold yellow] Your favorite footballer is: {user_input}[/bold yellow]")
    if user_input in bestfb:
        print(f"[bold green] You have chosen all the time great player: {user_input} [/bold green] ")
    else:
        print(f"Error.Please enter the correct name")

playerlist()
