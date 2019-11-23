import pygame
import textbox
import cards
import button
from button import Button
from textbox import TextBox,display_testbox,input_textbox
from cards import *


pygame.init()
X = 1360
Y = 768
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Rummy')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
#
#Stage 1 : Take name
#Stage 2 : Take number of Rounds
#Stage 3 : Instructions
#Stage 4 : Game
#Stage 5 : Score Display and winner declared
#
#GLOBAL VARIABLES

stage = [1]
fontName = "centurygothic"
running = True
black = [0,0,0]
card_gap = 10
padding = 20

#Stage 0 :
heading_font = pygame.font.Font("Pacifico-Regular.ttf", 200)
heading = heading_font.render("Rummy", True, textbox.color2)
heading_rect = heading.get_rect()
heading_rect.center = [X//2, Y//4]

#Stage 1 :
name = TextBox("Enter Name : ")
#Stage 2 :
rounds = TextBox("Enter Rounds : ")
#Stage 3 :
#Instructions .. will be dealt with later
#Stage 4 :
deck = Deck(2)
user = Player("Rohan",5)
computer = Player("PC")
user.deal_cards(deck)
computer.deal_cards(deck)
deck.shuffle_cards()
deck.set_joker()
cardss = deck.draw_card()
deck.update_pile(cardss)
draw = Card('A', 'spades')
swap = Button("Swap", (3*X//4 + 120, 3*Y//4 + 140))
insert = Button("Insert", (3*X//4 + 120, 3*Y//4))
sort = Button("Sort",(3*X//4, 3*Y//4))
shut = Button("Shut",(3*X//4, 3*Y//4 + 140))
discard = Button("Discard",(3*X//4 + 120, 3*Y//4 + 70 ))
showCP = Button("Show Computer", (3*X//4, Y//2))
user.turn = True
discard_mode = False
swap_mode = False
insert_mode = False
index = []

def show_game(screen, player, deck):
    images = player.show_hand()
    count = 0
    #Show Player Cards
    for i in images:
        if count < 7:
            player.hand[count].position = (count*(i.get_width() + card_gap)+ padding ,Y - 2*i.get_height() - padding- card_gap)
            screen.blit(i, (count*(i.get_width() + card_gap)+ padding ,Y - 2*i.get_height() - padding- card_gap))
        else:
            player.hand[count].position = ((count-7)*(i.get_width() + card_gap)+ padding ,Y - i.get_height() - padding)
            screen.blit(i, ((count-7)*(i.get_width() + card_gap)+ padding ,Y - i.get_height() - padding))
        count += 1
    back = pygame.image.load('assets/back.png')
    back = pygame.transform.scale(back, (back.get_width()//4,back.get_height()//4))
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
        deck.pile[i].position = (5*padding, 2*(img[i].get_height() + card_gap + padding))
        screen.blit(img[i], (5*padding, 2*(img[i].get_height() + card_gap + padding)))
    #show Joker
    img = deck.joker.show()
    screen.blit(img, (8*(back.get_width() + card_gap) + padding ,2*(back.get_height() + card_gap + padding)))
    joker_font = pygame.font.SysFont(fontName, 25)
    joker = joker_font.render("Joker", True,black)
    joker_rect = joker.get_rect()
    joker_rect.center = [8*(back.get_width() + card_gap) + back.get_width()//2 + padding ,3*(back.get_height() + card_gap + padding)]
    screen.blit(joker, joker_rect)
    #show deck
    draw.position = (7*(back.get_width() + card_gap) + padding ,2*(back.get_height() + card_gap + padding))
    screen.blit(back, (7*(back.get_width() + card_gap) + padding ,2*(back.get_height() + card_gap + padding)))
    #show buttons
    sort.display(screen)
    shut.display(screen)
    discard.display(screen)
    showCP.display(screen)
    insert.display(screen)
    swap.display(screen)

def player_turn(event, mouse_pos):
    global discard_mode, swap_mode, index, insert_mode
    sort.check(mouse_pos, event)
    draw.check(mouse_pos, event)
    insert.check(mouse_pos,event)
    shut.check(mouse_pos, event)
    swap.check(mouse_pos, event)
    discard.check(mouse_pos, event)
    for i in range(len(deck.pile)):
        deck.pile[i].check(mouse_pos,event)
    for i in range(len(user.hand)):
        user.hand[i].check(mouse_pos, event)

    if len(deck.pile) != 0 :
        if deck.pile[0].is_clicked and len(user.hand) == 13:
                user.draw_card(deck.pile.pop(0))
    i = 0
    while i < len(user.hand):
        # if user.hand[i].is_clicked :
        #     print(i)
        if user.hand[i].is_clicked and discard_mode and len(user.hand) == 14:
            print("Discard ", i)
            user.turn = False
            computer.turn = True
            # if user.hand == 14:
            deck.update_pile(Card(user.hand[i].rank, user.hand[i].suit))
            user.discard_card(user.hand[i])
            i -= 1
            discard_mode = False
        if user.hand[i].is_clicked and swap_mode :
            index.append(i)
            if len(index) >= 2:
                swap_mode = False
                user.swap(index)
                print(index[0],index[1]) # got to implement swap function in player class
                index = []
        if user.hand[i].is_clicked and insert_mode :
            index.append(i)
            if len(index) >= 2:
                insert_mode = False
                user.insert(index)
                print("Insert",index[0],index[1]) # got to implement insert function in player class
                index = []
        i += 1
    if swap.is_clicked or swap_mode or (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
        swap_mode = True
    #     if event.type == pygame.MOUSEBUTTONDOWN :
    #         # code to check which card mouse points to
    #         index = (mouse_pos[0] - padding)// (draw.width + card_gap)
    #         print(index)
    #         if index < 7 :
    #             swap_mode = False
    if insert.is_clicked or insert_mode or (event.type == pygame.KEYDOWN and event.key == pygame.K_i):
        insert_mode = True
        # ind = (mouse_pos[0] - padding)// (draw.width + card_gap)
        # print(ind)
        # if mouse_pos[1] < Y and mouse_pos[1] > Y - draw.width - padding:
        #     ind += 7
        # index.append(ind)
        # if len(index) > 2:
        #     insert_mode = False
        #     print("Insert : ", index[0], index[1])

    if sort.is_clicked :
        user.hand = sort_hand(user.hand)
    if draw.is_clicked and len(user.hand) == 13:
        user.draw_card(deck.draw_card())
    if shut.is_clicked:
        if user.shut_game()[0] :
            print("True")
        else:
            print("False")
    if discard.is_clicked or discard_mode:
        discard_mode = True
    pygame.display.update()

    # screen.blit()
#GAME LOOP
while running:
    screen.fill([220,220,220])
    if stage[0] == 1:
        display_testbox(name, screen)
        screen.blit(heading, heading_rect)
    elif stage[0] == 2:
        display_testbox(rounds, screen)
        screen.blit(heading, heading_rect)
    elif stage[0] == 3:
        show_game(screen, user, deck)
    for event in pygame.event.get():
        if stage[0] == 3:
            showCP.check(pygame.mouse.get_pos(), event)
            if user.turn :
                player_turn(event, pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    user.hand = sort_hand(user.hand)
        if stage[0] == 2:
            input_textbox(rounds, event, stage)
        elif stage[0] == 1:
            input_textbox(name, event, stage)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
