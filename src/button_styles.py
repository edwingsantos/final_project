#Contains button creation functions

import pygame

class Button:
    def __init__(self,text,color,hover_color,size=(200,100),position=(0,0)):
        self.text = text
        self.rect_vis = pygame.Rect(position + size)
        self.font = pygame.font.SysFont(None,28)
        self.color = color
        self.hovering_color = hover_color

    def show(self,screen):

        mouse_position = pygame.mouse.get_pos()

        #changes color of button if the mouse is over it
        if self.rect_vis.collidepoint(mouse_position):
            color = self.hovering_color

            #mouse is not on it so leave it normal
        else:
            color = self.color
        
        #actual button
        pygame.draw.rect(screen, color, self.rect_vis,border_radius=4)
        #border for button
        pygame.draw.rect(screen, "black",self.rect_vis,4,border_radius=4)

        #create text
        t_surface = self.font.render(self.text,True,"black")
        #puts text in the middle of the box
        t_pos = t_surface.get_rect(center=self.rect_vis.center)

        screen.blit(t_surface,t_pos)
    
    def click_check(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect_vis.collidepoint(event.pos)
        return False