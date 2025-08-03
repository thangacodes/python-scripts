from tkinter import *
from tkinter import scrolledtext

# def FuncSendText():
#     UserInput = InputText.get("1.0", END).strip().lower()
#     DisplayText.config(state=NORMAL)
#     DisplayText.insert(END, "You: " + UserInput + "\n")
#     if "hello" in UserInput or "hey" in UserInput:
#       DisplayText.insert(END, "Bot: I am doing good, thanks for asking!\n")
#     elif "need your help" in UserInput:
#       DisplayText.insert(END, "Bot: How can I help you today?\n")
#     elif "help" in UserInput or "assist" in UserInput or "assistance" in UserInput:
#         DisplayText.insert(END, "Bot: How can I help you today?\n")
#     else:
#         DisplayText.insert(END, "Bot: Please specify the exact issue that you're facing..\n")
#     DisplayText.config(state=DISABLED)
#     InputText.delete("1.0", END)

def FuncSendText():
    UserInput = InputText.get("1.0", END).strip().lower()
    DisplayText.config(state=NORMAL)
    DisplayText.insert(END, "Bot: Welcome to IT HelpDesk. How can I help you?\n")
    DisplayText.insert(END, "You: " + UserInput + "\n")
    # Show keyword suggestions if input is empty or contains 'help'
    if UserInput == "" or UserInput == "help":
        DisplayText.insert(END, "Bot: Please select from the following issues:\n")
        DisplayText.insert(END, "- password locked\n")
        DisplayText.insert(END, "- corp account issue\n")
        DisplayText.insert(END, "- os booting issue\n")
        DisplayText.insert(END, "- wifi-issue\n")
        DisplayText.insert(END, "- laptop hardware peripherals issue\n")
    # Greeting response
    elif "hello" in UserInput or "hey" in UserInput:
        DisplayText.insert(END, "Bot: I am doing good, thanks for asking!\n")
    # Help-related responses
    elif "need your help" in UserInput or "assist" in UserInput or "assistance" in UserInput:
        DisplayText.insert(END, "Bot: How can I help you today?\n")
    # Keyword-specific responses
    elif "password locked" in UserInput:
        DisplayText.insert(END, "Bot: Please contact IT support to unlock your password or reset via the self-service portal.\n")
    elif "corp account issue" in UserInput:
        DisplayText.insert(END, "Bot: Kindly check your credentials and network access. If it persists, reach out to corporate IT.\n")
    elif "os booting issue" in UserInput:
        DisplayText.insert(END, "Bot: Please try rebooting in safe mode. If that fails, connect to Local IT Support for OS recovery.\n")
    elif "wifi-issue" in UserInput:
        DisplayText.insert(END, "Bot: Try forgetting the network and reconnecting. If it's still down, check with the network admin.\n")
    elif "laptop hardware peripherals issue" in UserInput:
        DisplayText.insert(END, "Bot: Please verify cables and device connections. If faulty, raise a hardware replacement request.\n")
    # Fallback
    else:
        DisplayText.insert(END, "Bot: Please specify the exact issue or type 'help' to see options.\n")
    DisplayText.config(state=DISABLED)
    InputText.delete("1.0", END)

# Logic begins
botpage = Tk()
botpage.title("My First Python Bot")
botpage.geometry("550x550")

# Title label inside the window with styling
bot_label = Label(botpage, text="ChatBot Via Python", font=('Calibri', 14, 'bold'))
bot_label.pack(pady=10)

## App Header section
AppHeader = Label(botpage, text="First ChatBot", bg="dark blue", fg="white", font=("Calibri", 14, "bold"))
AppHeader.pack(fill=X, expand=True)

DisplayText = scrolledtext.ScrolledText(botpage,state=DISABLED,wrap=WORD)
DisplayText.pack(fill=BOTH,expand=True)

InputText = scrolledtext.ScrolledText(botpage,wrap=WORD,height=3)
InputText.pack(fill=BOTH,expand=True)

SendButton = Button(botpage, text="Send", font=("Calibri", 10),command=FuncSendText)
SendButton.pack()

botpage.mainloop()
