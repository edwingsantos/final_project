# LV 1st Solitaire

# import random
# import csv
# import tkinter (or customtkinter for GUI) - or find another way to do it
# from Lizzie's code import saving to CSV function and move function
# Asegurarme que en verdad funcione para Solitaire y no para Freecell 
# Que la logica funcione bien y sea entendible para que funcione de la manera que queremos
# Creo que ya lo solucione
import pygame
import random
import csv
from LD_psuedocode import *

# MENU - Screen set up
# Create window
# Add button "Play Solitaire"
#      when clicked, start solitaire game
# Add button "Instructions"
#      show how to play
# Add button "Exit"
#      close program
# Display window

screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0]) #sets screen size to whatever the first monitor's dimension

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


# CREATE DECK -  call the JSON with the cards
# Make empty list called deck
# For each suit (hearts, diamonds, clubs, spades):
#     For each value (A, 2–10, J, Q, K):
#         Add card to deck
# Return deck

def deck():
    deck = []
# Aun no se como hacer esta parte pero lo voy a averiguar y despues le agrego el pygame

# SHUFFLE DECK
#def shuffle_deck(deck):
    # Create an empty list to store shuffled cards
    # While there are still cards left in the original deck
    # Generate a random index between 0 and the last position in the deck       
        # Remove the card at that random index from the original deck
        # Add that card to the shuffled deck
    # Once all cards have been moved, return the shuffled deck

def shuffle_deck(deck):   
    shuffled_deck = []
    while len(deck) > 0:       
        random_index = random.randint(0, len(deck) - 1)
        selected_card = deck.pop(random_index)
        shuffled_deck.append(selected_card)
    return shuffled_deck


# SETUP BOARD (7 COLUMNS)
#Create 7 empty columns (tableau)
#FOR column = 1 TO 7:
#    FOR i = 1 TO column:
#        Remove top card from deck
#        Add card to tableau[column]
#        IF i == column:
#            Set card.face_up = True
#        ELSE:
#            Set card.face_up = False
#Set remaining cards as STOCK (face-down)
#Create empty WASTE pile
#Create 4 empty FOUNDATION piles
#Return tableau, stock, waste, foundations

def set_board():
    column =[] # Despues ver como hago las 7 columnas pero mas eficiente que 1-7 
   


# SHOW BOARD
# Display all columns
# Show top card clearly
# (Maybe: hide cards underneath)

# PLAYER INPUT
# import lizzies func that makes sure if it is the same color or not 
# Ask player for move type:
#    1. Move card
#    2. Draw from stock
#IF move:
#    Ask for source (column or waste)
#    Ask for destination (column or foundation)
#Return move choice


# VALID MOVE CHECK -Lizzie
# If moving card:
#     Check colors are opposite (red vs black)
#     Check value is one less than destination card
# If both true:
#     Move is valid
# Else:
#     Move is invalid

# MOVE FUNCTION
# Take card (or stack) from source
#Check if move is valid
#IF valid:
#    Move card(s) to destination
#    IF source column now has a face-down card on top:
#        Flip it face-up
#ELSE:
#    Print "Error, can't move that card"

# FOUNDATION RULES
# Cards must be same suit
# Must go in order: A to  K
# Only Ace can start foundation

# WIN CONDITION
# Check all 4 foundation piles
# If each pile has 13 cards in correct order:
#     Player wins

# SAVE GAME STATS - Lizzie
# Open CSV file
# Write win or loss
# Save and close file

# GAME LOOP - Only for testing
# While game is not over:
#     Show board
#     Get player move
#     Try to move card
#     If win condition met:
#         Print "You win"
#         Save result
#         End game