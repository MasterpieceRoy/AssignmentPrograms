from LinkedListOrder import *


class OrderedList:

    file = open("numbers.txt", "r+")

    number = file.read().split(" ")

    for i in range(0, len(number)):
        for j in range(0, len(number)-1):
            if number[j] > number[j+1]:
                temp = number[j]
                number[j] = number[j+1]
                number[j+1] = temp
    print(number)
    index = 0
    list1 = LinkedListOrder()
    while index < len(number):
        list1.insertdata(str(number[index]))
        index += 1
    # list1.printList()
    digit = int(input("Enter the number which you want to search"))
    result = list1.search(digit)
    if result:
        print("number found")
        list1.deleteword(digit)
        list1.printList()
    else:
        print("number not found")
        print("Number will be updated in the list")
        list1.insertdata(digit)
    list1.updateList()

