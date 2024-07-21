import rich
from rich import print

def banner():
    mess = """
    
     @@@@ Hello, Good Morning To All!!! @@@@
    """
    for i in range(5):
        print(f"[bold red] Python Banner message is: {mess} [/bold red]")

# Call the banner function to print the message 10 times
banner()
