from game_params import *
import pygame
from random import choice, randint
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH+100,y=HEIGHT//2):
        super().__init__()
        self.assets = [
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0000.png',
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0004.png',
            'assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0008.png',
            'assests/rougelike_shooter_pack/PNG/Players/Tiles/tile_0008.png'
        ]
        self.fp = choice(self.assets)
        self.image = pygame.image.load(self.fp)
        self.image = pygame.transform.flip(self.image,1,0)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        # place the center of the rect
        self.rect.center = (self.x,self.y)

        self.speed = 2 # speed

    def update(self, player):
        # move the enemy 
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.hypot(dx, dy) #found hypotenuse func
        
        if distance != 0:
            dx /= distance
            dy /= distance 
        
        self.x += dx * self.speed
        self.y += dy * self.speed
       
        # update the rect
        self.rect.center = (self.x, self.y)
    
    def draw(self, screen):
        # blit our enemy to the screen
        screen.blit(self.image, self.rect)