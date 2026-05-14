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
import sys
import csv
from LD_psuedocode import *
path = "files/solitaire.csv"
from card_styles import Card_styles
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
    
def create_deck(json_path,face_cardss,value):

    deck = []

    with open(json_path, "r") as f:
        data = json.load(f)
    for key in data:
        card_data = data[key]
    card = Card(
            suit=card_data["Suit"].lower(),
            value=card_data["Value"]
        )

    match deck.suit:
        case "Clubs":
            symbol = "♣"
        case "Spades":
            symbol = "♠"
        case "Diamonds":
            symbol = "♦"
        case "Hearts":
            symbol = "♥"

    return face_cardss.get(value,0)

def king_removal(tableu,discard,shown_pile,picked_card,warning_text):
    #call accessibility function for accessible cards
    
    
    with open("files/cards.json","r") as card_info:
        deck = json.load(card_info)

    #check if the card is a king
    removed = False
    #if yes
    if deck[picked_card]["Value"] == 13:
        # if card is in tableu
            #remove from tableu
        for x in tableu:
            for y in x:
                if y == picked_card:
                    x.insert(x.index(y),None)
                    x.remove(y)
                    removed = True
                    break
        #else
        if removed == False:
            #remove from draw
            shown_pile.pop(0)
        #add to discard pile
        discard.insert(0,picked_card)
    #if no
    else:
        #display error message stating that the card selected was not a king
        warning_text = "Select only one king"
    return discard, shown_pile, tableu, warning_text

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

        waste.reverse()

        while len(waste) > 0:

            card = waste.pop()

            card.face_up = False

            stock.append(card)

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
def draw_card(x, y, card, selected=False):

    if card.face_up:

        pygame.draw.rect(screen, WHITE, (x, y, CARD_W, CARD_H))

        text_color = (200, 0, 0) if card.color == "red" else BLACK

        text = FONT.render(str(card), True, text_color)

    else:

        pygame.draw.rect(screen, GRAY, (x, y, CARD_W, CARD_H))

        text = FONT.render("X", True, BLACK)

    screen.blit(text, (x + 10, y + 40))

    # DRAW HIGHLIGHT LAST
    if selected:

        pygame.draw.rect(
            screen,
            (255, 215, 0),
            (x, y, CARD_W, CARD_H),
            4
        )

# Esto es para ver las 7 columnas de las cartas
def draw_tableau(tableau, selected_card):
    start_x = 50
    start_y = 120
    spacing_x = 130
    spacing_y = 25

    for col_index, column in enumerate(tableau):
        for row_index, card in enumerate(column):
            x = start_x + col_index * spacing_x
            y = start_y + row_index * spacing_y
            draw_card(
                x,
                y,
                card,
                card == selected_card
            )
def get_clicked_card(tableau, pos):

    start_x = 50
    start_y = 120
    spacing_x = 130
    spacing_y = 25

    for col_index, column in enumerate(tableau):

        for row_index, card in enumerate(column):

            x = start_x + col_index * spacing_x
            y = start_y + row_index * spacing_y

            rect = pygame.Rect(x, y, CARD_W, CARD_H)

            if rect.collidepoint(pos):

                if card.face_up:
                    return card

    return None

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
        pygame.draw.rect(screen, WHITE, (50, 20, CARD_W, CARD_H), 2)
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

class Button:
    def __init__(self, text, x, y, w, h, action):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        label = FONT.render(self.text, True, WHITE)
        label_rect = label.get_rect(center=self.rect.center)
        screen.blit(label, label_rect)
    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

def instruction_screen():

    running = True

    instructions = [
        "SOLITAIRE RULES",
        "",
        "Goal:",
        "Move all cards to the foundation piles.",
        "",
        "Rules:",
        "- Red and black cards alternate",
        "- Cards go in descending order",
        "- Kings start empty columns",
        "- Draw cards from the stock pile",
        "",
        "Click anywhere to go back"
    ]

    while running:

        screen.fill(GREEN)

        title = FONT.render("Instructions", True, WHITE)
        screen.blit(title, (400, 50))

        for i, line in enumerate(instructions):

            text = FONT.render(line, True, WHITE)

            screen.blit(text, (120, 120 + i * 40))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        pygame.display.flip()

def quit_game():
    pygame.quit()
    sys.exit()



def solitaire():

    deck = shuffle_deck("files/cards.json")

    tableau, stock, waste, foundations = setup_board(deck)

    running = True
    selected_card = None

    while running:

        screen.fill(GREEN)

        # TITLE
        title = FONT.render("Solitaire", True, WHITE)
        screen.blit(title, (400, 20))

        # DRAW STOCK + WASTE
        draw_stock_waste(stock, waste)

        # DRAW TABLEAU
        draw_tableau(tableau, selected_card)

        # STOCK HITBOX
        stock_rect = pygame.Rect(50, 20, CARD_W, CARD_H)
        king_discard = Button("Discard King","white","grey",position=(650,900))
        hit_box_cards = []
        card_hit_boxes = {}
        # CREATE BUTTONS HERE
        instruction_button = draw_button(
            "Instructions",
            750,
            20,
            180,
            50
        )

        quit_button = draw_button(
            "Quit",
            750,
            90,
            180,
            50
        )

        # EVENT LOOP
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # STOCK CLICK
                if stock_rect.collidepoint(event.pos):
                    draw_from_stock(stock, waste)

            if king_discard.click_check(event):
                if selected == 1:
                    for card in hit_box_cards:
                        if card_hit_boxes[card]["Selected"] == True:
                            king = card
                    discard_pile, shown_draw_pile, tableu, warning_text = king_removal(tableu,discard_pile,shown_draw_pile,king,warning_text)
                    card_hit_boxes[king]["Selected"] = False
                    card_hit_boxes.pop(king)
                    hit_box_cards.remove(king)
                    
                    selected -= 1
                    
                elif selected == 2:
                    warning_text = "Too many cards selected"
                else:
                    warning_text = "No cards selected"
                # INSTRUCTIONS BUTTON
                if instruction_button.collidepoint(event.pos):
                    instruction_screen()

                # QUIT BUTTON
                if quit_button.collidepoint(event.pos):
                    quit_game()

                # CARD CLICKING
                clicked_card = get_clicked_card(
                    tableau,
                    event.pos
                )

                if clicked_card:

                    if selected_card is None:

                        selected_card = clicked_card

                    else:

                        if solitaire_valid_move(
                            selected_card,
                            clicked_card
                        ):

                            move_card(
                                tableau,
                                selected_card,
                                clicked_card
                            )
                        
                        else:
                            print("Invalid move")

                        selected_card = None

        pygame.display.flip()

        clock.tick(60)
solitaire()