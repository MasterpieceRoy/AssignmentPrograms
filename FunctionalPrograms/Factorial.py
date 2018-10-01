'''
*********************************************************************************************
 Purpose: Generates palindrome of a number

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   21-09-18


**********************************************************************************************
'''
def generate_factorial(num):
    if num == 1:
        return 1
    else:
        return num*generate_factorial(num-1)


num = int(input(" Enter the number "))
fact = generate_factorial(num)
print(str(fact))
