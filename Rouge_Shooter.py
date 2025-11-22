import pygame
from random import randint
from game_params import *
from game_background import *
from player import Player 
from text import Zombie_Text
from enemy import Enemy

# pygame setup
pygame.init()
#make width and height 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#make a background 
background = make_background()

#make reset function 
def reset_game():
    global player, enemy_group, game_over, score_thres, enemy_increase
    #resets all assests
    enemy_group = pygame.sprite.Group()
    for i in range(20):
        enemy_group.add(Enemy(randint(WIDTH,WIDTH+200), randint(0,HEIGHT)))
    player = Player(enemy_group)
    score_thres = 50 #when reaches 50 
    enemy_increase = 5 
    game_over = False
#make enemies 
enemy_group = pygame.sprite.Group()
for i in range(20):
    # make a new enemy and append
    enemy_group.add(Enemy(randint(WIDTH,WIDTH+200), randint(0,HEIGHT)))

player = Player(enemy_group)

#make title 
title = Zombie_Text()

game_over = False

score_thres = 50 #when reaches 50 
enemy_increase = 5 

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #player event and update 
        if not game_over:
            player.check_event(event) 
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
    #update things
    if not game_over:
        enemy_group.update(player)
        if player.score >= score_thres:
            for x in range(enemy_increase):
                enemy_group.add(Enemy(randint(WIDTH, WIDTH + 200), randint(0, HEIGHT)))
            score_thres += 50
            enemy_increase += 1
    # flip() the display to put your work on screen
        screen.blit(background, (0,0))
        player.draw(screen)
        enemy_group.draw(screen)
        player.update()
    #draw title and score 
        title.update()
        title.update_score(player.score, screen)
        title.draw(screen)

        if not player.live:
            game_over= True
    else: 
        #game over screen
        screen.fill((255,255,255))
        screen.blit(player.game_over, player.game_over_rect)
        font = player.score_font
        score_text = font.render(f"Your Score: {player.score}", True, (0, 0, 0))
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT - 200))
        screen.blit(score_text, score_rect)
        restart = font.render('Press R to Restart', 1, (0,0,0))
        restart_rect = restart.get_rect(center=(WIDTH//2, HEIGHT - 100))
        screen.blit(restart, restart_rect)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()