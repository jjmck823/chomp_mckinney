import pygame
from random import randint 
from game_params import *
def make_background():
    #make a tiled background 
    grass_tile_loc = 'assests/background_blocks/tile_0110.png'
    grass_tile = pygame.image.load(grass_tile_loc)

    sand_top_a_loc = 'assests/background_blocks/tile_0056.png'
    sand_top_a= pygame.transform.rotozoom(pygame.image.load(sand_top_a_loc), 0, 5)

    water_title_loc= 'assests/background_blocks/tile_0042.png'
    water_tile = pygame.transform.rotozoom(pygame.image.load(water_title_loc), 0, 5)

    shrubs_loc = "assests/background_blocks/tile_0060.png"
    shrubs = pygame.transform.rotozoom(pygame.image.load(shrubs_loc), 0, 2)

    shrubs_single_loc = "assests/background_blocks/tile_0048.png"
    shrub_single = pygame.transform.rotozoom(pygame.image.load(shrubs_single_loc), 0, 2)

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

    #make some sand 
    #y_sand = HEIGHT - 5 * tile_height
    #for x in range(0, int(WIDTH/2), tile_width):
    #    background.blit(sand_top_a, (x, y_sand))


    #place random shrubs\

    num_shrubs = 8    
    for i in range(num_shrubs):
        x = randint(0,WIDTH)
        y = randint(0,HEIGHT)
        # blit that seaweed
        background.blit(shrubs,(x,y))
    #blit single shrubs 

    num_shrubs_single = 10    
    for i in range(num_shrubs_single):
        x = randint(0,WIDTH)
        y = randint(0,HEIGHT)
        # blit that seaweed
        background.blit(shrub_single,(x,y))


    return background

 
    

