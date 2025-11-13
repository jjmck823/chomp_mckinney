# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from game_params import *
from game_background import *
from player import Player 
from text import Zombie_Text
from enemy import Enemy

# pygame setup
pygame.init()
#make width and height 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#make a background 
background = make_background()


#make enemies 
enemy_list = []
for i in range(20):
    # make a new fish and append
    enemy_list.append(Enemy(randint(WIDTH,WIDTH+200), randint(0,HEIGHT)))

player = Player(enemy_list)

#make title 
title = Zombie_Text()





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #player event and update
        player.check_event(event) 
    #update things
    player.update()
    for f in enemy_list:
        f.update()
  


    # flip() the display to put your work on screen
    screen.blit(background, (0,0))
    player.draw(screen)
    for f in enemy_list:
        f.draw(screen)

    #draw title and score 
    title.update()
    title.update_score(player.score)
    title.draw(screen)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()