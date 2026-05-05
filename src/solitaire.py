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
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solitaire")

GREEN = (0, 120, 0)
WHITE = (255, 255, 255)
GRAY = (80, 80, 80)
BLACK = (0, 0, 0)



# CREATE DECK -  call the JSON with the cards
# Make empty list called deck
# For each suit (hearts, diamonds, clubs, spades):
#     For each value (A, 2–10, J, Q, K):
#         Add card to deck
# Return deck
# Talves en vez de clases immporto el json y de repente funciona
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.face_up = False

    def color(self):
        return "red" if self.suit in ["hearts", "diamonds"] else "black"

    def __repr__(self):
        return f"{self.value}{self.suit[0]}"
    
def create_deck():
    deck = []
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = ["A", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K"]

    for suit in suits:
        for value in values:
            deck.append(Card(suit, value))

    return deck

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
        selected_card = deck.remove(random_index) # tengo qu avergiuar como funciona esta parte porque lamentabemente no funciona el remove
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

# Tal vez cambie esto porque tengfo que importar el json cards
def setup_board(deck):
    tableau = [[] for _ in range(7)]

    for col in range(7):
        for row in range(col + 1):
            card = deck.pop()
            if row == col:
                card.face_up = True
            tableau[col].append(card)

    stock = deck
    waste = []
    foundations = {
        "hearts": [],
        "diamonds": [],
        "clubs": [],
        "spades": []
    }

    return tableau, stock, waste, foundations


# SHOW BOARD
# Display all columns
# Show top card clearly
# (Maybe: hide cards underneath)
CARD_W, CARD_H = 70, 100

# Tal vez esto cambie pero tengo que mejorar unas cuatnas cosas
def draw_card(x, y, card):
    if card.face_up:
        pygame.draw.rect(screen, WHITE, (x, y, CARD_W, CARD_H))
        #text = FONT.render(str(card), True, BLACK)
    else:
        pygame.draw.rect(screen, GRAY, (x, y, CARD_W, CARD_H))
        #text = FONT.render("X", True, BLACK)
# Encontrar porque no funciona esto de aqui
    screen.blit(text, (x + 10, y + 40))

# Esto es para ver las 7 columnas de las cartas
def draw_tableau(tableau):
    start_x = 50
    start_y = 120
    spacing_x = 130
    spacing_y = 25

    for col_index, column in enumerate(tableau):
        for row_index, card in enumerate(column):
            x = start_x + col_index * spacing_x
            y = start_y + row_index * spacing_y
            draw_card(x, y, card)

# PLAYER INPUT
# import lizzies func that makes sure if it is the same color or not 
# Ask player for move type:
#    1. Move card
#    2. Draw from stock
#IF move:
#    Ask for source (column or waste)
#    Ask for destination (column or foundation)
#Return move choice

#Esta es la funcion pero la cosa es que lo tengo que importar mas no copiar y pegar
# Y tengo que usar json para las cartas
def opp_color(card_id1, card_id2):
    def get_color(id):
        with open("P:/DeLong, Lizzie/final_project/files/cards.json", 'r') as json:
            for item in json:
                if str(id) == item:
                    color = item["Color"]
                    break
                else:
                    continue
        return color
    
    # main part of this function
    card_color1 = get_color(card_id1)
    card_color2 = get_color(card_id2)

    if card_color1 == card_color2:
        # The colors match and they cannot be on top of each other
        return False
    else:
        # card colors should be opposite and therefore can be on each other
        return True
# VALID MOVE CHECK -Lizzie
# If moving card:
#     Check colors are opposite (red vs black)
#     Check value is one less than destination card
# If both true:
#     Move is valid
# Else:
#     Move is invalid
# Esto es de Lizzie pero tengo que importarlo mas no copiar y pegar y tnewgo que agregarlo a main
def valid_move(moved_card_id, moved_onto_id):
    valid_color = opp_color(moved_card_id, moved_onto_id)
    valid_num = card_num_check(moved_card_id,moved_onto_id)

    if valid_color == True and valid_num == True:
        return True
    else:
        return False
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
def win():
    # Necesito saber como hacer 4 foundation piles
    # de acuerdo a eso 

# SAVE GAME STATS - Lizzie
# Open CSV file
# Write win or loss
# Save and close file
def write_2_solitaire(path, won):
    game_num = get_game_num(path)
    try:
        with open(path, "a", newline='') as file:
            fieldnames = ['Game Number', 'Win Game']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Game Number': game_num, 'Win Game': won})
    except Exception as e:
        print(f"Could not open the file given.\nPath given: {path}\nReason for error: {e}")
# Esto es para guardarlo en un CSV 

# GAME LOOP - Only for testing
# While game is not over:
#     Show board
#     Get player move
#     Try to move card
#     If win condition met:
#         Print "You win"
#         Save result
#         End game
# tengo que agregar el tableau en alguna parte del loop

def loop():
    while running: # running no esta definido y es un problema que tengo
        #clock.tick(60)
        screen.fill(GREEN)

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # detects mouse is clicked, store the position of the click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                # check tableau clicks
                start_x = 50
                start_y = 120
                spacing_x = 130
                spacing_y = 25

                for col_i, col in enumerate(tableau):
                    for row_i, card in enumerate(col):
                        x = start_x + col_i * spacing_x
                        y = start_y + row_i * spacing_y

                        rect = pygame.Rect(x, y, CARD_W, CARD_H)

                        if rect.collidepoint(mx, my) and card.face_up:
                            selected = card if selected is None else None

        # DRAW BOARD
        draw_tableau(tableau)

        # SHOW SELECTION STATUS
        if selected:
            text = FONT.render(f"Selected: {selected}", True, WHITE)
            screen.blit(text, (50, 20))

        pygame.display.flip()

    pygame.quit()
loop()