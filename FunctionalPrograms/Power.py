'''
*********************************************************************************************
 Purpose: Generates number until 2 to power of n

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   20-09-18


**********************************************************************************************
'''
n=input("Enter the power value N")
if(int(n)>30&int(n)<0):
    print("The value of N will overflow so kindly try again")
else:
    print("The values are:")
    for i in range(int(n)):
        print(pow(2,i))

