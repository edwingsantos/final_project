#Contains classes for displaying each card

import pygame

#class for all clubs:
class Clubs:
    #initialize card size - Name, Card Value, suit is clubs, color is black, if it is a royal use royal class
    def __init__(self,card_name,card_value,is_royal):
        self.name = card_name
        self.value = card_value
        self.royalty = is_royal

    #Show Card method (coordinates):
    def show_card(self,screen,coords_and_size=(100,100,100,140)):
        #design a card with pygame and then this sprite will be created and displayed at coordinates (top-left)
        pygame.draw.rect(screen,"white",coords_and_size,border_radius=5)
        pygame.font.SysFont(self.name,216)
        pygame.surface

#class for all spades:
    #initialize card size - Name, Card Value, suit is spades, color is black, if it is a royal use royal class

    #Show Card method (coordinates):
        #design a card with pygame and then this sprite will be created and displayed at coordinates (top-left)

#class for all diamonds:
    #initialize card size - Name, Card Value, suit is diamonds, color is red, if it is a royal use royal class

    #Show Card method (coordinates):
        #design a card with pygame and then this sprite will be created and displayed at coordinates (top-left)

#class for all hearts:
    #initialize card size - Name, Card Value, suit is hearts, color is red, if it is a royal use royal class

    #Show Card method (coordinates):
        #design a card with pygame and then this sprite will be created and displayed at coordinates (top-left)
