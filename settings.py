
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""

        #Screen settings

        self.screen_width = 550
        self.screen_height = 420
        self.bg_color = (255,255,255)

        #Ship Settings

        self.ship_speed = 1.5

        #Bullet Settings

        self.bullet_speed= 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
