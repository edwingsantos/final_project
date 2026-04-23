#USE IF JSON CARDS ARE WIPED
import json


def replace_deck_of_cards():
    suits = ["Clubs","Spades","Diamonds","Hearts"]
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    royal_names = ["Jack","Queen","King"]
    #create all the cards
    deck = {}
    #for each suit
    id = 0
    for x in suits:

        #create a card for each value
        for y in values:
            #determine if the card is a royal and assign royal suit
            is_royal = False
            royal_type = "Normal"
            if y > 10:
                is_royal = True
                if y == 11:
                    royal_type = "Jack"
                elif y == 12:
                    royal_type = "Queen"
                elif y == 13:
                    royal_type = "King"
            
            #ID is the number of card in the deck so shuffling can happen a lot easier (pick random number and match that with ID)
            id+=1

            if is_royal:
                match y:
                    case 11:
                        name = f"Jack of {x}"
                    case 12:
                        name = f"Queen of {x}"
                    case 13:
                        name = f"King of {x}"
            elif y == 1:
                name = f"Ace of {x}"
            else:
                name = f"{y} of {x}"

            #determines if the card is red or black
            if suits.index(x) < 2:
                color = "Black"
            else:
                color = "Red"



            
            #adds card to deck
            deck[name] = {
                "Value":y,
                "Suit":x,
                "Color":color,
                "Id":id,
                "IsRoyal":is_royal,
                "RoyalType":royal_type
                }

    with open("files/cards.json","w") as file:
        file.truncate(0)
        file.seek(0)
        json.dump(deck,file,indent=4)

replace_deck_of_cards()