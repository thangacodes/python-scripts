import datetime
from subprocess import Popen, PIPE

time_now = datetime.datetime.now()
print(f"Script is run at: {time_now}")

# Display disk space usage
process = Popen(['df', '-h'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

# Print output and errors
print("DISK_SPACE:\n", stdout.decode())
print("ERROR:\n", stderr.decode())
