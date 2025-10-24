# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from game_params import *
from game_background import *

# pygame setup
pygame.init()
#make width and height 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#make a background 
background = make_background()

screen.blit(background, (0,0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()