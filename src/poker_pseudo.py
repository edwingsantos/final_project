# Pseudocode for Poker (LD)

# Open the poker csv. Use LD helper function to check if there are any saved games
# if that call = True, 
    # Open csv. read the headers. do: last_line = file.readlines()[-1]. in last_line, user_mon = last_line[2 or "Money"] <- (this depends on whether I do a reader or DictReader)
# else: user_mon = 100

# Check for Royal Flush. Im hard coding this, there are only four possible royal flushes
    # Parameter = list of card VALUES and card SUITS created earlier
    # BUILD 

# GAMEPLAY ASSISTANT FUNTIONS
    # CHECK HANDS (parameters = card_ID_1, card_ID_2, card_ID_3, card_ID_4, card_ID_5, card_ID_6, card_ID_7)
        # Variable: empty list that will be passed into sub-functions
        # FUNCTION TO TURN IDS INTO CARD INFO NEEDED
            # for each of the 7 ids: access json, use id to get VALUE and SUIT. append these into the empty list created. It will look like [Value1, Suit1, Value2, Suit2, Value3, Suit3, Value4, Suit4, etc to 7]

        # BUILD ALL THIS
        # Check for ROYAL FLUSH (A, K, Q, J, 10 in all same suit)
            # how do this???
        # Check for STRAIGHT FLUSH (five consecutive #'s in same suit)
            # kjfdglhdsaf
        # Check for FOUR OF A KIND (four cards with the same number)
            # lkdsfljdf
        # Check for FULL HOUSE (3 cards with smae number, two cards with same number)
            # djflkadsf
        # Check for FLUSH (five cards with same suit)
            # adhgahd
        # Check for STRAIGHT (five consecutive numbers)
            # dsglkd
        # Check for THREE OF A KIND (three cards with same number)
            # ahfdkh
        # Check for TWO PAIR (two cards with same number, two cards with same number)
            # kdhfkjdsa
        # Check for ONE PAIR (two cards with same number)
            # ldkflad
        # Check for HIGH CARD of FIRST TWO PASSED IN IDS
            # kedsjhflksajhd

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
# take the first two card ids and give them to the player (remove these ids from the list). Display the cards for these Ids
# take the next two card ids and give them to the computer (remove these ids from the list). Save these cards as comp_card_1 and comp_card_2. Display card BACKS to not let the player know the computer's cards
# Have a "discarded" list and a "table" list

# have user bet (call ES betting func) (required!). Make sure computer MATCHES what the user has in
# Variable: bet_amount = what the user has betted (this could be added onto with future optional bets)

# remove first id from shuffled deck list and put it into discared list.
# remove next THREE ids from shuffled list and put them into the table list
# display the cards from the table list

# call PLAY ROUND func

# They should come here if they didn't fold
# call PLAY ROUND func for LAST TIME

# "Flip" computer's cards (Display the card instead of the back)

# BUILD END OF GAME