import pygame
from game_params import WIDTH, HEIGHT

class ZombieText:
    """
    Handles title, score, and game over display with fade effects.
    """
    def __init__(self):
        self.black = (0, 0, 0)

        # Fonts
        self.title_font = pygame.font.Font(
            'assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 150
        )
        self.score_font = pygame.font.Font(
            'assests/Fonts/pickyside-font/PickysideRegular-vn7w4.otf', 60
        )

        # Title surfaces
        self.title_surface = self.title_font.render("SURVIVE", True, self.black)
        self.title_rect = self.title_surface.get_rect(center=(WIDTH // 2, HEIGHT * 0.3))

        # Game over surfaces
        self.game_over_surface = self.title_font.render("GAME OVER", True, self.black)
        self.game_over_rect = self.game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT * 0.3))

        # Score
        self.score_surface = self.score_font.render("0", True, self.black)

        # Fade effect
        self.birth_time = pygame.time.get_ticks()
        self.fade_duration = 2000  # milliseconds

    # ---------------------------
    # Score update
    # ---------------------------
    def update_score(self, score):
        self.score_surface = self.score_font.render(str(score), True, self.black)

    # ---------------------------
    # Title fade effect
    # ---------------------------
    def update(self):
        elapsed = pygame.time.get_ticks() - self.birth_time
        alpha_percent = min(elapsed / self.fade_duration, 1)
        self.title_surface.set_alpha(255 - int(alpha_percent * 255))

    # ---------------------------
    # Draw gameplay UI
    # ---------------------------
    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.score_surface, (20, 20))

    # ---------------------------
    # Draw game over screen
    # ---------------------------
    def draw_game_over(self, screen, score):
        screen.fill((255, 255, 255))
        screen.blit(self.game_over_surface, self.game_over_rect)

        score_surface = self.score_font.render(f"Your Score: {score}", True, self.black)
        score_rect = score_surface.get_rect(center=(WIDTH // 2, HEIGHT - 200))
        screen.blit(score_surface, score_rect)

        restart_surface = self.score_font.render("Press R to Restart", True, self.black)
        restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        screen.blit(restart_surface, restart_rect)

    # ---------------------------
    # Reset fade effect
    # ---------------------------
    def reset_fade(self):
        self.birth_time = pygame.time.get_ticks()
