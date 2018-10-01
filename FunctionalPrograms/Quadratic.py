'''
*********************************************************************************************
 Purpose: Generates roots of Quadratic Equation

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   19-09-18


**********************************************************************************************
'''
import math
try:
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    c = int(input("Enter the value of c"))

    delta = pow(b, 2)-4*a*c  # calculates the value of delta

    root1_Of_x = (-b+math.sqrt(delta))/(2*a)  # generates the first root of the quadratic equation
    root2_Of_x = (-b-math.sqrt(delta))/(2*a)  # generates the second root of the quadratic equation

    print('The roots of the equation', str(a), 'x*x+', str(b), 'x', str(c), ' are ')
    print(root1_Of_x, "and ", root2_Of_x)
except Exception:
    print("Invalid Value")