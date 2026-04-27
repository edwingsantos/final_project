#Es betting fuction 

#make a money saved dictionary to put how much they have won 
user_money = {}
#make a dictionary called money to safe how much they want to bet 
betting_money = {}

#make a funtion for the beggining bets 

    #ask user what their starting amount for betting is 

    #ask to make sure if that is the amount they want
    #if yes then safe that amount of money in the dictionary called money 
    #elif no then just send them back to the beggining of the funtion using return 



#make a FUNCTION for loose, take the amount of money safed in the dictionary and take it
    #safe the money amount in the "money saved" dictionary and call the lizzie funtion 


#make a FUNTION for win,take the amount of money in the "money" dictionary and double it 
    #safe the money amount in the "money saved" dictionary and call the lizzie funtion 


#make a FUNTIOM if its a tie then just return the amount of the money back to their accound and call the lizze funtio to money is up to date


# import pygame
import pygame
from pygame_textinput import *
pygame.init()

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# create the display surface
screen = pygame.display.set_mode((screen_width, screen_height), vsync=1)

# change the window screen title
pygame.display.set_caption('Our Text')

textinput = TextInputVisualizer()
clock = pygame.time.Clock()

# But more customization possible: Pass your own font object
font = pygame.font.SysFont("Consolas", 55)
# Create own manager with custom input validator
manager = TextInputManager(validator = lambda input: len(input) <= 50)

running = True
while running:
    screen.fill((255, 255, 255))

    events = pygame.event.get()

    textinput.update(events)

    screen.blit(textinput.surface, (10, 10))
    
    textinput.update(pygame.event.get())
    screen.blit(textinput.surface, (10, 10))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)