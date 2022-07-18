import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #Set background color -- initializes the background color in bg_color variable
        self.bg_color= (230,230,230)

    def run_game(self):
        """Start the main loop of the game"""

        while True:
            # Watch for keyboard and mouse events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.bg_color) # uses the screen object that contains the pygame display 
                # class to call the fill method to background fill
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

