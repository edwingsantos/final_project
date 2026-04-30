#ES starting spedocode

# import pygame, json, sys 
import pygame
import json
import sys
from betting_func import *

#call the shufle funtion from lucci and append it to the points dictionary 
# do the same thing but just append it to the dealers hand 


#use dictionary called point to safe the cards choosen 
#make a dictionary for the dealers hand 
#use an other dictionary for the amount of games played 
#use another dictianry for win games
#user another library for money 
#check if the 3rd line of the csv is 0
# if the 3rd line is empty give the user 100$ and append it to the money dictionary 


#SET up screen 
#set up the board with two cards you can see, these cards have to match with the ones in the points dicitonary 
#Have two card for the dealer and make one card show, remember one of those have to match in the dictionary

#make a funtion for blackjack 
def blackjack_game():
    print("blackjack")
    #call the beggingin of the betting funtion 
    starting_bet()
    #safe those amounts into the ductionaries 

    #show users their cards and let them see the dealers cards
    #if the user has an instant 21 call the winning funtion from betting funtion 


    #make a funtion for DRAW cards
    #ask user if they want to draw a card
    #if they do call the funtion again and add the points to the libraries
    #if not then continue with the code

    #make a funtion for reveal cards
    #if the dealer have cards values less than 16 call the draw funtion but add it to the dealer dictionary
    #if the dealer has a 21 then the dealer wins, call the loosing funtion
    #if the dealer has more than 16 then compare the two values of the dictionaries
        #if the dealer has a grater amount of points, call the loosing funtion
        #if the dealer has a less amount of points, call the winning funtion
    #if the users have the same amount of points call the tie funtion from the betting funtion 


#ask the user if they want to play blackjack again
    #if choice is yes then call the blackjack funtion
    #if choice is no the go to the main menu





import tkinter as tk

def show_choices(root):
# Still have to add when to call the funcitons for each game !!!!!
    # Title label
    instruction = tk.Label(root, text="Choose a Game")
    instruction.pack()

    # Solitaire button
    solitaire = tk.Button(
        root,
        text="Solitaire",
        command=lambda: print("Launch Solitaire")  # replace later
    )
    solitaire.pack()

    # Black Jack button
    black_jack = tk.Button(
        root,
        text="Black Jack",
        command=lambda: blackjack_game()
    )
    black_jack.pack()

    # Pyramid Solitaire button
    pyramid = tk.Button(
        root,
        text="Pyramid Solitaire",
        command=lambda: print("Launch Pyramid Solitaire")
    )
    pyramid.pack()

    # Freecell button
    freecell = tk.Button(
        root,
        text="Freecell",
        command=lambda: print("Launch Freecell")
    )
    freecell.pack()

    # Poker button
    poker = tk.Button(
        root,
        text="Poker",
        command=lambda: print("Launch Poker")
    )
    poker.pack()

    # Quit button
    quit_button = tk.Button(
        root,
        text="Quit",
        command=root.quit
    )
    quit_button.pack()

def main():

    root = tk.Tk()
    root.title("Cardds Game")
    root.geometry("300x300")

    welcome = tk.Label(root, text="Welcome! Click continue to start")
    welcome.pack()

    def start_menu():
        welcome.destroy()
        continue_btn.destroy()
        show_choices(root)

    continue_btn = tk.Button(root, text="Continue", command=start_menu)
    continue_btn.pack()

    root.mainloop()
    
main()