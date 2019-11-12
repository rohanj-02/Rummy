from enum import Enum
import random
import copy

HAND_SIZE = 13
SUIT = ['spades', 'hearts', 'clubs', 'diamonds']
RANK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
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
    hand.sort(key = lambda x: x.rank_val)
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
    clubs_hand = []
    diamonds_hand = []
    spades_hand = []
    hearts_hand = []
    for i in hand:
        if i.suit == 'clubs':
            clubs_hand.append(i)
        if i.suit == 'diamonds':
            diamonds_hand.append(i)
        if i.suit == 'hearts':
            hearts_hand.append(i)
        if i.suit == 'spades':
            spades_hand.append(i)
    sort_by_rank(clubs_hand)
    sort_by_rank(diamonds_hand)
    sort_by_rank(spades_hand)
    sort_by_rank(hearts_hand)
    sorted_hand = spades_hand + hearts_hand + clubs_hand + diamonds_hand
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
    if not (len(set) == 3 or len(set) == 4):
        return False
    for i in range(len(set)-1):
        if not set[i].is_joker():
            if set[i].rank != set[i+1].rank or set[i].suit == set[i+1].suit:
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
    for i in range(len(set)):
        if set[i].suit != set[0].suit:
            return False

    for i in range(len(set)):
        if set[i].rank_val == 1:
            set[i].rank_val = 14

    sort_by_rank(set)
    if set[0].rank == '2':
        for i in range(len(set)):
            if set[i].rank_val == 14:
                set[i].rank_val = 1
        sort_by_rank(set)

    for i in range(len(set) - 1):
        if set[i].rank_val != set[i + 1].rank_val - 1:
             return False
    return True
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
    jokers = []
    no_jokers = 0
    i = 0
    set = copy.deepcopy(set)
    while i < len(set):
        if set[i].is_joker():
            jokers.append(set.pop(i))
            no_jokers += 1
            i -= 1
        i += 1
    if no_jokers >= 2:
        return False

    for i in range(len(set)):
        if set[i].rank_val == 1:
            set[i].rank_val = 14

    sort_by_rank(set)
    if set[0].rank == '2' or set[0].rank == '3':
        for i in range(len(set)):
            if set[i].rank_val == 14:
                set[i].rank_val = 1
        sort_by_rank(set)

    i = 0
    while i < len(set) - 1:
        if set[i].rank_val !=set[i + 1].rank_val - 1:
            if no_jokers == 0:
                return False
            if no_jokers > 0:
                no_jokers -= 1
                j = jokers[0]
                j.rank_val = set[i].rank_val + 1
                set = set[:i + 1] + [j] + set[i + 1:]
                print(list(map(str, set)))
        i += 1

    jokers[0].rank_val = RANK_VAL[jokers[0].rank]
    return True
    pass

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
    def __init__(self, card_rank, card_suit, isjoker = False):
        self.rank = card_rank
        self.suit = card_suit
        self.isjoker = isjoker
        self.rank_val = RANK_VAL[self.rank]
        self.ismatched = False

    def __str__(self):
        """
            Overloading of the str() operator. str(card) gives "suit-rank"
        """
        return str(self.suit) + "-" + str(self.rank)

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

    def is_matched(self):
        """
            Returns true when card is matched else false
        """
        return self.ismatched


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

    def set_joker(self, jok = None):
        """
            Sets a random card as joker and returns it. Also sets each joker card's isjoker to True.
        """
        if jok == None:
            joker = random.randint(0,len(self.cards) - 1)
            joker = self.cards[joker]
        else:
            joker = jok
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

    def __init__(self, name, score = 0, hand = []):
        self.name = name
        self.score = score
        self.hand = hand
        self.turn = False

    def __str__(self):
        """
            Returns the player's hand as suit-rank suit-rank etc.
        """
        ans = ""
        for i in self.hand:
            ans += str(i) + " "
        return ans

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
            self.hand.append(deck.draw_card())
        return None

    def shut_game(self):
        """
            Shut the game by player.
            Returns True if player can shut the round. Else False
        """

        return False

full_deck = Deck(2)
player1 = Player('Rohan')
jok = full_deck.set_joker(Card('J','spades'))
player1.deal_cards(full_deck)
print(str(player1))
player1.hand = sort_hand(player1.hand)
print(str(player1))
# print(str(jok))
#testing is sequence is set is impure sequence
Set1 = [Card('J', 'hearts'), Card('J', 'hearts'), Card('J', 'clubs')]
Set2 = [Card('J', 'spades'), Card('Q', 'hearts'), Card('K', 'clubs')]
Set3 = [Card('2', 'spades'), Card('A', 'spades'), Card('3','spades')]
Set4 = [Card('J', 'spades'), Card('J', 'hearts'), Card('J', 'clubs')]
Set5 = [Card('K', 'spades',True), Card('A', 'spades'), Card('Q','spades'), Card('2', 'spades')]
Set6 = [Card('J', 'spades', True), Card('5', 'clubs'), Card('6', 'clubs')]
print(is_set(Set1))
print(is_set(Set4))
print(is_sequence(Set2), is_sequence(Set5))
print(is_impure_sequence(Set5), is_impure_sequence(Set6))
# print(list(map(str, Set5)))
