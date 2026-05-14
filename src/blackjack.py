#ES starting spedocode

# import pygame, json, sys 
import pygame
import json
import sys
import csv 
import random 
#from solitaire import *
from betting_func import *
from card_styles import *
#from LD_psuedocode import *
path = "files/blackjack.csv"


#use dictionary called point to safe the cards choosen 
#make a dictionary for the dealers hand 
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

        match card.suit:
            case "clubs":
                card.symbol = "♣"
            case "spades":
                card.symbol = "♠"
            case "diamonds":
                card.symbol = "♦"
            case "hearts":
                card.symbol = "♥"

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






def blackjack():
    pygame.init()

    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("blackjack")

    clock = pygame.time.Clock()
    FONT= pygame.font.SysFont(None,24)

    CARD_W, CARD_H = 70,100

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

    running = True
    state =  "typing"
    typed_text = ""

    #betting
    betting_money = starting_bet()

    #shoufle deck
    deck = shuffle_deck("files/cards.json")

    #hands
    player_hand = []
    dealer_hand = []

    #dealing cards
    # DEAL CARDS
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())

    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    #variables for games
    player_turn = True
    result = ""

    # check for instant win
    if hand_value(player_hand) == 21:
        result = "You win! you got 21"
        winning(user_data, betting_money)
        player_turn = False
    pygame.init()
    WIDTH, HEIGHT = 1000, 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)
    #backround
    screen.fill("darkgreen")
    while running:
        #events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            #quit thing
                if event.key == pygame.K_q:
                    sys.exit() 
                    return
                    
                if event.key == pygame.K_r:
                    return blackjack()

                #hit (get more cards)
                if event.key == pygame.K_h and player_turn:
                    player_hand.append(deck.pop())
                    player_total = hand_value(player_hand)
                    #if player has 21
                    if player_total == 21:
                        result = "You win! you got 21"
                        winning(user_data, betting_money)
                        player_turn = False
                    #if player busts
                    elif player_total > 21:
                        result = "You loose, you busted "
                        losing(user_data, betting_money)
                        player_turn = False


                #stand (like not to get cards)
                if event.key == pygame.K_s and player_turn:
                    player_turn = False
                    #dealer draws card
                    while hand_value(dealer_hand) < 17:
                        dealer_hand.append(deck.pop())
                    #total hand values
                    player_total = hand_value(player_hand)
                    dealer_total = hand_value(dealer_hand)
                    #results
                    if dealer_total > 21:
                        result = "dealer busts, you win "
                        winning(user_data, betting_money)
                    elif dealer_total > player_total:
                        result = "dealer wins, you loose"
                        losing(user_data, betting_money)
                    elif dealer_total < player_total:
                        result = "You win, got bigger value than dealer"
                        winning(user_data, betting_money)
                    else:
                        result = "tie"
                        tie(user_data)

        player_title = font.render("PLAYER",True,(255, 255, 255))
        screen.blit(player_title, (450, 450))


        x = 375

        for card in dealer_hand:

            draw_card = Card_styles(
            card.value,
            card.symbol,
            card.color()
        )
            draw_card.show_card(
            screen,
            size=(100,140),
            coords=(x,200)
        )
            x += 125


        x = 375

        for card in player_hand:

            draw_card = Card_styles(card.value,card.symbol,card.color())

            draw_card.show_card(
            screen,size=(100,140),coords=(x,600))

            x += 125





        if player_turn and state == "typing":
            text1 = font.render("press H to hit | press S to stand",True,(250, 250, 250))
            text3 = font.render("DEALER",True,(250, 250, 250))
            #cursor effect
            display_text = typed_text
             #typing font and making sure its tru
            text2 = font.render(display_text, True, (0, 0, 0))
            screen.blit(text1, (400, 400))
            screen.blit(text2, (100, 300))
            screen.blit(text3, (450, 100))
            
        else:
            text4 = font.render("PRESS q TO EXIT or PRESS r TO REPEAT",True,(255, 255, 255))
            text5 = font.render(f"(total money is: ${user_data['money']})",True,(255, 255, 255))
            screen.blit(text4, (450, 775))
            screen.blit(text5, (450, 800))
            





    #ask parker about this
        pygame.display.update()




def blackjack_instructions():
    running =  True
    pygame.init()
    WIDTH, HEIGHT = 1000, 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)
    screen.fill("darkgreen")

    while running:
        #events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            #quit thing
                if event.key == pygame.K_c:
                    running = False
                    blackjack()

        description = f"Objective: Beat the dealer by having a higher total,\n without exceeding 21.\n\nCard Values: Number cards (2 to 10) are face value. \nJacks, Queens, and Kings are worth 10. \nAces are worth 1 or 11.\n\nThe Setup: Players place bets, and each is dealt two cards face up.\n The dealer receives one card face up and one face down (the hole card\n\nHit: Ask for another card to increase your total.\n You can hit until you stand or exceed 21.\n\nStand: Keep your current total and end your turn.\n\nBust: If your hand total exceeds 21, you immediately lose your wager.\n\nWinning: You win if your total is higher than the dealer's or if the dealer busts.\n\n\nPRESS c TO CONTINUE)."
        lines = description.split("\n")
        for i, line in enumerate(lines):
            rules_surface = font.render(line,True,"black")
            screen.blit(rules_surface,(100,100 + i * 30))
        pygame.display.flip()










#MAKE SO THE DEALER SHOWS ONE SINGULAR CARD,   YOU CAN PLACE A SHAPE OVER IT AND WHEN THE USER STANDS THEN TAKE IT AWAY