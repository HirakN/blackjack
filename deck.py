from card import Card 
import random

'''
The deck represents a full standard deck of card objects.
'''
class Deck():
    test_var = 1
    def __init__(self):
        self.cards = []

        for suit in ['H','D','C','S']:
            for rank in list(map(str,range(2,11))):
                self.cards.append(Card(suit,rank))

            for rank in ['J','Q','K','A']:
                self.cards.append(Card(suit,rank))

    def __len__(self):
        return len(self.cards)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0)

if __name__ == "__main__":
    d = Deck()
    print(len(d))
    h = d.cards
    print(type(d.cards))
    for card in d.cards:
        print(card)