#ES starting spedocode


# import pygame, random, json, sys 


#check if the 3rd line of the csv is empty

# if the 3rd line is empty give the user 100$

#pull the value 

# make variables of how big you want to screen

# set up the screen and name it the game you need 


# make the main loop of the game
    # let the window close when clicking the exit botton 





















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