class GameStats:
    """Track Statistics for alien invasion"""

    def __init__(self, ai_game):
        """Initialize Statistics"""

        # Start game in an inactive state
        self.game_active = False
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change through game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
