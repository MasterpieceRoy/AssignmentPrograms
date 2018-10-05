import itertools
import random

carddeck = list(itertools.product(["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"], ["Clubs", "Diamonds", "Hearts", "Spades"]))

random.shuffle(carddeck)


def player1(n):
    print("Player 1 gets:-\n")
    for i in range(n):
        print(carddeck[i][0], carddeck[i][1])
        carddeck.remove(carddeck[i])


def player2(n):
    print("\nPlayer 2 gets:-\n")
    for j in range(n):
        print(carddeck[j][0], carddeck[j][1])
        carddeck.remove(carddeck[j])


def player3(n):
    print("\nPlayer 3 gets:-\n")
    for k in range(n):
        print(carddeck[k][0], carddeck[k][1])
        carddeck.remove(carddeck[k])


def player4(n):
    print("\nPlayer 4 gets:-\n")
    for l in range(n):
        print(carddeck[l][0], carddeck[l][1])
        carddeck.remove(carddeck[l])


player1(9)
player2(9)
player3(9)
player4(9)
