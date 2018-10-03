'''
***********************************************************************************************************
 Purpose: Program which checks if the entered word is palindrome or not with the help of Deque

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   03-10-18


***********************************************************************************************************
'''
from Deque import *


def palchecker(word):
    queue = Deque()  # creates a reference for Deque object class

    for ch in word:
        queue.addRear(ch)  # adds all the characters from back

    is_equal = True

    while queue.size() > 1 and is_equal:
        first = queue.removeFront()  # removes the characters from the front of the queue
        last = queue.removeRear()  # removes the characters from the rear of the queue
        if first != last:
            is_equal = False

    return is_equal


word = input("Enter the word ")

status = palchecker(word)

print(status)
