import pandas as pd
import time, sys
# Loading the weather report
file_path = "/Users/td/Downloads/weather-nyc.xlsx"
# reading the excel file contents
print(f"finding the maximum temperature first..")
dataframe = pd.read_excel(file_path)
print(dataframe['max_temp'].max())
time.sleep(1)
print(f"finding maximum temperature greater than or equal to 90 on any dates...")
print(dataframe['date'][dataframe['max_temp'] >= 90])