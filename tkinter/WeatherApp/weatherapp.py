import tkinter
from tkinter import scrolledtext, PhotoImage, ttk          #ttk is a class used for drop-down functionality
import os, sys, datetime, subprocess, logging, socket
import requests
import json

# Meta information
sys_hostname = socket.gethostname()
runtime      = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
spath        = os.getcwd()

# Defining Weather function
def func_get_weather():
  print("Send the user input to the function defined in this script, as we've confirmed that it's working")
  city = select_city_dropdown.get()
  # print(f"The user wanted to check the weather in City: {city}")
  api_key = "ENTER YOUR API KEY"
  api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  server_data = requests.get(api_url)
  server_data_json = server_data.json()
  temperature = server_data_json["main"]["temp"]
  feels = server_data_json["main"]["feels_like"]
  temp_min = server_data_json["main"]["temp_min"]
  temp_max = server_data_json["main"]["temp_max"]
  pressure = server_data_json["main"]["pressure"]
  humidity = server_data_json["main"]["humidity"]
  # print(f"You chosen City as: {city} and it's current Temperature is: {temperature}")
  # human_under_data = json.dumps(server_data_json,indent=4)
  # print(human_under_data)
  output_label.config(
    text=f"You have chosen the city of {city}. Its current weather report is as follows: \n"
         f"Temperature: {temperature}°C\n"
         f"Feels_like: {feels}°C\n"
         f"Min.Temperature: {temp_min}°C\n"
         f"Max.Temperature: {temp_max}°C\n"
         f"Pressure: {pressure} hPa\n"
         f"Humidity is: {humidity}%\n",
    font=("Roman", 11, "bold"))
  output_frame.pack()
    
# Tkinter logic starts here
wpage = tkinter.Tk()
wpage.geometry("850x850")
wpage.title("Weather App")
image_path   = "/Users/tmurugan/Desktop/weather-image.png"
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
app_header = tkinter.Label(wpage,text="Weather App",font=("Calibri", 18,"bold"),bg='light grey',fg='black',highlightbackground='blue',highlightthickness=5)
app_header.pack(pady=20)

select_city_label = tkinter.Label(wpage,text="Select City",font=("Calibri", 11, "bold"),bg='light grey',fg='black',highlightbackground='blue',highlightthickness=5)
select_city_label.pack(pady=20)

city_list = ["Bengaluru", "Chennai", "Delhi", "Goa", "Kerala", "Mumbai"]
select_city_dropdown = ttk.Combobox(wpage,values=city_list, font=('Calibri','11','bold'),foreground='black',background='light grey')
select_city_dropdown.pack(pady=20)

get_weather_button = tkinter.Button(wpage, text="Get Weather",font=('Calibri','11','bold'), command=func_get_weather, highlightbackground='blue',highlightthickness=5)
get_weather_button.pack(pady=20)

output_frame = tkinter.Frame(wpage,highlightbackground='red',highlightthickness=5)
output_label = tkinter.Label(output_frame, text="",font=('Calibri', 15))
output_label.pack(pady=10)
wpage.mainloop()






