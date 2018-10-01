'''
*********************************************************************************************
 Purpose: Guesses the number that the user has in mind with a series of questions

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   26-09-18


**********************************************************************************************
'''
from Util import *  # imports all the function definitions from Util package

try:
    number = int(input("Enter the maximum number"))
    print("Think of a number between 0 to ", str(number))
    Util.find_number(0, number)  # tries to guess the number that the user thinks by asking a series of questions

except Exception:
    print("Invalid Input")

