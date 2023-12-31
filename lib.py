# Created by Dogan Alp Akbas 25.05.2023
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
# playing = True

# Card class where each Card object has a suit and a rank

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return self.rank + ' of ' + self.suit

# Deck Class store 52 card objects in a list that can later be shuffled

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_all = ''
        for card in self.deck:
            deck_all += '\n' + card.__str__()
        return "The deck has:" +deck_all


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
# Working with either player or dealer card
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):

        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please enter your bet : "))
        except:
            print("Please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips! You have {}". format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()





def show_some(player, dealer):
    print("\n Dealer's Hand: ")
    print("First Card is Hidden ! ")
    print(dealer.cards[1])
    print("\n Player's Hand: ", *player.cards, sep='\n')


def show_all(player, dealer):
    print("\n Dealer's Hand : ", *dealer.cards, sep= '\n')
    print("The total value of Dealer's hand is: {}".format(dealer.value))
    print("\n Player's Hand: ", *player.cards, sep='\n')
    print("The total value of Player's hand is: {}".format(player.value))

def player_busts(player, dealer, chips):
    print("\nPlayer BUST !")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("\nPlayer WIN !")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("\nPlayer WIN ! Dealer BUST !")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("\nDealer WIN ! Player Bust !")
    chips.lose_bet()

def push(player, dealer):
    print("\nDealer and Player tie ! ")

