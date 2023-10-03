"""This program runs a game of Blackjack"""
from time import time
from random import Random
import argparse

LOSE_MESSAGE = "You lose!"
WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "Draw!"
MAX_SCORE = 21

def shuffle(deck: list[str], seed: int) -> list[str]:
    """Randomises a deck of cards"""

    copy_of_deck = deck.copy()
    Random(seed).shuffle(copy_of_deck)

    return copy_of_deck


def generate_deck() -> list[str]:
    """Generates a deck of cards and returns them"""

    cards = []
    card_list = ['A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K']
    suit_list = ['S', 'D', 'C', 'H']

    for suit in suit_list:
        for card in card_list:
            cards.append(card+suit)
    return cards


def points_for(cards: list[str]) -> int:
    """Calculates the amount of points for a given list of cards"""

    card_value = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10}
    points = 0

    if len(cards) == 2:
        if cards[0][0] == 'A' and cards[1][0] == 'A' or len(cards) >= 6:
            return MAX_SCORE
        
    for card in cards:
        if card[0] in card_value:
            points += card_value.get(card[0])
    return points


def player_turn(deck: list[str], hand: list[str]) -> bool:
    """
    Asks the player for their next choice and changes the game state
    based on their response of either 'hit' or 'stick'
    """

    print(f"Your hand is {', '.join(hand)} ({points_for(hand)} points)")

    if points_for(hand) >= MAX_SCORE:
        return False

    action = input('What do you want to do? ("hit" or "stick"): ')

    if action == "hit":
        new_card = deck.pop(0)
        hand.append(new_card)
        print('Hitting')
        print(f'You drew {new_card}')
        return True
    
    if action == "stick":
        return False


def dealer_turn(deck: list[str], hand: list[str]) -> bool:
    """
    Dealer turn once the player has completed his turn
    """

    print(f"Dealer's hand is {', '.join(hand)} ({points_for(hand)} points)")

    if points_for(hand) < 17:
        new_card = deck.pop(0)
        hand.append(new_card)
        print('Hitting')
        print(f'Dealer drew {new_card}')
        return True
    
    return False

def game_outcome(player_hand: list[str], dealer_hand: list[str]) -> None:
    if points_for(dealer_hand) > MAX_SCORE:
        print("Dealer busts...")
        print(WIN_MESSAGE)

    elif points_for(player_hand) > points_for(dealer_hand):
        print('You scored higher than the dealer!')
        print(WIN_MESSAGE)

    elif points_for(player_hand) == points_for(dealer_hand):
        print(DRAW_MESSAGE)

    elif points_for(player_hand) < points_for(dealer_hand):
        print('You scored lower than the dealer!')
        print(LOSE_MESSAGE)
    

def play(seed: int) -> None:
    """
    Generates a deck and deals cards to the player and dealer.

    The 'seed' parameter is used to set a specific game. If you play the game
    with seed=313131 it will always have the same outcome (the order the cards are dealt)
    """
    new_deck = generate_deck()
    shuffled_deck = shuffle(new_deck, seed)

    player_hand = [shuffled_deck.pop(0), shuffled_deck.pop(0)]

    is_player_turn = True

    print('Welcome to a game of Blackjack 21 \nShuffling deck.. \nDealing cards...\n')
    print('Player turn begins...')

    while is_player_turn:
        is_player_turn = player_turn(shuffled_deck, player_hand)

    if points_for(player_hand) == MAX_SCORE:
        print(WIN_MESSAGE)
        return
    elif points_for(player_hand) > MAX_SCORE:
        print("Player busts...")
        print(LOSE_MESSAGE)
        return

    dealer_hand = [shuffled_deck.pop(0), shuffled_deck.pop(0)]

    is_dealer_turn = True

    print("Dealers turn begins...")

    while is_dealer_turn:
        is_dealer_turn = dealer_turn(shuffled_deck, dealer_hand)

    game_outcome(player_hand, dealer_hand)
    

def get_seed() -> int:
    """
    You can safely ignore this function. It is used to accept a seed from the command line.
    For example

    python3 blackjack.py --seed 313131

    Would play the game with defined seed of 313131
    """
    parser = argparse.ArgumentParser("blackjack")
    parser.add_argument(
        "--seed", dest='seed', help="The seed that a game will be played with", type=int)
    args = parser.parse_args()
    seed = args.seed

    if seed is None:
        return time()

    return seed


# if __name__ == "__main__":
#     game_seed = get_seed()
#     play(game_seed)

card = 'A'

def points(card) -> int:
    """Gets the correct number of points for a card"""

    card_value = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10}

    for rank in card_value.keys():
        if  card == rank:
            return card_value[rank]


         