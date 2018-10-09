'''
*********************************************************************************************
 Purpose: Displays a Calendar of the Month

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   04-10-18


**********************************************************************************************
'''
import math


def isLeapYear(year):  # function to check whether the entered year is a leap year or not
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):  # checks whether the year is a century year or not
        return True

    return False

# Function to find the day
# @param month
# @param day
# @param year
# return the day


def day(month, day, year):
    y = math.ceil(year - (14 - month) / 12)

    x = math.floor(y + y / 4 - y / 100 + y / 400)

    m = month + (12 * int(((14 - month))/12) - 2)

    d = int((day + x + ((31 * m) / 12)) % 7)

    return d

# Function to print the Calendar
# @param month
# @param year


def calendar(month, year):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]  # Stores the Month in an array

    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # since the index in an array starts from 0 and month
    # is 1

    if month == 2 and isLeapYear(year):  # checks if the month entered is February leap year or not
        days[month] = 29  # if yes sets the no. of days in February as 29

    print("        ", months[month - 1] + " ", year, "\n")   # used to display the the calendar of the month
    print(" Su Mo Tu We Th Fr Sa")
    print("++++++++++++++++++++++")

    d = day(month, 1, year)  # gets the number of days
    i = 0
    # print(d)
    while i < d:
        print("   ", end=''),  # prints spaces based on the days
        i += 1
    # print(i)
    i = 1
    while i <= days[month]:
        print("%2d" % i, end=' '),  # prints in 2 decimal format

        if int(i+d) % 7 == 0 or (i == days[month]):  # if week is over returns a new line

            print("\n")
        i += 1  # increments the i count


class Calendar:

    month = input("enter the month\n")  # takes the month as an input
    year = input("enter the year\n")

    try:
        calendar(int(month), int(year))  # calls the function to display the calendar
    except Exception:
        print("Invalid input")
