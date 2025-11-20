#import pygame
#from game_params import *
#from player import *
#from enemy import *

#class  Bullet(pygame.sprite.Sprite):
     #   def __init__(self,coords):
       #     super().__init__()
      #      self.x = coords[0]
          #  self.y= coords[1]
           # self.speed=5
    
            #self.image = pygame.image.load("assests/rougelike_shooter_pack/PNG/Weapons/Tiles/tile_0023.png")
            #self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
            #self.rect = self.image.get_rect()
            #self.rect_center = (coords)
        
        #def update(self):
         #   self.x += 2
            #kill if goes off 
          #  if self.x > WIDTH:
           #     self.kill()
            #update rect
            #self.rect_center = (self.x, self.y)
        
        #def draw(self,screen):
         #   screen.blit(self.image, self.rect)