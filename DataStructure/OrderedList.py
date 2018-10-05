number = int(input('Enter a number'))

llist =list()
with open("numbers.txt","r") as f:
    for line in f:
        for number in line.split():
            llist.append(number)
            llist.sort()
        print(llist)


