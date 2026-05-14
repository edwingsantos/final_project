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
    return symbol


def check_hands(hand, table):
    def format_cards(id):
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
            print("Something happened in formatting cards function.\nFile: poker_psuedo.py\nLine: 32")
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
            print("Something happened in formatting cards function.\nFile: poker_psuedo.py\nLine: 61")
        
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
    return rank


def play_poker():
    def make_bet():
        bet = True
        while bet:
            # Make player bet
            initial_bet = starting_bet()
            bet = False
        return initial_bet
    
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
            print("Something happened when comparing who won in poker.\nFile:poker_psudo.py\nLine: 120")
        return win, user_mon
    
    def draw_table(cards_shown):
        x_possition = 500; y_possition = 400
        count = 0
        for the_card in table:
            if count < cards_shown:
                card_info = deck[the_card]
                pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
                pretty_card.show_card(screen,coords=(x_possition,y_possition))
                x_possition += 80; y_possition += 0
                #print("Shown")
            else:
                pygame.draw.rect(screen,"red",(x_possition,y_possition,100,140),0,border_radius=4)
                pygame.draw.rect(screen,"white",(x_possition,y_possition,100,140),4,border_radius=4)
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
            x_pos += 80; y_pos += 0
        
        x = 500; y = 650
        for _ in computer_hand:
            pygame.draw.rect(screen,"red",(x,y,100,140),0,border_radius=4)
            pygame.draw.rect(screen,"white",(x,y,100,140),4,border_radius=4)
            x += 80; y += 0

        draw_table(table_amount)

        # draw a discard card
        pygame.draw.rect(screen,"red",(200,400,100,140),0,border_radius=4)
        pygame.draw.rect(screen,"white",(200,400,100,140),4,border_radius=4)

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
            x_pos += 80; y_pos += 0
        
        x = 500; y = 650
        for cards in computer_hand:
            card_info = deck[cards]
            pretty_card = Card_styles(card_info["Value"],suit_match(card_info["Suit"]),card_info["Color"])
            pretty_card.show_card(screen,coords=(x,y))
            x += 80; y += 0

        draw_table(5)

        # draw a discard card
        pygame.draw.rect(screen,"red",(200,400,100,140),0,border_radius=4)
        pygame.draw.rect(screen,"white",(200,400,100,140),4,border_radius=4)

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
            print("Something went wrong... Line 253")
        # draw text about player winning
        win_text = f"Your hand: {player_hand_rank}\nComputer's hand: {comp_hand_rank}\n{player_won}"
        lines = win_text.split("\n")
        for i, line in enumerate(lines):
            rules = FONT.render(line,True,"black")
            screen.blit(rules,(100,100 + i * 30))

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
                money = make_bet()
                bet_amount += money
            elif fold_rect.collidepoint(event.pos):
                waiting = False
                end_game("False", user_mon)
                return
        clock.tick(60)
    
    play, any_mon = draw_main_game(3)
    if play == 0 and any_mon == 0:
        # the user hit the close button on the window
        return
    
    game1 = True
    game2 = False
    while game1:
        if play == "Check" or play == "Bet":
            bet_amount += any_mon
            play_again, more_mon = draw_main_game(4)
            if play_again == "Fold":
                # display something about the user returning to games menu because of folding
                bet_amount += more_mon
                money = user_mon-bet_amount
                end_game(won="False", money=money)
                return
            elif play_again == "Check" or play_again == "Bet":
                bet_amount += more_mon
                final_play, final_bet = draw_main_game(5)
                game2 = True
                break
            elif play_again == 0 and more_mon == 0:
                return
            else:
                print("Something went wrong with playing again. See line 396")
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
            draw_ending()
            break
        elif final_play == 0 and final_bet == 0:
            return
        else:
            print("Something went wrong with playing again. See line 319")
        pygame.display.flip()
        clock.tick(60)

def poker_instructions():
    pygame.init()
    GREEN = (0, 120, 0)
    FONT= pygame.font.SysFont(None,24)
    BUTTON_COLOR = (60, 60, 60)
    screen = pygame.display.set_mode((1440, 1100))
    screen.fill(GREEN)

    pygame.draw.rect(screen, "white", (280, 80, 1000, 450), border_radius=8)
    
    # Text to display
    description = "How to Play Poker:\nPoker is a betting game where you want to get the best of five cards possible.\nThe rankings from best to worst are:\n - Royal Flush: Ace, King, Queen, Jack, and Ten in the SAME SUIT\n - Straight Flush: Five consecutive cards in the SAME SUIT (ex: 7, 8, 9, 10, Jack all in clubs)\n - Four of a Kind: Four cards with the same number, suit doesn't matter\n - Full House: Three cards with the same number AND two cards with the same number (3 Aces and 2 Kings)\n - Flush: Five cards with the same suit (card number doesn't matter)\n - Straight: Five consecutive numbers (suit does not matter)\n - Three of a Kind: Three cards with the same number\n - Two Pair: two cards with matching numbers, plus another two cards with matching numbers (2 Aces and 2 Queens)\n - Pair: Two cards with matching numbers\n - High Card: When no other combination is possible, the card with the highest value from your hand.\nIf you believe you have a higher hand than the computer, put in money! You want to maximize your winnings!"
    lines = description.split("\n")
    for i, line in enumerate(lines):
        rules = FONT.render(line,True,"black")
        screen.blit(rules,(300,100 + i * 30))

    play_poker_button = pygame.draw.rect(screen, BUTTON_COLOR, (500, 625, 150, 50), 5, 0)
    button_text = FONT.render("Play Poker!", True, "black")
    screen.blit(button_text, (525, 645))

    pygame.display.flip()

    waiting = True
    while waiting:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_poker_button.collidepoint(event.pos):
                waiting = False
                play_poker()
                return

#play_poker()
#poker_instructions()