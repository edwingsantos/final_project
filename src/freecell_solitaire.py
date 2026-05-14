#PS 1st FreeCell pseudocode

#import necessary libraries
from card_styles import *
from button_styles import *
import json
import pygame
import csv
import random

#Note:all cards are stored by ID NOT value

#shuffle cards func
def shuffle():
    with open("files/cards.json","r") as card_info:
        deck_info = json.load(card_info)
    
    deck = list(deck_info.keys())

    random.shuffle(deck)

    return deck

#setup func
def setup():
    deck = shuffle()
    
    #useful vars
    freecells = [None,None,None,None]
    ace_piles = [
        [],
        [],
        [],
        []
    ]
    
    #tableau contains lists which represent columns
    tableau = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    
    #load tableau
    for i, card in enumerate(deck):
        tableau[i % 8].append(card)
    
    return freecells, ace_piles, tableau

#CHECKS
def moveable_cards(tableau, freecells, ace_piles, card_status):

    moveable = []

    for i,pile in enumerate(tableau):
        if pile:
            top = pile[-1]
            moveable.append(top)
            card_status[top]["Accessible"] = True
    
        else:
            key = f"TableauEmpty{i}"

            if key not in card_status:
                card_status[key] = {
                    "HitBox": (150 + (125 * i), 300, 100, 140),
                    "Selected": False,
                    "Accessible": True,
                    "InAcePile": False,
                    "Immoveable": True
                }

            card_status[key]["HitBox"] = (150 + (125 * i),300,100,140)

            moveable.append(key)

    for i in range(4):

        if freecells[i] is not None:
            card = freecells[i]
            moveable.append(card)
            card_status[card]["Accessible"] = True

        else:
            key = f"FreeCellEmpty{i}"

            if key not in card_status:
                card_status[key] = {
                    "HitBox": (650 + 125*i, 125, 100, 140),
                    "Selected": False,
                    "Accessible": True,
                    "InAcePile": False,
                    "Immoveable": True
                }

            moveable.append(key)

    for i in range(4):

        if ace_piles[i]:
            top = ace_piles[i][-1]
            moveable.append(top)
            card_status[top]["Accessible"] = True

        else:
            key = f"AceEmpty{i}"

            if key not in card_status:
                card_status[key] = {
                    "HitBox": (150 + 125*i, 125, 100, 140),
                    "Selected": False,
                    "Accessible": True,
                    "InAcePile": True,
                    "Immoveable": True
                }
                if i == 0:
                    card_status[key]["Suit"] = "Spades"
                if i == 1:
                    card_status[key]["Suit"] = "Clubs"
                if i == 2:
                    card_status[key]["Suit"] = "Hearts"
                if i == 3:
                    card_status[key]["Suit"] = "Diamonds"

            
            moveable.append(key)

    return moveable, card_status

#validate player decision funcs
def val_choice(card_ID,destination_ID,tableau,freecells,acepiles,card_status,moveable):
    with open("files/cards.json","r") as file:
        deck = json.load(file)
    
    destination_type = ""
    card = deck[card_ID]
    
    if destination_ID[0] == "F":
        destination_type = "Freecell"
    elif destination_ID[0] == "A":
        destination_type = "AcePile"
    elif destination_ID[0] == "T":
        destination_type = "EmptyTableau"
    else:
        destination_type = "AnotherCard"
        destination = deck[destination_ID]
    
    match destination_type:
        case "Freecell":
            freecell_index = int(destination_ID[-1])

            # Check if freecell empty
            if freecells[freecell_index] is None:

                # Remove card from tableau
                for column in tableau:
                    if card_ID in column:
                        column.remove(card_ID)
                        break
                
                # Remove from freecells
                for i in range(4):
                    if freecells[i] == card_ID:
                        freecells[i] = None

                # Remove from ace piles
                for pile in acepiles:
                    if card_ID in pile:
                        pile.remove(card_ID)

                            # Place into freecell
                freecells[freecell_index] = card_ID
            
            else:
                print("Invalid move")
        case "AcePile":
            #get the right ace pile
            pile_suit = card_status[destination_ID]["Suit"]

            suit_map = {
                "Spades":0,
                "Clubs":1,
                "Hearts":2,
                "Diamonds":3
            }
            
            pile_index = suit_map[pile_suit]
            pile = acepiles[pile_index]

            #if there is no cards in the ace pile
            if len(pile) == 0:
                #Check if value is 1, and is the same suit
                if card["Value"] == 1 and card["Suit"] == pile_suit:

                    for col in tableau:
                        if card_ID in col:
                            col.remove(card_ID)
                            break
                
                    pile.append(card_ID)
                    card_status[card_ID]["InAcePile"] = True
            
                #if there is cards in the ace pile
            else:
                if card["Value"] == destination["Value"]+1:
                    print("Value Check Pass")
                    if card["Suit"] == destination["Suit"]:
                        print("Suit Check pass")
                        
                        for col in tableau:
                            if card_ID in col:
                                col.remove(card_ID)
                                break
                        pile.append(card_ID)
                        card_status[card_ID]["InAcePile"] = True

        case "AnotherCard":
            #Check if card outside Tableau
            in_tableau = False
            in_ace = False

            for col in tableau:
                for c in col:
                    if c == destination_ID:
                        in_tableau = True
                        break
            
            source_col = None
            dest_col = None

            for column in tableau:
                if card_ID in column:
                    source_col = column
                if destination_ID in column:
                    dest_col = column
            
            if card_ID in freecells:
                source_col = freecells
                        
            for x,pile in enumerate(acepiles):
                if destination_ID in pile:
                    in_ace = True
                    moveable.remove(destination_ID)
                    break
            
            if in_tableau:
                print("In Tableau detected")
                #Check if color is opposite, Check if number of incoming is +1 of destination
                if card["Color"] != destination["Color"]:
                    print("Color Check Passed")
                    if card["Value"] == (destination["Value"]-1):
                        print("Value Check Passed")

                        #remove initial card and append to new place
                        source_col.remove(card_ID)
                        dest_col.append(card_ID)
                        moveable.remove(destination_ID)
            
            elif in_ace:
                #make sure that suit match
                if card["Suit"] == destination["Suit"]:
                    #make sure that card is +1 of card already there
                    if card["Value"] == (destination["Value"]+1):
                        acepiles[x].append(card_ID)
                        moveable.remove(card_ID)
                        source_col.remove(card_ID)
    
        case "EmptyTableau":

            column_index = int(destination_ID[-1])

            # remove card from tableau
            for col in tableau:
                if card_ID in col:
                    col.remove(card_ID)

            # remove from freecells
            for i in range(4):
                if freecells[i] == card_ID:
                    freecells[i] = None

            # remove from ace piles
            for pile in acepiles:
                if card_ID in pile:
                    pile.remove(card_ID)

            # place card into empty tableau column
            tableau[column_index].append(card_ID)
    
    card_status[destination_ID]["Selected"] = False
    card_status[card_ID]["Selected"] = False
    if len(freecells) != 4:
        freecells.append(None)
    
    return tableau,freecells,acepiles,card_status,moveable


#match suit (for displaying)
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

#game func
def free_cell_game():
    #normal vars
    freecells, ace_piles, tableau = setup()
    moveable = []
    #all moveable cards are stored with selected bool, accessibility bool, rect-object and in_ace_pile bool
    card_status = {}
    selected = 0
    move_select = ""
    place_select = ""
    rules = "Rules For FreeCell:\n\nGoal: Remove all cards from the tableau (big grid with cards)\nAnd put them all in the foundation piles (piles with suit logos)\n\nWays to do this:\n\nMove cards onto other stacks to free up space\nMove cards to freecells (limited one card per spot)\nMove Cards into Suit Piles (cards go from ace-king or 1-13 in value)\n\nCaveat - You can only move one card at a time,\n\n if at any time the puzzle seems impossible to complete,\n\nQuit the game and start over!\n\n Yellow highlight is the card to move,\n red highlight is the place to move it to"
    lines = rules.split("\n")
    warning_message = ""

    with open("files/cards.json", "r") as info:
        deck = json.load(info)
    
    #setup pygame
    pygame.init()
    screen = pygame.display.set_mode((1800,1200))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont(None,48)
    font_2 = pygame.font.SysFont(None,40)
    font_3 = pygame.font.SysFont(None,24)
    st_font = pygame.font.SysFont("segoeuisymbol",48)
    
    #put buttons here
    move_button = Button("Move Selected Card","white","grey",size=(250,100),position=(1200,1000))

    #game loop
    while running:

        #reset accessibility
        for card in card_status:
            card_status[card]["Accessible"] = False
        
        #make empty slots accessible again
        for i in range(4):
            freecell_key = f"FreeCellEmpty{i}"
            ace_key = f"AceEmpty{i}"

            if freecell_key in card_status:
                card_status[f"FreeCellEmpty{i}"]["Accessible"] = True
            
            if ace_key in card_status:
                card_status[f"AceEmpty{i}"]["Accessible"] = True
        
        for i in range(8):
            tab_key = f"TableauEmpty{i}"

            if tab_key in card_status.keys():
                card_status[tab_key]["Accessible"] = True
        
        #visuals
        screen.fill("darkgreen")

        title_surface = font.render("FreeCell",True,"white")
        
        screen.blit(title_surface,(800,50))

        pygame.draw.rect(screen,"black",(100,100,1650,1000),width=1,border_radius=8)

        #display tableau
        for i, x in enumerate(tableau):
            if not x:
                empty_spot = 150 + (125 * i)

                pygame.draw.rect(screen,"darkgrey",(empty_spot, 300, 100, 140),border_radius=4)

                key = f"TableauEmpty{i}"

                if key not in card_status:
                    card_status[key] = {
                        "Selected": False,
                        "Accessible": True,
                        "Immoveable": True
                    }

                card_status[key]["HitBox"] = (empty_spot, 300, 100, 140)

            for a, y in enumerate(x):
                #get info
                card_info = deck[y]
                
                #add to statuses
                new_x = 150+(125*i)
                new_y = 300+(75*a)
                
                if y not in card_status:
                    card_status[y] = {
                        "HitBox": (new_x,new_y,100,140),
                        "Selected":False,
                        "Accessible":False,
                        "InAcePile":False,
                        "Immoveable":False
                    }
                card_status[y]["HitBox"] = (new_x,new_y,100,140)

                #create visual object
                new_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
                

                #display
                new_card.show_card(screen,coords=(new_x,new_y))


        #display ace piles
        for x in range(4):
            newer_x = 150+(125*x)
            try:
                card_info = deck[ace_piles[x][-1]]
                new_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
                new_card.show_card(screen,coords=(newer_x,125))
                card_id = ace_piles[x][-1]
                card_status[card_id]["InAcePile"] = True
                card_status[card_id]["HitBox"] = (newer_x,125,100,140)
            except (IndexError,KeyError):
                pygame.draw.rect(screen,"darkgrey",(newer_x,125,100,140),border_radius=4)
                symbols = ["♠", "♣", "♥", "♦"]
                symbol_surface = st_font.render(symbols[x],True,"darkgreen")
                screen.blit(symbol_surface,(180+(125*x),150))
                key = f"AceEmpty{x}"

                if key not in card_status:
                    card_status[key] = {}
                    card_status[key]["Selected"] = False
                    card_status[key]["Accessible"] = True
                    card_status[key]["Immoveable"] = True
                    match x:
                        case 0:
                            card_status[key]["Suit"] = "Spades"
                        case 1:
                            card_status[key]["Suit"] = "Clubs"
                        case 2:
                            card_status[key]["Suit"] = "Hearts"
                        case 3:
                            card_status[key]["Suit"] = "Diamonds"
                card_status[key]["HitBox"] = (newer_x, 125, 100, 140)

        #display free cells
        for x in range(4):
            newer_x = 650+(125*x)
            try:
                card_info = deck[freecells[x]]
                new_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
                new_card.show_card(screen,coords=(newer_x,125))
                card_id = freecells[x]
                card_status[card_id]["HitBox"] = (newer_x,125,100,140)
            except (IndexError,KeyError):
                pygame.draw.rect(screen,"darkgrey",(newer_x,125,100,140),border_radius=4)
                key = f"FreeCellEmpty{x}"

                if key not in card_status:
                    card_status[key] = {}
                    card_status[key]["Selected"] = False
                    card_status[key]["Accessible"] = True
                    card_status[key]["Immoveable"] = True

                card_status[key]["HitBox"] = (newer_x, 125, 100, 140)
        
        #Display Instructions and Control Center
        pygame.draw.rect(screen,"white",(1200,125,535,600),border_radius=8)
        pygame.draw.rect(screen,"black",(1200,730,450,250),border_radius=8)


        for i, line in enumerate(lines):
            rules_surface = font_3.render(line,True,"black")
            screen.blit(rules_surface,(1210,140 + i * 30))

        warning_title = font_2.render("Warning Center:",True,"red")
        screen.blit(warning_title,(1225,825))
        warning = font_2.render(warning_message,True,"green")
        screen.blit(warning,(1225,900))
        
        #button
        move_button.show(screen)

        #find movable cards
        moveable,card_status = moveable_cards(tableau,freecells,ace_piles,card_status)

        #check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if move_button.click_check(event):
                if selected != 2:
                    warning_message = "Must select start+end points"
                else:
                    tableau, freecells, ace_piles, card_status, moveable = val_choice(move_select,place_select,tableau,freecells,ace_piles,card_status,moveable)
                    selected = 0
                    move_select = ""
                    place_select = ""

            #mouse button clicked and it is the left button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #scan to see if card clicked
                for card in moveable:
                    #checks if unavailable
                    if "HitBox" not in card_status[card]:
                        continue
                    w,x,y,z = card_status[card]["HitBox"]
                    rect = pygame.Rect(w,x,y,z)

                    if rect.collidepoint(event.pos):
                        #deselecting
                        if card_status[card]["Selected"]:
                            
                            if card == move_select:
                                move_select = ""
                                card_status[card]["Selected"] = False
                                selected = 0
                                if place_select:
                                    card_status[place_select]["Selected"] = False
                                    place_select = ""
                            elif card == place_select:
                                card_status[place_select]["Selected"] = False
                                if move_select:
                                    card_status[move_select]["Selected"] = False
                                place_select = ""
                                move_select = ""
                                selected = 0
                            else:
                                print("NOTHING TO DESELECT")
                        #selecting
                        else:
                            if card_status[card]["Accessible"]:

                                if selected >= 2:
                                    warning_message = "Too many cards selected"
                                
                                elif selected == 0:
                                    
                                    if not card_status[card]["Immoveable"]:
                                        card_status[card]["Selected"] = True
                                        move_select = card
                                        selected += 1
                                
                                elif selected == 1:
                                    card_status[card]["Selected"] = True
                                    place_select = card
                                    selected += 1
                                
                                else:
                                    print("Selection error occurred")
        
        #highlight system
        for i in moveable:
            if card_status[i]["Selected"] == True:
                x,y,width,height = card_status[i]["HitBox"]
                if i == move_select:
                    pygame.draw.rect(screen,(255, 215, 0),(x,y,width,height),width=8,border_radius=4)
                elif i == place_select:
                    pygame.draw.rect(screen,(255, 0, 0),(x,y,width,height),width=8,border_radius=4)
                else:
                    print("An error occured in highlight system")
    
        #find places for cards to be moved - Ace piles, other parts of tableau, free cells

        #check if game is over
            #if yes, end game loop and save to csv
        
        counter = 0
        for x in tableau:
            if len(x) == 0:
                counter+=1
        
        if counter == 8 and freecells == [None,None,None,None]:
            print("YOU WIN!")
            running = False
            with open("files/freecell.csv","r",newline="",encoding="utf-8") as scores:
                reader = list(csv.reader(scores))
                game_num = int(reader[-1][0]) + 1
                win_num = int(reader[-1][1]) + 1

            with open("files/freecell.csv","a",newline="",encoding="utf-8") as scores:
                writer = csv.writer(scores)
                writer.writerow([game_num,win_num])
    
        pygame.display.flip()

        dt = clock.tick(60) / 100
    
    pygame.quit()
