import random
from copy import deepcopy
import copy
import pygame
from button import Button

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
    # if not (len(set) == 3 or len(set) == 4):
    if len(set) != 3:
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
    if len(set) < 3:
        return False
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
    if len(set) < 3:
        return False
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
        if set[i].suit != set[0].suit:
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
        if set[i].rank_val != set[i + 1].rank_val - 1:
            if no_jokers == 0:
                return False
            if no_jokers > 0:
                no_jokers -= 1
                j = jokers[0]
                j.rank_val = set[i].rank_val + 1
                set = set[:i + 1] + [j] + set[i + 1:]
        i += 1
    if len(jokers) > 0:
        jokers[0].rank_val = RANK_VAL[jokers[0].rank]
    return True
    pass

def calculate_score(card, hand):
    """
        Calculates the score of the card in the hand. Higher the score of the card the more are the possibilities of combinations of that card.
        Added to implement the computer logic.
    """

    if card.isjoker:
        return 50
    hand == copy.deepcopy(hand)
    score = 0

    if card.rank == '2':
        for i in range(len(hand)):
            if hand[i].rank_val == 14:
                hand[i].rank_val == 1

        card_three = Card('3', card.suit, card.isjoker)
        if card_three.isIn(hand):
            score += 10
        card_ace = Card('A', card.suit, card.isjoker)
        if card_ace.isIn(hand):
            score += 10
        card_four = Card('4', card.suit, card.isjoker)
        if card_four.isIn(hand):
            score += 5
        for i in SUIT:
            if i != card.suit:
                same_rank_card = Card(card.rank, i, card.isjoker)
                if same_rank_card.isIn(hand):
                    score += 10
        return score

    if card.rank == '3':
        for i in range(len(hand)):
            if hand[i].rank_val == 14:
                hand[i].rank_val == 1

    if card.rank == 'K':
        for i in range(len(hand)):
            if hand[i].rank_val == 1:
                hand[i].rank_val == 14

        card_queen = Card('Q', card.suit, card.isjoker)
        if card_queen.isIn(hand):
            score += 10
        card_ace = Card('A', card.suit, card.isjoker)
        if card_ace.isIn(hand):
            score += 10
        card_jack = Card('J', card.suit, card.isjoker)
        if card_jack.isIn(hand):
            score += 5
        for i in SUIT:
            if i != card.suit:
                same_rank_card = Card(card.rank, i, card.isjoker)
                if same_rank_card.isIn(hand):
                    score += 10
        return score

    if card.rank == 'Q':
        for i in range(len(hand)):
            if hand[i].rank_val == 1:
                hand[i].rank_val == 14

    if card.rank == 'A':
        card_queen = Card('Q', card.suit, card.isjoker)
        if card_queen.isIn(hand):
            score += 5
        card_king = Card('K', card.suit, card.isjoker)
        if card_king.isIn(hand):
            score += 10
        card_two = Card('2', card.suit, card.isjoker)
        if card_two.isIn(hand):
            score += 10
        card_three = Card('3', card.suit, card.isjoker)
        if card_three.isIn(hand):
            score += 5
        for i in SUIT:
            if i != card.suit:
                same_rank_card = Card(card.rank, i, card.isjoker)
                if same_rank_card.isIn(hand):
                    score += 10
        return score

    list_cards = []
    for i in range(-2,3):
        if i != 0 :
            if int(card.rank_val) + i == 1:
                list_cards.append(Card('A', card.suit, card.isjoker))
            elif int(card.rank_val) + i <= 10:
                list_cards.append(Card(str(int(card.rank_val) + i), card.suit, card.isjoker))
            elif int(card.rank_val) + i == 11:
                list_cards.append(Card('J', card.suit, card.isjoker))
            elif int(card.rank_val) + i == 12:
                list_cards.append(Card('Q', card.suit, card.isjoker))
            elif int(card.rank_val) + i == 13:
                list_cards.append(Card('K', card.suit, card.isjoker))
            elif int(card.rank_val) + i == 14:
                list_cards.append(Card('A', card.suit, card.isjoker))
    for i in range(len(list_cards)):
        if list_cards[i].isIn(hand):
            if i == 2 or i == 1:
                score += 10
            else:
                score += 5
    for i in SUIT:
        if i != card.suit:
            same_rank_card = Card(card.rank, i, card.isjoker)
            if same_rank_card.isIn(hand):
                score += 10
    return score

def add_points(l):
    points = 0
    for i in l:
        if type(i) == Card:
            if i.isjoker:
                points += 0
            elif i.rank_val <= 10:
                points += i.rank_val
            else:
                points += 10
    return points


class Card():
    """
        It represents a card in a playing card deck

        Object Attributes:
            rank, suit : Rank and Suit
            isjoker : boolean true if card is joker else fase

        Object Methods:
            display(): Displays the suit and rank of the playing cards
            __str__() : Overloading of the str() operator. str(card) gives "suit-rank"
    """
    def __init__(self, card_rank, card_suit, isjoker = False):
        self.position = (0,0)
        img = pygame.image.load('assets/back.png')
        # img = pygame.transform.scale(img, (img.get_width()//4, img.get_height()//4))
        self.is_hover = False
        self.is_clicked = False
        self.width = img.get_width()
        self.height = img.get_height()
        self.rank = card_rank
        self.suit = card_suit
        self.isjoker = isjoker
        self.offset = 0
        self.rank_val = RANK_VAL[self.rank]
        self.ismatched = False

    def __str__(self):
        """
            Overloading of the str() operator. str(card) gives "suit-rank"
        """
        return str(self.suit) + "-" + str(self.rank)

    def isIn(self, l):
        """
            Returns the index at which given card is in a list. If not present it returns False
        """
        for i in range(len(l)):
            if self.suit == l[i].suit and self.rank == l[i].rank:
                return i
        return False
        pass

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

    def show(self):
        """
            Returns image object to render the card on the screen
        """
        img_name = str(self)
        card_img = pygame.image.load("assets/"+img_name+".png")
        # card_img = pygame.transform.scale(card_img, (card_img.get_width()//4, card_img.get_height()//4))
        return card_img

    def check(self, mouse_pos, event):
        """
            To check if the mouse is hovering on the card or clicking the card.
        """
        if mouse_pos[0] >= self.position[0] and mouse_pos[0] <= self.position[0] + self.width and mouse_pos[1] >= self.position[1] and mouse_pos[1] <= self.position[1] + self.height:
            self.is_hover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_hover = False
                self.is_clicked = True
            else:
                self.is_clicked = False
        else:
            self.is_clicked = False
            self.is_hover = False


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
        self.joker = None
        self.pile = []
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
            self.joker = self.cards[joker]
        else:
            for i in range(len(self.cards)):
                if self.cards[i].rank == jok.rank and self.cards[i].suit == jok.suit:
                    self.joker = jok
                    joker = i
        self.cards.pop(joker)
        for i in range(len(self.cards)):
            if self.cards[i].rank == self.joker.rank:
                self.cards[i].isjoker = True
        return self.joker

    def update_pile(self, card):
        """
            Updates the card at the open pile of cards.
        """
        self.pile.insert(0, copy.deepcopy(card))
        return None

    def show_pile(self):
        """
            Returns the image of the card at the pile.
        """
        img_list = []
        for card in range(len(self.pile)):
            if card <= 2 :
                img = pygame.image.load("assets/"+str(self.pile[card])+".png")
                img_list.append(img)
        return img_list


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
            declare_game():
    """

    def __init__(self, name, score = 0, hand = []):
        self.name = name
        self.score = score
        self.hand = hand
        self.turn = False
        self.allPossible = {}

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
        if len(self.hand) > 13:
            for i in range(len(self.hand)):
                if self.hand[i].suit == card.suit and self.hand[i].rank == card.rank and self.hand[i].isjoker == card.isjoker:
                    c = self.hand.pop(i)
                    # print(c)
                    return None
        return None

    def deal_cards(self, deck):
        """
            Deals 13 cards to the player.
            Parameters:
                deck : The deck in play
        """
        hand = []
        for i in range(HAND_SIZE):
            hand.append(deck.draw_card())
        self.hand = hand
        return None

    def draw_card(self, card):
        """
            Adds given card to the player's hand
        """
        if len(self.hand) <= 13 :
            self.hand.append(Card(card.rank, card.suit, card.isjoker))
        pass

    def fill_all_possible(self):
        """
            Fills the allPossible attribute as a dictionary containing combination of hands and whether they form a set/ sequence or not
        """
        self.allPossible = {}
        working_hand = copy.deepcopy(self.hand)
        for i in range(len(working_hand)):
            for j in range(len(working_hand)):
                for k in range(len(working_hand)):
                    if i != j and i != k and j != k:
                        small_set = [working_hand[i], working_hand[j], working_hand[k]]
                        small_set = sort_hand(small_set)
                        small_set_tuple = tuple(small_set)
                        if small_set_tuple not in self.allPossible.keys():
                            if is_sequence(small_set):
                                self.allPossible[small_set_tuple] = "pure"
                            elif is_impure_sequence(small_set):
                                self.allPossible[small_set_tuple] = "impure"
                            elif is_set(small_set):
                                self.allPossible[small_set_tuple] = "set"
                            else:
                                self.allPossible[small_set_tuple] = 'none'

                    for l in range(len(working_hand)):
                        if i != j and j != k and k != l and i != l:
                            set = [working_hand[i],working_hand[j],working_hand[k],working_hand[l]]
                            set = sort_hand(set)
                            set_tuple = tuple(set)
                            if set_tuple not in self.allPossible.keys():
                                if is_sequence(set):
                                    self.allPossible[set_tuple] = "pure"
                                elif is_impure_sequence(set):
                                    self.allPossible[set_tuple] = 'impure'
                                elif is_set(set):
                                    self.allPossible[set_tuple] = 'set'
                                else:
                                    self.allPossible[set_tuple] = 'none'
        pass

    def declare_game(self):
        """
            declare the game by player.
            Returns True if player can declare the round. Else False
        """
        pure_four = []
        pure_three = []
        impure_three = []
        impure_four = []
        set_three = []
        self.fill_all_possible()
        for k,v in self.allPossible.items():
            if len(k) == 4 and v == 'pure':
                pure_four.append(k)
            elif len(k) == 4 and v == 'impure':
                impure_four.append(k)
            elif len(k) == 3 and v == 'pure':
                pure_three.append(k)
            elif len(k) == 3 and v == 'impure':
                impure_three.append(k)
            elif len(k) == 3 and v == 'set':
                set_three.append(k)
        fillers_impure_four = pure_three + impure_three + set_three
        sequences_three = pure_three + impure_three
        hand_copy = copy.deepcopy(self.hand)
        for i in range(len(impure_four)): # if sequence of 4 is impure
            hand_without_impure = copy.deepcopy(hand_copy)
            for j in range(len(impure_four[i])): # to make hand without impure
                check = impure_four[i][j].isIn(hand_without_impure)
                if type(check) != type(False):
                    hand_without_impure.pop(check)
            if len(hand_without_impure) == 10:
                first_life = impure_four[i]
                for k in range(len(pure_three)):
                    hand_without_runs = copy.deepcopy(hand_without_impure)
                    for j in range(len(pure_three[k])): # hand_without runs =  hand - 4 impure - 3 pure
                        check2 = pure_three[k][j].isIn(hand_without_runs)
                        if type(check2) != type(False):
                            hand_without_runs.pop(check2)
                        else:
                            break
                    if len(hand_without_runs) == 7:
                        second_life = pure_three[k]
                        for l in range(len(fillers_impure_four)):
                            for m in range(len(fillers_impure_four)):
                                final_hand = copy.deepcopy(hand_without_runs)
                                for j in fillers_impure_four[l]:
                                    check3 = j.isIn(final_hand)
                                    if type(check3) != type(False):
                                        final_hand.pop(check3)
                                for j in fillers_impure_four[m]:
                                    check3 = j.isIn(final_hand)
                                    if type(check3) != type(False):
                                        final_hand.pop(check3)
                                extras = [fillers_impure_four[l], fillers_impure_four[m]]
                                if len(final_hand) == 1 :
                                    total_hand = [first_life] + [second_life] + extras
                                    return (True, total_hand)


        for i in range(len(pure_four)): # if sequence of 4 is pure
            hand_without_pure = copy.deepcopy(hand_copy)
            for j in range(len(pure_four[i])): # to make hand without pure
                check = pure_four[i][j].isIn(hand_without_pure)
                if type(check) != type(False):
                    hand_without_pure.pop(check)
            if len(hand_without_pure) == 10:
                first_life = pure_four[i]
                for k in range(len(sequences_three)):
                    hand_without_runs = copy.deepcopy(hand_without_pure)
                    for j in range(len(sequences_three[k])): # hand_without runs =  hand - 4 pure
                        check2 = sequences_three[k][j].isIn(hand_without_runs)
                        if type(check2) != type(False):
                            hand_without_runs.pop(check2)
                        else:
                            break
                    if len(hand_without_runs) == 7:
                        second_life = sequences_three[k]
                        for l in range(len(fillers_impure_four)):
                            for m in range(len(fillers_impure_four)):
                                final_hand = copy.deepcopy(hand_without_runs)
                                for j in fillers_impure_four[l]:
                                    check3 = j.isIn(final_hand)
                                    if type(check3) != type(False):
                                        final_hand.pop(check3)
                                for j in fillers_impure_four[m]:
                                    check3 = j.isIn(final_hand)
                                    if type(check3) != type(False):
                                        final_hand.pop(check3)
                                extras = [fillers_impure_four[l],fillers_impure_four[m]]
                                if len(final_hand) == 1 :
                                    total_hand = [first_life] + [second_life] + extras
                                    return (True, total_hand)
        return (False, False)

    def swap(self, index):
        """
            Swaps the cards present at the two indices.
        """
        index.sort()
        first = self.hand.pop(index[0])
        second = self.hand.pop(index[1]-1)
        self.hand.insert(index[0], second)
        self.hand.insert(index[1], first)

    def insert(self, index):
        """
            Pops the card present at index[0] and inserts it after index[1]
        """
        if index[0] > index[1]:
            elem = self.hand.pop(index[0])
            self.hand.insert(index[1] + 1, elem)
        else:
            elem = self.hand.pop(index[0])
            self.hand.insert(index[1], elem)

    def show_hand(self):
        """
            Returns a list of images of the card that are present in its hand
        """
        img_list = []
        for card in self.hand:
            img = pygame.image.load("assets/"+str(card)+".png")
            if card.is_hover == True:
                card.offset = -10
                # img = pygame.transform.scale(img,(img.get_width()//4, img.get_height()//4))
            else:
                card.offset = 0
                # img = pygame.transform.scale(img,(img.get_width()//4, img.get_height()//4))
            img_list.append(img)
            # i += 1
        return img_list

    def return_unmatched(self, matched):
        """
        Returns the unmatched cards of the hand if the matched cards are given.
        Currently of no use. Earlier used to implement max_matched()
        """
        working_hand = copy.deepcopy(self.hand)
        for i in matched:
            working_hand.pop(working_hand.index(i))
        working_hand = sort_hand(working_hand)
        return working_hand[-1]


    def calculate_points(self):
        """
            Calculates point of the player when the round has ended
        """
        pure_four = []
        pure_three = []
        impure_three = []
        impure_four = []
        set_three = []
        min_points = 80
        min_hand = []
        first_life= []
        second_life= []
        extras = ['','']
        self.fill_all_possible()
        for k,v in self.allPossible.items():
            if len(k) == 4 and v == 'pure':
                pure_four.append(k)
            elif len(k) == 4 and v == 'impure':
                impure_four.append(k)
            elif len(k) == 3 and v == 'pure':
                pure_three.append(k)
            elif len(k) == 3 and v == 'impure':
                impure_three.append(k)
            elif len(k) == 3 and v == 'set':
                set_three.append(k)
        fillers_impure_four = pure_three + impure_three + set_three
        sequences_three = pure_three + impure_three
        hand_copy = copy.deepcopy(self.hand)
        for i in range(len(impure_four)): # if sequence of 4 is impure
            hand_without_impure = copy.deepcopy(hand_copy)
            for j in range(len(impure_four[i])): # to make hand without impure
                check = impure_four[i][j].isIn(hand_without_impure)
                if type(check) != type(False):
                    hand_without_impure.pop(check)
            if len(hand_without_impure) == 9:
                first_life = impure_four[i]
            for k in range(len(pure_three)):
                hand_without_runs = copy.deepcopy(hand_without_impure)
                for j in range(len(pure_three[k])): # hand_without runs =  hand - 4 impure - 3 pure
                    check2 = pure_three[k][j].isIn(hand_without_runs)
                    if type(check2) != type(False):
                        hand_without_runs.pop(check2)
                    else:
                        break
                if len(hand_without_runs) == 6:
                    second_life = pure_three[k]
                for l in range(len(fillers_impure_four)):
                    final_hand = copy.deepcopy(hand_without_runs)
                    extras = ['','']
                    for j in fillers_impure_four[l]:
                        check3 = j.isIn(final_hand)
                        if type(check3) != type(False):
                            final_hand.pop(check3)
                    if len(final_hand) == 3:
                        extras[0] = fillers_impure_four[l]
                        extras[1] = ''
                    for m in range(len(fillers_impure_four)):
                        final_hand2 = copy.deepcopy(final_hand)
                        for j in fillers_impure_four[m]:
                            check3 = j.isIn(final_hand)
                            if type(check3) != type(False):
                                final_hand.pop(check3)
                        if len(final_hand2) == 0:
                            extras[1] = fillers_impure_four[m]
                    total_hand = list(first_life) + list(second_life) + list(extras[0]) + list(extras[1])
                    points = add_points(self.hand) - add_points(total_hand)
                    print("function alled")
                    if points < min_points:
                        min_points = points
                        min_hand = total_hand

        for i in range(len(pure_four)): # if sequence of 4 is pure
            hand_without_pure = copy.deepcopy(hand_copy)
            for j in range(len(pure_four[i])): # to make hand without pure
                check = pure_four[i][j].isIn(hand_without_pure)
                if type(check) != type(False):
                    hand_without_pure.pop(check)
            if len(hand_without_pure) == 9:
                first_life = pure_four[i]
            for k in range(len(sequences_three)):
                hand_without_runs = copy.deepcopy(hand_without_pure)
                for j in range(len(sequences_three[k])): # hand_without runs =  hand - 4 pure
                    check2 = sequences_three[k][j].isIn(hand_without_runs)
                    if type(check2) != type(False):
                        hand_without_runs.pop(check2)
                    else:
                        break
                # print(first_life)
                if len(hand_without_runs) == 6:
                    second_life = sequences_three[k]
                for l in range(len(fillers_impure_four)):
                    final_hand = copy.deepcopy(hand_without_runs)
                    extras = ['','']
                    for j in fillers_impure_four[l]:
                        check3 = j.isIn(final_hand)
                        if type(check3) != type(False):
                            final_hand.pop(check3)
                    if len(final_hand) == 3:
                        extras[0] = fillers_impure_four[l]
                        extras[1] = ''
                    for m in range(len(fillers_impure_four)):
                        extras[1] = ''
                        final_hand2 = copy.deepcopy(final_hand)
                        for j in fillers_impure_four[m]:
                            check3 = j.isIn(final_hand2)
                            if type(check3) != type(False):
                                final_hand2.pop(check3)
                        if len(final_hand2) == 0:
                            extras[1] = fillers_impure_four[m]
                        total_hand = list(first_life) + list(second_life) + list(extras[0]) + list(extras[1])
                        print(total_hand)
                        points = add_points(self.hand) - add_points(total_hand)
                        if points < min_points:
                            print("function")
                            min_points = points
                            min_hand = total_hand

        min_hand2 = []
        for i in min_hand:
            if type(i) == Card:
                min_hand2.append(i)
        min_hand = min_hand2
        return (min_points, min_hand)


if __name__ == "__main__":
    # full_deck = Deck(2)
    # player1 = Player("")
    # player2 = Player("")
    # d = Deck(1)
    # player1.deal_cards(d)
    # print(id(player1.hand) == id(player2.hand))
    # player1 = Player('Rohan', 0 ,test_hand)
    # player1.hand = sort_hand(player1.hand)
    # print(player1)
    # declare = player1.declare_game()
    # if declare[0]:
    #     for i in declare[1]:
    #         print(list(map(str, i)))
    # else:
    #     print(False)
    # deck = Deck(2)
    # print(str(deck.draw_card()))
    # player1.discard_card(Card('10','diamonds'))
    # player1.discard_card(Card('9','diamonds'))
    # player1.draw_card(Card('J', 'hearts',True))
    # player1.draw_card(Card('2', 'hearts',True))
    # print(player1)
    # declare = player1.declare_game()
    # if declare[0]:
    #     for i in declare[1]:
    #         print(list(map(str, i)))
    # else:
    #     print(False)
    # # print(len(player1.allPossible.values()))
    #
    # player1.hand = sort_hand(player1.hand)
    #
    # #testing is sequence is set is impure sequence
    # Set1 = [Card('3', 'clubs'), Card('3', 'hearts'), Card('3', 'spades')]
    # Set2 = [Card('J', 'spades'), Card('Q', 'hearts'), Card('K', 'clubs')]
    # Set3 = [Card('2', 'hearts', True), Card('8', 'spades'), Card('10','spades'), Card('9', 'spades')]
    # Set4 = [Card('J', 'spades'), Card('J', 'hearts'), Card('J', 'clubs')]
    # Set5 = [Card('K', 'spades'), Card('A', 'spades'), Card('Q','spades'), Card('2', 'hearts',True)]
    # Set6 = [Card('J', 'spades', True), Card('5', 'clubs'), Card('6', 'clubs')]
    # # print(is_set(Set1))
    # # print(is_set(Set4))
    # # print(is_impure_sequence(Set3))
    # # print(is_sequence(Set2), is_sequence(Set5))
    # # print(is_impure_sequence(Set5))
    # # print(list(map(str, Set5)))
    test_hand = [Card('5','hearts'),Card('7','diamonds'),Card('9','diamonds'),Card('2','spades'),Card('10','diamonds'),Card('7','clubs'),Card('8','diamonds'),Card('3','clubs'),Card('3','hearts'),Card('3','spades'),Card('7','hearts'),Card('6','clubs'),Card('6','hearts')]
    player1 = Player("Rohan", 0, test_hand)
    points = player1.calculate_points()
    # print(add_points(test_hand))
    print(points[0])
    # player1.fill_all_possible()
    # allPossible = {}
    # acceptable = ["pure","impure","set"]
    # for k,v in player1.allPossible.items():
    #     if v in acceptable:
    #         allPossible[k] = v
    # print(len(allPossible.keys()))
    # print(len(player1.allPossible.keys()))
    # max = player1.max_matched()
    # for i in max[0]:
    #     print(str(i))
    # for i in max:
    #     if type(i) != tuple:
    #         print(i)
