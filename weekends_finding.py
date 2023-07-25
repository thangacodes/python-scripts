import time 
print("Finding only weekend days in the given list")
weekends=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for w in weekends:
    print(w)
time.sleep(2)
print("Only when weekends found by Python script")
weekends=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for w in weekends:
    if w == "saturday" or w == "sunday":
        print(w)

