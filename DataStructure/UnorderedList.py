

# creates a node class with attributes of data and address
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creates a linked list class


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):  # function to add elements inside the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, data):  # function to remove a particular element from the linked list

        # Saves the head node
        temp = self.head

        # If head node contains the data which is to be deleted
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

            # if the element to be deleted is not present in linked list
        if temp == None:
            return

            # Unlink the node from linked list
        prev.next = temp.next

        temp = None


    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def search(self, data):
        if self.head is None:
            return False
        else:
            p = self.head
            while p is not None:
                if p.data == data:
                    return True
                p = p.next
            return False


llist = LinkedList()
with open('hello.txt', 'r') as f:
    for line in f:
        for word in line.split():
           llist.add(word)
        llist.print_list()
new_word = input("Enter the word that you want to search ")
ele = llist.search(new_word)
if ele:
    print("The entered element is present in the list")
    llist.remove(new_word)

    llist.print_list()
else:
    print("The element will be added to the list")
    llist.add(new_word)
    llist.print_list()

