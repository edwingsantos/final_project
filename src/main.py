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
import sys
from freecell_solitaire import free_cell_game
from pyramid_solitaire import game
#from solitaire import solitaire
from blackjack import blackjack_instructions
from poker_pseudo import poker_instructions
#from solitaire import solitaire
#from pyramid_solitaire import *
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
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Game Collection")

# COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (70, 70, 70)
GREEN = (0, 120, 0)
BLUE = (40, 40, 120)

# FONT
FONT = pygame.font.SysFont(None, 40)
TITLE_FONT = pygame.font.SysFont(None, 60)

#  BUTTON CLASS
class Button:
    def __init__(self, text, x, y, w, h, action):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)

        label = FONT.render(self.text, True, WHITE)

        label_rect = label.get_rect(center=self.rect.center)

        screen.blit(label, label_rect)

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()


def launch_solitaire():
    print("Solitaire not ready yet")
# QUIT FUNCTION 
def quit_program():
    pygame.quit()
    sys.exit()

# GAME PLACEHOLDER SCREEN
def game_screen(game_name):
    """
    Temporary game screen until the real game is added
    """

    back_button = Button("Back to Menu", 320, 450, 250, 70, main)

    running = True

    while running:

        screen.fill(BLUE)

        title = TITLE_FONT.render(game_name, True, WHITE)
        screen.blit(title, (300, 150))

        message = FONT.render("Game Coming Soon!", True, WHITE)
        screen.blit(message, (300, 250))

        back_button.draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_program()

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button.click(event.pos)

        pygame.display.flip()

# GAME FUNCTIONS 
# Poker would be here, but it is not complete. The files exist for future improvement

def launch_pyramid():
    game()

def launch_freecell():
    free_cell_game()

def launch_poker():
    poker_instructions()

def launch_blackjack():
    blackjack_instructions()

#  MAIN MENU 
def main():

    buttons = [
        Button("Pyramid Solitaire", 300, 225, 300, 70, launch_pyramid),
        Button("Freecell", 300, 300, 300, 70, launch_freecell),
        Button("Poker", 300, 375, 300, 70, launch_poker),
        Button("Blackjack", 300, 450, 300, 70, launch_blackjack),
        Button("Quit", 300, 525, 300, 70, lambda: sys.exit())

    ]

    running = True

    while running:

        screen.fill(GREEN)

        title = TITLE_FONT.render("Choose a Game", True, WHITE)
        screen.blit(title, (260, 40))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_program()

            if event.type == pygame.MOUSEBUTTONDOWN:

                for button in buttons:
                    button.click(event.pos)

        for button in buttons:
            button.draw()

        pygame.display.flip()

main()