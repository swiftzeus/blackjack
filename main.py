# This is an attempt to create a game of blackjack.

import random as rd

from BJFuncs import Deal

card_deck = Deal()
account = card_deck.start_game()
print("You have {} chips.".format(account))
deck = card_deck.card_pack()

i = 0
x = 0
while i < 2:
    card, x = card_deck.card(deck,x)
    i += 1




