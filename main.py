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
c = deck.draw_card()
deck.update_pile(c)
sort = Button("Sort",(3*X//4, 3*Y//4))
draw = Button("Draw", (3*X//4, 3*Y//4 + 70))
shut = Button("Shut",(3*X//4, 3*Y//4 + 140))
draw_from_pile = Button("Draw Pile", (3*X//4 + 120, 3*Y/4 + 140))
discard = Button("Discard",(3*X//4 + 120, 3*Y//4 + 70 ))
showCP = Button("Show Computer", (3*X//4, Y//2))


def show_game(screen, player, deck):
    images = player.show_hand()
    count = 0
    #Show Player Cards
    for i in images:
        if count < 7:
            screen.blit(i, (count*(i.get_width() + card_gap)+ padding ,Y - 2*i.get_height() - padding- card_gap))
        else:
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
    # img = pygame.transform.scale(img, (img.get_width()//4, img.get_height()//4))
    screen.blit(img, (5*padding, 2*(img.get_height() + card_gap + padding)))
    #show Joker
    img = deck.joker.show()
    screen.blit(img, (8*(back.get_width() + card_gap) + padding ,2*(back.get_height() + card_gap + padding)))
    joker_font = pygame.font.SysFont(fontName, 25)
    joker = joker_font.render("Joker", True,black)
    joker_rect = joker.get_rect()
    joker_rect.center = [8*(back.get_width() + card_gap) + back.get_width()//2 + padding ,3*(back.get_height() + card_gap + padding)]
    screen.blit(joker, joker_rect)
    #show deck
    screen.blit(back, (7*(back.get_width() + card_gap) + padding ,2*(back.get_height() + card_gap + padding)))
    #show buttons
    sort.display(screen)
    draw.display(screen)
    shut.display(screen)
    draw_from_pile.display(screen)
    discard.display(screen)
    showCP.display(screen)

def player_turn(event, mouse_pos):
    sort.check(mouse_pos, event)
    draw.check(mouse_pos, event)
    shut.check(mouse_pos, event)
    draw_from_pile.check(mouse_pos, event)
    discard.check(mouse_pos, event)
    if sort.is_clicked :
        user.hand = sort_hand(user.hand)
    if draw.is_clicked :
        user.draw_card(deck.draw_card())
    if draw_from_pile.is_clicked :
        user.draw_card(deck.pile)
    if shut.is_clicked:
        if user.shut_game()[0] :
            print("True")
        else:
            print("False")
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
        # screen.blit(spadeJ.show(), (X//2,Y//2))
    for event in pygame.event.get():
        if stage[0] == 3:
            showCP.check(pygame.mouse.get_pos(), event)
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
