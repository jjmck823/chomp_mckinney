import pygame
from random import randint
from game_params import *


# ---------------------------------------------
#   LOAD ALL BACKGROUND ASSETS ONCE
# ---------------------------------------------
def load_background_assets():
    """Load and return all tile images for the background."""

    assets = {
        "grass": pygame.image.load(
            'assests/rougelike_shooter_pack/PNG/Tiles/Tiles/tile_0024.png'
        ),

        "shrubs": pygame.transform.rotozoom(
            pygame.image.load('assests/rougelike_shooter_pack/PNG/Tiles/Tiles/tile_0044.png'),
            0, 1
        ),

        "shrub_single": pygame.transform.rotozoom(
            pygame.image.load('assests/rougelike_shooter_pack/PNG/Tiles/Tiles/tile_0062.png'),
            0, 1
        ),
    }

    return assets


# ---------------------------------------------
#   GENERATE BACKGROUND SURFACE
# ---------------------------------------------
def make_background():
    """Builds and returns the full background surface."""

    assets = load_background_assets()
    grass_tile = assets["grass"]
    shrubs = assets["shrubs"]
    shrub_single = assets["shrub_single"]

    tile_w, tile_h = grass_tile.get_width(), grass_tile.get_height()

    # Create full-screen background surface
    background = pygame.Surface((WIDTH, HEIGHT))

    # -----------------------------------------
    #  TILE THE GRASS (fixed tiling loop)
    # -----------------------------------------
    for x in range(0, WIDTH, tile_w):
        for y in range(0, HEIGHT, tile_h):
            background.blit(grass_tile, (x, y))

    # -----------------------------------------
    #  PLACE RANDOM SHRUBS
    # -----------------------------------------
    for _ in range(20):  # shrubs
        x, y = randint(0, WIDTH), randint(0, HEIGHT)
        background.blit(shrubs, (x, y))

    for _ in range(15):  # small shrubs
        x, y = randint(0, WIDTH), randint(0, HEIGHT)
        background.blit(shrub_single, (x, y))

    return background
