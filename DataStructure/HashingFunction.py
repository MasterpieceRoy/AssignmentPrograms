from LinkedListHashing import *

ll = LinkList()
try:
    num = input("Enter the number you want to search")
    num = int(num)
    o = open("Numbers.txt", 'r')
    read = o.read()
    read = read.lstrip()
    store = ""
    for i in range(len(read)):
        if read[i] != " ":
            store = store + read[i]
        if read[i] == " " or i == len(read) - 1:
            v = int(store)
            ll.insert(v)
            store = ""
    ll.find(num, "Numbers.txt")
    print("The values present currently are ")
    ll.show()
    o.close()
except Exception as e:
    print(e)
