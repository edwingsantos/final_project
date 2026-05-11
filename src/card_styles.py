#Contains classes for displaying each card

import pygame

#!HOW TO CREATE A CARD WITH THIS CLASS! - for the team. - Delete the comments line 5 through 11 once everyone has read them

    #symbols: ♠ ♥ ♦ ♣

    #Step 1: create object
        #ex: mycard = Card(10,"♥","red")
    
    #Step Two: Display the card (screen is from your pygame game-loop) You can also change the preset coords
        #ex: mycard.show_card(screen,coords=(100,100))

#class for all clubs:
class Card:
    #initialize card size - Name, Card Value, suit (as segoeuisymbol - from symbols comment), color
    def __init__(self,card_value,suit,color):
        self.value = card_value
        self.color = color
        self.suit = suit
        
        match self.value:
            case 1:
                self.symbol = "A"
        
            case 11:
                self.symbol = "J"

            case 12:
                self.symbol = "Q"
        
            case 13:
                self.symbol = "K"
            
            case _:
                self.symbol = str(card_value)

    #Show Card method (coordinates):
    def show_card(self,screen,size=(100,140),coords=(100,100)):
        #design a card with pygame and then this sprite will be created and displayed at coordinates (top-left)

        font = pygame.font.SysFont(None,48)
        st_font = pygame.font.SysFont("segoeuisymbol",48)

        #stuff on card
        font_surface = font.render(self.symbol,False,self.color)
        suit_surface = st_font.render(self.suit,True,self.color)

        #creates surface with given size and makes the actual surface translucent
        card = pygame.Surface(size, pygame.SRCALPHA)
        
        #creates shape
        pygame.draw.rect(card, "white", card.get_rect(), border_radius=8)
        pygame.draw.rect(card, "black", card.get_rect(), 3, border_radius=8)
        
        #flipped card stuff
        flipped_text = pygame.transform.rotate(font_surface,180)
        flipped_suit = pygame.transform.rotate(suit_surface, 180)

        #normal text
        card.blit(font_surface,(2,10))
        card.blit(suit_surface,(35,-10))
        
        #upside down text
        card.blit(flipped_text,(65,100))
        card.blit(flipped_suit,(35,90))
        
        screen.blit(card,coords)
        