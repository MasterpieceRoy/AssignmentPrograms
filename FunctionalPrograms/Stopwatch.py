'''
*********************************************************************************************
 Purpose: Simulates a stop watch program

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   20-09-18


**********************************************************************************************
'''
import time  # imports the built-in time package


def startTime():
    return time.time()  # used to find the current time in seconds


def stopTime():
    return time.time()  # used to find the new current time in seconds


start = int(input("Enter 1 to start the time"))
firstTime = 0
secondTime = 0
if start == 1:
    firstTime = startTime()
    stop = int(input("Enter 2 to stop the time"))
    if stop == 2:
        secondTime = stopTime()
        totalTime = float(secondTime - firstTime)  # calculates the elapsed between two time period
        print("The total elapsed time is")
        print(str(totalTime) + " seconds")
    else:
        print("Incorrect input !!! Please try again")
else:
    print("Incorrect input !!! Please try again")


