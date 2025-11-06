import pygame
from random import randint 
from game_params import *
def make_background():
    #make a tiled background 
    grass_tile_loc = 'assests/rougelike_shooter_pack/PNG/Tiles/Tiles/tile_0024.png'
    grass_tile = pygame.image.load(grass_tile_loc)

    shrubs_loc = "assests/rougelike_shooter_pack/PNG/Tiles/Tiles/tile_0044.png"
    shrubs = pygame.transform.rotozoom(pygame.image.load(shrubs_loc), 0, 1)

    shrubs_single_loc = "assests/rougelike_shooter_pack/PNG/Tiles/Tiles/tile_0062.png"
    shrub_single = pygame.transform.rotozoom(pygame.image.load(shrubs_single_loc), 0, 1)

    #get tile width and height 
    tile_width = grass_tile.get_width()
    tile_height = grass_tile.get_height()
    #make a new surface - background with the same width as screen
    background = pygame.Surface((WIDTH, HEIGHT))

    #loop over background and place tiles 
    for x in range(0,WIDTH,tile_width):
        background.blit(grass_tile, (x,0))
        for y in range(0,HEIGHT,tile_height):
            background.blit(grass_tile, (x,y))



    #place random shrubs\

    num_shrubs = 20    
    for i in range(num_shrubs):
        x = randint(0,WIDTH)
        y = randint(0,HEIGHT)
        # blit that seaweed
        background.blit(shrubs,(x,y))
    #blit single shrubs 

    num_shrubs_single = 15    
    for i in range(num_shrubs_single):
        x = randint(0,WIDTH)
        y = randint(0,HEIGHT)
        # blit that seaweed
        background.blit(shrub_single,(x,y))


    return background

 
    

