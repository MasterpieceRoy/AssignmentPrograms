'''
*********************************************************************************************
 Purpose: Calculates the square root of a number based on Newton's Method

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   25-09-18


**********************************************************************************************
'''
import math  # imports the math library


def calcsqr(c):
    t = c
    epsilon = 1 * pow(10, -15)  # calculates the 1e-15
    while abs(t - c/t) > epsilon * t:  # iterates until the t -c/t is greater than the epsilon * t value
        t = (c / t + t) / 2.0  # calculates the average

    print(t)

try:
    c = int(input("Enter a number"))
    if c < 0:  # checks if the entered number is positive or not
        print("Enter non-negative number only")
        exit(0)
    else:
        calcsqr(c)
except Exception:
    print("Invalid input")