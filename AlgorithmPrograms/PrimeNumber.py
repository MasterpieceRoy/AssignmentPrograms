'''
*********************************************************************************************
 Purpose: Generates Prime Number from 0 to 1000

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   24-09-18


**********************************************************************************************
'''

from Util import *

try:
    number = Util.isprime(1000)  # calls the prime number method
    print(number)  # prints the number which are prime from 0 to 1000
except Exception:
    print("Invalid input")
