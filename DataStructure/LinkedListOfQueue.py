class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListOfQueue:

    def __init__(self):
        self.first = None

    def isEmpty(self):
        return self.front == self.first

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
