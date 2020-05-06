'''
Card object holds the rank and suit of the card
'''
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
       return self.suit+self.rank