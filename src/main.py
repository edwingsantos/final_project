# LV 1st Main
# Run this file for full program
# import games - Solitaire, Freecell, Black Jack, Pyramid Solitaire
# from Lizzie's code import ..
# from Parkers's code import ..
# from Edwing's code import ..
# from Lucci's code import ..
# import tkinter
# import sys
import pygame
import tkinter as tk
import sys
#from blackjack import blackjack_game
from freecell_solitaire import *
from solitaire import *

# def show_choices(root):
#     Display a label that says "Choose a game"
#     
#     Create button for Solitaire
#         When clicked - call Solitaire game function
#
#     Create button for Black Jack
#         When clicked - call Black Jack game function
#
#     Create button for Pyramid Solitaire
#         When clicked - call Pyramid Solitaire function
#
#     Create button for Freecell
#         When clicked - call Freecell function
#
#     Create button for Poker
#         When clicked - call Poker function
#
#     Create Quit button
#         When clicked - exit program completely

# FUNCTION Exit
# def exit_program():
#     Use system command to close program -sys.exit

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
        command=lambda: print("Launch Black Jack")
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

# MAIN FUNCTION
# def main():

#     Create main window using tkinter
#     Set window title (example: "Personal Finance Main")
#     Set minimum window size (300 x 200)

#     Display welcome message
#         Example: "Welcome! Click continue to start"

#     Create "Continue" button
#         When clicked:
#             Remove welcome message from screen
#             Remove continue button
#             Call function to show game choices

#     Start the program loop (root.mainloop)
#         This keeps the window open and running
#main()
def main():

    root = tk.Tk()
    root.title("Cards Game")
    root.attributes('-fullscreen', True) # Fullscreen!!!!
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