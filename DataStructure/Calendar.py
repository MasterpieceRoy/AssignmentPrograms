def isleapyear(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True

    return False


# Function to find the day
def day(month, day, year):
    y = year - (14 - month) / 12
    # print (y)
    x = y + y / 4 - y / 100 + y / 400
    # print (x)
    m = month + 12 * ((14 - month) / 12) - 2
    # print (m)
    d = (day + x + (31 * m) / 12) % 7
    # print (d)
    return d

# Function to print the Calendar
# @param month
# @param year


def calendar(month, year):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    if month == 2 and isleapyear(year):
        days[month] = 29

    print("        ", months[month - 1] + " ", year, "\n")
    print(" Su Mo Tu We Th Fr Sa")
    print("----------------------")

    d = day(month, 1, year)

    i = 0

    while i < d:
        print("  ")
        i += 1
    i = 1
    while i <= days[month]:
        print("%2d" % i, end='')
        if ((i+d) % 7 == 0) or (i == days[month]):
            print("\n")
            print("----------------------")
        i += 1


class Calendar:

    month = int(input("enter the month\n"))
    year = int(input("enter the year\n"))

    calendar(month, year)
