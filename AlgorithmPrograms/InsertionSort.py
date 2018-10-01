'''
*********************************************************************************************
 Purpose: Arranges the words in the list in alphabetical order with the help of Insertion Sort

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   27-09-18


**********************************************************************************************
'''


from Util import *  # imports all the function definitions from Util package
try:
    lis = list()
    size = int(input("Enter how many words do you want to enter "))
    print("Enter the words")
    for i in range(size):  # takes the input from the user
        word = input()
        lis.append(word)
    Utility.insertion_sort_string(lis)  # calls the insertion sort function
    print(lis)
except Exception:
    print("Invalid input")
