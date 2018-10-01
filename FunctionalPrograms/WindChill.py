'''
*********************************************************************************************
 Purpose: Calculates the Wind Chill in the atmosphere

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   20-09-18


**********************************************************************************************
'''

import math  # invokes the predefined math package
try:
    t = float(input("Enter the temperature in Fahrenheit"))
    v = float(input("Enter the wind speed in miles per hour"))

    if t > abs(50) and v > 120 or v < 3:
        print("Invalid input detected")
    else:
        w = 35.74+0.6215*t+(0.4275*t-35.75)*math.pow(v, 0.16)  # calculates the wind chill

    print("The WindChill in the atmosphere is", str(w), "degrees Fahrenheit")
except Exception:
    print("Invalid Input")
