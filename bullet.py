import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullet fired from Ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        res = tuple(map(sum, zip(ai_game.ship.rect.midtop, (10, 0))))
        self.rect.midtop = res
        # ai_game.ship.rect.midtop

        # Store the bullets position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect, 3)
