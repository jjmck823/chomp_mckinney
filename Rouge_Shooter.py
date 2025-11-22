import pygame
from random import randint
from game_params import *
from game_background import make_background
from player import Player
from text import Zombie_Text
from enemy import Enemy
#------------------------------
#  INIT
#------------------------------

pygame.init()

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ------------------------------
# HELPER FUNCTIONS
# ------------------------------

def create_enemies(amount):
    """Create a new enemy group with a set number of enemies."""
    group = pygame.sprite.Group()
    for _ in range(amount):
        x = randint(WIDTH, WIDTH + 200)
        y = randint(0, HEIGHT)
        group.add(Enemy(x, y))
    return group


def reset_game():
    """Fully resets the game state."""
    global player, enemy_group, game_over, score_threshold, enemies_to_add

    enemy_group = create_enemies(20)
    player = Player(enemy_group)

    score_threshold = 50      # Score required for next difficulty increase
    enemies_to_add = 5        # Number of new enemies added each step
    game_over = False


# ------------------------------
# INITIAL GAME SETUP
# ------------------------------

background = make_background()
title = Zombie_Text()

enemy_group = create_enemies(20)
player = Player(enemy_group)

# Difficulty settings
score_threshold = 50
enemies_to_add = 5

game_over = False
running = True


# ------------------------------
# GAME LOOP
# ------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            player.check_event(event)

        else:
            # Press R to restart after death
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

    # --------------------------
    # UPDATE GAME
    # --------------------------
    if not game_over:

        # Update enemies and player
        enemy_group.update(player)
        player.update()

        # Difficulty scaling
        if player.score >= score_threshold:
            # Add new enemies
            for _ in range(enemies_to_add):
                enemy_group.add(Enemy(randint(WIDTH, WIDTH + 200), randint(0, HEIGHT)))

            score_threshold += 50        # Next target
            enemies_to_add += 1          # Increase difficulty slowly

        # Death check
        if not player.live:
            game_over = True

        # --------------------------
        # DRAW GAMEPLAY SCREEN
        # --------------------------
        screen.blit(background, (0, 0))
        player.draw(screen)
        enemy_group.draw(screen)

        title.update()
        title.update_score(player.score, screen)
        title.draw(screen)

    else:
        # --------------------------
        # GAME OVER SCREEN
        # --------------------------
        screen.fill((255, 255, 255))

        # Headline text
        screen.blit(player.game_over, player.game_over_rect)

        font = player.score_font
        # Score Text
        score_text = font.render(f"Your Score: {player.score}", True, (0, 0, 0))
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT - 200))
        screen.blit(score_text, score_rect)
        # Reset Text  
        restart_text = font.render("Press R to Restart", True, (0, 0, 0))
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        screen.blit(restart_text, restart_rect)

    # --------------------------
    # DISPLAY UPDATE
    # --------------------------
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
