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
import json
import csv
from LD_psuedocode import *
path = "files/solitaire.csv"

# MENU - Screen set up
# Create window
# Add button "Play Solitaire"
#      when clicked, start solitaire game
# Add button "Instructions"
#      show how to play
# Add button "Exit"
#      close program
# Display window
pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solitaire")

clock = pygame.time.Clock()
FONT= pygame.font.SysFont(None,24)

GREEN = (0, 120, 0)
WHITE = (255, 255, 255)
GRAY = (80, 80, 80)
BLACK = (0, 0, 0)

CARD_W, CARD_H = 70,100

# CREATE DECK -  call the JSON with the cards
# Make empty list called deck
# For each suit (hearts, diamonds, clubs, spades):
#     For each value (A, 2–10, J, Q, K):
#         Add card to deck
# Return deck
# Talves en vez de clases immporto el json y de repente funciona
class Card:
    def __init__(self, card_id, suit, value, color):
        self.id = card_id
        self.suit = suit
        self.value = value
        self.color = color
        self.face_up = False

    def __repr__(self):
        return f"{self.value}{self.suit[0]}"

def get_card_value(value):

    face_cardss = {
        "ace": 1,
        "jack": 11,
        "queen": 12,
        "king": 13,
        "a": 1,
        "j": 11,
        "q": 12,
        "k": 13
    }

    if isinstance(value, int):
        return value

    value = str(value).lower()

    if value.isdigit():
        return int(value)

    return face_cardss[value]

def create_deck(json_path):

    deck = []

    with open(json_path, "r") as f:
        data = json.load(f)

    for key in data:

        card_data = data[key]

        card = Card(
            card_id=key,
            suit=card_data["Suit"].lower(),
            value=card_data["Value"],
            color=card_data["Color"].lower() # Doesnt really work
        )

        deck.append(card)

    return deck

# SHUFFLE DECK
#def shuffle_deck(deck):
    # Create an empty list to store shuffled cards
    # While there are still cards left in the original deck
    # Generate a random index between 0 and the last position in the deck       
        # Remove the card at that random index from the original deck
        # Add that card to the shuffled deck
    # Once all cards have been moved, return the shuffled deck

# Aun no hace nada para mi codigo simplemente imprime lo mismo cada vez y esto no me ayuda

def shuffle_deck(json_path):

    deck = create_deck(json_path)

    random.shuffle(deck)

    return deck



def draw_from_stock(stock, waste):

    if len(stock) > 0:

        card = stock.pop()
        card.face_up = True
        waste.append(card)

    else:
        # Reset stock from waste
        while len(waste) > 0:

            card = waste.pop()
            card.face_up = False
            stock.append(card)  # Doesnt really work


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
                card.face_up = True # Tengo que averiguar qur esta pasando aqui
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
        text_color = (200, 0, 0) if card.color == "red" else BLACK
        text = FONT.render(str(card), True, text_color)
    else:
        pygame.draw.rect(screen, GRAY, (x, y, CARD_W, CARD_H))
        text = FONT.render("X", True, BLACK)
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


# VALID MOVE CHECK -Lizzie
# If moving card:
#     Check colors are opposite (red vs black)
#     Check value is one less than destination card
# If both true:
#     Move is valid
# Else:
#     Move is invalid
def solitaire_valid_move(selected_card, target_card):

    # Opposite colors
    if selected_card.color == target_card.color:
        return False

    selected_value = get_card_value(selected_card.value)
    target_value = get_card_value(target_card.value)

    # Descending order
    if selected_value + 1 == target_value:
        return True

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

# Esto es de Lizzie pero tengo que importarlo mas no copiar y pegar y tnewgo que agregarlo a main


# FOUNDATION RULES
# Cards must be same suit
# Must go in order: A to  K
# Only Ace can start foundation
def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, GRAY, (x, y, w, h))
    label = FONT.render(text, True, WHITE)
    screen.blit(label, (x + 10, y + 10))
    return pygame.Rect(x, y, w, h)
def draw_stock_waste(stock, waste):

    # STOCK
    if len(stock) > 0:
        pygame.draw.rect(screen, GRAY, (50, 20, CARD_W, CARD_H))
    else:
        pygame.draw.rect(screen, WHITE, (50, 20, CARD_W, CARD_H), 2)

    # WASTE
    if len(waste) > 0:
        draw_card(150, 20, waste[-1])

# WIN CONDITION
# Check all 4 foundation piles
# If each pile has 13 cards in correct order:
#     Player wins
def move_card(tableau, selected_card, target_card):

    source_col = None
    target_col = None

    for col in tableau:

        if selected_card in col:
            source_col = col

        if target_card in col:
            target_col = col

    if source_col and target_col:

        source_col.remove(selected_card)
        target_col.append(selected_card)    # Aqui pato algo que no se

        # Flip top card in old column
        if len(source_col) > 0:
            source_col[-1].face_up = True

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

# tengo que agregar el tableau en alguna parte del loop
deck = shuffle_deck("files/cards.json")
tableau, stock,waste,foundations = setup_board(deck) 

def solitaire():
    global state

    next_button = pygame.Rect(0, 0, 0, 0)

    running = True
    while running:
        screen.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                if state == "menu":
                    play_btn = draw_button("Play Solitaire", 350, 200, 300, 60)
                    inst_btn = draw_button("Instructions", 350, 300, 300, 60)
                    exit_btn = draw_button("Exit", 350, 400, 300, 60)

                    if play_btn.collidepoint(mx, my):
                        state = "game"

                    if inst_btn.collidepoint(mx, my):
                        state = "instructions"

                    if exit_btn.collidepoint(mx, my):
                        running = False

                elif state == "instructions":
                    if next_button.collidepoint(mx, my):
                        state = "game"

        # DRAW MENU
        if state == "menu":
            draw_button("Play Solitaire", 350, 200, 300, 60)
            draw_button("Instructions", 350, 300, 300, 60)
            draw_button("Exit", 350, 400, 300, 60)

        # DRAW INSTRUCTIONS SCREEN
        elif state == "instructions":
            screen.fill(GREEN)

            instructions = [
                "HOW TO PLAY SOLITAIRE",
                "",
                "Goal: Move all cards to foundations (Ace → King).",
                "",
                "Rules:",
                "- Build tableau in alternating colors",
                "- Build foundation by same suit",
                "- Only Kings can go into empty columns",
                "",
                "Controls:",
                "- Click card to select",
                "- Click destination to move",
                "- Click stock to draw cards",
                "",
                "Press NEXT to start game"
            ]

            y = 60
            for line in instructions:
                text = FONT.render(line, True, WHITE)
                screen.blit(text, (50, y))
                y += 28

            next_button = draw_button("NEXT", 400, 600, 200, 50)

        # START GAME
        elif state == "game":
            game_loop()

        pygame.display.flip()

    pygame.quit()

def game_loop():
    global state
    running = True
    selected = None

    while running and state == "game":

