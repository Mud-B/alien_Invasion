import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ class represent single alien """

    def __init__(self, ai_game):
        # inital alien and set it's position
        super().__init__()
        self.screen = ai_game.screen

        # load alien picture and set it's rect propeties
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()

        # initial alien at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien parallel position
        self.x = float(self.rect.x)