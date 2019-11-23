import pygame
import textbox
import cards
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


heading_font = pygame.font.SysFont(fontName, 200, True)
heading = heading_font.render("RUMMY", True, textbox.color2)
heading_rect = heading.get_rect()
heading_rect.center = [X//2, Y//4]

spadeJ = Card('J', 'spades')
# use player 1

name = TextBox("Enter Name : ")
rounds = TextBox("Enter Rounds : ")

#GAME LOOP
while running:
    screen.fill(black)
    if stage[0] == 1:
        display_testbox(name, screen)
        screen.blit(heading, heading_rect)
    elif stage[0] == 2:
        display_testbox(rounds, screen)
        screen.blit(heading, heading_rect)
    elif stage[0] == 3:
        images = player1.show_hand()
        count = 0
        for i in images:
            if count < 7:
                screen.blit(i, (count*(i.get_width() + card_gap)+ padding ,Y - 2*i.get_height() - padding- card_gap))
            else:
                screen.blit(i, ((count-7)*(i.get_width() + card_gap)+ padding ,Y - i.get_height() - padding))
            count += 1
        # screen.blit(spadeJ.show(), (X//2,Y//2))
    for event in pygame.event.get():
        if stage[0] == 3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player1.hand = sort_hand(player1.hand)
        if stage[0] == 2:
            input_textbox(rounds, event, stage)
        elif stage[0] == 1:
            input_textbox(name, event, stage)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
