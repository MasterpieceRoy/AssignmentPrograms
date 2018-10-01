'''
*********************************************************************************************
 Purpose: Converts a decimal number to its binary equivalent and swap the nibbles and give back it's binary equivalent

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   27-09-18


**********************************************************************************************
'''
from Util import *  # imports all the function definitions from Util package

try:
    number = int(input("Enter a number"))
    value = str(to_binary(number))  # converts the number to a binary number
    print("The binary equivalent of", number, "is")
    if len(value) >= 3 and len(value) < 5:
        new_value = value.zfill(4)
        print(new_value)
    elif len(value) >= 5 and len(value) < 8:
        new_value = value.zfill(8)
        print(new_value)

    new_value = int(new_value)

    new_number = Util.split8Bit(number)  # swaps the nibbles and gets back it's decimal equivalent
    print(new_number)  # prints the new number

except Exception:
    print("Invalid input")
