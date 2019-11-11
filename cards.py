from enum import Enum
import random
import copy

HAND_SIZE = 13
SUIT = ['spades', 'hearts', 'clubs', 'diamonds']
RANK = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VAL = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 11, 'Q' : 12, 'K' : 13,'A' : 14 }
#global functions
def sort_by_suit(hand):
    """
        Sorts the provided hand on the basis of suits.
        Parameters:
            hand : The hand of cards to be sorted
    """
    hand.sort(key = lambda x: x.suit)
    return None

def sort_by_rank(hand):
    """
        Sorts the provided hand on the basis of ranks.
        Parameters:
            hand : The hand of cards to be sorted
    """
    hand.sort(key = lambda x: RANK_VAL[x.rank])
    return None

def sort_hand(hand):
    """
        Sorts the given hand of cards by suit and then rank.
        Parameters:
            hand : The hand of cards to be sorted
        Returns :
            hand : the sorted hand by suit and then by rank
    """
    sort_by_suit(hand)
    club_hand = []
    diamond_hand = []
    spades_hand = []
    hearts_hand = []
    for i in hand:
        if i.suit.value == 'clubs':
            club_hand.append(i)
        if i.suit.value == 'diamonds':
            diamond_hand.append(i)
        if i.suit.value == 'hearts':
            heart_hand.append(i)
        if i.suit.hand == 'spades':
            spades_hand.append(i)
    sort_by_rank(club_hand)
    sort_by_rank(diamond_hand)
    sort_by_rank(spades_hand)
    sort_by_hand(hearts_hand)
    sorted_hand = spades_hand + hearts_hand + club_hand + diamond_hand
    return sorted_hand

def is_set(set):
    """
        Checks if the provided set of cards form a set(three cards of the same value).
        Parameters:
            set : a set of cards
        Returns:
            True if set forms Set.
            else False
    """
    if len(set) != 3:
        return False
    # for i in range(len(set)): # moving joker to the end
    #     if set[i].is_joker():
    #         set.append(set.pop(i))
    for i in range(len(set)-1):
        if not set[i].is_joker():
            if set[i].rank != set[i+1].rank:
                return False
    return True

def is_sequence(set):
    """
        Checks if the provided set of cards form a pure sequence.
        Parameters:
            set : a set of cards
        Returns:
            True if set forms pure sequence
            else False
    """
    RANK_VAL['A'] = 14

    for i in range(len(set)):
        if set[i].suit != set[0].suit:
            return False

    sort_rank(set)
    if set[0].rank == '2':
        RANK_VAL['A'] = 1
        sort_rank(set)

    for i in range(len(set) - 1):
        if set[i].rank != set[i + 1].rank - 1:
             return False
    pass

def is_impure_sequence(set):
    """
        Checks if the provided set of cards form an impure sequence.
        Parameters:
            set : a set of cards
        Returns:
            True if set forms impure sequence
            else False
    """
    RANK_VAL['A'] = 14
    jokers = []
    for i in range(len(set)):
        if set[i].is_joker():
            jokers.append(set.pop(i))
            no_of_jokers += 1

    sort_rank(set)
    if set[0].rank == '2' or set[0].rank == '3':
        RANK_VAL['A'] = 1
        sort_rank(set)

    for i in range(len(set) - 1):
        if set[i].rank != set[i + 1].rank - 1:
            if len(jokers) > 0:
                j = joker.pop(0)
                j.rank = set[i].rank + 1
                set = [:i] + j + [i:]
            if len(jokers) == 0:
                return
    pass

# class Suit(Enum):
#     """
#         An Enum object corresponding to the suits in a playing card Deck.
#     """
#     SPADES = 'spades'
#     HEARTS = 'hearts'
#     CLUBS = 'clubs'
#     DIAMONDS = 'diamonds'
#
# class Rank(Enum):
#     """
#         An Enum object corresponding to the ranks found in a playing card deck.
#     """
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#     FIVE = 5
#     SIX = 6
#     SEVEN = 7
#     EIGHT = 8
#     NINE = 9
#     TEN = 10
#     JACK = 11
#     QUEEN = 12
#     KING = 13
#     ACE = 14

class Card():
    """
        It represents a card in a playing card deck

        Object Attributes:
            rank, suit : Enums of Rank and Suit
            isjoker : boolean true if card is joker else fase

        Object Methods:
            display(): Displays the suit and rank of the playing cards
            __str__() : Overloading of the str() operator. str(card) gives "suit-rank"
    """
    def __init__(self, card_rank, card_suit):
        self.rank = card_rank
        self.suit = card_suit
        self.isjoker = False

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

    def is_joker(self):
        """
            Returns true when card is joker else false
        """
        return self.isjoker

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
            set_joker() : Sets a random card as joker and marks corresponding cards as joker.
    """
    def __init__(self, no_of_decks):

        self.cards = []
        self.discarded = []
        for i in range(no_of_decks):
            for s in SUIT:
                for r in RANK:
                    self.cards.append(Card(r, s))

    def draw_card(self):
        """
            Draws a card from the deck and returns it.
        """
        random_card = random.randint(0, len(self.cards) - 1)
        self.discarded.append(self.cards[random_card])
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

    def set_joker(self):
        """
            Sets a random card as joker and returns it. Also sets each joker card's isjoker to True.
        """
        joker = random.randint(0,len(self.cards) - 1)
        joker = self.cards[joker]
        for i in range(len(self.cards)):
            if self.cards[i].rank == joker.rank:
                self.cards[i].isjoker = True
        return joker

class Player():
    """
        Object of this classes represents a player.

        Object Attributes:
            name : name of the player
            score : score of the player
            hand[] : a list containing all the cards player has in their hand
            turn : a boolean to check if it is the player's turn or not

        Object Methods:
            discard_card(card) : discards card from player's hand
            deal_card(deck): Deals the player 13 cards from deck
            shut_game():
    """

    def __init__(self, name, score = 0, hand = None):
        self.name = name
        self.score = score
        self.hand = hand
        self.turn = False

    def discard_card(self, card):
        """
            Discards card from player's hand.

            Parameters:
                card : the card to be discarded from the player's hand.
        """
        if card in self.hand:
            self.hand.pop(self.hand.index(card))
        return None

    def deal_cards(self, deck):
        """
            Deals 13 cards to the player.
            Parameters:
                deck : The deck in play
        """
        for i in range(HAND_SIZE):
            self.hands.append(deck.draw_card())
        return None

    def shut_game(self):
        """
            Shut the game by player.
            Returns True if player can shut the round. Else False
        """

        return False

# full_deck = Deck(2)
# working_deck = Deck(2)
# drawn_card = working_deck.draw_card()
# print(str(drawn_card))
# drawn_card.display()
# working_deck.display()
# working_deck.shuffle_cards()
# working_deck.display()
