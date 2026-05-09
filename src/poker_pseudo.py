# Pseudocode for Poker (LD)
import random
import pygame
import json
from treys import Evaluator, Card
from shuffle_deck import shuffle_deck
from LD_psuedocode import stuff_in_CSV, write_2_gambling
from betting_func import starting_bet

#csv_path = path to poker csv
csv_path = "files/poker.csv"

# Open the poker csv. Use LD helper function to check if there are any saved games
# if that call = True, 
    # Open csv. read the headers. do: last_line = file.readlines()[-1]. in last_line, user_mon = last_line[2 or "Money"] <- (this depends on whether I do a reader or DictReader)
# else: user_mon = 100


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

    # PLAY ROUND: display a button to "Check" (continue without betting), "Bet" (when clicked, call bet function and add to bet_amount), "Fold" (end the game)
    # if check:
        # pass, they don't do anything
    # elif bet:
        # call bet function and add to bet_amount
        # pass (?)
    # elif fold:
        # won = False
        # user_mon -= bet_amount
        # call END GAME func
    # else:
        # this shouldn't happen. . . .

    # END GAME: call LD write to gambling csv and pass in poker.csv path, win = won, money = user_mon
        # leave game and return to main menu


def play():
    def play_round():
        continue_game = True
        while continue_game:
            # Show the buttons to Check, Bet, or Fold
            check_rect = pygame.draw.rect(screen, BUTTON_COLOR, (150, 625, 50, 50), 5, 0) # Check
            text = FONT.render(str("Check"), True, BLACK)
            screen.blit(text, (150 + 10, 625 + 40))

            bet_rect = pygame.draw.rect(screen, BUTTON_COLOR, (200, 625, 50, 50), 5, 0) # bet
            text2 = FONT.render(str("Bet"), True, BLACK)
            screen.blit(text2, (150 + 10, 625 + 40))

            fold_rect = pygame.draw.rect(screen, BUTTON_COLOR, (250, 625, 50, 50), 5, 0) # fold
            text3 = FONT.render(str("Fold"), True, BLACK)
            screen.blit(text3, (150 + 10, 625 + 40))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if check_rect.collidepoint(event.pos):
                        print("They Check")
                    elif bet_rect.collidepoint(event.pos):
                        print("They Bet")
                    elif fold_rect.collidepoint(event.pos):
                        print("They Fold")
            
            pygame.display.flip()

    def make_bet():
        while bet:
            # Make player bet
            initial_bet = starting_bet()
            bet_amount += initial_bet
            bet = False

    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FONT= pygame.font.SysFont(None,24)

    GREEN = (0, 120, 0)
    BUTTON_COLOR = (60, 60, 60)
    WHITE = (255, 255, 255)
    GRAY = (80, 80, 80)
    BLACK = (0, 0, 0)

    CARD_W, CARD_H = 70,100
    # This is what will be called when the user chooses to play poker.
    # get the variables needed for play
    saved_game = stuff_in_CSV(csv_path)
    if saved_game == True:
        try:
            with open(csv_path, "r") as file:
                last_line = file.readlines()[-1]
                user_mon = last_line[2]
        except Exception as e:
            print(f"Could not open the file given.\nPath given: {csv_path}\nReason for error: {e}")
    else:
        user_mon = 100

    player_hand = []
    computer_hand = []
    discard = []
    table = []
    bet_amount = 0

    # Call LV shuffle card function
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


    pygame.init()
    screen = pygame.display.set_mode((1440, 1100))
    game = True
    bet = True
    
    while game:
        screen.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bet_rect.collidepoint(event.pos):
                    print("They Bet")
                    make_bet()
        
        # draw the cards
        for card in player_hand:
            x_pos = 500; y_pos = 100
            pygame.draw.rect(screen, WHITE, (x_pos, y_pos, CARD_W, CARD_H))
            text = FONT.render(str(card), True, BLACK)
            screen.blit(text, (x_pos + 10, y_pos + 40))
            x_pos += 80; y_pos += 0
        
        for card2 in computer_hand:
            x = 500; y = 650
            pygame.draw.rect(screen, GRAY, (x, y, CARD_W, CARD_H))
            text = FONT.render("X", True, BLACK)
            screen.blit(text, (x + 10, y + 40))
            x += 80; y += 0

        # when drawing is done:
        bet_rect = pygame.draw.rect(screen, BUTTON_COLOR, (200, 625, 50, 50), 5, 0) # bet
        text2 = FONT.render(str("Initial Bet"), True, BLACK)
        screen.blit(text2, (150 + 10, 625 + 40))

        # remove first id from shuffled deck list and put it into discared list.
        discard.append(shuffled_deck[0])
        shuffled_deck.pop(0)

        # remove next THREE ids from shuffled list and put them into the table list. 
        for _ in range(3):
            table.append(shuffled_deck[0])
            shuffled_deck.pop(0)

        # display the cards from the table list

        # call PLAY ROUND func
        play_round()

        # They should come here if they didn't fold
        # call PLAY ROUND func for LAST TIME

        # "Flip" computer's cards (Display the card instead of the back)

        # Have new lists for the FORMATED cards from the table, computer, and player lists. Put "formated" infront of the new lists names

        # Call treys' evaluate class function and pass in formated_player_hand and formated_table. Save this call as "player_score"
        player_score = check_hands(player_hand, table)
        # Call the same function again but pass in formated_comp_hand and formated_table. Save this as "comp_score"
        comp_score = check_hands(computer_hand, table)

        if player_score < comp_score:
            win = 'True'
            user_mon += bet_amount
            game = False
        elif comp_score < player_score:
            win = 'False'
            user_mon -= bet_amount
            game = False
        elif player_score == comp_score:
            win = 'Tie'
            user_mon = user_mon
            game = False
        else:
            # something went wrong
            print("Something happened when comparing who won in poker.\nFile:poker_psudo.py\nLine: 197")
        
        # Tell the user who won, new money amount, and end the Pygame loop
        pygame.display.flip()
        # call LD's write to CSV for gambling function and pass in csv_path, win, user_mon
        # return to main menu
    write_2_gambling(csv_path, win, user_mon)

play()