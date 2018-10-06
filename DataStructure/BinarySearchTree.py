def facto(ele):
    facto = 1
    while ele > int(1):
        facto = facto * ele
        ele -= 1
    return facto


class BinarySearchTree:

    number = int(input("enter the number of test cases"))

    count = 0
    list = []

    while len(list) < number:
        ele = int(input("Enter the nodes "))
        list.append(ele)
        print(list)
    i = 0
    while i < len(list):

        a = facto(2 * list[i])
        b = facto((list[i] + 1))
        c = facto(list[i])
        count = a/(b*c)
        print("No. of nodes is ", list[i], "======>  No. of tree is ", count)
        i += 1
