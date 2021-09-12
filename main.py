# This is an attempt to create a game of blackjack.
# Rules are as follows:
# Rule 1

import random

print()
print("insert rules here")
print()
print("insert controls/commands here")
playerlist = []
cardlist = []
player = 0


def deal_cards(cardamount, numberofpeople):
    numberofpeople = int(numberofpeople)
    y = 0
    cardlist = []

    # three lines at the beginning
    while y < 3:
        print()
        y += 1
    x = 0

    # loops through all the card players
    while x < numberofpeople:
        player = x + 1
        playerlist.append([])
        cardamount = int(cardamount)

        #Correctly names the cards
        i = 0
        while i < cardamount:
            playerlist[player][i].append(random.randint(1, 14))
            if playerlist[player][i] == 11:
                playerlist[player][i] = "Jack"
            elif playerlist[player][i] == 12:
                playerlist[player][i] = "Queen"
            elif playerlist[player][i] == 13:
                playerlist[player][i] = "King"
            elif playerlist[player][i] == 1 or playerlist[player][i] == 14:
                playerlist[player][i] = "Ace"
            playerlist[player][i] = str(playerlist[player][i])

            #Selects the suits
            suit = random.randint(1, 4)
            suit = str(suit)
            if suit == "1":
                suit = "Clubs"
            elif suit == "2":
                suit = "Spades"
            elif suit == "3":
                suit = "Hearts"
            elif suit == "4":
                suit = "Diamonds"

            playerlist[player][i] = playerlist[player][i] + " of " + suit
            i += 1

        if player == 1:
            print("Player " + str(player) + "(dealer)'s Cards: " + str(cardlist))
        else:
            print("Player " + str(player) + "'s Cards: " + str(cardlist))

        # prints number of lines after each set of cards
        lines = 1
        linenum = 0
        while linenum < lines:
            if player != numberofpeople:
                print()
            linenum += 1



    y = 0
    while y < 3:
        print()
        y += 1
    return


deal_cards(2, 2)
print()
print(cardlist)
print('ANDREW is the best')