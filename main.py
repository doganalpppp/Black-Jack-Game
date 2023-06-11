# Created by Dogan Alp Akbas 25.05.2023

# The game has one player versus a computer dealer
# The game keep track of the player's total money

from lib import Card
from lib import Deck, Hand, Chips
from lib import hit
from lib import take_bet
from lib import show_some, show_all
from lib import player_busts, dealer_busts, dealer_wins, player_wins ,push
playing =True

def hit_or_stand(deck, hand):
    global playing

    while True:
        ask_hit = input("You have {}. Do you want to hit another card ? (Y/N) : ".format(hand.value))
        if ask_hit == 'Y' or ask_hit == 'y':
            hit(deck, hand)

        elif ask_hit == 'N' or ask_hit == 'n':
            print("You stay with {} in your hand".format(hand.value))
            playing = False

        else:
            print("Please provide a Y or N")
            continue
        break



while True:
    print("Welcome to BlackJack Game! Your dealer's name will be Alp. Enjoy while you are playing !")
    print("============ HAVE FUN =============")
    new_deck = Deck()
    new_deck.shuffle()

    player = Hand()

    player.add_card(new_deck.deal())
    player.add_card(new_deck.deal())

    dealer = Hand()
    dealer.add_card(new_deck.deal())
    dealer.add_card(new_deck.deal())

    player_chips = Chips()
    take_bet(player_chips)
    show_some(player, dealer)

    while playing:

        hit_or_stand(new_deck, player)
        show_some(player, dealer)
        if player.value > 21:
            player_busts(player, dealer, player_chips)
            break

    if player.value <= 21:
        while dealer.value < player.value:
            hit(new_deck, dealer)

        show_all(player, dealer)

        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, player_chips)
        elif dealer.value < player.value:
            player_wins(player, dealer, player_chips)
        else:
            push(player, dealer)

    print("Player total chips are {}".format(player_chips.total))

    new_game = input("Would you like to play another hand ? (Y/N)")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing !")
        break






