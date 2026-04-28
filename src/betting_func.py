#Es betting fuction 
import pygame

pygame.init()


#set up screen, clock and font
screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0]) #sets screen size to whatever the first monitor's dimension

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

#make a money saved dictionary to put how much they have won 
user_money = {}
#make a dictionary called money to safe how much they want to bet 
betting_money = {}


player = "Player1"


#had to add the cursor beucase it was confusing without it 
cursor_visible = True
cursor_timer = 0

# make a function for the beginning bets
def starting_bet(player):
#BTW this is not in my spedocode so I know what is what, and a lot i used videos so im not 100% what does what, but have a very good imaje of the structure
    typed_text = ""
    state = "typing"
    running = True

    global cursor_visible, cursor_timer
    #main loop 
    while running:
        clock.tick(60)
        screen.fill((255, 255, 255))
    
        #cursor blink
        cursor_timer += 1
        # blink speed
        if cursor_timer % 30 == 0: 
            cursor_visible = not cursor_visible
        #checks whats going on on the screen 
        for event in pygame.event.get():

            #teh X at the screen cornert 
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                #typing numbers
                if state == "typing":
                    #checking if its digit
                    if event.unicode.isdigit():
                        typed_text += event.unicode

                    elif event.key == pygame.K_BACKSPACE:
                        typed_text = typed_text[:-1]

                    elif event.key == pygame.K_RETURN:

                        #max of 100 doolars betting 
                        if typed_text != "" and int(typed_text) <= 100:
                            money = typed_text
                            state = "confirm"
                            typed_text = ""

                if state == "confirm":
                    if event.key == pygame.K_y:
                        betting_money[player] = int(money)
                        running = False

                    elif event.key == pygame.K_n:
                        return starting_bet(player)

        #ask user what their starting amount for betting is 
        if state == "typing":

            text1 = font.render("Enter bet (max $100):", True, (0, 0, 0))

            # cursor effect
            display_text = typed_text
            if cursor_visible:
                display_text += "|"

            #typing font and making sure its tru 
            text2 = font.render(display_text, True, (0, 0, 0))
            screen.blit(text1, (200, 200))
            screen.blit(text2, (200, 300))


        #ask to make sure if that is the amount they want
        elif state == "confirm":

            # cursor effect
            display_text = typed_text
            if cursor_visible:
                display_text += "|"

            text1 = font.render(f"Confirm bet: ${money}", True, (0, 0, 0))
            text2 = font.render("Press Y = Yes / N = No", True, (0, 0, 0))
            #the text font for that one 
            screen.blit(text1, (200, 200))
            screen.blit(text2, (200, 300))
        #keep updating the display 
        pygame.display.update()

        #confirm input
        #also ngl i still need to make sure how this works
        #for event in pygame.event.get():
        #    if event.type == pygame.KEYDOWN and state == "confirm":
        #        #if yes then safe that amount of money in the dictionary called money 
        #        if event.key == pygame.K_y:
        #            betting_money[player] = int(typed_text)
        #            running = False
        #        #elif no then just send them back to the beggining of the funtion using return 
        #        elif event.key == pygame.K_n:
        #            return starting_bet(player)


#running the thing 
starting_bet(player)
#quiting the game 
pygame.quit()


print(betting_money)

#make a FUNCTION for loose, take the amount of money safed in the dictionary and take it
    #safe the money amount in the "money saved" dictionary and call the lizzie funtion 


#make a FUNTION for win,take the amount of money in the "money" dictionary and double it 
    #safe the money amount in the "money saved" dictionary and call the lizzie funtion 


#make a FUNTIOM if its a tie then just return the amount of the money back to their accound and call the lizze funtio to money is up to date