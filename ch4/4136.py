#!/usr/bin/python3
def isYearLeap(year):
    if 0 != year % 4:
        return False
    elif 0 != year % 100:
        return True
    elif 0 != year % 400:
        return False
    else:
        return True


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
