#PS 1st FreeCell pseudocode

#import necessary libraries
from card_styles import *
from button_styles import *
import json
import pygame
import csv
import random

#Note:all cards are stored by ID NOT value

#shuffle cards func
def shuffle():
    with open("files/cards.json","r") as card_info:
        deck_info = json.load(card_info)
    
    deck = list(deck_info.keys())

    random.shuffle(deck)

    return deck

#setup func
def setup():
    deck = shuffle()
    
    #useful vars
    freecells = []
    ace_piles = [
        [],
        [],
        [],
        []
    ]
    
    #tableau contains lists which represent columns
    tableau = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    
    #load tableau
    for i, card in enumerate(deck):
        tableau[i % 8].append(card)
    
    return freecells, ace_piles, tableau

#CHECKS
def moveable_cards(tableau,freecells,ace_piles):
    moveable = []
    for x in tableau:
        moveable.append(x[-1])
    
    for x in freecells:
        moveable.append(x)
    
    for x in ace_piles:
        moveable.append(x-1)
    
    return moveable

#places to move check

#valid places
        

#game func
def free_cell_game():
    #normal vars
    freecells, ace_piles, tableau = setup()
    print(tableau)
    moveable = []
    card_status = {}
    selected = 0
    landing_positions = []
    
    #setup pygame
    pygame.init()
    screen = pygame.display.set_mode((1600,1200))
    clock = pygame.time.Clock()
    running = True
    
    #put buttons here

    #game loop
    while running:
        
        #visuals
        screen.fill("darkgreen")

        font = pygame.font.SysFont(None,48)
        title_surface = font.render("FreeCell",True,"white")
        
        screen.blit(title_surface,(700,50))


    #check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #display tableu

    #display ace piles

    #display free cells

    #find movable cards

    #find places for cards to be moved - Ace piles, other parts of tableau, free cells

    #check if game is over
        #if yes, end game loop and save to csv
    
        pygame.display.flip()

        dt = clock.tick(60) / 100
    
    pygame.quit()

free_cell_game()