from random import Random

MAX_SCORE = 21


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit.capitalize()
        self.card_points = self.points

    def to_string(self) -> str:
        """Returns the correct string to represent the hand"""
        return f'{self.rank}{self.suit}'

    @property
    def points(self) -> int:
        """Gets the correct number of points for a card"""

        card_value = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10}

        for rank in card_value.keys():
            if self.rank == rank:
                return card_value[rank]


class Hand:
    def __init__(self, cards: list) -> None:
        all_cards = all(isinstance(card, Card) for card in cards)

        if (not all_cards):
            raise Exception('A Hand can only contain Cards')

        self.cards = cards

    @property
    def points(self) -> int:
        """Calculates the points for a hand of cards"""

        points_sum = 0

        if len(self.cards) == 2:
            if self.cards[0].rank == 'A' and self.cards[1].rank == 'A' or len(self.cards) >= 6:
                return MAX_SCORE

            
        for card in self.cards:
                points_sum += card.points

        return points_sum
    

class Deck:
    def __init__(self) -> None:
        self.deck = self.cards


    @property
    def cards(self) -> list[Card]:
        """Generates a deck of cards and returns them"""

        deck = []

        card_list = ['A', '2', '3', '4', '5', '6',
                    '7', '8', '9', '10', 'J', 'Q', 'K']
        suit_list = ['S', 'D', 'C', 'H']

        for suit in suit_list:
            for card in card_list:
                deck.append(Card(card,suit))
        
        return deck

    def draw(self) -> Card:
        """Removes and returns the top card from the deck"""
        return self.deck.pop(0)

    def shuffle(self) -> None:
        """Shuffles the cards in this deck"""
        copy_of_deck = self.deck.copy()
        Random().shuffle(copy_of_deck)

        return copy_of_deck

deck1 = Deck()

