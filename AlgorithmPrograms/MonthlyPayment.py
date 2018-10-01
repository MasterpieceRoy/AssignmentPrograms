'''
*********************************************************************************************
 Purpose: Calculates the amount of money to be paid on a monthly basis

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   28-09-18


**********************************************************************************************
'''
from Util import *  # imports all the function definitions from Util package

try:
    principle = float(input("Enter Principle Amount \t"))  # inputs the principle amount
    year = float(input("Enter the total number of years \t"))  # inputs the year
    rate = float(input("Enter the Rate percent\t"))  # inputs the rate percent
    Util.monthlypayment(principle, year, rate)  # calls the monthly payment function from the Util package

except Exception:
    print("Invalid Input")
