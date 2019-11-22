import pygame
pygame.init()

X = 1360
Y = 768
color1 = [100,50,100]
color2 = [50,100,100]
black = [0,0,0]
running= True
shift = False
padding = 40
stage = 1
fontName = "centurygothic"

screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Loading Screen')
heading_font = pygame.font.SysFont(fontName, 200, True)
heading = heading_font.render("RUMMY", True, color2)
heading_rect = heading.get_rect()
heading_rect.center = [X//2, Y//4]


class TextBox():
    """
        class defined to present a text box to take input
    """
    def __init__(self, title):
        """
            Parameters : Title of textbox
        """
        self.title = title
        self.text = ""
        self.font = pygame.font.SysFont(fontName, 50)
        self.font_img = self.font.render(self.text, True, color1)
        self.title_img = self.font.render(self.title, True, color1)
        self.title_img_rect = self.title_img.get_rect()
        self.title_img_rect.center = (padding + self.title_img.get_width()//2, 5*Y//8)
        self.img_rect = self.font_img.get_rect()
        self.img_rect.center = [self.title_img.get_width() + self.font_img.get_width()//2 + padding, 5*Y//8]

    def update_text(self,ch):
        """
             Adds ch to the text input.
            Parameters : ch
        """
        self.text += chr(ch)
        self.update()

    def update(self):
        """
            Updates the renderring image of text input to show after every loop. Also updates position
        """
        rect = self.img_rect.center
        self.font_img = self.font.render(self.text, True, color1)
        self.img_rect = self.font_img.get_rect()
        self.img_rect.center = [self.title_img.get_width() + self.font_img.get_width()//2 + padding, 5*Y//8]


def input_textbox(textbox):
    """
        Takes an parameter textbox and adds text to that textbox
    """
    global shift, stage
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
            stage += 1
        else:
            if shift:
                textbox.update_text(event.key - 32)
            else:
                textbox.update_text(event.key)
    pygame.display.update()

def display_testbox(textbox):
    """
        Takes a parameter textbox and displays its title as well as the text that is being given as input
    """
    screen.blit(textbox.title_img, textbox.title_img_rect)
    screen.blit(textbox.font_img, textbox.img_rect)


name = TextBox("Enter Name : ")
rounds = TextBox("Enter Rounds : ")


#GAME LOOP
while running:
    screen.fill(black)
    screen.blit(heading, heading_rect)
    if stage == 1:
        display_testbox(name)
    elif stage == 2:
        display_testbox(rounds)
    for event in pygame.event.get():
        if stage == 2:
            input_textbox(rounds)
        elif stage == 1:
            input_textbox(name)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
