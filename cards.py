from enum import Enum
import random
import copy

class Suit(Enum):
    """
        An Enum object corresponding to the suits in a playing card Deck.
    """
    SPADES = 'spades'
    HEARTS = 'hearts'
    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'

class Rank(Enum):
    """
        An Enum object corresponding to the ranks found in a playing card deck.
    """
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
    """
        It represents a card in a playing card deck

        Object Attributes:
            rank, suit : Enums of Rank and Suit

        Object Methods:
            display(): Displays the suit and rank of the playing cards
            __str__() : Overloading of the str() operator. str(card) gives "suit-rank"
    """
    def __init__(self, card_rank, card_suit):
        self.rank = card_rank
        self.suit = card_suit

    def __str__(self):
        """
            Overloading of the str() operator. str(card) gives "suit-rank"
        """
        return str(self.suit.value) + "-" + str(self.rank.value)

    def display(self):
        """
            Displays the suit and rank of the playing card
        """
        print("Suit: " , self.suit)
        print("Rank: ", self.rank)

class Deck():
    """
        A deck object represents the playing cards in the deck.

        Object Attributes:
            cards[] : a list storing all the cards currently in the deck
            discarded[] : a list storing all the cards that have been discarded

        Object Methods:
            draw_card() : Draws a card from the deck and returns it.
            display() : Displays the remaining deck of cards.
            suffle_cards() : Shuffles the cards in the deck.
    """
    def __init__(self, no_of_decks):

        self.cards = []
        self.discarded = []
        for i in range(no_of_decks):
            for s in Suit:
                for r in Rank:
                    self.cards.append(Card(Rank(r),Suit(s)))

    def draw_card(self):
        """
            Draws a card from the deck and returns it.
        """
        random_card = random.randint(0, len(self.cards) - 1)
        self.discarded.append(random_card)
        return self.cards.pop(random_card)

    def display(self):
        """
            Displays the remaining deck of cards.
        """
        for i in self.cards:
            print("Suit: ", i.suit)
            print("Rank: ", i.rank )
        return None

    def shuffle_cards(self):
        """
            Shuffles the cards in the deck.
        """
        random.shuffle(self.cards)
        return None

class Player():
    """
        Object of this classes represents a player.

        Object Attributes:
            name : name of the player
            score : score of the player
            hand[] : a list containing all the cards player has in their hand
            turn : a boolean to check if it is the player's turn or not

        Object Methods:
            discard(card) : discards card from player's hand

    """

    def __init__(self, name, score = 0, hand = None):
        self.name = name
        self.score = score
        self.hand = hand
        self.turn = False

    def discard(self, card):
        """
            Discards card from player's hand.

            Parameters:
                card : the card to be discarded from the player's hand.
        """
        if card in self.hand:
            self.hand.pop(card)
        return None

full_deck = Deck(2)
working_deck = Deck(2)
drawn_card = working_deck.draw_card()
print(str(drawn_card))
# drawn_card.display()
# working_deck.display()
# working_deck.shuffle_cards()
# working_deck.display()
