import pandas as pd
import time, sys, datetime, logging, subprocess
file_path = "/Users/durai/Downloads/weather-nyc.xlsx"
dataframe = pd.read_excel(file_path)
print(dataframe['max_temp'].max())
time.sleep(1)
print(dataframe['date'][dataframe['max_temp'] >= 90])
