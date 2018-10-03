class Queue:
    def __init__(self, size, people):
        self.size = size
        self.rear = people
        self.front = 0
        self.arr = list()

    def Enque(self):
        if self.isFull():
            print("The queue is full")
        else:
            self.rear = self.rear + 1

    def Deque(self):
        if self.isEmpty():
            print("The queue is already empty ")
        else:
            self.front = self.front + 1

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.size

    def no_of_people(self):
        return self.rear - self.front


