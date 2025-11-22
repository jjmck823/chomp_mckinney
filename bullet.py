import pygame
import math
from random import randint
from game_params import *


class Bullet(pygame.sprite.Sprite):
    """
    Bullet fired by the player that homes toward the selected enemy.
    Hits ANY enemy it touches (not just the target).
    """

    def __init__(self, start_pos, target_enemy, player, enemy_group):
        super().__init__()

        # -----------------------------
        #         POSITION
        # -----------------------------
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.player = player
        self.enemy_group = enemy_group
        self.speed = 5

        # -----------------------------
        #          GRAPHICS
        # -----------------------------
        img = pygame.image.load('assests/rougelike_shooter_pack/PNG/Weapons/Tiles/tile_0023.png')
        self.image = pygame.transform.rotozoom(img, 0, 0.7)
        self.rect = self.image.get_rect(center=start_pos)

        # -----------------------------
        #     MOVEMENT VECTOR
        # -----------------------------
        dx = target_enemy.x - self.x
        dy = target_enemy.y - self.y
        distance = math.hypot(dx, dy)

        if distance == 0:
            distance = 1  # avoid division by zero

        self.vx = (dx / distance) * self.speed
        self.vy = (dy / distance) * self.speed

    # --------------------------------------------------------
    #                      UPDATE
    # --------------------------------------------------------
    def update(self):
        # Move bullet
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (self.x, self.y)

        # OFF SCREEN? Kill it
        if (self.x < 0 or self.x > WIDTH or
            self.y < 0 or self.y > HEIGHT):
            self.kill()
            return

        # Check collision with ANY enemy
        hit_list = pygame.sprite.spritecollide(self, self.enemy_group, False)

        for enemy in hit_list:
            # Score increase
            self.player.score += 10

            # Respawn enemy randomly
            enemy.x = randint(WIDTH, WIDTH + 200)
            enemy.y = randint(0, HEIGHT)
            enemy.rect.center = (enemy.x, enemy.y)

            self.kill()
            break  # bullet destroyed after one hit

    # --------------------------------------------------------
    #                       DRAW
    # --------------------------------------------------------
    def draw(self, screen):
        screen.blit(self.image, self.rect)
