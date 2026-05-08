#ES starting spedocode

# import pygame, json, sys 
import pygame
import json
import sys
import csv 
#from betting_func import *
from solitaire import *
from LD_psuedocode import *
csv_path = "files/blackjack.csv"



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



#shuffle_deck(deck)
print(shuffle_deck)
#use an other dictionary for the amount of games played 
games_num =  get_game_num(csv_path)
#use another dictianry for win games
games_win = []
#user another library for money 
money = get_money(csv_path)


#ASK LIZZIE FOR HELP IN THIS


#check if the 3rd line of the csv is 0
# if the 3rd line is empty give the user 100$ and append it to the money dictionary 




#SET up screen 
#set up the board with two cards you can see, these cards have to match with the ones in the points dicitonary 
#Have two card for the dealer and make one card show, remember one of those have to match in the dictionary

#make a funtion for blackjack 
def blackjakc():
    running = True
    #call the beggingin of the betting funtion 
    while running:
        clock.tick(60)
        screen.fill((255, 255, 255))
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





blackjakc()


