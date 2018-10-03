'''
*********************************************************************************************
 Purpose: Gambler places a bet

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   19-09-18


**********************************************************************************************
'''


from random import randint
stake = int(input("How much money do you want to bet"))
goal = int(input("How much is your goal"))
times = int(input("How many times do you want to play"))
wins = 0
loss = 0
for i in range(times):
    cash = stake
    while cash < goal and cash > 0:  # checks if the gambler has reached his goal or his cash is 0
        money =randint(0, 1)  # generates a random number between 0 and 1
        if money < 0.5:
            cash += 1  # The Gambler wins $1
        else:
            cash -= 1  # The Gambler loses $1

    if cash == goal:  # if gambler reaches his goal he wins else loses
        exit(0)
    else:
        loss += 1
print("The total wins is ", str(wins))
print("The percentage of wins is ")
print(wins*100/times)
print(cash)
print("The percentage of loss is ")
print(loss*100/times)
print("The total loss", str(loss))
