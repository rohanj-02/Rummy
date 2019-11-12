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
        if set[i].rank_val !=set[i + 1].rank_val - 1:
            if no_jokers == 0:
                return False
            if no_jokers > 0:
                no_jokers -= 1
                j = jokers[0]
                j.rank_val = set[i].rank_val + 1
                set = set[:i + 1] + [j] + set[i + 1:]
                # print(list(map(str, set)))
        i += 1
    if len(jokers) > 0:
        jokers[0].rank_val = RANK_VAL[jokers[0].rank]
    return True
    pass

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

    # def __eq__(self,other):
    #     return self.suit == other.suit and self.rank == other.rank

    def isIn(self, l):
        for i in range(len(l)):
            if self.suit == l[i].suit and self.rank == l[i].rank:
                return i
        return 0
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
        self.allPossible = {}
        self.has_pure = False
        self.has_four = False

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

    def fill_all_possible(self):
        """
            Returns all the occurences of sequences of size 4 (pure or impure) in the player's hand.
            Return : A list containing all such sequences
        """
        working_hand = copy.deepcopy(self.hand)
        set_of_4_sequences = []
        # self.allPossible = {}
        for i in range(len(working_hand)):
            for j in range(len(working_hand)):
                for k in range(len(working_hand)):
                    for l in range(len(working_hand)):
                        if i != j and j != k and k != l and i != l:
                            set = [working_hand[i],working_hand[j],working_hand[k],working_hand[l]]
                            small_set = [working_hand[i], working_hand[j], working_hand[k]]
                            small_set = sort_hand(small_set)
                            small_set_tuple = tuple(small_set)
                            # print(small_set_tuple)
                            set = sort_hand(set)
                            set_tuple = tuple(set)
                            if small_set_tuple not in self.allPossible.keys():
                                if is_sequence(small_set):
                                    working_hand[i].ismatched = True
                                    working_hand[j].ismatched = True
                                    working_hand[k].ismatched = True
                                    working_hand[l].ismatched = True
                                    self.allPossible[small_set_tuple] = "pure"
                                elif is_impure_sequence(small_set):
                                    working_hand[i].ismatched = True
                                    working_hand[j].ismatched = True
                                    working_hand[k].ismatched = True
                                    working_hand[l].ismatched = True
                                    self.allPossible[small_set_tuple] = "impure"
                                elif is_set(set):
                                    working_hand[i].ismatched = True
                                    working_hand[j].ismatched = True
                                    working_hand[k].ismatched = True
                                    working_hand[l].ismatched = True
                                    self.allPossible[small_set_tuple] = "set"
                                else:
                                    self.allPossible[small_set_tuple] = 'none'

                            if set_tuple not in self.allPossible.keys():
                                if is_sequence(set):
                                    working_hand[i].ismatched = True
                                    working_hand[j].ismatched = True
                                    working_hand[k].ismatched = True
                                    working_hand[l].ismatched = True
                                    self.allPossible[set_tuple] = "pure"
                                    # self.has_pure = True
                                    if set not in set_of_4_sequences:
                                        set_of_4_sequences.append(set)
                                elif is_impure_sequence(set):
                                    working_hand[i].ismatched = True
                                    working_hand[j].ismatched = True
                                    working_hand[k].ismatched = True
                                    working_hand[l].ismatched = True
                                    self.allPossible[set_tuple] = 'impure'
                                    if set not in set_of_4_sequences:
                                        set_of_4_sequences.append(set)
                                elif is_set(set):
                                    working_hand[i].ismatched = True
                                    working_hand[j].ismatched = True
                                    working_hand[k].ismatched = True
                                    working_hand[l].ismatched = True
                                    self.allPossible[set_tuple] = 'set'
                                else:
                                    self.allPossible[set_tuple] = 'none'
                            else:
                                if self.allPossible[set_tuple] == 'pure' or self.allPossible[set_tuple] == 'impure':
                                    if set not in set_of_4_sequences:
                                        set_of_4_sequences.append(set)
        return set_of_4_sequences

    def shut_game(self):
        """
            Shut the game by player.
            Returns True if player can shut the round. Else False
        """
        #check for sequence of 4
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
        # for i in set_three:
        fillers_impure_four = pure_three + impure_three + set_three
        #     print(list(map(str, i)))
        hand_copy = copy.deepcopy(self.hand)
        for i in impure_four:
            print(list(map(str, i)))
        for i in range(len(impure_four)):
            print("1")
            hand_without_impure = copy.deepcopy(hand_copy)
            print("length", len(impure_four[i]))
            for j in range(len(impure_four[i])): # to make hand without impure
                check = impure_four[i][j].isIn(hand_without_impure)
                if check != 0 :
                    hand_without_impure.pop(check)
                    print(impure_four[i][j])
                    print("Should come 4 times")
            if len(hand_without_impure) == 10:
                print("length impure", len(hand_without_impure))
                for k in range(len(pure_three)):
                    # print("2")
                    hand_without_runs = copy.deepcopy(hand_without_impure)
                    for j in range(len(pure_three[k])): # hand_without runs =  hand - 4 impure - 3 pure
                        check2 = pure_three[k][j].isIn(hand_without_runs)
                        if check2 != 0:
                            hand_without_runs.pop(check2)
                            print("length2", len(hand_without_runs))
                        else:
                            break
                    if len(hand_without_runs) == 7:
                            # print("1")
                        for l in range(len(fillers_impure_four)):
                            for m in range(len(fillers_impure_four)):
                                # for n in range(len(fillers_impure_four)):
                                if l != m:
                                        # print("3")
                                    final_hand = copy.deepcopy(hand_without_runs)
                                        # print(len(final_hand))
                                    new_filler = list(fillers_impure_four[l]) + list(fillers_impure_four[m]) # take two at a time and di the same processecen if onesays len == 1 then true/.
                                        # print(new_filler)
                                    for j in range(len(new_filler)):
                                        check3 = new_filler[j].isIn(final_hand)
                                        if check3 != 0:
                                                # print("3")
                                            final_hand.pop(check3)
                                    print(len(final_hand))
                                            # else:
                                            #     break
                                    if len(final_hand) == 1 :
                                        return True
        return False

full_deck = Deck(2)
test_hand = [Card('5','hearts'),Card('2','clubs',True),Card('5','diamonds'),Card('6','diamonds'),Card('8','clubs'),Card('9','clubs'),Card('7','clubs'),Card('8','diamonds'),Card('3','clubs'),Card('3','hearts'),Card('3','spades'),Card('7','hearts'),Card('6','hearts'),Card('10','diamonds')]
player1 = Player('Rohan', 0 ,test_hand)
shut = player1.shut_game()
print(shut)
# for i in shut:
#     print(list(map(str,i)))
# jok = full_deck.set_joker(Card('J','spades'))
# player1.deal_cards(full_deck)
# print(str(player1))
player1.hand = sort_hand(player1.hand)
# print(str(player1))
# print(str(jok))
#testing is sequence is set is impure sequence
Set1 = [Card('J', 'hearts'), Card('J', 'hearts'), Card('J', 'clubs')]
Set2 = [Card('J', 'spades'), Card('Q', 'hearts'), Card('K', 'clubs')]
Set3 = [Card('2', 'hearts', True), Card('8', 'spades'), Card('10','spades'), Card('9', 'spades')]
Set4 = [Card('J', 'spades'), Card('J', 'hearts'), Card('J', 'clubs')]
Set5 = [Card('K', 'spades',True), Card('A', 'spades'), Card('Q','spades'), Card('2', 'spades')]
Set6 = [Card('J', 'spades', True), Card('5', 'clubs'), Card('6', 'clubs')]
# print(is_set(Set1))
# print(is_set(Set4))
# print(is_impure_sequence(Set3))
# print(is_sequence(Set2), is_sequence(Set5))
# print(is_impure_sequence(Set5), is_impure_sequence(Set6))
# print(list(map(str, Set5)))
a = Card('5','spades')
b = Card('6', 'hearts')
list = [a,b]
tuple1 = tuple(list)
tuple2 = (3,4)
all ={}
all[tuple1] = 1
all[tuple2] = 3
# print(all)
a = Card('7','diamonds')
# for k,v in all.i
