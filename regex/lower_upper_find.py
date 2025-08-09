import datetime, re, time
exec_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at: {exec_date}")
print(f"Script to find Lower/Upper cases letters from the given string")
print("================================================================")
lc = "i love you Da"
print(f"Script to find Lowercase letters from the given string")
result = re.findall("[a-z]",lc) # Searches for all lowercase letters (a to z) in the string.
time.sleep(2)
print(result)
print(f"Finding the Uppercase letters from the given string")
uc = "I LOVE YOU Da"
result1 = re.findall("[A-Z]", uc)
print(result1)
