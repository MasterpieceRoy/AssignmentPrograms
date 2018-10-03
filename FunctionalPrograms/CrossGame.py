'''
*********************************************************************************************
 Purpose: Simulate a Cross Game between the user and the computer

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   22-09-18


**********************************************************************************************
'''
import random


def tic_tac_toe():  # function definition
    print("Welcome to the Cross Game \n")
    print("Player 1 is the computer and will play first\n")
    name = input("But first Player 2 Enter your name Please \t")

    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]  # this pattern appears in the cross game
    end = False  # it is used as a flag is set to False to check the conditions in the end

    # a tuple is created which contains the winning conditions
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():  # used to print the cross game board
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():  # function definition which makes the player one i.e. computer play
        n = random.randint(0, 8)  # occupies any of the empty cells 0 to 8
        if board[n] == "X" or board[n] == "O":  # checks if the cell is already occupied or not
            p1()  # if present, recursively calls the function again
        else:
            board[n] = "X"

    def p2():  # function definition which executes when Player Two Plays
        n = choose_number()  # asks the player to choose a cell
        if board[n] == "X" or board[n] == "O":  # checks if cell is empty or not
            print("\nAlready Occupied !!Try again")
            p2()
        else:
            board[n] = "O"  # if cell is empty then inserts 'O' in the cell

    def choose_number():  # checks if the selected cell is present in the range or not
        # while True:
        while True:
            a = input()
            try:
                a = int(a)
                a -= 1
                if a in range(0, 9):
                    return a
                else:
                    print("\n Invalid choice. Try again")
                    continue
            except Exception:
               print("\nInvalid Input. Try again")
               continue

    def check_board():  # checks who wins the game
        count = 0
        for a in win_combinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Computer Wins!\n")
                print("Better luck next time\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print
                print("Congratulations!", name.upper()+" You Win!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Draw. No one wins !!! \n")
                return True

    while not end:  # checks if the game has ended or not
        draw()
        end = check_board()
        if end == True:
            break
        print("Computer plays")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print(name.upper()+" choose where to place an O\t")
        p2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()
try:
    tic_tac_toe()
except Exception:
    print("Incorrect input provided")
