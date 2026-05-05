#PS 1st CP2 Final - Pyramid Soliaire source code

#import shuffle function
from solitaire import shuffle_deck
#import csv management functions
import json
import pygame

#setup function
def setup():
    with open("files/cards.json","r") as cards:
        deck = json.load(cards)
    ordered_deck = list(deck.keys())
    #call shuffle function to return a randomized list
    shuffled_deck = shuffle_deck(ordered_deck)
    #create 7 lists for each row of the pyramid and put those inside another creating a matrix
    tableu = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
        ]
    #count each iteration of the loop to determine number of cards in each row
    count = 0
    #Loop for every row (7 times)
    for x in range(7):
        count+=1
        #put one card in row one and then 2 cards and row to and so on
        tableu[x].append(shuffled_deck[0])
        shuffled_deck.pop(0)
        for y in range(x):
            tableu[x].append(shuffled_deck[0])
            shuffled_deck.pop(0)

    #put the rest of the cards in the draw pile list

    #DISPLAY TABLEU - have each row slightly offsetted
    #output tableu, discard pile (empty), draw pile, shown draw pile
    
    discard_pile = []
    shown_draw = []
    for x in tableu:
        print(x)
    return tableu, discard_pile ,shuffled_deck, shown_draw

#Accessible cards function (tableu list)
def Accessible(tab):
    #for each row
    blocked = {}
    for x in tab:
        #check if there is a row above it
        above = tab.index(x)-1
        #if there is
        if above >= 0:
            #for each card in current row,
            for y in x:
                #save each of the indexes in a dict that is formatted like this: dictname:{top_row_allowable:{card1:[0,1]},second:{card2:[0,1],card3:[1,2]} etc. etc. (see activity diagram for what indexes mean)
                index_y = x.index(y)
                below_row = [index_y,index_y+1]
                card_allowable = {y:below_row}
                blocked[x] = card_allowable
                #!!!!!!!!!FINISH LOGIC!!!!!!!!!!!
                
    
    #output the dictionary
    return blocked

#valid Combo Function (card1_id,card2_id,list_of_cards)
def val_combo(ID_1,ID_2,tableu,draw_pile):
    #get both of the dictionaries for the cards in the JSON
    with open("files/cards.json","r") as cards:
        deck = json.load(cards)
    
    card1_info = deck[ID_1]
    card2_info = deck[ID_2]

    #if card1[value] + card2[value] == 13:
    if card1_info["Value"] + card2_info["Value"] == 13:
        #pop those ids out of the tableu add them to the discard pile
        for z in range(2):
            for x in tableu:
                for y in x:
                    if y == ID_1 or y == ID_2:
                        x.pop(y)

        for i in draw_pile:
            if i == ID_1 or i == ID_2:
                draw_pile.pop(i)
        
    #else:
    else:
        #display invalid value error
        print("NOT A VALID MATCH")

#Options funcs

#draw card function (draw pile, shown draw pile)
def draw(draw_pile,shown_pile):
    #check if draw pile has cards in it
    # if yes
    if draw_pile:
        #remove card from draw pile and add it shown draw pile and display that card face up
        shown_pile.insert(0,draw_pile[0])
        draw_pile.pop(0)
    #if no
    else:
        #make draw pile equal to shown and then clear shown
        draw_pile = shown_pile
        shown_pile.clear()
        
        #reverse order of draw pile to represent flipping of pile over
        draw_pile.reverse()

        #remove card from draw pile and add it shown draw pile and display that card face up
        shown_pile.insert(0,draw_pile[0])
        draw_pile.pop(0)

#Discard King function (tableu, discard pile, shown draw pile)
    #call accessibility function for accessible cards
    #allow user to select a card that is accessible
    
    #check if the card is a king
    
    #if yes
        # if card is in tableu
            #remove from tableu
        #else
            #remove from draw
        #add to discard pile
    #if no
        #display error message stating that the card selected was not a king


#matching check (card1, card2)
    #use JSON reading to get values of card1 and card2
    #if card1[value] + card2[value] is = 13
        #output True
    #else
        #output false

#Matching inside tableu (tableu, discard pile, shown draw pile)
    #call acessiblility function
    # allow user to select any valid card from tableu
    # allow user to select another card
    # call matching check (card1, card2)
    #if matching check is True
        #remove cards from tableu
        #add cards to discard pile
    #else
        #display invalid match (values)

#matching from draw pile and tableu (tableu, discard pile, shown draw pile)
    #call accessibility function
    # allow user to select a card from tableu   
    # use card from the top of shown draw pile
    # call matching check (tableu card, draw pile card)
    #if matching cards check is True
        #Remove card from tableu
        #remove card from draw pile
        #add both to discard pile
    #else 
        #display invalid match (values)


#Gameloop (setup variables)
    #call setup and save returned values
    #call accessibility function and save the dict
    
    #actual gameloop

        #allow user to click button to choose type of move to do
        #onclick of draw card button
            #call draw cards function
        #onclick of discard king button
            #call draw cards function
        #onclick of matching inside tableu button
            #call corresponding function
        #onclick of matching from draw and tableu
            #call corresponding function
        
        #update display

        #check if tableu is gone
        #if yes
            #leave gameloop
            #save game number and win
        #else
            #continue

        #If user clicks the quit button
            #leave gameloop
            #save game number and lose
        