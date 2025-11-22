import pygame
import math
from random import choice
from game_params import *


# ===========================================================
#                          ENEMY
# ===========================================================

class Enemy(pygame.sprite.Sprite):
    """
    Enemy that moves toward the player using basic homing movement.
    Spawns on the right side of the screen and walks inward.
    """

    def __init__(self, x=WIDTH + 100, y=HEIGHT // 2):
        super().__init__()

        # -----------------------------
        #      LOAD SPRITE
        # -----------------------------
        self.image = self._load_random_sprite()
        self.rect = self.image.get_rect()

        # -----------------------------
        #     POSITION / MOVEMENT
        # -----------------------------
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

        self.speed = 2  # movement speed

    # --------------------------------------------------------
    #               LOAD RANDOM ENEMY SPRITE
    # --------------------------------------------------------
    def _load_random_sprite(self):
        """Loads a random enemy sprite and applies flipping if needed."""
        assets = [
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0000.png',
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0004.png',
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0008.png',
            'assests/rougelike_shooter_pack/PNG/Players/Tiles/tile_0008.png'
        ]

        fp = choice(assets)
        img = pygame.image.load(fp)

        # Flip so enemies face left (toward player)
        img = pygame.transform.flip(img, True, False)

        return img

    # --------------------------------------------------------
    #                       UPDATE
    # --------------------------------------------------------
    def update(self, player):
        """Moves the enemy toward the player's position."""

        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.hypot(dx, dy)

        # Normalize vector
        if distance > 0:
            dx /= distance
            dy /= distance

        # Move enemy
        self.x += dx * self.speed
        self.y += dy * self.speed

        # Update sprite position
        self.rect.center = (self.x, self.y)

    # --------------------------------------------------------
    #                        DRAW
    # --------------------------------------------------------
    def draw(self, screen):
        """Draws the enemy."""
        screen.blit(self.image, self.rect)
