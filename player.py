import pygame
from game_params import *
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, enemy_group, x=WIDTH/2, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.live = True
        self.vx = 0
        self.vy = 0
        self.black = (0,0,0)
        self.title_font = pygame.font.Font('assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 150)
        self.score_font = pygame.font.Font('assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 70)
        self.game_over= self.title_font.render('GAME OVER', 1, self.black)
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = (WIDTH//2, HEIGHT*0.3)
        self.image = pygame.image.load('assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0012.png')
        # make player sprite and change size 
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect()
        self.score=0
        self.enemy_group = enemy_group
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.bullet_group.update()
        # get rect
        self.rect.center = (self.x, self.y)
        colliding_kill = pygame.sprite.spritecollide(self,self.enemy_group,0)
        if colliding_kill:
            self.live = False
            print('you got hit') 
       
            
    
        
    def shoot(self):
        #create new bullet 
        new_bullet = Bullet(self.rect.center, self.enemy_group, self)
        self.bullet_group.add(new_bullet)
                

    def check_event(self, event):
        # check key event 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.vy += -0.5
                # player goes up
            if event.key == pygame.K_s:
                # player goes down
                self.vy  += 0.5
            if event.key == pygame.K_d:
                #player goes right 
                self.vx += 0.5
            if event.key == pygame.K_a:
                #player goes right 
                self.vx += -0.5
            if event.key == pygame.K_SPACE:
                print('shoot')
                self.shoot()

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullet_group.draw(screen)
        for b in self.bullet_group:
            b.draw(screen)
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords, enemy_group, player):
        super().__init__()
        self.x= coords[0]
        self.y=coords[1]
        self.speed = 5
        self.score = 0
        self.bull_image = pygame.image.load('assests/rougelike_shooter_pack/PNG/Weapons/Tiles/tile_0023.png')
        self.bull_image = pygame.transform.rotozoom(self.bull_image, 0, 0.7)
        self.image = self.bull_image
        self.rect = self.image.get_rect()
        self.enemy_group = enemy_group
        self.player = player
        self.rect.center = (coords)
    
    def update(self):
        #make it move 
        self.x += self.speed
        #kill if off screen
        if self.x > WIDTH:
            self.kill()
        #update rect 
        self.rect.center = (self.x, self.y)
        colliding_enemy = pygame.sprite.spritecollide(self,self.enemy_group,0)
        # check and see if a collision occured
        if colliding_enemy:
            self.player.score +=10
            # move the collided enemy to the right of the screen
            for f in colliding_enemy:
                f.x = randint(WIDTH, WIDTH+200)
                f.y = randint(0,HEIGHT)
    
    def draw(self, screen):
        self.rect = self.image.get_rect(center = self.rect.center)
        screen.blit(self.image, self.rect)


