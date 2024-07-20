import time
import datetime
import rich
from rich import print


def online_shop():
    banner = """
    @@@@  Welcome To Thanga's Online Shopping World  @@@@    
    """
    print(f"[bold blue] {banner} [/bold blue]")  # Print the banner message when the function is called
    time.sleep(2)  # Delay added here

    script_begin()  # Call script_begin function after the banner is printed

def script_begin():
    currentDate = datetime.datetime.today()
    date = currentDate.strftime("%m-%d-%Y")
    print(f"[bold blue] The Script is executed on: {date} [/bold blue]")
    print(f"[bold green] Script is to order fruits in online ... [/bold green]")

    fruits = ["apple", "banana", "grape", "blackberry", "blueberry", "pineapple", "strawberry", "cherry", "watermelon"]
    userinput = input("Please enter the fruit that you would like to order: ")
    print(f"[bold green] The user entered fruit is: {userinput}[/bold green] ")

    if userinput in fruits:
        print(f"[bold yellow] Yes, {userinput} is available and you can proceed to order it. [/bold yellow] ")
    else:
        print(f"[bold red] No, {userinput} is not a fruit and it's not available at this time. Please retry... [/bold red] ")

online_shop()
