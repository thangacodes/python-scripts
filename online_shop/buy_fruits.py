import time
import datetime
from rich import print

def online_shop():
    banner = """
    @@@@  Welcome To Thanga's Online Shopping World  @@@@    
    """
    print(f"[bold blue] {banner} [/bold blue]")  # Print the banner message when the function is called
    time.sleep(2)  # Delay added here
    available_fruits()
    script_begin()  # Call script_begin function after the banner is printed

def available_fruits():
    stock = ["apple", "banana", "grape", "blackberry", "blueberry", "pineapple", "strawberry", "cherry", "watermelon", "orange"]
    print("[bold green] Available fruits in our shop: [/bold green]")
    for fruit in stock:
        print(f"[bold green] - {fruit} [/bold green]")

def script_begin():
    currentDate = datetime.datetime.today()
    date = currentDate.strftime("%m-%d-%Y")
    print(f"[bold blue] The Script is executed on: {date} [/bold blue]")
    print(f"[bold green] Script is used to order fruits online... [/bold green]")

    fruits = ["apple", "banana", "grape", "blackberry", "blueberry", "pineapple", "strawberry", "cherry", "watermelon", "orange"]
    userinput = input("Please enter the fruit that you would like to order: ").strip().lower()

    if userinput in fruits:
        print(f"[bold yellow] Yes, {userinput} is available and good to order it. [/bold yellow]")
    else:
        print(f"[bold red] Sorry, {userinput} is not available in our shop. Please choose from the available fruits listed above [/bold red]")

# Call the main function to start the script
online_shop()
