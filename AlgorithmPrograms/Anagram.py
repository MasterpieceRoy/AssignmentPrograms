'''
*********************************************************************************************
 Purpose: Checks if entered words are anagram of each other or not

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   24-09-18


**********************************************************************************************
'''
from Util import *  # imports all the function definitions from Util package


try:
    class Anagram:
        word1 = input("Enter the first string")  # takes the first string as input
        word2 = input("Enter the second string")  # takes the second string as input
        Util.is_anagram(word1, word2)  # checks if both the strings are anagram or not
except Exception:
    print("Invalid input")
