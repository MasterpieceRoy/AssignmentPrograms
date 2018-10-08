import math
def isLeapYear(year):
    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        return True

    return False

# Function to find the day
# @param month
# @param day
# @param year
# return
def day(month, day, year):
    y = math.ceil(year - (14 - month) / 12)

    x = math.floor(y + y / 4 - y / 100 + y / 400)


    m = month + ((12 * int(((14 - month))/12) - 2))

    d = int((day + x + ((31 * m) / 12)) % 7)

    return d

# Function to print the Calendar
# @param month
# @param year
def calendar(month, year): #9 2018
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and isLeapYear(year):
        days[month] = 29

    print("        ", months[month - 1] + " ", year, "\n")
    print(" Su Mo Tu We Th Fr Sa")
    print("----------------------")

    d = day(month, 1, year)

    i = 0
    # print(d)
    while i < d:
        print("   ", end=''),
        i += 1
    # print(i)
    i = 1
    while i <= days[month]:
        print("%2d" % i, end=' '),

        if int(i+d) % 7 == 0 or (i == days[month]):

            print("\n")
            # print("----------------------")
        i += 1

class Calendar:

    month = input("enter the month\n")
    year = input("enter the year\n")

    calendar(int(month), int(year))
