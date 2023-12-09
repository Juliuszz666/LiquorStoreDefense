import pygame
import screen
from settings import *


class Alive_Being(pygame.sprite.Sprite):
    """
    Parent class for player and enemies
    """
    def __init__(self, health, speed, position, width, height, aura_range):
        """Abstract constructor

        Args:
            health (float): no need to explain
            speed (float): no need to explain
            position (tuple): top left of being (x,y)
            width (float): being width
            height (float): being height
            aura_range (float): for melee being area where enemy takes damage
        """
        pygame.sprite.Sprite.__init__(self)
        self.health_points = health
        self.speed = speed
        (self.position_x, self.position_y) = position
        self.hitbox = self.hitbox = pygame.Rect(self.position_x, self.position_y, width, height)
        self.damage_aura = pygame.rect.Rect((self.position_x - ((aura_range - width) / 2),
                                             self.position_y - ((aura_range - height) / 2)), (aura_range, aura_range))
        self.visible = True

    def update(self) -> None:
        pygame.sprite.Sprite.update(self)
