def printmonth(year, month):
    printmonthtitle(year, month)
    printmonthtitle(year, month)


def printmonthtitle(year, month):
    print(" ", getmonthname(month), " ", year)
    print("----------------------------------")
    print("Sun Mon Tue Wed Thu Fri Sat")


def getmonthname(month):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month


year = int(input("Enter the year"))

month = int(input("Enter the month"))

if month < 1 or month > 12 or year < 1980:
    print("Invalid input")
    exit(0)
else:
    printmonth(year, month)


