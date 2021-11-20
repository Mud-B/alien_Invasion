import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ manage bullet shot from ship """


    def __init__(self, ai_game):
        """ build a bullet object at ship current position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # build a rectangle at (0,0) represent a bullet,than set corret position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet position in floating num
        self.y = float(self.rect.y)

    def update(self):
        """ move bullet """
        # update bullet position
        self.y -= self.settings.bullet_speed
        # update rectangle of bullet shape
        self.rect.y = self.y

    def draw_bullet(self):
        """ draw bullte in screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
