#ES starting spedocode

# import pygame, json, sys 
import pygame
import json
import sys
from betting_func import betting_money

#call the shufle funtion from lucci and append it to the points dictionary 
# do the same thing but just append it to the dealers hand 


#use dictionary called point to safe the cards choosen 
#make a dictionary for the dealers hand 
#use an other dictionary for the amount of games played 
#use another dictianry for win games
#user another library for money 
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
import pygame
import json
import random
from betting_func import starting_bet, winning, losing, tie, betting_money

pygame.init()

screen = pygame.display.set_mode((900, 600))
font = pygame.font.SysFont(None, 40)

player = "Player1"
user_data = {"money": 1000, "game_number": 1}


# LOAD DECK FROM JSON
def load_deck():
    with open("files/cards.json", "r") as f:
        data = json.load(f)
    return list(data.values())


# YOUR SHUFFLE FUNCTION
def shuffle_deck(deck):   
    shuffled_deck = []
    while len(deck) > 0:       
        random_index = random.randint(0, len(deck) - 1)
        selected_card = deck.pop(random_index)
        shuffled_deck.append(selected_card)
    return shuffled_deck


# CARD VALUE
def card_value(card):
    value = card["Value"]
    if value > 10:
        return 10
    if value == 1:
        return 11
    return value


# TOTAL HAND VALUE
def hand_total(hand):
    total = sum(card_value(c) for c in hand)
    aces = sum(1 for c in hand if c["Value"] == 1)

    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


# DISPLAY HAND
def hand_names(hand):
    return [card["Name"] for card in hand]


def draw_text(text, x, y):
    img = font.render(text, True, (0,0,0))
    screen.blit(img, (x, y))


# MAIN BLACKJACK FUNCTION
def blackjack_game():

    # call betting
    starting_bet(player)
    bet = betting_money[player]

    # setup deck
    deck = shuffle_deck(load_deck())

    # dictionaries (your pseudocode idea)
    player_hand = []
    dealer_hand = []

    # deal starting cards
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())

    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    state = "player"
    running = True

    # check instant 21
    if hand_total(player_hand) == 21:
        winning(user_data, bet)
        return

    while running:
        screen.fill((255,255,255))

        # show cards
        draw_text(f"Your hand: {hand_names(player_hand)} ({hand_total(player_hand)})", 50, 300)

        if state == "player":
            draw_text(f"Dealer: [{dealer_hand[0]['Name']}, ?]", 50, 100)
        else:
            draw_text(f"Dealer: {hand_names(dealer_hand)} ({hand_total(dealer_hand)})", 50, 100)

        draw_text("H = Draw | S = Stand", 50, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                # DRAW FUNCTION
                if state == "player":
                    if event.key == pygame.K_h:
                        player_hand.append(deck.pop())

                        if hand_total(player_hand) > 21:
                            losing(user_data, bet)
                            state = "end"

                    # STOP DRAWING
                    elif event.key == pygame.K_s:
                        state = "dealer"

                # DEALER LOGIC
                elif state == "dealer":

                    # dealer draws until 16+
                    while hand_total(dealer_hand) < 16:
                        dealer_hand.append(deck.pop())

                    player_total = hand_total(player_hand)
                    dealer_total = hand_total(dealer_hand)

                    if dealer_total > 21:
                        winning(user_data, bet)
                    elif dealer_total > player_total:
                        losing(user_data, bet)
                    elif dealer_total < player_total:
                        winning(user_data, bet)
                    else:
                        tie(user_data, bet)

                    state = "end"

                # PLAY AGAIN
                elif state == "end":
                    if event.key == pygame.K_y:
                        return blackjack_game()
                    elif event.key == pygame.K_n:
                        return

        if state == "end":
            draw_text("Play again? Y / N", 50, 550)

        pygame.display.update()


blackjack_game()