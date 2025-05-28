import time
import os
print("another method to find out 'interview' keyword in a file")
with open("test.txt", "r") as file:
   content = file.read().lower()
if "interview" in content:
   print("The word 'interview' was found")
else:
   print("The word 'interview' was not found")
time.sleep(2)
df = subprocess.run(["ls", "-ltr"], capture_output=True, text=True, check=False)
if df.stdout:
    print("Linux command is functioning")
    print("Output:\n", df.stdout)
else:
    print("Linux command is not functioning")
    print("Error message:\n", df.stderr)
