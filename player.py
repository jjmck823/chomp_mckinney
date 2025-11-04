import pygame
from game_params import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x=WIDTH*0.1, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.image = pygame.image.load('assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0012.png')
        # make player sprite and changr size 
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # get rect
        self.rect.center = (self.x, self.y)
    
    def check_event(self, event):
        # check key event 
        if event.type == pygame.KEYDOWN:
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.vy += -2
                # player goes up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # player goes down
                self.vy  += 2
            if event.key == pygame.K_d:
                #player goes right 
                self.vx += 2
            if event.key == pygame.K_a:
                #player goes right 
                self.vx += -2
            
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    

    


