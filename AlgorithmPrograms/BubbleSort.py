'''
*********************************************************************************************
 Purpose: Bubble Sorts the elements present in the list

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   28-09-2018


**********************************************************************************************
'''

from Util import *  # imports all the function definitions from Util package
try:
    size = int(input("Enter the total elements that you want to enter"))
    print("Enter the numbers")
    lis = list()
    for i in range(size):
        ele = input()
        lis.append(ele)
    Utility.bubble_sort_number(lis)  # calls for the bubble sort definition from the Util file
    print("The sorted elements are ", lis)
except Exception:
    print("Invalid input")
