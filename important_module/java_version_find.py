import re
from subprocess import Popen,PIPE

cmd='java -version'
sp=Popen(cmd.split(),shell=False,stdout=PIPE,stderr=PIPE,text=True)
rt=sp.wait()
output,error=sp.communicate()
if rt ==0:
    print (f"Name of the Software is: Java: {error.split()[0]} ")
    print (f"Version Number is: {error.split()[2]}")
else:
   print(f"Error is: {error}")
