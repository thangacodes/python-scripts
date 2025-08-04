import tkinter
from tkinter import scrolledtext, PhotoImage, ttk          #ttk is a class used for drop-down functionality
import os, sys, datetime, subprocess, logging, socket

# Meta information
sys_hostname = socket.gethostname()
runtime      = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
spath        = os.getcwd()

# Defining Weather function
def func_get_weather():
  print("Send the user input to the function defined in this script, as we've confirmed that it's working")
  city=select_city_dropdown.get()
  print(f"The user wanted to check the weather in City: {city}")
  # api_key = ""
  # api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"

# Tkinter logic starts here
wpage = tkinter.Tk()
wpage.geometry("550x650")
wpage.title("Weather App")
image_path   = "/Users/durai/Desktop/weather-image.png"
bg_image     = PhotoImage(file=image_path)
set_bg_image = tkinter.Label(wpage,image=bg_image)
set_bg_image.place(relheight=1,relwidth=1)


## Display Meta Information on WeatherApp GUI
runtime_label = tkinter.Label(wpage, text=f"Script runs at: {runtime}", font=('Calibri', 10))
runtime_label.pack(anchor=tkinter.W, padx=10, pady=5)

system_label = tkinter.Label(wpage, text=f"Hostname Is: {sys_hostname}", font=('Calibri', 10))
system_label.pack(anchor=tkinter.W, padx=10, pady=5)

tkinter.Label(wpage, text=f"Path: {spath}", font=('Calibri', 10)).pack(anchor=tkinter.W, padx=10, pady=5)

# Header design
app_header = tkinter.Label(wpage,text="Weather App",font=("Calibri", 18,"bold"),bg='light grey',fg='blue')
app_header.pack(pady=20)

select_city_label = tkinter.Label(wpage,text="Select City",font=("Calibri", 11, "bold"),bg='light grey',fg='black')
select_city_label.pack(pady=20)

city_list = ["Bengaluru", "Chennai", "Delhi", "Goa", "Kerala", "Mumbai"]
select_city_dropdown = ttk.Combobox(wpage,values=city_list, font=('Calibri','11','bold'))
select_city_dropdown.pack(pady=20)

get_weather_button = tkinter.Button(wpage, text="Get Weather",font=('Calibri','11','bold'), command=func_get_weather)
get_weather_button.pack(pady=20)

wpage.mainloop()
