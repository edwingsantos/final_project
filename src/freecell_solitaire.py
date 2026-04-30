# LD Pseudocode for Freecell

# import LD's valid move func and LV's shuffle deck function

# shuffle deck

# to deal the cards: 8 lists (these are the columns). Four lists will have 7 ids while the other four will have 6 ids

# user only can move a card that is the LAST indext in the lists

# when selecting a card to move, IF the id == 1, 14, 27 or 40, it is an Ace and can be moved to the ace spot.
# Each of these four spots will be kept as a list. When a card is moved onto an Ace, append that ID into the correct symbol list.

# allow user to move cards. Call LD's valid move function every time a card is moved.

# When ALL FOUR of the Ace lists reach a length of 13, user has moved all the cards onto the ace piles and have thus won. Win = True

# Call LD's write to solitaire CSV function and pass in the freecell.csv path and Win

# return to main menu