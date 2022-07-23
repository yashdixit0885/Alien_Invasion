import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Set background color -- initializes the background color in bg_color variable
        
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
               
    def _check_keydown_events(self,event):
        # Respond to key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        #Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets)< self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()

            # Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
         # print(len(self.bullets))


    def _create_fleet(self):
        """Create the fleet of aliens"""

        #Create an alien and find the number of aliens in a row
        #Spacing between each alien is equal to one alien width

        
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2* alien_width)
        number_aliens_x = available_space_x // (2* alien_width)

        #create first row of aliens

        for alien_number in range(number_aliens_x):
            alien= Alien(self)
            alien.x = alien_width + 2 *alien_width*alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

       




    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


    def run_game(self):
        """Start the main loop of the game"""

        while True:
            # Watch for keyboard and mouse events

            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
                      
            



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

