'''
*********************************************************************************************
 Purpose: Create a Linked List using Stack

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   04-10-18


**********************************************************************************************
'''

# used to define a Node Structure


class Node:

    def __init__(self, data):  # used to define a Linked List
        self.data = data
        self.next = None

# used to create a linked list


class LinkedListOfStack:

    def __init__(self):  # initial condition
        self.head = None

    def isEmpty(self):  # if linked list is empty
        return self.head is None  # since linked list is empty head is null

    def push(self, data):  # pushes the data into the linked list
        if self.head is None:  # checks if head points to None if true it means the node is the first node
            self.head = Node(data)  # head saves the address of the node
        else:
            # used for traversing and storing the elements inside the linked list
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):  # function definition to pop elements from the linked list
        if self.head is None:  # check if head is empty or not
            return "list is empty"
        else:
            # pops elements from the array
            popped = self.head.data
            self.head = self.head.next
            return popped

    def display(self):  # function to display the linked list
        temp = self.head
        while(temp != None):
            print(self.pop())
            temp = temp.next  # used to traverse to  the next node in the linked list
