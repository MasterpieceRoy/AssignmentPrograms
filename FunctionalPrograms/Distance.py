'''
*********************************************************************************************
 Purpose: Calculates the Euclidean distance between 2 points

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   18-09-18


**********************************************************************************************
'''

import math
try:
    x2 = int(input("Enter the value of x"))
    y2 = int(input("Enter the value of y"))
    print("The Euclidean distance between the two points is")

    print(math.sqrt(math.pow(x2, 2)+math.pow(y2, 2)))  # calculates and prints the distance
except Exception:
    print("Invalid Input")
