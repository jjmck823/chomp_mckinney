import pygame
from game_params import *

class Zombie_Text():
    def __init__(self):
        # load up a font
        self.title_font = pygame.font.Font('assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 150)

        self.black = (0, 0, 0)
        self.title_surface = self.title_font.render('SURVIVE', 1, self.black)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (WIDTH//2, HEIGHT*0.3)
        self.birth_time = pygame.time.get_ticks()
        self.death_time = 2000

        # make a score font / surface
        self.score_font = pygame.font.Font('assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 60)
        self.score_surface = self.score_font.render('0',1,self.black)

    def update_score(self, score):
        self.score_surface = self.score_font.render(f"{score}",1,self.black)

    def update(self):
        # make it fade
        current_age = pygame.time.get_ticks() - self.birth_time
        current_age_percent = current_age/self.death_time
        self.title_surface.set_alpha(255 - current_age_percent * 255)


    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.score_surface, (20,20))