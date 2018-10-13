'''
*********************************************************************************************
 Purpose: Contains different types of Search and Sort Algorithm and calculates the time taken

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   28-09-18


**********************************************************************************************
'''
from Util import *  # imports all the function definitions from Util package
import time

try:
    choice = int(input("Enter your choice \n 1.Binary Search Integer\n 2.Binary Search String\n 3.Insertion Sort Intege"
                       "r\n 4.Insertion Sort String\n 5.Bubble Sort Integer\n 6.Bubble Sort String \n"))

    # asks the user to enter the choice

    if choice == 1:
        n = int(input("How many elements do you want to enter ?"))
        lis = list()
        print("Enter the elements")
        for i in range(n):
            ele = int(input())
            lis.append(ele)  # adds the elements to the list lis
            lis.sort()
        key = int(input("Enter the number you want to search"))  # asks the element that you want to search
        t1 = time.clock()  # used to give the current time
        print(lis)
        Utility.binary_search_number(key, lis)
        t2 = time.clock()
        print('Took {} Seconds'.format(t2-t1))  # calculates the time

    elif choice == 2:
        n = int(input("How many elements do you want to enter ?"))
        lis = list()  # stores the element
        print("Enter the words")
        for i in range(n):
            ele = input()
            lis.append(ele)
            lis.sort()
        key = input("Enter the word you want to search")
        t3 = time.clock()
        Utility.binary_search_word(lis, key)
        t4 = time.clock()
        print('Took {} Seconds'.format(t4 - t3))

    elif choice == 3:
        n = int(input("How many elements do you want to enter ?"))
        lis = list()
        print("Enter the elements")
        for i in range(n):
            ele = input()
            lis.append(ele)
        t5 = time.clock()
        Utility.insertion_sort_number(lis)
        print(lis)
        t6 = time.clock()
        print('Took {} Seconds'.format(t6-t5))

    elif choice == 4:
        n = int(input("How many elements do you want to enter ?"))
        lis = list()
        print("Enter the characters")
        for i in range(n):
            ele = input()
            lis.append(ele)
        t7 = time.clock()
        Utility.insertion_sort_string(lis)
        print(lis)
        t8 = time.clock()
        print('Took {} Seconds'.format(t8-t7))

    elif choice == 5:
        n = int(input("How many elements do you want to enter ?"))
        lis = list()
        print("Enter the numbers")
        for i in range(n):
            ele = input()
            lis.append(ele)
        t9 = time.clock()
        Utility.bubble_sort_number(lis)
        print(lis)
        t10 = time.clock()
        print('Took {} Seconds'.format(t10-t9))

    elif choice == 6:
        n = int(input("How many elements do you want to enter ?"))
        lis = list()
        print("Enter the characters")
        for i in range(n):
            ele = input()
            lis.append(ele)
        t11 = time.clock()
        Utility.bubble_sort_string(lis)
        print(lis)
        t12 = time.clock()
        print('Took {} Seconds'.format(t12-t11))


except KeyboardInterrupt:
    print("Stopped using keyboard")


