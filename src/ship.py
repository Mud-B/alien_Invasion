import pygame

from settings import Settings

class Ship:
    """ manage ship """

    def __init__(self, ai_game):
        """ initial ship & set up initial position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship settings
        self.settings = Settings()
        
        # Load ship image & get it's shape in rectangle
        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()

        # Put each new ship to the middle of the bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Store minimal x in ship properties
        self.x = float(self.rect.x)
        
        # Moving flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ Adjust ship by moving flag """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Refresh rect Obiect by self.x
        self.rect.x = self.x
        
    def blitme(self):
        """ draw ship in special position """
        self.screen.blit(self.image, self.rect)
