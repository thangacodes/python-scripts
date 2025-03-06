import os
import time as t
import datetime as d
script_execdate = d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Script executed at: {script_execdate}")
print("Script to fetch OS env variable values..")
mac_username = os.getenv('USER')
print(f"Logged into the macbook user as: {mac_username}")
mac_userlogname= os.getenv('LOGNAME')
print(f"User logname as: {mac_userlogname}")
mac_usershell = os.getenv('SHELL')
print(f"default macbook user shell is: {mac_usershell}")
mac_userhomedir = os.getenv('HOME')
print(f"default macbook user home dir is: {mac_userhomedir}")
t.sleep(1)
mac_userpath = os.getenv('OLDPWD')
print(f"User old present working directory is: {mac_userpath}")
