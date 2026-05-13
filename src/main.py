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
pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

FONT = pygame.font.SysFont(None, 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (70, 70, 70)
GREEN = (0, 120, 0)

class Button:
    def __init__(self, text, x, y, w, h, action):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        label = FONT.render(self.text, True, WHITE)
        screen.blit(label, (self.rect.x + 20, self.rect.y + 15))

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()


def launch_solitaire():
    pygame.quit()
    print("Freecell not ready yet")
    sys.exit()


# Need to add buttons for poker, and blackjack
def launch_pyramid():
    pygame.quit()
    print("Freecell not ready yet")
    sys.exit()

def launch_freecell():
    pygame.quit()
    print("Freecell not ready yet")
    sys.exit()


def main():
    buttons = [
        Button("Solitaire", 300, 150, 300, 70, launch_solitaire),
        Button("Pyramid Solitaire", 300, 250, 300, 70, launch_pyramid),
        Button("Freecell", 300, 350, 300, 70, launch_freecell),
        Button("Quit", 300, 450, 300, 70, lambda: sys.exit())

    ]

    running = True

    while running:
        screen.fill(GREEN)

        title = FONT.render("Choose a Game", True, WHITE)
        screen.blit(title, (330, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    b.click(event.pos)

        for b in buttons:
            b.draw()

        pygame.display.flip()


main()