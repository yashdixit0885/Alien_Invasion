
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""

        #Screen settings

        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Ship Settings

        self.ship_limit= 3

        #Bullet Settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien Settings

        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up

        self.speedup_scale = 1.2

        # How quickly the point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings throughout the game"""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        self.alien_points = 10

        

    def increase_speed(self):
        """Increase speed settings and alien point values"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        


