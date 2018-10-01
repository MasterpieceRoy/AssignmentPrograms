'''
*********************************************************************************************
 Purpose: Converts the Temperature to Celsius and Fahrenheit

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   24-09-18


**********************************************************************************************
'''
from Util import *  # import all the function definitions from Util package

try:
    choice = int(input("Enter 1.Convert to Fahrenheit \n 2. Convert to Celsius"))

    if choice == int(1):
        ch = "Celsius"
        print("Input temperature in ", ch)
        temp = float(input())
        Util.temperaturconversion(choice, temp)  # calls the function to convert the temperature
    elif choice == int(2):
        ch = "Fahrenheit"
        print("Input temperature in ", ch)
        temp = float(input())
        Util.temperaturconversion(choice, temp)  # calls the function to convert the temperature
    else:
        print("Incorrect input detected")
        exit(0)
except Exception:
    print("Invalid input")