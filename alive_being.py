import pygame
from settings import *


class Alive_Being(pygame.sprite.Sprite):
    """
    Parent class for player and enemies
    """
    def __init__(self, being_dict, position):
        """Abstract constructor

        Args:
            being_dict (_type_): _description_
            position (_type_): _description_
        """
        pygame.sprite.Sprite.__init__(self)
        self.health_points = being_dict['hp']
        self.speed = being_dict['speed']
        (self.position_x, self.position_y) = position
        self.graphics = pygame.transform.scale_by(pygame.image.load(being_dict['src_file']), being_dict['scale'])
        self.hitbox = self.graphics.get_rect()
        self.hitbox.topleft = (self.position_x, self.position_y)
        
    def update(self) -> None:
        pygame.sprite.Sprite.update(self)
