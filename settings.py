
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""

        #Screen settings

        self.screen_width = 900
        self.screen_height = 900
        self.bg_color = (255,255,255)

        #Ship Settings

        self.ship_speed = 1.5

        #Bullet Settings

        self.bullet_speed= 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        # Alien Settings

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        

