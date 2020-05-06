import random

'''
Dealer has hand of cards and a hidden hand which is not revealed to the player
'''
class Dealer():
    def __init__(self):
        # Lists of card objects
        self.hand = []
        self.hidden_hand = []
        self.reveal = False
        self.bet = 0

    def welcome(self):
        print('Dealer: Welcome to blackjack!')

    def list_cards_in_hand(self):
        if self.reveal:
            cards_list = [str(card) for card in self.hand + self.hidden_hand]
        else:
            cards_list = [str(card) for card in self.hand]
        return ' '.join(cards_list)

    def score(self):
        if self.reveal:
            card_ranks = [card.rank for card in self.hand + self.hidden_hand]
        else:
            card_ranks = [card.rank for card in self.hand]

        score = 0
        aces = 0
        
        for rank in card_ranks:
            if rank in list(map(str,range(2,11))):
                score += int(rank)
            elif rank in ['J','Q','K']:
                score += 10
            elif rank == 'A':
                aces += 1

        for ace in range(aces):
            if score < 11:
                score += 11
            else:
                score += 1
        
        return score
                
