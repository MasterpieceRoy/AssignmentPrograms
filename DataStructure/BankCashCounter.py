'''
***********************************************************************************************************
 Purpose: Program which creates Banking Cash Counter where people come in to deposit Cash and withdraw Cash

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   03-10-18


***********************************************************************************************************
'''

import collections
from Queue import *

try:
    bal_bank = int(100000)

    size = int(input("Enter size of the queue"))

    people = int(input("Enter the number of people in the queue"))

    obj = Queue(size, people)

    while 1:
        print("Select one of the choice from below")
        print("1.Deposit Cash")
        print("2. Withdraw Cash")
        print("3. Check Account Balance")
        print("4. Find how many persons in the Queue")
        print("5. Remove a person from the Queue")
        print("6. Add a person to the Queue")
        print("7. Exit")

        choice = int(input())

        if choice == 1:
            deposit = int(input("Enter the amount of money you want to deposit"))
            bal_bank = deposit + bal_bank
            print("The Bank Balance is ", bal_bank)

        elif choice == 2:
            withdraw = int(input("Enter the amount of money you want to withdraw"))
            if bal_bank > withdraw:
                bal_bank = bal_bank - withdraw
                print("The amount now present in the bank is ", str(bal_bank))
            else:
                print("Sorry !!! The bank has insufficient funds.Please come back later")

        elif choice == 3:
            print("The balance present in the bank is ", str(bal_bank))

        elif choice == 4:
            no_of_persons = obj.no_of_people()
            print("The number of persons present in the queue are ", no_of_persons)

        elif choice == 5:
            obj.Deque()
            no_of_people = obj. no_of_people()
            print("The number of people now present in the queue are ", no_of_people)

        elif choice == 6:
            obj.Enque()
            no_of_people = obj.no_of_people()
            print("The number of people now present in the queue are ", no_of_people)

        elif choice == 7:
            exit(0)
        else:
            print("Wrong Input Detected. Please try again")

except Exception:
    print("Invalid Input Detected")

