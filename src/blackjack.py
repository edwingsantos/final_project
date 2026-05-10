#ES starting spedocode

# import pygame, json, sys 
import pygame
import json
import sys
import csv 
import random 
#from solitaire import *
from betting_func import *
#from LD_psuedocode import *
path = "files/blackjack.csv"



screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

#use dictionary called point to safe the cards choosen 
#make a dictionary for the dealers hand 
shuffled_deck = []
dealer_shuffled_deck = []

#call the shufle funtion from lucci and append it to the points dictionary 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.face_up = False

    def color(self):
        return "red" if self.suit in ["hearts", "diamonds"] else "black"

    def __repr__(self):
        return f"{self.value}{self.suit[0]}"


def card_to_id(card):
    return str(card.value) + "_" + card.suit

def create_deck(json_path):

    deck = []

    with open(json_path, "r") as f:
        data = json.load(f)

    for key in data:
        card_data = data[key]

        card = Card(
            suit=card_data["Suit"].lower(),
            value=card_data["Value"]
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



def hand_value(hand):

    total = 0
    aces = 0

    for card in hand:

        if card.value in ["J", "Q", "K"]:
            total += 10

        elif card.value == "A":
            total += 11
            aces += 1

        else:
            total += int(card.value)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


#use an other dictionary for the amount of games played 

#use another dictianry for win games
games_win = []
#user another library for money 
try:
    games_num = get_game_num(path)
except:
    games_num = 1

try:
    money = get_money(path)
except:
    money = 100

#ASK LIZZIE FOR HELP IN THIS


#check if the 3rd line of the csv is 0
# if the 3rd line is empty give the user 100$ and append it to the money dictionary 




#SET up screen 
#set up the board with two cards you can see, these cards have to match with the ones in the points dicitonary 
#Have two card for the dealer and make one card show, remember one of those have to match in the dictionary

#make a funtion for blackjack 

    #call the beggingin of the betting funtion 
    
    #safe those amounts into the ductionaries 

    #show users their cards and let them see the dealers cards
    #if the user has an instant 21 call the winning funtion from betting funtion 


    #make a funtion for DRAW cards
    #ask user if they want to draw a card
    #if they do call the funtion again and add the points to the libraries
    #if not then continue with the code

    #make a funtion for reveal cards
    #if the dealer have cards values less than 16 call the draw funtion but add it to the dealer dictionary
    #if the dealer has a 21 then the dealer wins, call the loosing funtion
    #if the dealer has more than 16 then compare the two values of the dictionaries
        #if the dealer has a grater amount of points, call the loosing funtion
        #if the dealer has a less amount of points, call the winning funtion
    #if the users have the same amount of points call the tie funtion from the betting funtion 


#ask the user if they want to play blackjack again
    #if choice is yes then call the blackjack funtion
    #if choice is no the go to the main menu
def get_game_num(path):

    try:
        with open(path, "r") as file:

            reader = csv.reader(file)
            rows = list(reader)

            # remove header row
            data_rows = rows[1:]

            # if no data yet
            if len(data_rows) == 0:
                return 1

            last_line = data_rows[-1]

            # try to read first column as number
            try:
                game_num = int(last_line[0])
            except:
                game_num = 0

            return game_num + 1

    except Exception as e:
        print(f"CSV error: {e}")
        return 1
# Blackjack UI Rewrite

# Blackjack UI Rewrite


def blackjack():

    running = True

    # BETTING
    betting_money = starting_bet()

    # SHUFFLE DECK
    deck = shuffle_deck("files/cards.json")

    # HANDS
    player_hand = []
    dealer_hand = []

    # DEAL CARDS
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())

    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    # GAME VARIABLES
    player_turn = True
    result = ""

    # BLACKJACK CHECK
    if hand_value(player_hand) == 21:

        result = "BLACKJACK! YOU WIN"

        winning(user_data, betting_money)

        player_turn = False

    while running:

        clock.tick(60)

        # GREEN BACKGROUND
        screen.fill((20, 120, 20))

        # EVENTS
        for event in pygame.event.get():

            # QUIT
            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            # KEYBOARD
            if event.type == pygame.KEYDOWN:

                # EXIT GAME
                if event.key == pygame.K_ESCAPE and not player_turn:

                    running = False

                # HIT
                if event.key == pygame.K_h and player_turn:

                    player_hand.append(deck.pop())

                    player_total = hand_value(player_hand)

                    # PLAYER GETS 21
                    if player_total == 21:

                        result = "21! YOU WIN"

                        winning(user_data, betting_money)

                        player_turn = False

                    # PLAYER BUSTS
                    elif player_total > 21:

                        result = "BUST! DEALER WINS"

                        losing(user_data, betting_money)

                        player_turn = False

                # STAND
                if event.key == pygame.K_s and player_turn:

                    player_turn = False

                    # DEALER DRAWS
                    while hand_value(dealer_hand) < 17:

                        dealer_hand.append(deck.pop())

                    # TOTALS
                    player_total = hand_value(player_hand)

                    dealer_total = hand_value(dealer_hand)

                    # RESULTS
                    if dealer_total > 21:

                        result = "DEALER BUSTS! YOU WIN"

                        winning(user_data, betting_money)

                    elif dealer_total > player_total:

                        result = "DEALER WINS"

                        losing(user_data, betting_money)

                    elif dealer_total < player_total:

                        result = "YOU WIN"

                        winning(user_data, betting_money)

                    else:

                        result = "TIE"

                        tie(user_data)

        # ---------------- PLAYER HAND ----------------

        player_title = font.render(
            "PLAYER",
            True,
            (255, 255, 255)
        )

        screen.blit(player_title, (650, 450))

        # DRAW PLAYER CARDS
        player_x = 500

        for card in player_hand:

            # CARD RECTANGLE
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (player_x, 500, 100, 140)
            )

            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (player_x, 500, 100, 140),
                3
            )

            # CARD VALUE
            card_text = font.render(
                str(card.value),
                True,
                (0, 0, 0)
            )

            screen.blit(card_text, (player_x + 35, 550))

            player_x += 120

        # PLAYER TOTAL
        total_text = font.render(
            f"TOTAL: {hand_value(player_hand)}",
            True,
            (255, 255, 255)
        )

        screen.blit(total_text, (620, 670))

        # ---------------- DEALER HAND ----------------

        dealer_title = font.render(
            "DEALER",
            True,
            (255, 255, 255)
        )

        screen.blit(dealer_title, (650, 50))

        # DRAW DEALER CARDS
        dealer_x = 500

        for i, card in enumerate(dealer_hand):

            # CARD RECTANGLE
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (dealer_x, 100, 100, 140)
            )

            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (dealer_x, 100, 100, 140),
                3
            )

            # HIDDEN CARD
            if i == 0 and player_turn:

                hidden_text = font.render(
                    "?",
                    True,
                    (0, 0, 0)
                )

                screen.blit(hidden_text, (dealer_x + 40, 150))

            else:

                dealer_text = font.render(
                    str(card.value),
                    True,
                    (0, 0, 0)
                )

                screen.blit(dealer_text, (dealer_x + 35, 150))

            dealer_x += 120

        # ---------------- CONTROLS ----------------

        if player_turn:

            controls = font.render(
                "PRESS H TO HIT | PRESS S TO STAND",
                True,
                (255, 255, 255)
            )

        else:

            controls = font.render(
                "PRESS ESC TO EXIT",
                True,
                (255, 255, 255)
            )

        screen.blit(controls, (450, 750))

        # ---------------- RESULT ----------------

        result_text = font.render(
            result,
            True,
            (255, 255, 0)
        )

        screen.blit(result_text, (550, 350))

        pygame.display.update()


blackjack()