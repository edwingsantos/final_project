#USE IF JSON CARDS ARE WIPED
import json


def replace_deck_of_cards():
    suits = ["Clubs","Spades","Diamonds","Hearts"]
    values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    #create all the cards
    deck = {}
    #for each suit
    id = 0
    for x in suits:
        #create a card for each value
        for y in values:
            id+=1
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
                "Id":id
                }

    with open("files/cards.json","w") as file:
        file.truncate(0)
        file.seek(0)
        json.dump(deck,file,indent=4)

replace_deck_of_cards()