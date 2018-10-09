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
    bal_bank = int(100000)  # sets the amount available in the bank as 100000

    size = int(input("Enter size of the queue"))  # asks the total size of the queue

    people = int(input("Enter the number of people in the queue"))  # asks the number of people present in the queue

    obj = Queue(size, people)  # passes the size of the queue and the number of people in the queue

    while 1:  # Loops until the user chooses to exit
        print("Select one of the choice from below")
        print("1.Deposit Cash")
        print("2. Withdraw Cash")
        print("3. Check Account Balance")
        print("4. Find how many persons in the Queue")
        print("5. Remove a person from the Queue")
        print("6. Add a person to the Queue")
        print("7. Exit")

        choice = int(input())  # takes the input from the user

        if choice == 1:  # Deposit Part
            deposit = int(input("Enter the amount of money you want to deposit"))  # asks the amount of money from the
            # user
            bal_bank = deposit + bal_bank  # adds the amount of money to the bank
            print("The Bank Balance is ", bal_bank)  # displays the current bank balance

        elif choice == 2:  # Withdrawal part
            withdraw = int(input("Enter the amount of money you want to withdraw"))  # asks the amount of money to
            # withdraw

            if bal_bank > withdraw:  # checks if the bank has sufficient balance to withdraw
                bal_bank = bal_bank - withdraw  # reduces the withdrawn amount from the current bank balance
                print("The amount now present in the bank is ", str(bal_bank))  # displays the amount present in the
                # bank after withdrawal
            else:
                print("Sorry !!! The bank has insufficient funds.Please come back later")

        elif choice == 3:  # checks the bank balance
            print("The balance present in the bank is ", str(bal_bank))  # displays the current bank balance

        elif choice == 4:  # checks the number of people present in the queue
            no_of_persons = obj.no_of_people()
            print("The number of persons present in the queue are ", no_of_persons)

        elif choice == 5:  # removes a person from the queue
            obj.Deque()  # calls the deque function
            no_of_people = obj. no_of_people()
            print("The number of people now present in the queue are ", no_of_people)

        elif choice == 6:  # adds a person in the queue
            obj.Enque()  # calls the Enque function to add a person to the queue
            no_of_people = obj.no_of_people()
            print("The number of people now present in the queue are ", no_of_people)

        elif choice == 7:  # Used to exit from the program
            exit(0)
        else:
            print("Wrong Input Detected. Please try again")

except Exception:
    print("Invalid Input Detected")

