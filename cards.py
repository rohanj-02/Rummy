from enum import Enum
from enum import IntEnum
import random
import copy

class Suit(Enum):

    SPADES = 'spades'
    HEARTS = 'hearts'
    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'

class Value(IntEnum):

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Card():

    def __init__(self, card_value, card_suit):
        self.value = card_value
        self.suit = card_suit

    def display(self):
        print("Suit: " , self.suit)
        print("Value: ", self.value)

def create_deck():
    deck = []
    for s in Suit:
        for v in Value:
            deck.append(Card(Value(v),Suit(s)))
    return deck

def draw_card(deck):
    random_card = random.randint(0, len(deck) - 1)
    return deck.pop(random_card)
    pass

def print_deck(deck):
    for i in deck:
        print("Suit: ", i.suit)
        print("Value: ", i.value )

full_deck = create_deck()
working_deck = copy.deepcopy(full_deck)

drawn_card = draw_card(working_deck)
drawn_card.display()
print_deck(working_deck)
print_deck(full_deck)
