'''
*********************************************************************************************
 Purpose: Arranges the elements in the list with the help of MergeSort Algorithm

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   26-09-18


**********************************************************************************************
'''
from Util import *
lis = []  # creates an array which will be used to store the elements
try:
    n = int(input("Enter the number of elements"))
    print("Enter the elements")
    for i in range(n):  # accepts the element and stores it in the array
        ele = input()
        lis.append(ele)  # add the elements to the array lis
    print(lis)
    mergesort(lis, 0, n-1)  # calls the merge sort function

    print("The sorted array is ", lis)
except Exception:
    print("Invalid input")
