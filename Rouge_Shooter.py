import pygame
from random import randint, choice
from game_params import *
from game_background import make_background
from player import Player
from text import ZombieText
from enemy import Enemy

# ------------------------------
# INITIALIZATION
# ------------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# ------------------------------
# HELPER FUNCTIONS
# ------------------------------

def spawn_enemy_edge():
    """
    Spawn an enemy from a random edge: right, top, or bottom.
    Returns an Enemy object.
    """
    edge = choice(["right", "top", "bottom"])
    if edge == "right":
        x = WIDTH + 50
        y = randint(0, HEIGHT)
    elif edge == "top":
        x = randint(0, WIDTH)
        y = -50
    else:  # bottom
        x = randint(0, WIDTH)
        y = HEIGHT + 50
    return Enemy(x, y)

def create_enemies(amount):
    """
    Create a sprite group of enemies spawning from random edges.
    """
    group = pygame.sprite.Group()
    for _ in range(amount):
        group.add(spawn_enemy_edge())
    return group

def reset_game():
    """
    Resets all game state including player, enemies, score thresholds, etc.
    """
    global player, enemy_group, game_over, score_threshold, enemies_to_add

    enemy_group = create_enemies(20)
    player = Player(enemy_group)

    score_threshold = 50
    enemies_to_add = 5
    game_over = False

# ------------------------------
# INITIAL GAME SETUP
# ------------------------------
background = make_background()
title = ZombieText()

enemy_group = create_enemies(20)
player = Player(enemy_group)

# Difficulty scaling
score_threshold = 50
enemies_to_add = 5
game_over = False

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

    # --------------------------
    # GAME UPDATE
    # --------------------------
    if not game_over:
        enemy_group.update(player)
        player.update()

        # Difficulty scaling based on score
        if player.score >= score_threshold:
            for _ in range(enemies_to_add):
                enemy_group.add(spawn_enemy_edge())
            score_threshold += 50
            enemies_to_add += 1

        # Check player death
        if not player.live:
            game_over = True

        # --------------------------
        # DRAW GAMEPLAY SCREEN
        # --------------------------
        screen.blit(background, (0, 0))
        player.draw(screen)
        enemy_group.draw(screen)

        title.update()
        title.update_score(player.score)
        title.draw(screen)

    else:
        # --------------------------
        # GAME OVER SCREEN
        # --------------------------
        title.draw_game_over(screen, player.score)

    # --------------------------
    # DISPLAY UPDATE
    # --------------------------
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
