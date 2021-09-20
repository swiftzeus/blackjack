# This is an attempt to create a game of blackjack.

import random as rd

from BJFuncs import Deal

card_deck = Deal()
account = card_deck.start_game()
if account == 0:
    exit()
else:
    print("You have {} chips.".format(account))

deck = card_deck.card_pack()


