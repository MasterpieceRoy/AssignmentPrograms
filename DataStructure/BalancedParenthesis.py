'''
*********************************************************************************************
 Purpose: Checks whether the entered expression has equal number of parenthesis or not

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   03-10-18


**********************************************************************************************
'''

# Stack class


class Stack:
    def __init__(self):  # for function definition
        self.items = []

    def is_empty(self):  # checks if the Stack is empty or not
        return self.items == []

    def push(self, data):  # pushes elements inside the Stack
        self.items.append(data)

    def pop(self):  # pops elements outside the Stack
        return self.items.pop()


s = Stack()  # creates a reference for Stack class
try:
    exp = input('Please enter the expression: ')

    for c in exp:
        if c == '(':  # checks if open '(' is present then pushes
            s.push(1)
        elif c == ')':  # checks if the character occurring is ')'
            if s.is_empty():  # checks if the stack is empty or not
                is_balanced = False  # if empty it means that the ')' is a unbalanced equation
                break
            s.pop()  # if it's True then pops the remaining ')'
    else:
        if s.is_empty():
            is_balanced = True
        else:
            is_balanced = False

    if is_balanced:
        print('Expression has equal number of parenthesis.')
    else:
        print('Expression is not correctly parenthesized.')
except Exception:
    print("Invalid Input")
