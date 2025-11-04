# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from game_params import *
from game_background import *
from player import Player 

# pygame setup
pygame.init()
#make width and height 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#make a background 
background = make_background()

#make player 
player = Player()



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #player event and update
        player.check_event(event) 
    player.update()
   
   
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    screen.blit(background, (0,0))
    player.draw(screen)
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()