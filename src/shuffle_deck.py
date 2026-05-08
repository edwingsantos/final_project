import random
import json

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.face_up = False

    def color(self):
        return "red" if self.suit in ["hearts", "diamonds"] else "black"

    def __repr__(self):
        return f"{self.value}{self.suit[0]}"


def card_to_id(card):
    return str(card.value) + "_" + card.suit

def create_deck(json_path):

    deck = []

    with open(json_path, "r") as f:
        data = json.load(f)

    for key in data:
        card_data = data[key]

        card = Card(
            suit=card_data["Suit"].lower(),
            value=card_data["Value"]
        )

        deck.append(card)

    return deck

# SHUFFLE DECK
#def shuffle_deck(deck):
    # Create an empty list to store shuffled cards
    # While there are still cards left in the original deck
    # Generate a random index between 0 and the last position in the deck       
        # Remove the card at that random index from the original deck
        # Add that card to the shuffled deck
    # Once all cards have been moved, return the shuffled deck

# Aun no hace nada para mi codigo simplemente imprime lo mismo cada vez y esto no me ayuda

def shuffle_deck(json_path):

    deck = create_deck(json_path)

    random.shuffle(deck)

    return deck