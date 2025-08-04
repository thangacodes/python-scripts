import tkinter
from tkinter import scrolledtext, PhotoImage
import os, sys, datetime, subprocess, logging, socket

# Meta information
sys_hostname = socket.gethostname()
runtime      = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
scr_path     = os.getcwd()

# Tkinter logic starts here
wpage = tkinter.Tk()
wpage.geometry("550x650")
wpage.title("Weather App")

## Display Meta Information on WeatherApp GUI
runtime_label = tkinter.Label(wpage, text=f"Script runs at: {runtime}", font=('Calibri', 10))
runtime_label.pack(anchor=tkinter.W, padx=10, pady=5)

system_label = tkinter.Label(wpage, text=f"Machine Hostname Is: {sys_hostname}", font=('Calibri', 10))
system_label.pack(anchor=tkinter.W, padx=10, pady=5)

tkinter.Label(wpage, text=f"Script Path: {scr_path}", font=('Calibri', 10)).pack(anchor=tkinter.W, padx=10, pady=5)


wpage.mainloop()
