import pygame
from random import randint
from game_params import *
import math
from bullet import Bullet


# ===========================================================
#                         PLAYER CLASS
# ===========================================================

class Player(pygame.sprite.Sprite):
    """
    Handles player movement, shooting, and collision.
    """

    def __init__(self, enemy_group, x=WIDTH * 0.2, y=HEIGHT // 2):
        super().__init__()

        # -----------------------------
        #   MOVEMENT
        # -----------------------------
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.accel = 0.5
        self.friction = 0.9

        # -----------------------------
        #   GAME STATE
        # -----------------------------
        self.live = True
        self.score = 0
        self.enemy_group = enemy_group
        self.bullet_group = pygame.sprite.Group()

        # -----------------------------
        #   ALL ASSETS
        # -----------------------------
        self.image = pygame.image.load(
            "assests/rougelike_shooter_pack/PNG/Enemies/Tiles/tile_0012.png"
        )
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect()

        # Sounds
        self.shoot_sound = pygame.mixer.Sound(
            "assests/rougelike_shooter_pack/Sounds/shoot-d.ogg"
        )
        self.death_sound = pygame.mixer.Sound(
            "assests/rougelike_shooter_pack/Sounds/lose-a.ogg"
        )

        # Fonts / Game Over
        self._load_game_over_text()

    # ----------------------------------------------------
    #   LOAD GAME OVER TEXT
    # ----------------------------------------------------
    def _load_game_over_text(self):
        """Loads and prepares Game Over text objects."""
        black = (0, 0, 0)
        self.title_font = pygame.font.Font(
            "assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf", 150
        )
        self.score_font = pygame.font.Font(
            "assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf", 70
        )

        self.game_over = self.title_font.render("GAME OVER", True, black)
        self.game_over_rect = self.game_over.get_rect(center=(WIDTH // 2, HEIGHT * 0.3))

    # ----------------------------------------------------
    #   MOVEMENT / BOUNDARIES / UPDATES
    # ----------------------------------------------------
    def update(self):
        """Updates player movement, boundaries, bullets, and collision."""
        self.movement()
        self.apply_boundaries()

        # Update position
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (self.x, self.y)

        # Update bullets
        self.bullet_group.update()

        # Collision with enemies
        if pygame.sprite.spritecollide(self, self.enemy_group, False):
            self.live = False
            self.death_sound.play()

    def movement(self):
        """Processes input (WASD) and applies acceleration & friction."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vx -= self.accel
        if keys[pygame.K_d]:
            self.vx += self.accel
        if keys[pygame.K_w]:
            self.vy -= self.accel
        if keys[pygame.K_s]:
            self.vy += self.accel

        # Apply friction
        self.vx *= self.friction
        self.vy *= self.friction

    def apply_boundaries(self):
        """Prevents the player from leaving the screen."""
        half_w = self.rect.width // 2
        half_h = self.rect.height // 2

        self.x = max(half_w, min(WIDTH - half_w, self.x))
        self.y = max(half_h, min(HEIGHT - half_h, self.y))

    # ----------------------------------------------------
    #                     SHOOTING
    # ----------------------------------------------------
    def shoot(self):
        """Shoots toward the closest enemy."""
        if not self.enemy_group:
            return

        # Get closest enemy
        closest_enemy = min(
            self.enemy_group,
            key=lambda e: math.hypot(e.x - self.x, e.y - self.y)
        )

        # Create bullet
        bullet = Bullet(self.rect.center, closest_enemy, self, self.enemy_group)
        self.bullet_group.add(bullet)

        # Play sound
        self.shoot_sound.play()

    def check_event(self, event):
        """Handles shoot key input."""
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.shoot()

    # ----------------------------------------------------
    #                        DRAW
    # ----------------------------------------------------
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullet_group.draw(screen)

        # bullets have custom draw (rotated or special)
        for bullet in self.bullet_group:
            bullet.draw(screen)
