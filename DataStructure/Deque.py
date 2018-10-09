# Deque function for operation on a Doubly ended Queue
'''
*********************************************************************************************
 Purpose: Function of Doubly Ended Queue

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   03-10-18


**********************************************************************************************
'''

class Deque:
    def __init__(self):  # used to initialise with the items
        self.items = []

    def isEmpty(self):  # used to check if the deque is empty
        return self.items == []

    def addFront(self, item):  # used to add an item to the front of the queue
        self.items.append(item)

    def addRear(self, item):  # used to add an item to the rear of the queue
        self.items.insert(0, item)

    def removeFront(self):  # used to remove an item from the front of the queue
        return self.items.pop()

    def removeRear(self):  # used to remove an item from the back of the queue
        return self.items.pop(0)

    def size(self):  # used to check the size of the queue
        return len(self.items)

