import tkinter
from tkinter import *
from tkinter import scrolledtext
import os, sys, subprocess, datetime, logging

## Initialize greeted flag
greeted = False

def FuncSendText():
    global greeted
    UserInput = InputText.get("1.0", END).strip().lower()
    DisplayText.config(state=NORMAL)
    # Show welcome message only once
    if not greeted:
        DisplayText.insert(END, "Bot: Welcome to IT HelpDesk. How can I help you?\n", "bot")
        greeted = True
    DisplayText.insert(END, "You: " + UserInput + "\n", "user")
    # Show keyword suggestions if input is empty or contains 'help'
    if UserInput == "" or UserInput == "help":
        DisplayText.insert(END, "Bot: Please select from the following issues:\n", "bot")
        DisplayText.insert(END, "- password locked\n", "bot")
        DisplayText.insert(END, "- corp account issue\n", "bot")
        DisplayText.insert(END, "- os booting issue\n", "bot")
        DisplayText.insert(END, "- wifi-issue\n", "bot")
        DisplayText.insert(END, "- laptop hardware peripherals issue\n", "bot")
    # Greeting response
    elif "hello" in UserInput or "hey" in UserInput:
        DisplayText.insert(END, "Bot: I am doing good, thanks for asking!\n", "bot")
    # Help-related responses
    elif "need your help" in UserInput or "assist" in UserInput or "assistance" in UserInput:
        DisplayText.insert(END, "Bot: How can I help you today?\n", "bot")
    # Keyword-specific responses
    elif "password locked" in UserInput:
        DisplayText.insert(END, "Bot: Please contact IT support to unlock your password or reset via the self-service portal.\n", "bot")
    elif "corp account issue" in UserInput:
        DisplayText.insert(END, "Bot: Kindly check your credentials and network access. If it persists, reach out to corporate IT.\n", "bot")
    elif "os booting issue" in UserInput:
        DisplayText.insert(END, "Bot: Please try rebooting in safe mode. If that fails, connect to Local IT Support for OS recovery.\n", "bot")
    elif "wifi-issue" in UserInput:
        DisplayText.insert(END, "Bot: Try forgetting the network and reconnecting. If it's still down, check with the network admin.\n", "bot")
    elif "laptop hardware peripherals issue" in UserInput:
        DisplayText.insert(END, "Bot: Please verify cables and device connections. If faulty, raise a hardware replacement request.\n", "bot")
    # Fallback
    else:
        DisplayText.insert(END, "Bot: Please specify the exact issue or type 'help' to see options.\n", "bot")
    DisplayText.config(state=DISABLED)
    InputText.delete("1.0", END)

# Logic begins
botpage = Tk()
botpage.title("HelpDesk ChatBot")
botpage.geometry("550x550")

# Title label inside the window with styling
bot_label = Label(botpage, text="HelpDesk ChatBot", font=('Calibri', 14, 'bold'))
bot_label.pack(pady=10)

## App Header section
AppHeader = Label(botpage, text="Welcome to IT HelpDesk", bg="dark blue", fg="white", font=("Calibri", 14, "bold"))
AppHeader.pack(fill=X, expand=True)

DisplayText = scrolledtext.ScrolledText(botpage,state=DISABLED,wrap=WORD)
DisplayText.pack(fill=BOTH,expand=True)

DisplayText.tag_config("user", foreground="Dark Blue")
DisplayText.tag_config("bot", foreground="Dark Green")

InputText = scrolledtext.ScrolledText(botpage,wrap=WORD,height=3)
InputText.pack(fill=BOTH,expand=True)

SendButton = Button(botpage, text="Send", font=("Calibri", 10),command=FuncSendText)
SendButton.pack()

botpage.mainloop()
