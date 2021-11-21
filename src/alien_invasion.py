import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ manage resoure and action """

    def __init__(self):
        """ initial game and load resoure """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        """ start game main loop """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """ listening keyboard and mouse event """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                        
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Response keydown event """
        # Move ship to right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Move ship to left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Response keydown event """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ build a bullet, add it into group bullets """
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ update bullet position and delete dispared bullet """
        self.bullets.update()

        # delete dispared bullet 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """ initial alien group """
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        # Refresh screen 
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # make recent displayed screen visiable
        pygame.display.flip()
            
if __name__ ==  '__main__':
    # establish game instantiation & run game
    ai = AlienInvasion()
    ai.run_game()
