# LV 1st Main
# Run this file for full program
# import games - Solitaire, Freecell, Black Jack, Pyramid Solitaire
# from Lizzie's code import ..
# from Parkers's code import ..
# from Edwing's code import ..
# from Lucci's code import ..
# import tkinter
# import sys
import tkinter as tk
import sys

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
    def exit_program(sys):
        instruction = tk.Label(root, text = "Choose a Game")
        solitaire = tk.Button(root, text = "Solitaire", command = "menu") #Will change once we have the function for each game
        black_jack = tk.Button(root, text = "Black Jack", command = "menu")
        pyramid = tk.Button(root, text = "Pyramid Solitaire", command = "menu")
        freecell = tk.Button(root, text = "Freecell", command = "menu")
        poker = tk.Button(root, text = "Poker", command = "menu")

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