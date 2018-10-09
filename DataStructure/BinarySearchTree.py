'''
*********************************************************************************************
 Purpose: To find the number of Binary Search Trees Possible

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   04-10-18


**********************************************************************************************
'''


def facto(ele):  # function definition to calculate the number of possible nodes by factorial
    facto = 1
    while ele > int(1):
        facto = facto * ele  # calculates the factorial of the nodes to generate binary tree
        ele -= 1
    return facto


class BinarySearchTree:
    try:
        number = int(input("enter the number of test cases"))  # asks the number of test cases

        count = 0
        list = []

        while len(list) < number:
            ele = int(input("Enter the nodes "))  # adds the nodes
            list.append(ele)  # adds the nodes and appends it in the list
            print(list)
        i = 0
        while i < len(list):

            a = facto(2 * list[i])   # calculates since binary search tree has 2 nodes
            b = facto((list[i] + 1))   # calculates the value of the corresponding test case
            c = facto(list[i])
            count = a/(b*c)  # calculates the number of binary search trees possible
            print("No. of nodes is ", list[i], "======>  No. of tree is ", count)
            i += 1  # used to iterate the list
    except Exception:
        print("Invalid input")