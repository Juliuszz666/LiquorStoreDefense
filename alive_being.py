import pygame
from settings import *


class Alive_Being(pygame.sprite.Sprite):
    """
    Parent class for player and enemies
    """
    def __init__(self, being_dict, position):
        """Abstract constructor

        Args:
            being_dict (dictionary):\n
            \tAbstract dicitonary containint:
                \t-health\n
                \t-speed\n
                \t-source file of being image and it's scale\n
            position (tuple): initial position of being
        """
        pygame.sprite.Sprite.__init__(self)
        self.health_points = being_dict['hp']
        self.speed = being_dict['speed']
        (self.position_x, self.position_y) = position
        self.graphics = pygame.transform.scale_by(pygame.image.load(being_dict['src_file']), being_dict['scale'])
        self.rect = self.graphics.get_rect()
        self.rect.topleft = (self.position_x, self.position_y)

    def update(self) -> None:
        """Abstract class does nothing but it's convinient hook
        for child classes where we would upadate all sprites
        """
        pygame.sprite.Sprite.update(self)
