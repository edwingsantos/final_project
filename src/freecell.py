# LV 1st Freecell 

# import random
# import csv
# import tkinter (or customtkinter for GUI) - or find another way to do it
# from Lizzie's code import saving to CSV function and move function

# MENU - Call in Main
# Create window
# Add button "Play Solitaire"
#      when clicked, start solitaire game
# Add button "Instructions"
#      show how to play
# Add button "Exit"
#      close program
# Display window



# CREATE DECK -  call the JSON with the cards
# Make empty list called deck
# For each suit (hearts, diamonds, clubs, spades):
#     For each value (A, 2–10, J, Q, K):
#         Add card to deck
# Return deck

# SHUFFLE DECK
# Randomize order of deck
# Return shuffled deck
# Returns a list from numbers 1-52

# SETUP BOARD (7 COLUMNS)
# Create 7 empty columns
# First column gets 1 card
# Second column gets 2 cards
# Continue until seventh column gets 7 cards
# Remove cards from deck as placing them
# Return board and remaining deck

# SHOW BOARD
# Display all columns
# Show top card clearly
# (Maybe: hide cards underneath)

# PLAYER INPUT
# Ask player for:
#     source column
#     destination column
# Return move choice

# VALID MOVE CHECK -Lizzie
# If moving card:
#     Check colors are opposite (red vs black)
#     Check value is one less than destination card
# If both true:
#     Move is valid
# Else:
#     Move is invalid

# MOVE FUNCTION
# Take top card from selected column
# Check if move is valid
# If valid:
#     Place card in new column or foundation
# If not valid:
#     Print "Error, can't move that card"

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

