import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("arial", 30)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        # score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str, True, self.text_color, (
            255, 255, 0))

        # Display the score at the top right corner
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score  and level to the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):

        """Turn High Score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        # score_str = str(self.stats.score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, (
            255, 255, 0))

        # Display the score at the top right corner
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see i there is a new high score """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn Level  into a rendered image"""

        level_str = str(self.stats.level)
        # score_str = str(self.stats.score)
        self.level_img = self.font.render(level_str, True, self.text_color, (
            255, 255, 0))

        # Display the score at the top right corner
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are lift"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.image.load("images/ship.bmp").convert_alpha()
            ship.image =  pygame.transform.scale(ship.image, (60, 40))
            ship.rect = ship.image.get_rect()

            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10

            self.ships.add(ship)
