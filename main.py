# This is an attempt to create a game of blackjack.

import random as rd

class Deal():

    def __init__(self):
        pass

    def card_pack(self):

        suits = 0
        card_deck = []
        card = []
        while suits <= 4:
            value = 0
            suits += 1
            while value <= 13:
                value += 1
                if suits == 1:
                    card = ['Clubs', value]
                if suits == 2:
                    card = ['Spades', value]
                if suits == 3:
                    card = ['Hearts', value]
                if suits == 4:
                    card = ['Diamonds', value]
                card_deck.append(card)
        rd.shuffle(card_deck)
        return (card_deck)

x = 0
while x == 0:
    x = int(input('Do you want to play a game of BlackJack? '))
    if x == 0:
        print('works')
    else:
        print('finish')


card_deck = Deal()
deck = card_deck.card_pack()


