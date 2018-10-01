'''
*********************************************************************************************
 Purpose: Shows the day of the week according to Gregorian Calendar

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   29-09-18


**********************************************************************************************
'''
from Util import *

try:
    month = input("Enter the Month")  # accept the month as the input
    day = float(input("Enter the day"))  # accepts the day as the input
    year = float(input("Enter the year"))  # accepts the year as input

    Util.dayofweek(month, day, year)  # calls the function to calculate the day of the week

except Exception:
    print("Invalid input")
