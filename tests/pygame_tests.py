# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1440, 1100))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
velocity_y = 5000
velocity_x = 5000
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("tan")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    
    #bouncing logic

    if player_pos.y <= 0:
        player_pos.y = 0
        velocity_y *= -1

    if player_pos.y >= 1100:
        player_pos.y -= velocity_y * dt
        velocity_y *= -1
    
    if player_pos.x <= 0:
        player_pos.x = 0
        velocity_x *= -1
    
    if player_pos.x >= 1440:
        player_pos.x -= velocity_x * dt
        velocity_x *= -1
    
    else:
        player_pos.x += velocity_x * dt
        player_pos.y += velocity_y * dt



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()