'''
*********************************************************************************************
 Purpose: Generates harmonic number upto n

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   19-09-18


**********************************************************************************************
'''

try:
    n = int(input("Enter the value of N"))
    calculate = 0
    if n == 0:
        print("The value of N cannot be equal to zero")
    else:
        print("The Harmonic Value is :")
        for i in range(1, n+1):  # calculates Harmonic Value until the value of N
            calculate = calculate+(1.0/i)

        print(float(calculate))
except Exception:
    print("Invalid Entry")





