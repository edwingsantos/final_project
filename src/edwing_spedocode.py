#ES starting spedocode

# import pygame, json, sys 


#call the shufle funtion from lucy and append it to the points dictionary 
# do the same thing but just append it to the dealers hand 


#use dictionary called point to safe the cards choosen 
#make a dictionary for the dealers hand 
#use an other dictionary for the amount of games played 
#use another dictianry for win games
#user another library for money 
#check if the 3rd line of the csv is 0
# if the 3rd line is empty give the user 100$ and append it to the money dictionary 


#SET up screen 
#set up the board with two cards you can see, these cards have to match with the ones in the points dicitonary 
#Have two card for the dealer and make one card show, remember one of those have to match in the dictionary


#call the beggingin of the betting funtion 
#safe those amounts into the ductionaries 

#show users their cards and let them see the dealers cards
#if the user has an instant 21
    





















import pygame 
import sys 


GAME_WIDTH =  1000
GAME_HEIGHT = 1000

pygame.init()#always make this
screen = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("Blackjack card game")#title of the window

clock = pygame.time.Clock()
clock.tick(60)

running = True #a kind of break 

#keeps window open 
while running: #game loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #breaking the code by making to loop false