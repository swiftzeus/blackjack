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
        return card_deck

    def start_game(self):

        #Prompt for user input.
        userInput = input('Do you want to play a game of BlackJack? y/n ')
        userInput = userInput.lower()

        #Validate input.
        while userInput not in ['y', 'n']:
            print('Invalid input. Try again.')
            userInput = input('Do you want to play a game of BlackJack? y/n ')
            userInput = userInput.lower()

        if userInput == 'y':
            print('Your account has been loaded with 20 chips. Good luck.')
            player1_account = 20
            return player1_account
        if userInput == 'n':
            print('Goodbye')
            exit()

    def card(self,deck,x):
        card = ''
        if deck[x][1] == 11:
            card = 'Jack'
        elif deck[x][1] == 12:
            card = 'Queen'
        elif deck[x][1] == 13:
            card = 'King'
        elif deck[x][1] == 14:
            card = 'Ace'
        else:
            card = deck[x][1]
        card = str(deck[x][1]) + ' ' + deck[x][0]
        print(card)
        x += 1
        return (deck[x][1], x)