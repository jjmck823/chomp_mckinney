# Example file showing a basic pygame "game loop"
import pygame
from random import randint
# pygame setup
pygame.init()
#make width and height 
WIDTH= 1000
HEIGHT= 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


#make a tiled background 
water_tile_loc = 'assests/images/background_terrain.png'
water_tile = pygame.image.load(water_tile_loc)

sand_top_a_loc = 'assests/images/terrain_sand_top_a.png'
sand_top_a= pygame.image.load(sand_top_a_loc)

seaweed_a_loc= 'assests\images\seaweed_green_a_outline.png'
seaweed_tile = pygame.image.load(seaweed_a_loc)

#get tile width and height 
tile_width = water_tile.get_width()
tile_height = water_tile.get_height()
#make a new surface - background with the same width as screen
background = pygame.Surface((WIDTH, HEIGHT))

#loop over background and place tiles 
for x in range(0,WIDTH,tile_width):
    background.blit(water_tile, (x,0))
    for y in range(0,HEIGHT,tile_height):
        background.blit(water_tile, (x,y))

#make a row of sand 
y_sand = HEIGHT - tile_height
for x in range(0,WIDTH, tile_width):
    background.blit(sand_top_a, (x, y_sand))

#randomly place seaweed 
num_seaweed= 4
for i in range(num_seaweed):
    x = randint(0,WIDTH)
    y =  HEIGHT-tile_height
    background.blit(seaweed_tile, (x,y))




#blit to the screen
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