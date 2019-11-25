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
        if self.is_hover :
            pygame.draw.rect(screen, self.hover_color , (self.position[0], self.position[1], self.width, self.height))
        elif self.is_clicked :
            pygame.draw.rect(screen, self.click_color, (self.position[0], self.position[1], self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))
        screen.blit(self.title_img, self.title_img_rect)

    def set_center(self, pos):
        self.title_img_rect.center = pos
        self.position = (pos[0] - self.width // 2, pos[1] - self.height // 2)


# def max_matched(self):
#     self.fill_all_possible()
#     max = []
#     max_elem = 0
#     max_pure = False
#     max_four = False
#     new_four = False
#     new_pure = False
#     new = []
#     new_elem = 0
#     for i in allPossible.keys():
#         new = i
#         if allPossible[i] == "four":
#             new_four = True
#         if allPossible[i] == "pure":
#             new_pure = True
#         new_elem = len(i)
#         for j in allPossible.keys():
#             new_j = new
#             new_elem_j = new_elem
#             ans = True
#             for s in range(len(j)):
#                 check = j[s].isIn(new)
#                 if type(check) == type(False):
#                     ans = False
#             if ans:
#                 if allPossible[j] == "four":
#                     new_four = True
#                 if allPossible[j] == "pure":
#                     new_pure = True
#                 new_j += j
#                 new_elem_j += len(j)
#             for k in allPossible.keys():
#                 new_k = new_j
#                 new_elem_k = new_elem_j
#                 ans = True
#                 for s in range(len(k)):
#                     check = k[s].isIn(new)
#                     if type(check) == type(False):
#                         ans = False
#                 if ans:
#                     if allPossible[k] == "four":
#                         new_four = True
#                     if allPossible[k] == "pure":
#                         new_pure = True
#                     new_k += k
#                     new_elem_k += len(k)
#                 for l in allPossible.keys():
#                     ans = True
#                     new_l = new_k
#                     new_elem_l = new_elem_k
#                     for s in range(len(l)):
#                         check = l[s].isIn(new)
#                         if type(check) == type(False):
#                             ans = False
#                     if ans:
#                         if allPossible[l] == "four":
#                             new_four = True
#                         if allPossible[l] == "pure":
#                             new_pure = True
#                         new_l += l
#                         new_elem_l += len(l)
#                     if max_elem < new_elem_l:
#                         max = copy.deepcopy(new_l)
#                         max_elem = new_elem_l
#                         max_four = new_four
#                         max_pure = new_pure
#                     if max_elem == new_elem_l:
#                         if new_four and max_four:
#                             if new_pure and (not max_pure):
#                                 max = copy.deepcopy(new_l)
#                                 max_elem = new_elem_l
#                                 max_four = new_four
#                                 max_pure = new_pure
#                         if new_four and (not max_four):
#                             max = copy.deepcopy(new)
#                             max_elem = new_elem_l
#                             max_four = new_four
#                             max_pure = new_pure
#     return (max, max_elem, max_four, max_pure)
