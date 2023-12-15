import pygame
from settings import *


class Alive_Being(pygame.sprite.Sprite):
    """
    Parent class for player and enemies
    """
    def __init__(self, being_dict, position):
        """Abstract constructor

        Args:
            health (float): no need to explain
            speed (float): no need to explain
            position (tuple): top left of being (x,y)
            width (float): being width
            height (float): being height
        """
        pygame.sprite.Sprite.__init__(self)
        self.health_points = being_dict['hp']
        self.speed = being_dict['speed']
        (self.position_x, self.position_y) = position
        self.hitbox = self.hitbox = pygame.Rect(self.position_x, self.position_y, being_dict['width'], being_dict['height'])
        
    def update(self) -> None:
        pass
