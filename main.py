from player import Player
from dealer import Dealer
from deck import Deck
import random

def display_board():
    dealer_hand = dealer.list_cards_in_hand()
    player_hand = player.list_cards_in_hand()
    dealer_score = dealer.score()
    player_score = player.score()
    
    dealer_state = 'Dealer[{score}] ${money}\n{hand}\n'.format(hand=dealer_hand,score=dealer_score,money=dealer.bet)
    player_state = '{hand}\nPlayer[{score}] ${money}\n'.format(hand=player_hand,score=player_score,money=player.bankroll)

    print(dealer_state)
    print(player_state)

def deal_starting_cards():
    dealer.hidden_hand.append(deck.draw_card())
    dealer.hand.append(deck.draw_card())
    
    player.hand.append(deck.draw_card())
    player.hand.append(deck.draw_card())

def hit(person):
    person.hand.append(deck.draw_card())

def player_choice():
    while True:
        try:
            choice = input('Dealer: Hit or Stand[H/S]? ').upper()
            if choice != 'H' and choice != 'S':
                raise ValueError
        except ValueError:
            print('Dealer: I don\'t understand that!')
        else:
            break 
    return choice

def take_bet():
    while True:
        try:
            bet = int(input('Dealer: Place your bet. '))
            if player.bankroll - bet > 0:
                print('Dealer: Bet accepted! -{}'.format(bet))
                player.bankroll -= bet
                dealer.bet += bet
            else:
                print('Dealer: Insufficient funds.')
                raise
        except ValueError:
            print('Dealer: Please give me a number!')
        except:
            print('Dealer: You can\'t afford that much!')
        else:
            break 
    return bet

def bust(person):
    if person.score() > 21:
        return True
    else:
        return False

def win():
    # Player gets over 21
    if bust(player):
        print('Dealer: You went bust. Better luck next time. -{}'.format(dealer.bet))
        dealer.bet = 0
    # Player gets a 'natural' blackjack
    elif player.score() == 21 and len(player.hand) == 2:
        print('Dealer: Blackjack!! Bonus winnings for you! +{}'.format(dealer.bet*3))
        player.bankroll += dealer.bet*3
        dealer.bet = 0
    # Player less than 22 but higher than dealer
    elif not bust(player) and player.score() >= dealer.score():
        print('Dealer: Your hand beats mine. Enjoy your winnings! +{}'.format(dealer.bet*2))
        player.bankroll += dealer.bet*2
        dealer.bet = 0
    # Dealer busts, player does not
    elif bust(dealer) and not bust(player):
        print('Dealer: I\'m bust. Enjoy your winnings! +{}'.format(dealer.bet*2))
        player.bankroll += dealer.bet*2
        dealer.bet = 0
    # Dealer and Player same score
    elif not bust(player) and player.score() == dealer.score():
        print('Dealer: Nobody wins. You get your bet back. +{}'.format(dealer.bet))
        player.bankroll += dealer.bet
        dealer.bet = 0
    else:
        print('Dealer: Better luck next time. -{}'.format(dealer.bet))
        dealer.bet = 0
    
def reset(player,dealer):
    player.hand = []
    dealer.hand = []
    dealer.hidden_hand = []
    dealer.reveal = False

if __name__ == "__main__":
    dealer = Dealer()

    dealer.welcome()

    while True:
        try:
            starting_bet = int(input('Dealer: Whats your bankroll? '))
        except ValueError:
            print('Please enter a number!\n')
        else:
            break

    player = Player(starting_bet)

    replay = True

    while replay:
        deck = Deck()

        print('\nDealer: I\'ll shuffle the deck.')
        deck.shuffle_cards()

        bet = take_bet()

        print('Dealer: Time to deal cards.\n')
        deal_starting_cards()

        while True:
            display_board()

            choice = player_choice()

            if choice == 'H':
                hit(player)
                if bust(player):
                    print('\nDealer: You went bust!\n')
                    break
            else:
                break

        dealer.reveal = True
        
        if not bust(player):
            print('\nDealer: My turn.\n')

            while dealer.score() < 17:
                hit(dealer)

        display_board()
        win()
        
        while True:
            answer = input('\nDealer: Another round[Y/N]? ').upper()

            if answer == 'N':
                replay = False
                break
            elif answer == 'Y':
                reset(player,dealer)
                break
            else:
                print('\nDealer: I didn\'t understand that.')
