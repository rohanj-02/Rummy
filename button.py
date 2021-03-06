import pygame
pygame.init()

X = 1360
Y = 768
color1 = [250,250,250]
color2 = [50,100,100]
black = [0,0,0]
shift = False
padding = 40
fontName = "montserrat.ttf"

class Button():
    """
        class defined to present a button to perform some function
    """
    def __init__(self, title = "Button", position = (X//2,Y//2), width = 100, height = 50, fontname = fontName):
        """
            Parameters : Title of Button
        """
        self.title = title
        self.position = position
        self.width = width
        self.is_clicked = False
        self.is_hover = False
        self.height = height
        self.color = [240,0,40]
        self.hover_color = [220,0,0]
        self.click_color = [177,15,46]
        self.font = pygame.font.Font(fontname, 25)
        self.title_img = self.font.render(self.title, True, color1)
        self.title_img_rect = self.title_img.get_rect()
        self.title_img_rect.center = (self.position[0] + self.width //2, self.position[1] + self.height//2)

    def set_color(self,color):
        self.color = color

    def set_hover_color(self,hover):
        self.hover_color = hover

    def set_click_color(self,click):
        self.click_color = click

    def check(self, mouse_pos, event):
        """
            THe function checks whether the button was clicked or if the mouse is hovering on the button.
        """
        if mouse_pos[0] >= self.position[0] and mouse_pos[0] <= self.position[0] + self.width and mouse_pos[1] >= self.position[1] and mouse_pos[1] <= self.position[1] + self.height:
            self.is_hover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_hover = False
                self.is_clicked = True
            else:
                self.is_clicked = False
        else:
            self.is_clicked = False
            self.is_hover = False

    def display(self, screen):
        """
            Displays the button on the screen according to its position and the action on the button.
        """
        if self.is_hover :
            pygame.draw.rect(screen, self.hover_color , (self.position[0], self.position[1], self.width, self.height))
        elif self.is_clicked :
            pygame.draw.rect(screen, self.click_color, (self.position[0], self.position[1], self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))
        screen.blit(self.title_img, self.title_img_rect)

    def set_center(self, pos):
        """
            Sets the center for the button to the given parameters.
        """
        self.title_img_rect.center = pos
        self.position = (pos[0] - self.width // 2, pos[1] - self.height // 2)
