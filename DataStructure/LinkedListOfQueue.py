'''
*********************************************************************************************
 Purpose: Function for Linked List Operation using Queue

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   06-10-18


**********************************************************************************************
'''

# used to create a node


class Node:

    def __init__(self, data):  # used for initialising the node
        self.data = data
        self.next = None

# used to create a linked list using queue


class LinkedListOfQueue:

    def __init__(self):  # used to initialise
        self.first = None

    def isEmpty(self):  # used to check if it is empty or not
        return self.front == self.first  # assign the first place to the front

    def enque(self, data):
        newNode = Node(data)
        if self.first == None:
            self.first = newNode
            return
        tempData = self.first
        while(tempData.next != None):
            tempData = tempData.next
        tempData.next = newNode

    def deque(self):
        temp = self.first
        self.first = self.first.next
        return temp.data

    def display(self):
        tempNode = self.first
        while tempNode != None:
            print(self.deque())
            tempNode = tempNode.next
