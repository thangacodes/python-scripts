import tkinter
from tkinter import PhotoImage
import datetime
from tkinter import messagebox, ttk
import os
import socket
from tkinter.scrolledtext import ScrolledText
import sys

def OnClick_Submit():
    change      = change_textbox.get().strip()
    executor    = executor_textbox.get().strip()
    branch      = branch_dropdown.get().strip()
    environment = env_dropdown.get().strip()

    if change and executor and branch and environment:
        messagebox.showinfo("Status", "Data Submitted")
        messagebox.showinfo("Captured Data", f"CHANGE_RECORD: {change}\nEXECUTOR: {executor}\nBRANCH: {branch}\nENVIRONMENT: {environment}")
    else:
        messagebox.showwarning("Warning", "Please fill all the fields")

# GUI Setup
iacpage = tkinter.Tk()
iacpage.title("IaC Automation")
iacpage.geometry("750x750")

# Fetch System Meta Data dynamic info (after window creation)
runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
system_name = socket.gethostname()
script_path = os.getcwd()

# Background image setup
image_path = PhotoImage(file="/Users/durai/Desktop/pyac.png")
bg_image = tkinter.Label(iacpage, image=image_path)
bg_image.place(relheight=1, relwidth=1)
bg_image.lower()  # Send background image behind widgets

# Display system info labels
runtime_label = tkinter.Label(iacpage, text=f"Script runs at: {runtime}", font=('Calibri', 10))
runtime_label.pack(anchor=tkinter.W, padx=10, pady=5)

system_label = tkinter.Label(iacpage, text=f"Machine Hostname Is: {system_name}", font=('Calibri', 10))
system_label.pack(anchor=tkinter.W, padx=10, pady=5)

tkinter.Label(iacpage, text=f"Script Path: {script_path}", font=('Calibri', 10)).pack(anchor=tkinter.W, padx=10, pady=5)

# Title label
# tkinter.Label(iacpage, text="Python IaC Automation", font=('Calibri', 10, 'bold')).pack(anchor=tkinter.NE, padx=10)
tkinter.Label(iacpage, text="Python IaC Automation", font=('Calibri', 14, 'bold'),bg="light blue",fg="black",relief="ridge",pady=10).pack(fill="x", padx=5, pady=5)

# Change Details
tkinter.Label(iacpage, text="Enter CR Number (e.g., CHG123456)", font=('Calibri', 10, 'bold')).pack(anchor=tkinter.W, padx=10)
change_textbox = tkinter.Entry(iacpage)
change_textbox.pack(anchor=tkinter.W, padx=10)

# Executor Details
tkinter.Label(iacpage, text="Enter Executor Email (e.g., jack.jill@example.com)", font=('Calibri', 10, 'bold')).pack(anchor=tkinter.W, padx=10)
executor_textbox = tkinter.Entry(iacpage)
executor_textbox.pack(anchor=tkinter.W, padx=10)

# Branch Details
tkinter.Label(iacpage, text="Select the Git Branch", font=('Calibri', 10, 'bold')).pack(anchor=tkinter.W, padx=10)
branches = ["dev", "stage", "master"]
branch_dropdown = ttk.Combobox(iacpage, values=branches, state="readonly")
branch_dropdown.pack(anchor=tkinter.W, padx=10)

# Environment Details
tkinter.Label(iacpage, text="Select the Environment", font=('Calibri', 10, 'bold')).pack(anchor=tkinter.W, padx=10)
environments = ["dev", "stage", "ppe", "prod"]
env_dropdown = ttk.Combobox(iacpage, values=environments, state="readonly")
env_dropdown.pack(anchor=tkinter.W, padx=10)

# Submit Button
submit_button = tkinter.Button(
    iacpage,
    text="Submit",
    command=OnClick_Submit,
    bg="light blue",
    fg="black",
    activebackground="sky blue",
    relief="raised",
    font=('Calibri', 10, 'bold')
)
submit_button.pack(anchor=tkinter.W, padx=10, pady=10)

iacpage.mainloop()
