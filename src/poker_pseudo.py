# Pseudocode for Poker (LD)
import csv
from treys import Evaluator, Card
from solitaire import shuffle_deck
from LD_psuedocode import stuff_in_CSV

#csv_path = path to poker csv
csv_path = "files/poker.csv"

# Open the poker csv. Use LD helper function to check if there are any saved games
# if that call = True, 
    # Open csv. read the headers. do: last_line = file.readlines()[-1]. in last_line, user_mon = last_line[2 or "Money"] <- (this depends on whether I do a reader or DictReader)
# else: user_mon = 100
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


# GAMEPLAY ASSISTANT FUNTIONS
    # CHECK HANDS (parameters = card_ID_1, card_ID_2, card_ID_3, card_ID_4, card_ID_5, card_ID_6, card_ID_7)
        # use traderbagel's treys poker hand ranking functions
def check_hands(player_hand, table):
    def format_cards(id):
        # FORMAT CARDS (turn a card id into a shortened version like As (Ace of spades))
            # Take in ID. Compare to number 1-52 and based on result, give abreviation
        # check the beggining. (A-K)
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
            print("Somewthing happened in formatting cards function.\nFile: poker_psuedo.py\nLine: 58")
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
            print("Somewthing happened in formatting cards function.\nFile: poker_psuedo.py\nLine: 69")
        
        card_name = beginning+suit
        return card_name
    
    # main code for checking


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

# Call LV shuffle card function
# take the first two card ids and give them to the player (remove these ids from the list). Display the cards for these Ids. Append these cards into a list called player_hand.

# take the next two card ids and give them to the computer (remove these ids from the list). Save these cards in a comp_hand list. Display card BACKS to not let the player know the computer's cards

# Have a "discarded" list and a "table" list

# have user bet (call ES betting func) (required!). Make sure computer MATCHES what the user has in
# Variable: bet_amount = what the user has betted (this could be added onto with future optional bets)

# remove first id from shuffled deck list and put it into discared list.
# remove next THREE ids from shuffled list and put them into the table list. 
# display the cards from the table list

# call PLAY ROUND func

# They should come here if they didn't fold
# call PLAY ROUND func for LAST TIME

# "Flip" computer's cards (Display the card instead of the back)

# Have new lists for the FORMATED cards from the table, computer, and player lists. Put "formated" infront of the new lists names

# Call treys' evaluate class function and pass in formated_player_hand and formated_table. Save this call as "player_score"
# Call the same function again but pass in formated_comp_hand and formated_table. Save this as "comp_score"

# If player_score < comp_score (function returns a lower score for better hands): player win
    # Win = true
    # user_mon += bet_amount
# if player_score > comp_score (computer scored lower than player): player looses
    # Win = False
    # user_mon -= bet_amount
# if player_score == comp_score (tie, smae hand): no one wins (i dont want to figure out high card, unless treys does that, then maybe)
    # win = Tie
    # user_mon = user_mon

# call LD's write to CSV for gambling function and pass in csv_path, win, user_mon
# return to main menu