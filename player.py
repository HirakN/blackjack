'''
The player class represents the human player of the game
'''
class Player():
    other_bankroll = 50
    def __init__(self,bankroll):
        self.bankroll = bankroll
        self.hand = []
    
    def list_cards_in_hand(self):
        cards_list = [str(card) for card in self.hand]
        return ' '.join(cards_list)

    def score(self):
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