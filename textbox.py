import pygame
# pygame.init()

X = 1360
Y = 768
color1 = [17,75,95]
color2 = [23,170,170]
black = [0,0,0]
shift = False
padding = 40
fontName = "centuryGothic.ttf"


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
        self.font = pygame.font.Font(fontName, 40)
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
        # self.img_rect.center = [self.title_img.get_width() + self.font_img.get_width()//2 + padding, 5*Y//8]
        self.img_rect.center = rect

    def set_center(self, pos_title, pos_input):
        self.title_img_rect.center = pos_title
        self.img_rect.center = pos_input


def input_textbox(textbox, event, stage):
    """
        Takes an parameter textbox and adds text to that textbox
    """
    global shift
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
            stage[0] += 1
        else:
            if shift:
                textbox.update_text(event.key - 32)
            else:
                textbox.update_text(event.key)
    pygame.display.update()

def display_testbox(textbox, screen):
    """
        Takes a parameter textbox and displays its title as well as the text that is being given as input
    """
    screen.blit(textbox.title_img, textbox.title_img_rect)
    screen.blit(textbox.font_img, textbox.img_rect)
