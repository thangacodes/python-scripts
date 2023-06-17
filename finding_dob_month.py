def dob_finding():
    month_name =["January","February","March","April","May","June","July","August","September","October","November","December"]
    print (month_name)
    month_numbers =["January","February","March","April","May","June","July","August","September","October","November","December"]
    print(month_numbers)
    dob =input("Please enter your date of birth: ", )
    dob
    print("You've entered the dob is:", dob)
    month_value  = int(dob.split('/')[1])
    birth_number = print("you are birth month in number is:", month_value )
    birth_month  = print("You are born in the month of:", month_numbers[month_value -1])
dob_finding()


## Takeaway is, using split function, we can split dob date into '/' and then we can use that split variable in the last. If we use minus of date of split, it fullfil our requirements.
