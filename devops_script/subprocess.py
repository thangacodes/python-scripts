import time as t
import subprocess as s
import datetime as d 
exec_date = d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Script executed at: {exec_date}")
disk_free = s.run(['df', '-h'], capture_output=True, text=True)
print(disk_free)
t.sleep(1)
host_detail = s.run(['hostname'], capture_output=True, text=True)
print(f"Your computer hostname is: {host_detail.stdout.strip()}")
