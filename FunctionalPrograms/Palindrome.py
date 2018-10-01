'''
*********************************************************************************************
 Purpose: Checks if the number is palindrome or not

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   21-09-18


**********************************************************************************************
'''

def num_palind( num ):
    temp = num
    total = 0
    rev = 0
    while num != 0:  # loops until the number is equal to zero or not
        rev = num % 10  # removes the last number and stores it into the reverse variable
        total = total*10 + rev
        num = int(num/10)
    if total == temp:  # checks if the reversed number is equal to the original number or not
        print(str(temp), "is a Palindrome Number")
    else:
        print(str(temp), "is not a Palindrome Number")

def word_palind( word ):
    return word[::-1]

def isPalindrome(s):
        # Calling reverse function
        rev = word_palind(s)

        # Checking if both string are equal or not
        if s == rev:
            return True
        return False

try:
    num = int(input("Enter a number"))
    num_palind(num)
    word = input("Enter a word")
    r = isPalindrome(word)
    if r == 1:
        print("The entered word is palindrome")
    else:
        print("The entered word is not a palindrome")
except Exception:
    print("Invalid input detected")
