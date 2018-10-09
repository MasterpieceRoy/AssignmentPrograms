'''
*********************************************************************************************
 Purpose: Used to create a ordered linked list

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   05-10-18


**********************************************************************************************
'''

# creates an object of Node class


class Node:

    def __init__(self, data=None):  # used to initialise the node class
        self.data = data
        self.next = None

# creates an object of LinkedList
class LinkedListOrder:

    def __init__(self):  # used to initialise the initial Linked List condition
        self.head = None  # since no node is present head is null

    def insertdata(self, data):  # used to insert the node
        newNode = Node(data)   # creates a new node
        if self.head is None:  # executes if it is the first node
            self.head = newNode  # allocates the address of the new node to head
        else:
            temp = self.head
            while temp.next is not None:  # traverses until the last element in the link list
                temp = temp.next
            temp.next = newNode

    def printList(self):  # used to print the list
        temp = self.head
        while temp != None:  # used to traverse until the last element
            print(temp.data)
            temp = temp.next

    def search(self, digit):  # used to search the element entered by the user
        flag = 0  # it is used to mark
        temp = self.head
        while temp != None:
            if temp.data == digit:
                flag = 1
            temp = temp.next
        if flag == 0:
            return False
        else:
            return True

    def deleteword(self, word):
        if self.head.data == word:
            self.head = self.head.next

            print("Deleted the Number")


        else:
            temp = self.head.next
            prev = self.head

            while temp.data != word:
                prev = temp
                temp = temp.next

            prev.next = temp.next

    def updateList(self):
        f = open("numbers.txt", "w")
        if self.head is None:
            print("The list is empty")
        else:
            temp = self.head
            while temp is not None:
                f.write(str(temp.data))
                f.write(" ")
                temp = temp.next
