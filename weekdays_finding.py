import time
print("iterating weekdays using python for loop")
weekdays=["monday","tuesday","wednesday","thursday","friday"]
for w in weekdays:
    print(w)
time.sleep(3)
print("In the above weekdays list, print only when weekday is Thursday!!")
weekdays=["monday","tuesday","wednesday","thursday","friday"]
for w in weekdays:
    if w == "thursday":
        print(w)
