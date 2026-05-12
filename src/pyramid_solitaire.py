#PS 1st CP2 Final - Pyramid Soliaire source code


#import csv management functions
import json
import csv
import pygame
import random
from card_styles import *
from button_styles import *

#setup function
def setup():
    with open("files/cards.json","r") as cards:
        deck = json.load(cards)
    ordered_deck = list(deck.keys())
    #call shuffle function to return a randomized list
    random.shuffle(ordered_deck)
    shuffled_deck = ordered_deck
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
    return tableu, discard_pile ,shuffled_deck, shown_draw

#Accessible cards
def accessibility_checks(tableu,card_info):
    
    #reset Acessibility
    for card in card_info:
        card_info[card]["Accessible"] = False
    
    #bottom row acessible
    for card in tableu[-1]:
        if not card == None:
            card_info[card]["Accessible"] = True

    for row in range(len(tableu)-1):
        for column,card in enumerate(tableu[row]):

            if card is None or card not in card_info:
                continue

            try:
                blocked_left = tableu[row+1][column]
                blocked_right = tableu[row+1][column+1]

                if blocked_left is None and blocked_right is None:
                    card_info[card]["Accessible"] = True
            
            except IndexError:
                pass
    
    return card_info

#valid Combo Function (card1_id,card2_id,list_of_cards)
def val_combo(ID_1,ID_2,tableu,draw_pile,discard_pile,warning_text):
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
                        tableu[tableu.index(x)][x.index(y)] = None
                        discard_pile.append(y)
        if draw_pile:
            if ID_1 == draw_pile[0] or ID_2 == draw_pile[0]:
                draw_pile.pop(0)
                discard_pile.append(y)
        
    #else:
    else:
        #display invalid value error
        warning_text = "Match Values don't add to 13"

    return tableu, draw_pile, discard_pile, warning_text


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
        draw_pile = shown_pile.copy()
        shown_pile.clear()
        
        #reverse order of draw pile to represent flipping of pile over
        draw_pile.reverse()

    return draw_pile, shown_pile
    


#Discard King function (tableu, discard pile, shown draw pile)
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

def suit_match(suit):
    match suit:
        case "Clubs":
            symbol = "♣"
        case "Spades":
            symbol = "♠"
        case "Diamonds":
            symbol = "♦"
        case "Hearts":
            symbol = "♥"
    return symbol

#def select_cards()


#Gameloop (setup variables)
def game():
    #call setup and save returned values
    tableu,discard_pile,shuffled_deck,shown_draw_pile = setup()
    #call accessibility function and save the dict
    card_hit_boxes = {}
    hit_box_cards = []
    selected = 0
    warning_text = ""
    #top card coords
    top = (700,100)

    #card info
    with open("files/cards.json","r") as deck:
        deck_info = json.load(deck)


    #pygame setup
    pygame.init()
    screen = pygame.display.set_mode((2000,1100))
    clock = pygame.time.Clock()
    running = True
    description = f"Rules for pyramid Solitaire:\nGoal: Remove all cards from the pyramid\nMethods:\n\nDiscard a king\n - select a king a click 'Discard king'\n\nMatch Cards:\n Select two cards which aren't covered and click 'Match'\n\n\nIf you lose, just exit the window and try again!\nWhen all cards are gone from the pyramid, the game ends itself.\nFinally the draw button will flip a card over in the draw pile\n so it can be used. "
    lines = description.split("\n")

    #Button functionality
    show_card = Button("Draw","white","grey",position=(450,900))
    king_discard = Button("Discard King","white","grey",position=(650,900))
    remove = Button("Match","white","grey",position=(850,900))
    

    #actual gameloop
    while running:
        
        screen.fill("darkgreen")
        #text
        font = pygame.font.SysFont(None, 48)
        font_2 = pygame.font.SysFont(None, 24)
        title_surface = font.render("Pyramid Solitaire",True,"White")
        label_surface = font.render("Discard",True,"white")
        label2_surface = font.render("Draw Pile",True,"white")

        screen.blit(title_surface, (625,20))
        screen.blit(label_surface,(150,300))
        screen.blit(label2_surface,(1300,150))

        #surface for text to sit on
        pygame.draw.rect(screen,"white",(1500,80,495,475),border_radius=8)

        for i, line in enumerate(lines):
            rules_surface = font_2.render(line,True,"black")
            screen.blit(rules_surface,(1500,100 + i * 30))

        #Warning Message screen
        pygame.draw.rect(screen,"black",(1500,700,300,150),border_radius=8)
        
        warning_surface_title = font_2.render("Warning Center: ",True,"Green")
        screen.blit(warning_surface_title,(1550,725))
        
        warning_surface = font_2.render(warning_text,True,"red")
        screen.blit(warning_surface,(1550,750))
        
        #stop the program if the user exits the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #check if cards or buttons are clicked
            if show_card.click_check(event):
                try:
                    current_card = shown_draw_pile[0]
                    if current_card in card_hit_boxes:
                        if card_hit_boxes[current_card]["Selected"] == True:
                            selected -=1

                    
                        card_hit_boxes.pop(current_card)
                        hit_box_cards.remove(current_card)
                    

                except IndexError:
                    pass

                shuffled_deck,shown_draw_pile = draw(shuffled_deck,shown_draw_pile)
                try:
                    card_hit_boxes[shown_draw_pile[0]] = {
                        "HitBox":[1300,350,100,140],
                        "Selected":False,
                        "Accessible":True
                    }
                    hit_box_cards.append(shown_draw_pile[0])
                except IndexError:
                    pass
            
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
            
            if remove.click_check(event):
                if selected < 2:
                    warning_text = "Select two cards"
                else:
                    scanned = 0
                    selected_1 = None
                    selected_2 = None
                    for key, data in card_hit_boxes.items():
                        if data["Selected"] and scanned == 0:
                            selected_1 = key
                            scanned+=1
                        elif data["Selected"] and scanned == 1:
                            selected_2 = key
                            scanned+=1

                    tableu, shown_draw_pile, discard_pile, warning_text = val_combo(selected_1,selected_2,tableu,shown_draw_pile,discard_pile,warning_text)
                    card_hit_boxes[selected_1]["Accessible"] = False
                    card_hit_boxes[selected_1]["Selected"] = False
                    card_hit_boxes[selected_2]["Accessible"] = False
                    card_hit_boxes[selected_2]["Selected"] = False
                    selected -= 2

            #if left click happened
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for card in hit_box_cards:
                    #find where a card can be clicked
                    w,x,y,z = card_hit_boxes[card]["HitBox"]
                    rect = pygame.Rect(w,x,y,z)
                    #check to see if any of the cards got clicked
                    if rect.collidepoint(event.pos):
                        #if it is accessible
                        if card_hit_boxes[card]["Accessible"]:
                            #deselect
                            if card_hit_boxes[card]["Selected"]:
                                card_hit_boxes[card]["Selected"] = False
                                selected -= 1 
                            #checks to see if there is more than two cards selected
                            elif selected >= 2:
                                warning_text = "To many cards selected"
                            else:
                                #select it
                                if not card_hit_boxes[card]["Selected"]:
                                    card_hit_boxes[card]["Selected"] = True
                                    selected += 1
        
        

        pygame.draw.rect(screen,"black",(100,50,1400,800),width=1,border_radius=5)
        


        #display tableu
        for row_index, row in enumerate(tableu):
            
            for column_index, num in enumerate(row):
                if num != None:
                    card_info = deck_info[num]
                    
                    symbol = suit_match(card_info["Suit"])
                    
                    #finding position to put cards
                    coord_x,coord_y = top
                    new_x = coord_x + (column_index - row_index / 2) * 110
                    new_y = coord_y + row_index * 75
                    new_coords = (new_x,new_y)

                    hit_box = [new_x,new_y,100,140]
                    #check if already there
                    if num not in card_hit_boxes:
                        #save hitbox
                        card_hit_boxes[num] = {
                            "HitBox":hit_box,
                            "Selected":False,
                            "Accessible":False
                        }
                        hit_box_cards.append(num)
                    
                    else:
                        card_hit_boxes[num]["HitBox"] = hit_box

                    new_card = Card(card_info["Value"],symbol,card_info["Color"])
                    new_card.show_card(screen,coords=new_coords)
                else:
                    pass

        if shuffled_deck:
            #shadow
            pygame.draw.rect(screen,"black",(1300,200,100+len(shuffled_deck)/2,140+len(shuffled_deck)/2),border_radius=4)
            #create draw pile
            #inside
            pygame.draw.rect(screen,"red",(1300,200,100,140),0,border_radius=4)
            #border
            pygame.draw.rect(screen,"white",(1300,200,100,140),4,border_radius=4)
        else:
            pygame.draw.rect(screen,"darkgrey",(1300,200,100,140),border_radius=4)
        
        #create shown card
        try:
            #shadow
            pygame.draw.rect(screen,"black",(1300,350,100+len(shown_draw_pile)/2,140+len(shown_draw_pile)/2),border_radius=4)
            #card
            top_card = Card(deck_info[shown_draw_pile[0]]["Value"],suit_match(deck_info[shown_draw_pile[0]]["Suit"]),deck_info[shown_draw_pile[0]]["Color"])
            top_card.show_card(screen,coords=(1300,350))

        except IndexError:
            pygame.draw.rect(screen,"darkgrey",(1300,350,100,140),border_radius=4)

        #waste pile
        try:
            pygame.draw.rect(screen,"black",(150,350,100+len(discard_pile)/2,140+len(discard_pile)/2),border_radius=4)
            top_card = Card(deck_info[discard_pile[0]]["Value"],suit_match(deck_info[discard_pile[0]]["Suit"]),deck_info[discard_pile[0]]["Color"])
            top_card.show_card(screen,coords=(150,350))
        except IndexError:
            pygame.draw.rect(screen,"darkgrey",(150,350,100,140),border_radius=4)
        
        #check accessibility of cards
        card_hit_boxes = accessibility_checks(tableu,card_hit_boxes)

        #check accessibility of the draw pile
        try:
            card_hit_boxes[shown_draw_pile[0]]["Accessible"] = True
        except IndexError:
            pass
        except KeyError:
            pass
        
        #showing buttons
        show_card.show(screen)
        king_discard.show(screen)
        remove.show(screen)

        #highlight for selected card
        for card in hit_box_cards:
            if card_hit_boxes[card]["Selected"] == True:
                x,y,width,height = card_hit_boxes[card]["HitBox"]
                pygame.draw.rect(screen,(255, 215, 0),(x,y,width,height),8,border_radius=4)
        
        
        #update display

        #check if tableu is gone
        if not tableu[0][0]:
            #if yes
            #leave gameloop
            running = False
            print("YOU WIN!")
            #save game number and win
            with open("files/pyramid_solitaire.csv","r",newline="",encoding="utf-8") as scores:
                reader = list(csv.reader(scores))
                game_num = int(reader[-1][0]) + 1
                win_num = int(reader[-1][1]) + 1

            with open("files/pyramid_solitaire.csv","a",newline="",encoding="utf-8") as scores:
                writer = csv.writer(scores)
                writer.writerow([game_num,win_num])         

        #framerate variable
        dt = clock.tick(60) / 100
        pygame.display.flip()
game()