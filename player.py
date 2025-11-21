import pygame
from game_params import *
from random import randint
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, enemy_group, x=WIDTH/2, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.live = True
        self.vx = 0
        self.vy = 0
        self.accel = 0.1
        self.black = (0,0,0)
        self.score=0
        self.enemy_group = enemy_group
        self.bullet_group = pygame.sprite.Group()

        self.title_font = pygame.font.Font('assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 150)
        self.score_font = pygame.font.Font('assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 70)
        self.game_over= self.title_font.render('GAME OVER', 1, self.black)
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = (WIDTH//2, HEIGHT*0.3)
        self.image = pygame.image.load('assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0012.png')
        # make player sprite and change size 
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vx -= self.accel
        if keys[pygame.K_d]:
            self.vx += self.accel
        if keys[pygame.K_w]:
            self.vy -= self.accel
        if keys[pygame.K_s]:
            self.vy += self.accel
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (self.x, self.y)
        self.bullet_group.update()

        colliding_kill = pygame.sprite.spritecollide(self,self.enemy_group,0)
        if colliding_kill:
            self.live = False
            print('you got hit') 
       
            
    
        
    def shoot(self):
        #create new bullet 
        closest_enemy = min(self.enemy_group, key=lambda e: math.hypot(e.x - self.x, e.y - self.y))
        new_bullet = Bullet(self.rect.center, closest_enemy, self)
        self.bullet_group.add(new_bullet)
                

    def check_event(self, event):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print('shoot')
                self.shoot()

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullet_group.draw(screen)
        for b in self.bullet_group:
            b.draw(screen)
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords, enemy, player):
        super().__init__()
        self.x= coords[0]
        self.y=coords[1]
        self.speed = 5
        self.score = 0
        self.enemy = enemy
        self.player = player

        self.bull_image = pygame.image.load('assests/rougelike_shooter_pack/PNG/Weapons/Tiles/tile_0023.png')
        self.bull_image = pygame.transform.rotozoom(self.bull_image, 0, 0.7)
        self.image = self.bull_image
        self.rect = self.image.get_rect()
        self.rect.center = (coords)

        dx = self.enemy.x - self.x 
        dy= self.enemy.y - self.y 
        distance= math.hypot(dx, dy)
        if distance == 0:
            distance = 1
        self.vx = dx/distance *self.speed
        self.vy = dy/distance * self.speed
    
    def update(self):
        #make it move 
        self.x += self.vx
        self.y += self.vy
        #kill if off screen
        if self.x > WIDTH:
            self.kill()
        #update rect 
        self.rect.center = (self.x, self.y)
        if self.rect.colliderect(self.enemy.rect):
            self.player.score +=10
            # move the collided enemy to the right of the screen
            self.enemy.x = randint(WIDTH, WIDTH+200)
            self.enemy.y = randint(0,HEIGHT)
            self.enemy.rect.center = (self.enemy.x, self.enemy.y)
            self.kill()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)


