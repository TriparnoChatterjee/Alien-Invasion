class Settings:
    """A class to store all the settings foe Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = "images/background_image.jpg"
        self.ship_speed = 2.5

        # Bullet Settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right
        # fleet_direction of -1 represents left
        self.fleet_direction = 1

        # Ship Settings
        self.ship_limit = 2

        # How quickly the game speeds up
        self.speed_up_scale = 1.5
        self.initialize_dynamic_settings()

        # How quickly the aline point value increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change through out the game """
        self.ship_speed = 2.5
        self.bullet_speed = 2
        self.alien_speed = 1.0

        # fleet direction of 1 represents right ; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.alien_points *= self.speed_up_scale

    def start_as_intermediate_voyager(self):
        """Start as intermediate"""
        self.ship_speed = 3
        self.bullet_speed = 3
        self.alien_speed = 3
        self.ship_limit = 1

    def start_as_expert_voyager(self):
        """Start as expert"""
        self.ship_speed = 4
        self.bullet_speed = 4
        self.alien_speed = 4
        self.ship_limit = 0
