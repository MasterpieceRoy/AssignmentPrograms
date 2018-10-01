'''
*********************************************************************************************
 Purpose: Shows the denomination of notes to be dispensed from a Note Vending Machine

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   27-09-18


**********************************************************************************************
'''


def dispense_money(money, notes):
    if money == 0:  # checks if the money is equal to zero or not
        print("The number of minimum notes required are  ", str(notes))  # checks the number of minimum notes required
        exit()
    if money >= 1000:  # checks if the entered amount is more than or equal to 1000
        notes = notes + int(money / 1000)  # calculates the number of notes generated
        # print(str(notes))
        print("The number of 1000 Rupees notes are ", str(int(money / 1000)))  # calculates the number of 1000 Rs notes
        if int(money / 1000) == 0:
            return
        else:
            dispense_money(int(money % 1000), notes)  # calls the function recursively in order to calculate again

    elif money >= 500:  # checks if the entered amount is more than or equal to 500
        notes = notes + int(money / 500)  # calculates the number of notes generated
        # print(str(notes))
        print("The number of 500 Rupees notes are ", str(int(money / 500)))  # calculates the number of 500 Rs notes
        if int(money / 500) == 0:
            return
        else:
            dispense_money(int(money % 500), notes)  # calls the function recursively in order to calculate again

    elif money >= 100:  # checks if the entered amount is more than or equal to 100
        notes = notes + int(money / 100)  # calculates the number of notes generated
        # print(str(notes))
        print("The number of 100 Rupees notes are ", str(int(money / 100)))  # calculates the number of 100 Rs notes
        if int(money / 100) == 0:
            return
        else:
            dispense_money(int(money % 100), notes)  # calls the function recursively in order to calculate again

    elif money >= 50:  # checks if the entered amount is more than or equal to 50
        notes = notes + int(money / 50)  # calculates the number of notes generated
        print("The number of 50 Rupees notes are ", str(int(money / 50)))  # calculates the number of 50 Rs notes
        if int(money / 50) == 0:
            return
        else:
            dispense_money(int(money % 50), notes)  # calls the function recursively in order to calculate again

    elif money >= 10:  # checks if the entered amount is more than or equal to 10
        notes = notes + int(money / 10)  # calculates the number of notes generated
        print("The number of 10 Rupees notes are ", str(int(money / 10)))  # calculates the number of 10 Rs notes
        if int(money / 10) == 0:
            return
        else:
            dispense_money(int(money % 10), notes)  # calls the function recursively in order to calculate again

    elif money >= 5:  # checks if the entered amount is more than or equal to 5
        notes = notes + int(money / 5)  # calculates the number of notes generated
        print("The number of 5 Rupees notes are ", str(int(money / 5)))  # calculates the number of 5 Rs notes
        if int(money / 5) == 0:
            return
        else:
            dispense_money(int(money % 5), notes)  # calls the function recursively in order to calculate again

    elif money >= 2:  # checks if the entered amount is more than or equal to 2
        notes = notes + (int(money / 2))  # calculates the number of notes generated
        print("The number of 2 Rupees notes are ", str(int(money / 2)))  # calculates the number of 2 Rs notes
        if int(money / 2) == 0:
            return
        else:
            dispense_money(int(money % 2), notes)  # calls the function recursively in order to calculate again

    elif money >= 1:  # checks if the entered amount is more than or equal to 1
        notes = notes + int(money / 1)  # calculates the number of notes generated
        print("The number of 1 Rupee notes are ", str(int(money / 1)))  # calculates the number of 1 Re notes
        if int(money / 1) == 0:
            return
        else:
            dispense_money(int(money % 1), notes)  # calls the function recursively in order to calculate again
    # print(notes)


class VendingMachine:
    notes = 0
    try:
        money = int(input("Enter the required cash"))  # asks the user to input the amount
        # vm = VendingMachine
        dispense_money(money, notes)  # calls the dispense_money function to find out the denominations
    except Exception as ValueError:
        print("Invalid input")
