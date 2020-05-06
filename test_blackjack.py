import unittest
import main
from dealer import Dealer
from card import Card

class TestBlackJack(unittest.TestCase):

    def setUp(self):
        self.diamond_ace = Card('D','A')
        self.hearts_king = Card('H','K')
        self.hearts_queen = Card('H','Q')
        self.spade_eight = Card('S','8')
        self.spade_five = Card('S','5')
        self.spade_three = Card('S','3')
    
    def test_dealer_score_under_21(self):
        d = Dealer()
        d.hand = [self.hearts_king,self.spade_three]
        self.assertEqual(d.score(),13)

    def test_dealer_score_over_21(self):
        d = Dealer()
        d.hand = [self.hearts_king,self.spade_three,self.hearts_queen]
        self.assertEqual(d.score(),23)
        
    def test_dealer_score_over_21_with_ace(self):
        d = Dealer()
        d.hand = [self.diamond_ace,self.spade_eight,self.hearts_queen,self.spade_five]
        self.assertEqual(d.score(),24)

    def test_dealer_score_under_21_with_ace(self):
        d = Dealer()
        d.hand = [self.diamond_ace,self.spade_three,self.hearts_queen]
        self.assertEqual(d.score(),14)

if __name__ == '__main__':
    unittest.main()