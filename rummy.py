import pygame
#initialize the pygame
pygame.init()#has to be present

#creating screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Rummy")
# icon = pygame.image.load("playing-cards.png")
# pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("assets/back-cover.png")
playerX = 370
playerY = 480
def player(x, y):
    screen.blit(playerImg, (x, y))
    # pygame.transform.scale(playerImg, (20,40))
playerXD = 0
#Game Loop
running = True
while running:
    screen.fill((0,150,0)) # background
    # playerXD = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
                playerXD = 0.1
            if event.key == pygame.K_LEFT:
                playerXD = -0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerXD = 0

#Background
    playerX += playerXD
    player(playerX , playerY)
    pygame.display.update()#has to be present
