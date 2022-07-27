import sys

from time import sleep

import pygame

from settings import Settings

from game_stats import Game_Stats

from button import Button

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

        #Create an instance of game stats

        self.stats = Game_Stats(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")


        
        
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _start_game(self):
        """Starts a new game once called"""

        # Reset game statistics
        self.stats.reset_stats()
        self.stats.game_active = True

        #Get rid of any remaining bullets and aliens
        self.aliens.empty()
        self.bullets.empty()

        #Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        #Hide the mouse cursor visibility within the game area
        pygame.mouse.set_visible(False)

    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            

               
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
        elif event.key == pygame.K_p:
            self._start_game()

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
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
         
         #Check for any bullets that have hit aliens
         #If so, get rid of the bullet and alien

        collisions= pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        if not self.aliens:
            #Destroy existing bullets and create a new fleet

            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Update position of aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collision

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
        #Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()


    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""

        if self.stats.ships_left>0:


            #Decrement ships_left
            self.stats.ships_left -=1

            #Get rid of any aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create the new fleet and center the ship

            self._create_fleet()
            self.ship.center_ship()

            #Pause
            sleep(.5)
        else:
            self.stats.game_active= False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat the same as the ship got hit
                self._ship_hit()

    def _create_fleet(self):
        """Create the fleet of aliens"""

        #Create an alien and find the number of aliens in a row
        #Spacing between each alien is equal to one alien width

        
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2* alien_width)
        number_aliens_x = available_space_x // (2* alien_width)

        #Determine the number of rows of aliens that fit on the screen

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height)- ship_height)
        number_rows = available_space_y // (2* alien_height)

        #create full fleet of aliens

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self, alien_number,row_number):
            alien= Alien(self)
            alien_width,alien_height = alien.rect.size
            alien.x = alien_width + 2 *alien_width*alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2*alien.rect.height*row_number
            self.aliens.add(alien)  

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
               
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()


    def run_game(self):
        """Start the main loop of the game"""

        while True:
            # Watch for keyboard and mouse events

            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

            
                      
            



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

