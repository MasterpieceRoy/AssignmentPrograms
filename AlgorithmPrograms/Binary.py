'''
*********************************************************************************************
 Purpose: Converts a decimal number to its binary equivalent

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   27-09-18


**********************************************************************************************
'''

from Util import *  # imports all the function definitions from Util package
try:
    number = int(input("Enter a number"))  # takes a decimal number as input from the user
    value = str(to_binary(number))  # calls the to_binary function to convert it into binary
    print("The binary equivalent of", number, "is")
    if len(value) >= 3 and len(value) < 5:  # checks if the binary number is a 4 digit binary or not
        print(value.zfill(4))  # properly pads the number
    elif len(value) >= 5 and len(value) < 8:  # checks if the binary number is a 8 digit binary or not
        print(value.zfill(8))  # pad the binary number in a proper manner

except Exception:
    print("Invalid input")