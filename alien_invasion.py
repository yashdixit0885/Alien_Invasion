import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #Set background color -- initializes the background color in bg_color variable
        
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


    def run_game(self):
        """Start the main loop of the game"""

        while True:
            # Watch for keyboard and mouse events

            self._check_events()
            self.ship.update()
            self._update_screen()
                      
            



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

