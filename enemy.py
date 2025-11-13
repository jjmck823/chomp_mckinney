from game_params import *
import pygame
from random import choice

class Enemy():
    def __init__(self,x=WIDTH+100,y=HEIGHT//2):
        self.assets = [
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0000.png',
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0004.png',
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0008.png',
            'assests/rougelike_shooter_pack/PNG/Players/Tiles/tile_0008.png'
        ]
        self.fp = choice(self.assets)
        self.image = pygame.image.load(self.fp)
         # flip 
        self.image = pygame.transform.flip(self.image,1,0)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # place the center of the rect
        self.rect.center = (x,y)
        self.vx = -2 # x velo enemy

    def update(self):
        # move the enemy 
        self.x += self.vx
        # update the rect
        self.rect.center = (self.x, self.y)
    
    def draw(self, screen):
        # blit our enemy to the screen
        screen.blit(self.image, self.rect)