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

    #make a row of sand 
    y_sand = HEIGHT - 5 * tile_height
    for x in range(0, int(WIDTH/2), tile_width):
        background.blit(sand_top_a, (x, y_sand))

    #make water in top left 
    x_water = randint(0,WIDTH)
    Y_water= randint(0,HEIGHT)
    for y in range(0,WIDTH, tile_width):
        background.blit(water_tile, (x_water,Y_water))
    return background
