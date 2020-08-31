# Rummy

A variation of the card game rummy using python and pygame.

**Players :** User and Computer

Deal Rummy is a game where there are x number of deals and the person that wins the highest amount of rounds is declared as the winner.

![Homescreen](ReadMeAssets/Homescreen.png)

![Gamescreen](ReadMeAssets/Gamescreen.png)

You can see the gameplay in the ReadMeAssets folder.

## Objective

The objective of the game is to form Runs and Sets and declare your turn as soon as possible.

## Rules

-  Two 52-card decks are used. No jokers are used.
-  Each player is dealt 13 cards.
-  Stock pile consists of the remaining cards.
-  Discard pile consists of the cards that have been discarded by players.
-  The player as to pick a card in each turn either from the top of discard pile or from the top card of the stock pile.
<!--* The player also has to discard a card in each turn.-->
-  The player can choose to discard or declare after picking up their cards.
-  A valid declare has minimum 2 conditions : One run should be of size 4 and one run should be pure.
-  A card declared as joker cannot be used as a pure card.

#### Rules for making sets

A set consists of 3 cards of same rank but of different suits.
eg. 3 hearts, 3 clubs, 3 spades is a set.
eg. 3 hearts, 3 hearts, 3 clubs is not a set
eg. 3 clubs, 4 hearts, 5 spades is not a set

#### Rules for making pure sequences/runs

A run consists of 3 or 4 cards of same suit and are in consecutive order. The valid order being A-2-3-4-5-6-7-8-9-10-J-Q-K-A.
Thus with ace you can form the run A-2-3 or Q-K-A but you can not form K-A-2. Examples of valid runs are 4-5-6 , 9-10-J, 9-10-J-Q, A-2-3-4 and 8-9-10-J. These are pure or straight or natural runs (runs without a joker).

#### Rules for making improper sequenes/runs

A run can also use a joker as substitute for any missing card. Such a run is non pure run. Examples of non pure runs are 4-5-joker, 2-3-joker-5. In a run you can use only one joker as a wild card.

## Deal

-  Each player is dealt 13 cards face down.
-  The next card from the deck is placed face up on the table; this starts the discard pile.
-  Rest of the cards are placed face down in the centre of the table; this is the stock pile.
-  A card is picked from the stock pile and placed face up under the stock pile so that it is visible. All the cards of that rank regardless of the suit can be used as additional jokers.
   eg. if the card picked and kept visible is 3 hearts then all cards with rank 3 treated as jokers. i.e. 3 spades, 3 hearts, 3 clubs, 3 diamonds.

## Scoring

The player who declares first wins the round. The player to win the most number of rounds in a game wins the game.

**Execute main.py to run the game.**

**Rules as given in** [OctroRummy](https://rummy.octro.com/tutorial/)

Cards designed by [Dhruv Jain](https://www.behance.net/dhruv2703f7fd)

Music by [SoundSnap](https://www.soundsnap.com/)
