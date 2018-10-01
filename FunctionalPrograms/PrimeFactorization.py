'''
*********************************************************************************************
 Purpose: Generates factorization of prime numbers

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   22-09-18


**********************************************************************************************
'''

def primes(n):
    primfac = []

    i = 2
    while i*i <= n:
        while (n % i) == 0:  # checks if the number gives a zero remainder when divided by square of i
            primfac.append(i)
            n = int(n/i)
        i += 1
    if n > 1:
       primfac.append(n)
    print(primfac)

try:
    num = input("Enter the number")
    primes(int(num))
except Exception:
    print("Invalid Input Detected")
