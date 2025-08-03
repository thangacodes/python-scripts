import tkinter
from tkinter import PhotoImage, scrolledtext
import os, socket, sys, subprocess, datetime, time, logging

## Meta information about the machine
runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
system_name = socket.gethostname()
script_path = os.getcwd()

# Tkinter script begin..
samplepage = tkinter.Tk()       ## Tk() - is a method.
samplepage.title("Simple GUI by Python")
samplepage.geometry("1024x1024")

# Display system info labels
runtime_label = tkinter.Label(samplepage, text=f"Script runs at: {runtime}", font=('Calibri', 10))
runtime_label.pack(anchor=tkinter.W, padx=10, pady=5)

system_label = tkinter.Label(samplepage, text=f"Machine Hostname Is: {system_name}", font=('Calibri', 10))
system_label.pack(anchor=tkinter.W, padx=10, pady=5)

script_label = tkinter.Label(samplepage, text=f"Script Path: {script_path}", font=('Calibri', 10))
script_label.pack(anchor=tkinter.W, padx=10, pady=5)
print("==========================================================")

## App header
app_header = tkinter.Label(samplepage, font=('Calibri', 11, 'bold'), text="Concept for Scroll down in Tkinter")
app_header.pack()

## Scrolled text
text_scroll1 = scrolledtext.ScrolledText(samplepage, wrap=tkinter.WORD, height=20, state=tkinter.DISABLED, bg='light grey')
text_scroll1.pack(fill=tkinter.BOTH, expand=True)

text_scroll2 = scrolledtext.ScrolledText(samplepage, wrap=tkinter.WORD, height=20)
text_scroll2.pack(fill=tkinter.BOTH, expand=True)


samplepage.mainloop()
