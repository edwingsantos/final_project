# Pseudocode for Poker (LD)
import random
import pygame
import json
import csv
from treys import Evaluator, Card
from LD_psuedocode import stuff_in_CSV, write_2_gambling
from betting_func import starting_bet
from card_styles import *

#csv_path = path to poker csv
csv_path = "files/poker.csv"

# Open the poker csv. Use LD helper function to check if there are any saved games
# if that call = True, 
    # Open csv. read the headers. do: last_line = file.readlines()[-1]. in last_line, user_mon = last_line[2 or "Money"] <- (this depends on whether I do a reader or DictReader)
# else: user_mon = 100

#match suit (for displaying)
def suit_match(suit):
    if suit == "Clubs":
        symbol = "♣"
    elif suit == "Spades":
        symbol = "♠"
    elif suit == "Diamonds":
        symbol = "♦"
    elif suit == "Hearts":
        symbol = "♥"
    else:
        print("Code broke. Line 21, suit_match function")
    #match suit:
        #case "Clubs":
            #symbol = "♣"
        #case "Spades":
            #symbol = "♠"
        #case "Diamonds":
            #symbol = "♦"
        #case "Hearts":
            #symbol = "♥"
    return symbol


# GAMEPLAY ASSISTANT FUNTIONS
    # CHECK HANDS (parameters = card_ID_1, card_ID_2, card_ID_3, card_ID_4, card_ID_5, card_ID_6, card_ID_7)
        # use traderbagel's treys poker hand ranking functions
def check_hands(hand, table):
    def format_cards(id):
        # FORMAT CARDS (turn a card id into a shortened version like As (Ace of spades))
            # Take in ID. Compare to number 1-52 and based on result, give abreviation
        # check the beggining. (A-K)
        id = int(id)
        if id == 1 or id == 14 or id == 27 or id == 40:
            beginning = "A"
        elif id == 2 or id == 15 or id == 28 or id == 41:
            beginning = "2"
        elif id == 3 or id == 16 or id == 29 or id == 42:
            beginning = "3"
        elif id == 4 or id == 17 or id == 30 or id == 43:
            beginning = "4"
        elif id == 5 or id == 18 or id == 31 or id == 44:
            beginning = "5"
        elif id == 6 or id == 19 or id == 32 or id == 45:
            beginning = "6"
        elif id == 7 or id == 20 or id == 33 or id == 46:
            beginning = "7"
        elif id == 8 or id == 21 or id == 34 or id == 47:
            beginning = "8"
        elif id == 9 or id == 22 or id == 35 or id == 48:
            beginning = "9"
        elif id == 10 or id == 23 or id == 36 or id == 49:
            beginning = "T"
        elif id == 11 or id == 24 or id == 37 or id == 50:
            beginning = "J"
        elif id == 12 or id == 25 or id == 38 or id == 51:
            beginning = "Q"
        elif id == 13 or id == 26 or id == 39 or id == 52:
            beginning = "K"
        else:
            print("Somewthing happened in formatting cards function.\nFile: poker_psuedo.py\nLine: 17")
        # Now get the suit
        if id <= 13 and id >= 1:
            suit = "c" # clubs
        elif id <= 26 and id >= 14:
            suit = "s" # spades
        elif id <= 39 and id >= 27:
            suit = "d" # diamonds
        elif id <= 52 and id >= 40:
            suit = "h" # hearts
        else:
            print("Somewthing happened in formatting cards function.\nFile: poker_psuedo.py\nLine: 45")
        
        card_name = beginning+suit
        return card_name
    
    # main code for checking
    abrev_hand = []
    abrev_table = []
    bin_hand = []
    bin_table = []
    evaluator = Evaluator()
    # loop through the passed in table and had lists and get the abreviated card names
    for item in hand:
        abreviated = format_cards(item)
        abrev_hand.append(abreviated)
    for thing in table:
        abrev = format_cards(thing)
        abrev_table.append(abrev)
    # use treys Card.new on each item in the lists with the abreviations. But these into new lists again
    for i in abrev_hand:
        card = Card.new(i)
        bin_hand.append(card)
    for t in abrev_table:
        another_card = Card.new(t)
        bin_table.append(another_card)
    # use treys .evaluate and pass in the lists with the binary card representation created by Card.new
    rank = evaluator.evaluate(bin_table, bin_hand) # 1 is Royal Flush. Lower the number, the better
    score_class = evaluator.get_rank_class(rank)
    hand_rank = evaluator.class_to_string(score_class).format(rank) # Get the actual name of the hand rank
    return rank


def play_poker():
    def make_bet():
        nonlocal bet_amount
        bet = True
        while bet:
            # Make player bet
            initial_bet = starting_bet()
            bet_amount += initial_bet
            bet = False
    
    def determine_win(player, comp):
        nonlocal user_mon
        if player < comp:
            win = 'True'
            user_mon += bet_amount
        elif comp < player:
            win = 'False'
            user_mon -= bet_amount
        elif player == comp:
            win = 'Tie'
            user_mon = user_mon
        else:
            # something went wrong
            print("Something happened when comparing who won in poker.\nFile:poker_psudo.py\nLine: 197")
        return win, user_mon
    
    def draw_table(cards_shown):
        x_possition = 500; y_possition = 400
        count = 0
        for the_card in table:
            if count < cards_shown:
                print("Card drawn")
                card_info = deck[the_card]
                pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
                pretty_card.show_card(screen,coords=(x_possition,y_possition))
                #pygame.draw.rect(screen, WHITE, (x_possition, y_possition, CARD_W, CARD_H))
                #text = FONT.render(str(f'{the_card} (ID)'), True, BLACK)
                #screen.blit(text, (x_possition + 10, y_possition + 40))
                x_possition += 80; y_possition += 0
            else:
                print("Null card drawn")
                pygame.draw.rect(screen,"red",(1300,200,100,140),0,border_radius=4)
                pygame.draw.rect(screen,"white",(1300,200,100,140),4,border_radius=4)
                #pygame.draw.rect(screen, GRAY, (x_possition, y_possition, CARD_W, CARD_H))
                #text = FONT.render("X", True, BLACK)
                #screen.blit(text, (x_possition + 10, y_possition + 40))
                x_possition += 80; y_possition += 0
            count += 1
            pygame.display.flip()

    def draw_main_game(table_amount):
        screen = pygame.display.set_mode((1440, 1100))
        screen.fill(GREEN)
        nonlocal bet_amount
        
        # draw the cards
        x_pos = 500; y_pos = 100
        for card in player_hand:
            card_info = deck[card]
            pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
            pretty_card.show_card(screen,coords=(x_pos,y_pos))
            #pygame.draw.rect(screen, WHITE, (x_pos, y_pos, CARD_W, CARD_H))
            #text = FONT.render(str(f'{card} (ID)'), True, BLACK)
            #screen.blit(text, (x_pos + 10, y_pos + 40))
            x_pos += 80; y_pos += 0
        
        x = 500; y = 650
        for _ in computer_hand:
            pygame.draw.rect(screen,"red",(x,y,100,140),0,border_radius=4)
            pygame.draw.rect(screen,"white",(x,y,100,140),4,border_radius=4)
            #pygame.draw.rect(screen, GRAY, (x, y, CARD_W, CARD_H))
            #text = FONT.render("X", True, BLACK)
            #screen.blit(text, (x + 10, y + 40))
            x += 80; y += 0

        draw_table(table_amount)

        # draw a discard card
        card_info = deck[card]
        pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
        pretty_card.show_card(screen,coords=(x_pos,y_pos))
        #pygame.draw.rect(screen, WHITE, (200, 400, CARD_W, CARD_H))
        #text = FONT.render("Discard", True, BLACK)
        #screen.blit(text, (200 + 5, 400 + 40))

        check_rect = pygame.draw.rect(screen, BUTTON_COLOR, (150, 625, 100, 50), 5, 0) # Check
        text = FONT.render(str("Check"), True, BLACK)
        screen.blit(text, (150 + 10, 625 + 25))

        bet_rect = pygame.draw.rect(screen, BUTTON_COLOR, (150, 725, 100, 50), 5, 0) # bet
        text2 = FONT.render(str("Bet"), True, BLACK)
        screen.blit(text2, (150 + 10, 725 + 25))

        fold_rect = pygame.draw.rect(screen, BUTTON_COLOR, (150, 825, 100, 50), 5, 0) # fold
        text3 = FONT.render(str("Fold"), True, BLACK)
        screen.blit(text3, (150 + 10, 825 + 25))

        mon_text = FONT.render(str(f"You have bet ${bet_amount}. You have ${user_mon-bet_amount} left"), True, BLACK)
        screen.blit(mon_text, (100, 100))

        pygame.display.flip()

        wait = True
        while wait:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                wait = False
                return 0, 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bet_rect.collidepoint(event.pos):
                    wait = False
                    more_mon = make_bet()
                    return "Bet", more_mon
                elif fold_rect.collidepoint(event.pos):
                    wait = False
                    return "Fold", 0
                elif check_rect.collidepoint(event.pos):
                    wait = False
                    return "Check", 0
    def draw_ending():
        evaluator = Evaluator()

        player_score = check_hands(player_hand, table)
        comp_score = check_hands(computer_hand, table)
        won, final_mon = determine_win(player_score, comp_score)
        write_2_gambling(csv_path, won, final_mon)
        screen = pygame.display.set_mode((1440, 1100))
        screen.fill(GREEN)
        nonlocal bet_amount, user_mon
        
        # draw the cards
        x_pos = 500; y_pos = 100
        for card in player_hand:
            card_info = deck[card]
            pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
            pretty_card.show_card(screen,coords=(x_pos,y_pos))
            #pygame.draw.rect(screen, WHITE, (x_pos, y_pos, CARD_W, CARD_H))
            #text = FONT.render(str(f'{card} (ID)'), True, BLACK)
            #screen.blit(text, (x_pos + 10, y_pos + 40))
            x_pos += 80; y_pos += 0
        
        x = 500; y = 650
        for cards in computer_hand:
            card_info = deck[cards]
            pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
            pretty_card.show_card(screen,coords=(x_pos,y_pos))
            #pygame.draw.rect(screen, WHITE, (x, y, CARD_W, CARD_H))
            #text = FONT.render(f"{cards} (ID)", True, BLACK)
            #screen.blit(text, (x + 10, y + 40))
            x += 80; y += 0

        draw_table(5)

        # draw a discard card
        card_info = deck[cards]
        pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
        pretty_card.show_card(screen,coords=(x_pos,y_pos))
        #pygame.draw.rect(screen, WHITE, (200, 400, CARD_W, CARD_H))
        #text = FONT.render("Discard", True, BLACK)
        #screen.blit(text, (200 + 5, 400 + 40))

        # tell the user the results
        # first get the words for the hands they have
        player_score_class = evaluator.get_rank_class(player_score)
        player_hand_rank = evaluator.class_to_string(player_score_class).format(player_score)
        comp_score_class = evaluator.get_rank_class(comp_score)
        comp_hand_rank = evaluator.class_to_string(comp_score_class).format(comp_score)
        # get the result for the player to display later
        if player_score < comp_score:
            player_won = "You Won!!!"
            win = "True"
            money = user_mon + bet_amount
        elif comp_score < player_score:
            player_won = "You Lost. :("
            win = "False"
            money = user_mon - bet_amount
        elif player_score == comp_score:
            player_won = "It was a Tie!"
            win = "Tie"
            money = user_mon
        else:
            print("Something went wrong... Line 244")
        # draw text about player winning
        win_text = FONT.render(str(f"Your hand: {player_hand_rank}    Computer's hand: {comp_hand_rank}    {player_won}"), True, BLACK)
        screen.blit(win_text, (100, 100))

        # draw a button to leave (and write result to CSV)
        end_rect = pygame.draw.rect(screen, BUTTON_COLOR, (150, 625, 200, 50), 5, 0)
        end_text = FONT.render(str("End Game & Go Back"), True, BLACK)
        screen.blit(end_text, (150 + 10, 625 + 25))

        pygame.display.flip()

        wait = True
        while wait:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                wait = False
                return 0, 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if end_rect.collidepoint(event.pos):
                    wait = False
                    write_2_gambling(csv_path, win, money)
                    return
            
    def end_game(won=None, money = None):
        if won == None and money == None:
            won, money = determine_win(player=check_hands(player_hand), comp=check_hands(computer_hand))
        write_2_gambling(csv_path, won, money)
        return

    clock = pygame.time.Clock()
    FONT= pygame.font.SysFont(None,24)

    GREEN = (0, 120, 0)
    BUTTON_COLOR = (60, 60, 60)
    BLACK = (0, 0, 0)
    # This is what will be called when the user chooses to play poker.
    # get the variables needed for play
    saved_game = stuff_in_CSV(csv_path)
    if saved_game == True:
        try:
            with open(csv_path, "r") as file:
                reader = list(csv.reader(file))
                user_mon = int(reader[-1][2])
        except Exception as e:
            print(f"Could not open the file given.\nPath given: {csv_path}\nReason for error: {e}")
            user_mon = 100
    else:
        user_mon = 100

    player_hand = []
    computer_hand = []
    discard = []
    table = []
    bet_amount = 0

    # Shuffle the card ids
    with open("files/cards.json","r") as cards:
        deck = json.load(cards)
    shuffled_deck = list(deck.keys())
    random.shuffle(shuffled_deck)

    # take the first two card ids and give them to the player (remove these ids from the list). Display the cards for these Ids. Append these cards into a list called player_hand.
    for _ in range(2):
        player_hand.append(shuffled_deck[0])
        shuffled_deck.pop(0)

    # take the next two card ids and give them to the computer (remove these ids from the list). Save these cards in a comp_hand list. Display card BACKS to not let the player know the computer's cards
    for _ in range(2):
        computer_hand.append(shuffled_deck[0])
        shuffled_deck.pop(0)

    # remove first id from shuffled deck list and put it into discared list.
    discard.append(shuffled_deck[0])
    shuffled_deck.pop(0)

    # remove next THREE ids from shuffled list and put them into the table list. 
    for _ in range(3):
        table.append(shuffled_deck[0])
        shuffled_deck.pop(0)


    for _ in range(2):
        # discard and put the next card into table (card four and five for the table)
        discard.append(shuffled_deck[0])
        shuffled_deck.pop(0)
        table.append(shuffled_deck[0])
        shuffled_deck.pop(0)

    pygame.init()
    screen = pygame.display.set_mode((1440, 1100))
    screen.fill(GREEN)
    
    # show the user what they have and ask if they want to bet and play with it, or fold and not play this round
    
    hand_text = FONT.render("This is what you have. If you want to play with this hand, click 'Initial Bet' If you don't want to play with this hand, click 'Fold'", True, (BLACK))
    screen.blit(hand_text, (300, 100))

    x_pos = 500; y_pos = 200
    for card in player_hand:
        card_info = deck[card]
        pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
        pretty_card.show_card(screen,coords=(x_pos,y_pos))
        #pygame.draw.rect(screen, WHITE, (x_pos, y_pos, CARD_W, CARD_H))
        #text = FONT.render(str(f'{card} (ID)'), True, BLACK)
        #screen.blit(text, (x_pos + 10, y_pos + 40))
        x_pos += 80; y_pos += 0

    bet_rect = pygame.draw.rect(screen, BUTTON_COLOR, (200, 625, 150, 75), 5, 0) # bet
    text2 = FONT.render(str("Initial Bet"), True, BLACK)
    screen.blit(text2, (200 + 35, 625 + 30))

    fold_rect = pygame.draw.rect(screen, BUTTON_COLOR, (400, 625, 150, 75), 5, 0) # fold
    text3 = FONT.render(str("Fold"), True, BLACK)
    screen.blit(text3, (400 + 35, 625 + 30))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            game1 = False
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bet_rect.collidepoint(event.pos):
                waiting = False
                make_bet()
            elif fold_rect.collidepoint(event.pos):
                waiting = False
                end_game("False", user_mon)
                return
        clock.tick(60)
    
    play, any_mon = draw_main_game(3)
    print(f"Play:{play}, Money bet: {any_mon}")
    if play == 0 and any_mon == 0:
        # the user hit the close button on the window
        return
    
    game1 = True
    game2 = False
    while game1:
        if play == "Check" or play == "Bet":
            bet_amount += any_mon
            print(f"Bet amount: {bet_amount}")
            play_again, more_mon = draw_main_game(4)
            print("In game with four cards on the table")
            if play_again == "Fold":
                # display something about the user returning to games menu because of folding
                bet_amount += more_mon
                money = user_mon-bet_amount
                end_game(won="False", money=money)
                return
            elif play_again == "Check" or play_again == "Bet":
                print(f"Play:{play_again}, Money bet: {bet_amount}")
                bet_amount += more_mon
                final_play, final_bet = draw_main_game(5)
                game2 = True
                break
            elif play_again == 0 and more_mon == 0:
                return
            else:
                print("Something went wrong with playing again. See line 310")
        else:
            money = user_mon-bet_amount
            end_game(won="False", money=money)
            return
        pygame.display.flip()
    
    while game2:
        # determine if they went through with the final play
        if final_play == "Fold":
            # display something about the user returning to games menu because of folding
            money = user_mon - bet_amount
            end_game(won="False", money=money)
            return
        elif final_play == "Check" or final_play == "Bet":
            bet_amount += final_bet
            # "Flip" computer's cards (Display the card instead of the back)
            # THIS SHOULD HAPPEN IF USER NEVER FOLDED (fingers crossed)
            draw_ending()
            break
        elif final_play == 0 and final_bet == 0:
            return
        else:
            print("Something went wrong with playing again. See line 319")
        pygame.display.flip()
        # Tell the user who won, new money amount, and end the Pygame loop

        clock.tick(60)

def poker_instructions():
    pygame.init()
    GREEN = (0, 120, 0)
    FONT= pygame.font.SysFont(None,24)
    screen = pygame.display.set_mode((1440, 1100))
    screen.fill(GREEN)
    
    # Text to display
    description = f"How to Play Poker:\nPoker is a betting game where you want to get the best of five cards possible.\nThe rankings from best to worst are:\nRoyal Flush: Ace, King, Queen, Jack, and Ten in the SAME SUIT\n Straight Flush: Five consecutive cards in the SAME SUIT (ex: 7, 8, 9, 10, Jack all in clubs)\nFour of a Kind: Four cards with the same number, suit doesn't matter\nFull House: Three cards with the same number AND two cards with the same number (3 Aces and 2 Kings)\nFlush: Five cards with the same suit (card number doesn't matter)\nStraight: Five consecutive numbers (suit does not matter)\nThree of a Kind: Three cards with the same number\nTwo Pair: two cards with matching numbers, plus another two cards with matching numbers (2 Aces and 2 Queens)\nPair: Two cards with matching numbers\nHigh Card: When no other combination is possible, the card with the highest value from your hand.\nIf you believe you have a higher hand than the computer, put in money! You want to maximize your winnings!"
    lines = description.split("\n")
    for i, line in enumerate(lines):
        rules_surface = FONT.render(line,True,"black")
        screen.blit(rules_surface,(1500,100 + i * 30))
    pygame.display.flip()

#play_poker()
#poker_instructions()