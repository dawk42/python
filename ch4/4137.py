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
    return count  #dont use an else: here it breaks feb leap years not sure why
#test data
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

# iterate thru the test years
for i in range(len(testYears)):
#update vars yr and mo for each iteration
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	#runs function daysInMonth() with given input
	#compares results to to the test data testResults
	if result == testResults[i]:
		print("OK")
    
	else:
		print("Failed")
