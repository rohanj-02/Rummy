import pygame
import textbox
import cards
import button
from button import Button
from textbox import TextBox, display_testbox, input_textbox
from cards import *


pygame.init()
X = 1360
Y = 768
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Rummy')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
deal_card_sound = pygame.mixer.Sound("assets/dealcard.wav")
correct_declare = pygame.mixer.Sound("assets/correctdeclare.wav")
wrong_declare = pygame.mixer.Sound("assets/wrongdeclare.wav")
padding = 20
#TUTORIAL DEFINITIONS
next = Button('Next', (0,0), 100, 50, "Montserrat-Regular.ttf")
next.set_center((X - next.width//2 - padding, Y - next.height/2 - padding))
skip = Button('Skip', (0,0), 100, 50,"Montserrat-Regular.ttf")
skip.set_center((X - skip.width//2 - padding, skip.height//2 + padding))
finish = Button('Finish', (0,0), 100, 50,"Montserrat-Regular.ttf")
finish.set_center((X - finish.width//2 - padding, Y - next.height/2 - padding))
last_stage = 5
back = pygame.image.load('assets/back.png')
card_width = back.get_width()

#
# Stage 0 : Start
# Stage 1 : Take name
# Stage 2 : Points or Deal
# Stage 3 : Number of points or number of deals
# Stage 4 : Game
# Stage 5 : Score Display and winner declared
# Stage 6 : Instructions
#
#GLOBAL VARIABLES

stage = [0,0]
fontName = "centuryGothic.ttf"
running = True
black = [0,0,0]
card_gap = 15
padding = 20
points_mode = False
deal_mode = True
target = 0
deal = 0
# Heading :
heading_font = pygame.font.Font("Pacifico-Regular.ttf", 200)
button_font = pygame.font.Font("Montserrat-Regular.ttf", 30)
text_font = pygame.font.Font(fontName, 30)
textbox_font = pygame.font.Font(fontName, 20)
small_font = pygame.font.Font(fontName, 15)
heading = heading_font.render("Rummy", True, textbox.color2)
heading_rect = heading.get_rect()
heading_rect.center = [X//2, Y//4]
back_button = Button("Back", (0,0), 100, 50, "Montserrat-Regular.ttf")

#Stage 0:
start = Button("Start", (3*X//4 + 120, 3*Y//4 + 140), 200, 50, "Montserrat-Regular.ttf")
start.set_center((X // 2, 5*Y // 8))
how_to = Button("How To Play",(0,0), 200, 50, "Montserrat-Regular.ttf")
how_to.set_center((X//2, 5*Y//8 + start.height + padding))
#Stage 1 :
name = TextBox("Enter Name")
name.set_center((X // 2, 5*Y // 8 ), (X//2, 5*Y//8 + 70))
#Stage 2 :
points_rummy = Button("Points Rummy", (3*X//4 + 120, 3*Y//4 + 140), 240, 50, "Montserrat-Regular.ttf")
points_rummy.set_center((X // 2, 5*Y // 8))
deal_rummy = Button("Deal Rummy", (3*X//4 + 120, 3*Y//4 + 140), 240, 50, "Montserrat-Regular.ttf")
deal_rummy.set_center((X // 2, 5*Y // 8 + 70))
#Stage 3 :
points_text = button_font.render("Choose number of points", True, textbox.color1)
points_text_rect = points_text.get_rect()
points_text_rect.center = (X//2,5*Y//8)
deal_text = button_font.render("Choose number of deals", True, textbox.color1)
deal_text_rect = deal_text.get_rect()
deal_text_rect.center = (X//2,5*Y//8)
points_100 = Button("100 Points", (3*X//4 + 120, 3*Y//4 + 140), 200, 50, "Montserrat-Regular.ttf")
points_100.set_center((X // 2, 5*Y // 8 + 70))
points_200 = Button("200 Points", (3*X//4 + 120, 3*Y//4 + 140), 200, 50, "Montserrat-Regular.ttf")
points_200.set_center((X // 2, 5*Y // 8 + 140))
deal_1 = Button("1", (3*X//4 + 120, 3*Y//4 + 140), 50, 50, "Montserrat-Regular.ttf")
deal_1.set_center((X // 2 - 60, 5*Y // 8 + 70))
deal_3 = Button("3", (3*X//4 + 120, 3*Y//4 + 140), 50, 50, "Montserrat-Regular.ttf")
deal_3.set_center((X // 2, 5*Y // 8 + 70))
deal_5 = Button("5", (3*X//4 + 120, 3*Y//4 + 140), 50, 50, "Montserrat-Regular.ttf")
deal_5.set_center((X // 2 + 60, 5*Y // 8 + 70))
#Stage 4 :
deck = Deck(2)
user = Player("Rohan")
computer = Player("Computer")
deck.shuffle_cards()
deck.set_joker()
user.deal_cards(deck)
computer.deal_cards(deck)
cardss = deck.draw_card()
deck.update_pile(cardss)
draw = Card('A', 'spades')
swap = Button("Swap",(3*X//4, 3*Y//4) , 120, 50, "Montserrat-Regular.ttf")
insert = Button("Insert", (3*X//4 + 140, 3*Y//4 - 70), 120, 50, "Montserrat-Regular.ttf")
sort = Button("Sort",(3*X//4, 3*Y//4 - 70), 120, 50, "Montserrat-Regular.ttf")
declare = Button("Declare", (3*X//4, 3*Y//4 + 70) , 260, 50, "Montserrat-Regular.ttf")
discard = Button("Discard",(3*X//4 + 140, 3*Y//4), 120, 50, "Montserrat-Regular.ttf")
showCP = Button("Show Computer", (3*X//4, Y//2), 260, 50, "Montserrat-Regular.ttf")
user_name = text_font.render(user.name, True, textbox.color1)
user_name_rect = user_name.get_rect()
user_name_rect.center = (3*X//4, Y//5)
computer_name = text_font.render(computer.name, True, textbox.color1)
computer_name_rect = computer_name.get_rect()
computer_name_rect.center = (3*X//4 , Y//5 + 70)
name_text = text_font.render("Name", True, textbox.color1)
name_rect = name_text.get_rect()
name_rect.center = (3*X//4, Y//5 - 70)
score_text = text_font.render("Score", True, textbox.color1)
score_rect = score_text.get_rect()
score_rect.center = (3*X//4 + 200, Y//5 - 70)
user.turn = True
discard_mode = False
swap_mode = False
insert_mode = False
index = []
time = 0
computer_delay = 2
print_no_declare = False
#Stage 5 :
winning_hand = 0
winner = False
winner_text = 0
winner_text_rect = 0
new_round = 0
play_again = 0
game_over = False
# winnning_condition = False

def show_game(screen, player, deck):
    """
        Shows everything to be shown on the main game screen.
    """
    #Show scores:
    user_score = text_font.render(str(user.score), True, textbox.color1)
    user_score_rect = user_score.get_rect()
    user_score_rect.center = (3*X//4 + 200, Y//5)
    computer_score = text_font.render(str(computer.score), True, textbox.color1)
    computer_score_rect = computer_score.get_rect()
    computer_score_rect.center = (3*X//4 + 200, Y//5 + 70)
    screen.blit(computer_score, computer_score_rect)
    screen.blit(user_score, user_score_rect)
    screen.blit(user_name, user_name_rect)
    screen.blit(computer_name, computer_name_rect)
    screen.blit(name_text, name_rect)
    screen.blit(score_text, score_rect)
    # user_score
    images = player.show_hand()
    count = 0
    #Show Player Cards
    back = pygame.image.load('assets/back.png')
    # back = pygame.transform.scale(back, (back.get_width()//4,back.get_height()//4))
    for i in images:
        if count < 7:
            pos = (count*(back.get_width() + card_gap)+ padding ,Y - 2*back.get_height() - padding- card_gap + player.hand[count].offset)
            player.hand[count].position = pos
            screen.blit(i, pos)
        else:
            pos = ((count-7)*(back.get_width() + card_gap)+ padding ,Y - back.get_height() - padding + player.hand[count].offset)
            player.hand[count].position = pos
            screen.blit(i, pos)
        count += 1
    count = 0
    #Show computer cards
    images = computer.show_hand()
    for i in images:
        if not showCP.is_clicked :
            if count < 7:
                screen.blit(back, (count*(back.get_width() + card_gap)+ padding ,padding))
            else:
                screen.blit(back, ((count-7)*(back.get_width() + card_gap)+ padding ,back.get_height() + padding + card_gap))
        else:
            if count < 7:
                screen.blit(i, (count*(i.get_width() + card_gap)+ padding ,padding))
            else:
                screen.blit(i, ((count-7)*(i.get_width() + card_gap)+ padding ,i.get_height() + padding + card_gap))
        count += 1
    #show pile
    img = deck.show_pile()
    for i in range(len(img) - 1, -1,-1):
        # img = pygame.transform.scale(img, (img.get_width()//4, img.get_height()//4))
        pos = (5*padding, 2*(img[i].get_height() + card_gap + padding))
        deck.pile[i].position = pos
        screen.blit(img[i], pos)
    #show Joker
    img = deck.joker.show()
    screen.blit(img, (8*(back.get_width() + card_gap) + padding ,2*(back.get_height() + card_gap + padding)))
    joker_font = pygame.font.SysFont(fontName, 25)
    joker = joker_font.render("Joker", True,black)
    joker_rect = joker.get_rect()
    joker_rect.center = [8*(back.get_width() + card_gap) + back.get_width()//2 + padding ,3*(back.get_height() + card_gap + padding)]
    screen.blit(joker, joker_rect)
    if stage[0] == -1:
        d = joker_font.render("Deck", True, black)
        d_rect = d.get_rect()
        d_rect.center = (7*(back.get_width() + card_gap) + back.get_width()//2 + padding, 3*(back.get_height() + card_gap + padding))
        screen.blit(d, d_rect)
        d = joker_font.render("Pile", True, black)
        d_rect = d.get_rect()
        d_rect.center = (5*padding + back.get_width()//2, 3*(back.get_height() + card_gap + padding) - padding)
        screen.blit(d, d_rect)

    #show deck
    pos = (7*(back.get_width() + card_gap) + padding ,2*(back.get_height() + card_gap + padding))
    draw.position = pos
    screen.blit(back, pos)
    #show buttons
    sort.display(screen)
    declare.display(screen)
    discard.display(screen)
    showCP.display(screen)
    insert.display(screen)
    swap.display(screen)

def player_turn(mouse_pos, event):
    """
        Function to take mouse input and similarly check for buttons etc. in one frame of the game.
    """
    global discard_mode, swap_mode, index, insert_mode, winner, winning_condition, winning_hand, print_no_declare
    sort.check(mouse_pos, event)
    draw.check(mouse_pos, event)
    insert.check(mouse_pos,event)
    declare.check(mouse_pos, event)
    swap.check(mouse_pos, event)
    discard.check(mouse_pos, event)
    for i in range(len(deck.pile)):
        deck.pile[i].check(mouse_pos,event)

    for i in range(len(user.hand)):
        user.hand[i].check(mouse_pos, event)

    if len(deck.pile) != 0 :
        if deck.pile[0].is_clicked and len(user.hand) == 13:
                user.draw_card(deck.pile.pop(0))
                deal_card_sound.play()
    i = 0
    while i < len(user.hand):
        if user.hand[i].is_clicked and discard_mode and len(user.hand) == 14:
            user.turn = False
            computer.turn = True
            deck.update_pile(Card(user.hand[i].rank, user.hand[i].suit, user.hand[i].isjoker))
            user.discard_card(user.hand[i])
            deal_card_sound.play()
            i -= 1
            discard_mode = False
        if user.hand[i].is_clicked and swap_mode :
            index.append(i)
            if len(index) >= 2:
                swap_mode = False
                user.swap(index)
                index = []
        if user.hand[i].is_clicked and insert_mode :
            index.append(i)
            if len(index) >= 2:
                insert_mode = False
                user.insert(index)
                index = []
        i += 1
    if swap.is_clicked or swap_mode or (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
        swap_mode = True
        insert_mode = False
        discard_mode = False
    if insert.is_clicked or insert_mode or (event.type == pygame.KEYDOWN and event.key == pygame.K_i):
        insert_mode = True
        swap_mode = False
        discard_mode = False
    if sort.is_clicked or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) :
        user.hand = sort_hand(user.hand)
    if (draw.is_clicked or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)) and len(user.hand) == 13:
        deal_card_sound.play()
        user.draw_card(deck.draw_card())
    if declare.is_clicked:
        winning_hand = user.declare_game()
        if winning_hand[0] :
            winner = user
            correct_declare.play()
            # winning_condition = True
            round_over()
            stage[0] += 1
        else:
            wrong_declare.play()
            print_no_declare = True
    if (discard.is_clicked or discard_mode or (event.type == pygame.KEYDOWN and event.key == pygame.K_d)) and len(user.hand) == 14:
        discard_mode = True
        swap_mode = False
        insert_mode = False
    pygame.display.update()

def computer_turn():
    """
        Function to implement the moves of the computer
    """
    global winner, winning_hand, time
    computer.draw_card(deck.pile[0])
    winning_hand = computer.declare_game()
    if winning_hand[0]:
        #winning condition
        winner = computer
        round_over()
        stage[0] += 1
    else:
        score = [0] * 14
        min_pile = (0, 100)
        for i in range(len(computer.hand)):
            score[i] = calculate_score(computer.hand[i], computer.hand)
        for i in range(len(score)):
            if score[i] < min_pile[1]:
                min_pile = (i,score[i])
            elif score[i] == min_pile[1]:
                if computer.hand[i].rank >= computer.hand[min_pile[0]].rank:
                    min_pile = (i, score[i])

    computer.discard_card(deck.pile[0])

    joker_card = Card('3','spades',True)
    computer.draw_card(joker_card)
    score = [0] * 14
    min_deck = (0, 100)
    for i in range(len(computer.hand)):
        score[i] = calculate_score(computer.hand[i], computer.hand)
    for i in range(len(score)):
        if score[i] < min_deck[1]:
            min_deck = (i,score[i])
        elif score[i] == min_deck[1]:
            if computer.hand[i].rank >= computer.hand[min_deck[0]].rank:
                min_deck = (i, score[i])
    computer.discard_card(joker_card)


    if min_pile[1] <= min_deck[1]:
        #draw from pile
        if time == 0 :
            computer.draw_card(deck.pile.pop(0))
            deal_card_sound.play()
            time += 1
            # print("pile initialisation")
        elif time >= computer_delay:
        #DELAY
            deck.update_pile(computer.hand[min_pile[0]])
            computer.discard_card(computer.hand[min_pile[0]])
            deal_card_sound.play()
            # print("pile time condition")
            computer.hand = sort_hand(computer.hand)
            computer.turn = False
            user.turn = True
            time = 0
        else:
            # print("pile increment")
            time += 1
    else:
        #draw from deck
        #DELAY
        if time == 0:
            computer.draw_card(deck.draw_card())
            deal_card_sound.play()
            # print("deck initialisation")
            time += 1
        elif time >= computer_delay:
            # print("Deck time condition")
            winning_hand = computer.declare_hand()
            if winning_hand[0] :
                #winning condition
                winner = computer
                round_over()
                stage[0] += 1
                time = 0
            else:
                score = [0] * 14
                min_deck = (0, 100)
                for i in range(len(computer.hand)):
                    score[i] = calculate_score(computer.hand[i], computer.hand)
                for i in range(len(score)):
                    if score[i] < min_deck[1]:
                        min_deck = (i,score[i])
                    elif score[i] == min_deck[1]:
                        if computer.hand[i].rank >= computer.hand[min_deck[0]].rank:
                            min_deck = (i, score[i])
                deck.update_pile(computer.hand[min_deck[0]])
                computer.discard_card(computer.hand[min_deck[0]])
                time = 0
                deal_card_sound.play()
                computer.hand = sort_hand(computer.hand)
                computer.turn = False
                user.turn = True
        else:
            # print("deck increment condition")
            time += 1

def round_over():
    """
        Function to realise that the round is over. Takes care of score.
    """
    #print winner won this round
    #show their hand
    #show next round button
    global winner, winning_hand, new_round, game_over, winner_text, winner_text_rect, deal, play_again
    if deal_mode:
        deal -= 1
        if deal != 0 :
            winner.score += 1
            text = winner.name + ' has won this round!'
        else:
            game_over = True
            winner.score += 1
            if user.score > computer.score:
                text = user.name + ' has won the game!'
            else:
                text = computer.name + ' has won the game!'
    if points_mode:
        pass
    winner_text = button_font.render(text, True, textbox.color1)
    winner_text_rect = winner_text.get_rect()
    winner_text_rect.center = [X//2, Y//4]
    winn = []
    for i in winning_hand[1] :
        for j in i:
            winn.append(j)
    winning_hand = winn
    new_round = Button("Next Round", (X - 2*padding - 200, Y - 125), 200, 50, "Montserrat-Regular.ttf")
    play_again = Button("Play Again", (X - 2*padding - 200, Y - 125), 200, 50, "Montserrat-Regular.ttf")

def round_over_display():
    """
        To display the screen after the round is over.
    """
    global winner_text, winner_text_rect, winning_hand, game_over, new_round,stage
    screen.blit(winner_text, winner_text_rect)
    i = 0
    for card in winning_hand:
        img = pygame.image.load("assets/"+str(card)+".png")
        # img = pygame.transform.scale(img,(img.get_width()//4, img.get_height()//4))
        pos = (padding + i*(img.get_width() + card_gap), Y // 2)
        screen.blit(img, pos)
        i += 1
    if not game_over :
        new_round.display(screen)
    else:
        play_again.display(screen)

def round_over_event(mouse_pos, event):
    """
        To take mouse input for buttons etc. to go to the next round.
    """
    new_round.check(mouse_pos, event)
    play_again.check(mouse_pos, event)
    if new_round.is_clicked and deal > 0:
        stage[0] = 4
        game_reset()
    elif play_again.is_clicked and deal == 0:
        before_game_reset()
        stage[0] = 0

def game_reset():
    """
        Rests all the variables to initialise a round.
    """
    global deck, user, computer, draw, swap, insert, sort, declare, discard, showCP, user_name, user_name_rect, computer_name, computer_name_rect
    global name_text, name_rect, score_text, score_rect, discard_mode, swap_mode, insert_mode, index
    deck = Deck(2)
    deck.shuffle_cards()
    deck.set_joker()
    user.deal_cards(deck)
    computer.deal_cards(deck)
    cardss = deck.draw_card()
    deck.update_pile(cardss)
    user.turn = True
    discard_mode = False
    swap_mode = False
    insert_mode = False
    index = []

def winning_reset():
    """
        Resets all the variables to initialise another game.
    """
    global winning_hand, winner, winner_text, winner_text_rect, new_round, play_again, game_over
    winning_hand = 0
    winner = False
    winner_text = 0
    winner_text_rect = 0
    new_round = 0
    play_again = 0
    game_over = False

def before_game_reset():
    """
        Resets everything to default value.
    """
    global start, name, points_rummy, deal_rummy, points_text ,points_text_rect, deal_text, deal_text_rect, points_100, points_200
    global deal_1, deal_3, deal_5, winning_hand, winner, winner_text, winner_text_rect, new_round, play_again, game_over
    #Stage 1 :
    name = TextBox("Enter Name")
    name.set_center((X // 2, 5*Y // 8 ), (X//2, 5*Y//8 + 70))
    game_reset()
    winning_reset()

def tutorial_show():
    """
        The display of all the stages in the tutorial of the game.
    """
    global stage
    #Add code to display how to play above. looks weird right now
    if stage[1] != last_stage:
        next.display(screen)
        skip.display(screen)
    else:
        finish.display(screen)
    if stage[1] == 0:
        text = text_font.render("Rummy is played by 2 players, user and computer. It is played with 2 decks.", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (X//2 - padding - skip.width, Y//8)
        spade = pygame.image.load('assets/spades-A.png')
        pos_spade = (5*padding ,Y//2)
        spade_text = textbox_font.render("Spades", True, textbox.color1)
        spade_text_rect = spade_text.get_rect()
        spade_text_rect.center = (pos_spade[0] + spade.get_width()//2, pos_spade[1] + spade.get_height() + padding)
        heart = pygame.image.load('assets/hearts-A.png')
        pos_heart = (10*padding + heart.get_width() ,Y//2)
        heart_text = textbox_font.render("Hearts", True, textbox.color1)
        heart_text_rect = heart_text.get_rect()
        heart_text_rect.center = (pos_heart[0] + spade.get_width()//2, pos_heart[1] + spade.get_height() + padding)
        screen.blit(heart, pos_heart)
        screen.blit(heart_text, heart_text_rect)
        club = pygame.image.load('assets/clubs-A.png')
        pos_club = (15*padding + 2*heart.get_width() ,Y//2)
        club_text = textbox_font.render("Clubs", True, textbox.color1)
        club_text_rect = club_text.get_rect()
        club_text_rect.center = (pos_club[0] + club.get_width()//2, pos_club[1] + spade.get_height() + padding)
        screen.blit(club, pos_club)
        screen.blit(club_text, club_text_rect)
        diamond = pygame.image.load('assets/diamonds-A.png')
        pos_diamond = (20*padding + 3*heart.get_width() ,Y//2)
        diamond_text = textbox_font.render("Diamonds", True, textbox.color1)
        diamond_text_rect = diamond_text.get_rect()
        diamond_text_rect.center = (pos_diamond[0] + club.get_width()//2, pos_diamond[1] + spade.get_height() + padding)
        screen.blit(diamond, pos_diamond)
        screen.blit(diamond_text, diamond_text_rect)
        screen.blit(spade, pos_spade)
        screen.blit(spade_text, spade_text_rect)

        screen.blit(text, text_rect)

    elif stage[1] == 1:
        text = text_font.render("What is a pure sequence?", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//8)
        screen.blit(text,text_rect)
        text = textbox_font.render("A pure sequence consists of 3 or 4 cards of same suit in a consecutive order.", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//4)
        screen.blit(text,text_rect)
        text = textbox_font.render("For example :", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, 3*Y//8)
        screen.blit(text,text_rect)
        heartA = pygame.image.load('assets/hearts-A.png')
        pos_heartA = (12*padding + 2* heartA.get_width(), Y//2)
        heartK = pygame.image.load('assets/hearts-K.png')
        pos_heartK = (11*padding + heartA.get_width(), Y//2)
        heartQ = pygame.image.load('assets/hearts-Q.png')
        pos_heartQ = (10*padding, Y//2)
        screen.blit(heartA, pos_heartA)
        screen.blit(heartK, pos_heartK)
        screen.blit(heartQ, pos_heartQ)
        heart6 = pygame.image.load('assets/hearts-6.png')
        pos_heart6 = (X - 7*padding , Y//2)
        heartA = pygame.image.load('assets/hearts-5.png')
        pos_heartA = (X - 8*padding - heartA.get_width(), Y//2)
        heartK = pygame.image.load('assets/hearts-4.png')
        pos_heartK = (X - 9*padding - 2*heartA.get_width(), Y//2)
        heartQ = pygame.image.load('assets/hearts-3.png')
        pos_heartQ = (X - 10*padding - 3* heartA.get_width(), Y//2)
        screen.blit(heartA, pos_heartA)
        screen.blit(heartK, pos_heartK)
        screen.blit(heart6, pos_heart6)
        screen.blit(heartQ, pos_heartQ)

    elif stage[1] == 2:
        text = text_font.render("What is an impure sequence?", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//8)
        screen.blit(text,text_rect)
        text = textbox_font.render("An impure sequence can substitute a joker for a missing card.", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//4)
        screen.blit(text,text_rect)
        text = textbox_font.render("For example :", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, 3*Y//8)
        screen.blit(text,text_rect)
        heartA = pygame.image.load('assets/hearts-A.png')
        pos_heartA = (12*padding + 2* heartA.get_width(), Y//2)
        heartK = pygame.image.load('assets/hearts-K.png')
        pos_heartK = (11*padding + heartA.get_width(), Y//2)
        heartQ = pygame.image.load('assets/spades-3.png')
        pos_heartQ = (10*padding, Y//2)
        heart_text = textbox_font.render("Joker", True, textbox.color1)
        heart_text_rect = heart_text.get_rect()
        heart_text_rect.center = (pos_heartQ[0] + heartA.get_width()//2, pos_heartQ[1] + heartA.get_height() + padding)
        screen.blit(heart_text, heart_text_rect)
        screen.blit(heartA, pos_heartA)
        screen.blit(heartK, pos_heartK)
        screen.blit(heartQ, pos_heartQ)
        heart6 = pygame.image.load('assets/hearts-6.png')
        pos_heart6 = (X - 7*padding , Y//2)
        heartA = pygame.image.load('assets/diamonds-10.png')
        pos_heartA = (X - 8*padding - heartA.get_width(), Y//2)
        heart_text_rect.center = (pos_heartA[0] + heartA.get_width()//2, pos_heartA[1] + heartA.get_height() + padding)
        heartK = pygame.image.load('assets/hearts-4.png')
        pos_heartK = (X - 9*padding - 2*heartA.get_width(), Y//2)
        heartQ = pygame.image.load('assets/hearts-3.png')
        pos_heartQ = (X - 10*padding - 3* heartA.get_width(), Y//2)
        screen.blit(heartA, pos_heartA)
        screen.blit(heart_text, heart_text_rect)
        screen.blit(heartK, pos_heartK)
        screen.blit(heart6, pos_heart6)
        screen.blit(heartQ, pos_heartQ)

    elif stage[1] == 3:
        text = text_font.render("What is a set?", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//8)
        screen.blit(text,text_rect)
        text = textbox_font.render("A set consists of 3 cards of same rank but of different suits.", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//4)
        screen.blit(text,text_rect)
        text = textbox_font.render("For example :", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, 3*Y//8)
        screen.blit(text,text_rect)
        heartA = pygame.image.load('assets/hearts-5.png')
        pos_heartA = (12*padding + 2* heartA.get_width(), Y//2)
        heartK = pygame.image.load('assets/diamonds-10.png')
        pos_heartK = (11*padding + heartA.get_width(), Y//2)
        heartQ = pygame.image.load('assets/spades-5.png')
        pos_heartQ = (10*padding, Y//2)
        heart_text = textbox_font.render("Joker", True, textbox.color1)
        heart_text_rect = heart_text.get_rect()
        heart_text_rect.center = (pos_heartK[0] + heartA.get_width()//2, pos_heartK[1] + heartA.get_height() + padding)
        screen.blit(heart_text, heart_text_rect)
        screen.blit(heartA, pos_heartA)
        screen.blit(heartK, pos_heartK)
        screen.blit(heartQ, pos_heartQ)
        heartA = pygame.image.load('assets/diamonds-10.png')
        pos_heartA = (X - 8*padding - heartA.get_width(), Y//2)
        heartK = pygame.image.load('assets/hearts-10.png')
        pos_heartK = (X - 9*padding - 2*heartA.get_width(), Y//2)
        heartQ = pygame.image.load('assets/spades-10.png')
        pos_heartQ = (X - 10*padding - 3* heartA.get_width(), Y//2)
        screen.blit(heartA, pos_heartA)
        screen.blit(heartK, pos_heartK)
        screen.blit(heartQ, pos_heartQ)

    elif stage[1] == 4:
        text = text_font.render("Rules : ", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//8)
        screen.blit(text,text_rect)
        text = textbox_font.render("1. Each player will be dealt 13 cards.", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, Y//4)
        screen.blit(text,text_rect)
        text = textbox_font.render("2. A valid declare consists of :", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + padding, 3*Y//8)
        screen.blit(text,text_rect)
        text = textbox_font.render("a) A pure sequence", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + 5*padding, 7*Y//16)
        screen.blit(text,text_rect)
        text = textbox_font.render("b) A sequence of 4 cards", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + 5*padding, 8*Y//16)
        screen.blit(text,text_rect)
        text = textbox_font.render("c) The rest of the cards must form sets or sequences", True, textbox.color1)
        text_rect = text.get_rect()
        text_rect.center = (text_rect.width//2 + 5*padding, 9*Y//16)
        screen.blit(text,text_rect)
        # text = textbox_font.render("3. A card declared as a joker must not be used as a pure card.", True, textbox.color1)
        # text_rect = text.get_rect()
        # text_rect.center = (text_rect.width//2 + padding, 11*Y//16)
        # screen.blit(text,text_rect)

    elif stage[1] == 5:
        show_game(screen, user, deck)

        if declare.is_hover:
            text = small_font.render("You can click the declare button when ", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2, 3*Y//4 - 35)
            screen.blit(text,text_rect)
            text = small_font.render("your cards are a valid declare. Click the", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4)
            screen.blit(text,text_rect)
            text = small_font.render("declare button to finish and win the round.", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 35)
            screen.blit(text,text_rect)

        if swap.is_hover or swap_mode:
            text = small_font.render("To swap two cards click on the ", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2, 3*Y//4 - 35)
            screen.blit(text,text_rect)
            text = small_font.render("swap button then click on both", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4)
            screen.blit(text,text_rect)
            text = small_font.render("the cards that are to be swapped.", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 35)
            screen.blit(text,text_rect)

        if discard.is_hover or discard_mode:
            text = small_font.render("To discard a card click on the discard", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2, 3*Y//4 - 35)
            screen.blit(text,text_rect)
            text = small_font.render("button and then click on the card", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4)
            screen.blit(text,text_rect)
            text = small_font.render("to be discarded. Note: You must have", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 35)
            screen.blit(text,text_rect)
            text = small_font.render("14 cards in your hand to discard a card.", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 70)
            screen.blit(text,text_rect)

        if insert.is_hover or insert_mode:
            text = small_font.render("To reposition a card in the hand, click", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2, 3*Y//4 - 70)
            screen.blit(text,text_rect)
            text = small_font.render("on the insert button. Click on the card", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 - 35)
            screen.blit(text,text_rect)
            text = small_font.render("that is to be inserted at a different place", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4)
            screen.blit(text,text_rect)
            text = small_font.render("and then click on the card that is to", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 35)
            screen.blit(text,text_rect)
            text = small_font.render("be present before the inserted card.", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 70)
            screen.blit(text,text_rect)

        if sort.is_hover:
            text = small_font.render("Sort button sortes the hand according to", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 - 35)
            screen.blit(text,text_rect)
            text = small_font.render("suites and ranks. Added to ease the", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4)
            screen.blit(text,text_rect)
            text = small_font.render("arrangement of cards.", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 35)
            screen.blit(text,text_rect)

        if len(deck.pile) > 0 and deck.pile[0].is_hover:
            text = small_font.render("To take the card on top of the pile,", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 - 35)
            screen.blit(text,text_rect)
            text = small_font.render("click on the pile card.", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4)
            screen.blit(text,text_rect)

        if draw.is_hover:
            text = small_font.render("To draw a card from the deck then", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 - 35)
            screen.blit(text,text_rect)
            text = small_font.render("click on the card that is facing ", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4)
            screen.blit(text,text_rect)
            text = small_font.render("backwards in the middle of the game.", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (8 * card_gap + 7 * card_width + padding + text.get_width()//2 , 3*Y//4 + 35)
            screen.blit(text,text_rect)


def tutorial_check(mouse_pos, event):
    """
        To take mouse input for buttons etc. in the tutorial.
    """
    global stage
    if stage[1] == 5:
        player_turn(mouse_pos, event)
    if stage[1] != last_stage:
        next.check(mouse_pos, event)
        skip.check(mouse_pos, event)
        if skip.is_clicked:
            stage[0] = 0
            stage[1] = 0
        if next.is_clicked:
            stage[1] += 1

    else:
        finish.check(mouse_pos, event)
        if finish.is_clicked:
            stage[0] = 0
            stage[1] = 0

##############################
#
# winner = user
# deal_mode = True
# deal = 3
# winning_hand = [True,[user.hand]]
# round_over()
# computer = Player("ds", 0, test_hand)
# computer_turn()
##########################
# before_game_reset()
#GAME LOOP
while running:
    screen.fill([220,220,220])
    if not (stage[0] == 0 or stage[0] == 4):
        back_button.display(screen)
    if stage[0] == -1:
        tutorial_show()

    if stage[0] <= 3 and stage[0] >= 0:
        screen.blit(heading, heading_rect)

    if stage[0] == 0:
        start.display(screen)
        how_to.display(screen)

    elif stage[0] == 1:
        display_testbox(name, screen)

    elif stage[0] == 2:
        user.name = name.text
        user_name = text_font.render(user.name, True, textbox.color1)
        user_name_rect = user_name.get_rect()
        user_name_rect.center = (3*X//4, Y//5)
        points_rummy.display(screen)
        deal_rummy.display(screen)

    elif stage[0] == 3:
        user.name = name.text
        user_name = text_font.render(user.name, True, textbox.color1)
        if points_mode:
            screen.blit(points_text, points_text_rect)
            points_100.display(screen)
            points_200.display(screen)
        elif deal_mode:
            screen.blit(deal_text, deal_text_rect)
            deal_1.display(screen)
            deal_3.display(screen)
            deal_5.display(screen)

    elif stage[0] == 4:
        if print_no_declare:
            text = text_font.render("You don't have a valid declare!", True, textbox.color1)
            text_rect = text.get_rect()
            text_rect.center = (X//2, Y//2)
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            print_no_declare = False
        else:
            show_game(screen, user, deck)

    elif stage[0] == 5:
        round_over_display()

    for event in pygame.event.get():
        button_parameter = (pygame.mouse.get_pos(), event)
        back_button.check(button_parameter[0], button_parameter[1])
        if back_button.is_clicked :
            if stage[0] > 0:
                stage[0] -= 1
            elif stage[0] == -1:
                if stage[1] > 0:
                    stage[1] -= 1
                else:
                    stage[1] = 0
                    stage[0] = 0

        if stage[0] == 5:
            round_over_event(button_parameter[0], button_parameter[1])

        elif stage[0] == 4:
            showCP.check(button_parameter[0], button_parameter[1])
            if user.turn :
                player_turn(button_parameter[0], button_parameter[1])
            elif computer.turn :
                computer_turn()

        elif stage[0] == 3:
            if points_mode :
                points_100.check(button_parameter[0], button_parameter[1])
                points_200.check(button_parameter[0], button_parameter[1])
                if points_100.is_clicked:
                    target = 100
                    stage[0] += 1
                if points_200.is_clicked :
                    target = 200
                    stage[0] += 1
            if deal_mode:
                deal_1.check(button_parameter[0], button_parameter[1])
                deal_3.check(button_parameter[0], button_parameter[1])
                deal_5.check(button_parameter[0], button_parameter[1])
                if deal_1.is_clicked:
                    deal = 1
                    stage[0] += 1
                if deal_3.is_clicked:
                    deal = 3
                    stage[0] += 1
                if deal_5.is_clicked:
                    deal = 5
                    stage[0] += 1

        elif stage[0] == 2:
            points_rummy.check(button_parameter[0], button_parameter[1])
            deal_rummy.check(button_parameter[0], button_parameter[1])
            if points_rummy.is_clicked or deal_rummy.is_clicked :
                stage[0] += 1
            if points_rummy.is_clicked :
                points_mode = True
            if deal_rummy.is_clicked:
                deal_mode = True
            # input_textbox(rounds, event, stage)

        elif stage[0] == 1:
            input_textbox(name, event, stage)

        elif stage[0] == 0 :
            start.check(button_parameter[0], button_parameter[1])
            how_to.check(button_parameter[0], button_parameter[1])
            if start.is_clicked:
                stage[0] += 1
            if how_to.is_clicked :
                stage[0] = -1
                stage[1] = 0

        elif stage[0] == -1:
            tutorial_check(button_parameter[0], button_parameter[1])

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
