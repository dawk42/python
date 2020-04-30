#!user/bin/python3
year = int(input("Enter a year: "))
if year <= 1580:
    print ("Not within the Gregorian calendar period")
elif 0 != year % 4:
    print ("Common Year")
elif 0 != year % 100:
    print ("Leap Year")
elif 0 != year % 400:
    print ("Common Year")
else:
    print("Leap Year")
