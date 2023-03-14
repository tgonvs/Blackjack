import random

def deck():
    deck = []
    suits = ['♠', '♣', '♦', '♥']
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        for card in cards:
            deck.append(card + suit)
    return deck

def deal_hand(deck):
    return [deck.pop(), deck.pop()]

def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank.isnumeric():
            value += int(rank)
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += 10
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def play_again():
    while True:
        again = input('Do you want to play again? (Y/N) ')
        if again.lower() == 'y':
            return True
        elif again.lower() == 'n':
            return False
        else:
            print('Invalid input.')

def blackjack():
    while True:
        print('Welcome to Blackjack!')
        d = deck()
        random.shuffle(d)
        player_hand = deal_hand(d)
        dealer_hand = deal_hand(d)
        print(f'Dealer shows: {dealer_hand[0]}')
        while True:
            print(f'Your hand: {player_hand} ({hand_value(player_hand)})')
            if hand_value(player_hand) > 21:
                print('Bust!')
                if play_again():
                    break
                else:
                    return
            action = input('What would you like to do? (H)it or (S)tay ')
            if action.lower() == 'h':
                player_hand.append(d.pop())
            elif action.lower() == 's':
                break
            else:
                print('Invalid input.')
        print(f'Dealer shows: {dealer_hand} ({hand_value(dealer_hand)})')
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(d.pop())
            print(f'Dealer draws: {dealer_hand[-1]} ({hand_value(dealer_hand)})')
        if hand_value(dealer_hand) > 21:
            print('Dealer busts!')
        elif hand_value(dealer_hand) >= hand_value(player_hand):
            print('Dealer wins!')
        else:
            print('You win!')
        if play_again():
            continue
        else:
            return

blackjack()
