#!/usr/bin/python3
def isYearLeap(year):
#tests year for its leapness
    if 0 != year % 4:
        return False
    elif 0 != year % 100:
        return True
    elif 0 != year % 400:
        return False
    else:
        return True

def daysInMonth(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    count = days[month-1] 
    # calls number of days from the days list, month - 1 because list 
    #position starts at zero

    if  month == 2 and isYearLeap(year):
        count = 29
        #print ("Hello")  was having issues at first used this to make
        # sure this if was being run
    return count 

def dayOfYear(year,month,day):





print(dayOfYear(2000,12,31))
