# Psuedocode for LD parts of the program. 
# This is tempory and the code will later be moved into proper files.
# import csv

# Is a card being moved for the solitaires a VALID move (opposite color (red on black and vise versa), and number of moved cards is ONE LESS than the card being moved onto (10 onto a jack, 3 onto a 4, etc.))

# CHECK IF OPPOSITE COLOR (own func)
    # HELPER FUNCTION FOR THIS PART
    # parameter = ID of card
    # find the color in JSON based off of id
    # return color

# Get the ID (1-52) of the card being MOVED
# CALL HELPER
# Get the ID of the card being moved ONTO
# CALL HELPER
# if color of MOVED_CARD is NOT equal to MOVED_ONTO_CARD, valid move
    # retunr true
# else: (red == red), invalid move
    # return false

# CHECK NUMBER (own func)
    # HELPER FUNCTION FOR THIS PART
    # parameter = id of card
    # find the value (1-13) in JSON based off of ID
    # return value
# get ID of card being MOVED
# CALL HELPER
# get id of card being moved ONTO
# CALL HELPER
# if value of MOVED_CARD + 1 is equal to value of MOVED_ONTO_CARD, valid moved
    # example of logic: let's say that I move an ace onto a two. Ace = 1 and 2 = 2. 1 + 1 = 2. 2 == 2
    # return true
# else: (3 == 2 (i moved a 2 onto a 2)), invalid move
    # return false



# At the end of the game, write the final game retults to the CSV for that game
# for the soliaires, this will include game number and if they won
# for the gambling ones, this will include game number, if they won (beat the computer/dealer), and how much money they have
# when a game is selected, it will establish a CSV path that will be passed into my functions

# HELPER FUNC TO KNOW IF THERE IS EVEN STUFF IN THE CSV
# parameter = CSV_PATH
# read the headers
# TRY reading the next line
    # return True. There is stuff to try and figure out the game number
# EXCEPT
    # return False. No games saved yet

# GET GAME NUMBER FUNCTION (sub func)
# parameter = CSV_PATH
# call helper and pass in the CSV_PATH
# if helper = True
    # Open csv. read the headers. do: last_line = file.readlines()[-1]. in last_line, game_num = last_line[0 or "game number"] <- (this depends on whether I do a reader or DictReader)
    # recent_game_num = game_num + 1
# else
    # recent_game_num = 1
# return recent_game_num

# GET MONEY FUNCTION (func being called when a gambling game is selected)
# parameter = CSV_PATH
# call helper and pass in the CSV_PATH
# if helper = True
    # Open csv. read the headers. do: last_line = file.readlines()[-1]. in last_line, money =  last_line[2 or "Money"] <- (this depends on whether I do a reader or DictReader)
# else
    # money = 100
# return money

# WRITE TO CSV FOR SOLITAIRE (func being called by outside code)
# parameters = CSV_PATH, WON
# call GET GAME NUMBER and pass in CSV_PATH. This = game_num
# open csv based off of CSV_PATH
# append the line "game_num for Game Number and WON for Win Game"

# WRITE TO CSV FOR GAMBLING (func being called by outside code)
# parameters = 