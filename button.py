import pygame
pygame.init()

X = 1360
Y = 768
color1 = [100,50,100]
color2 = [50,100,100]
black = [0,0,0]
shift = False
padding = 40
fontName = "centurygothic"
screen = pygame.display.set_mode((X,Y))

#Title and Icon
pygame.display.set_caption("Rummy")

class Button():
    """
        class defined to present a button to perform some function
    """
    def __init__(self, title):
        """
            Parameters : Title of Button
        """
        self.title = title
        self.position = (X//2, Y//2)
        self.width = 100
        self.is_pressed = False
        self.is_hover = False
        self.height = 50
        self.color = [0,0,0]
        self.hover_color = [0,0,20]
        self.press_color = [0,20,0]
        self.font = pygame.font.Font(None, 50)
        self.title_img = self.font.render(self.title, True, color1)
        self.title_img_rect = self.title_img.get_rect()
        self.title_img_rect.center = (self.position[0] + self.width //2, self.position[1] + self.height//2)


    def isClicked(self, pos):
        """
            Takes an parameter textbox and adds text to that textbox
        """
        if pos[0] >= self.position[0] and pos[0] <= self.position[0] + self.width and pos[1] >= self.position[1] and pos[1] <= self.position[1] + self.height:
            return True
        return False

    def displayRect(self):
        pygame.draw.rect(screen, [255,0,0], (self.position[0], self.position[1], self.width, self.height))
        screen.blit(self.title_img, self.title_img_rect)











nice = Button("NICE")

running = True

while running:
    nice.displayRect()
    for event in pygame.event.get():
        # if nice.click(pygame.mouse.get_pos()):
            # print("HOVERRR")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if nice.click(pygame.mouse.get_pos()):
                print("NICE")
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
