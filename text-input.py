import pygame
pygame.init()

X = 500
Y = 500
color1 = [100,50,100]
color2 = [50,100,100]
white = [0,0,0]


screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Loading Screen')
font = pygame.font.Font("centuryGothic.ttf",30)
img = font.render('Enter Name : ', True, color1, color2)
rect = img.get_rect()
rect.center = (img.get_width()//2, Y//2)
shift = False
running= True
input_name = False


class text_input():
    def __init__(self):
        self.text = ""
        self.font = pygame.font.Font("centuryGothic.ttf", 30)
        self.font_img = self.font.render(self.text, True, color1)
        self.img_rect = self.font_img.get_rect()
        self.img_rect.center = [img.get_width() + self.font_img.get_width()//2, Y//2]

    def update_text(self,ch):
        self.text += chr(ch)
        self.update()

    def update(self):
        rect = self.img_rect.center
        self.font_img = self.font.render(self.text, True, color1)
        self.img_rect = self.font_img.get_rect()
        self.img_rect.center = [img.get_width() + self.font_img.get_width()//2, Y//2]

textbox = text_input()

def take_name():
    global shift, input_name
    screen.blit(img, rect)
    screen.blit(textbox.font_img, textbox.img_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift = True
            elif event.key == pygame.K_BACKSPACE:
                textbox.text = textbox.text[:-1]
                textbox.update()
            elif event.key == pygame.K_RETURN:
                input_name = True
            else:
                if shift:
                    textbox.update_text(event.key - 32)
                else:
                    textbox.update_text(event.key)
        pygame.display.update()

while running:
    screen.fill(white)
    if not input_name:
        take_name()
    else:
        print("Name taken")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
