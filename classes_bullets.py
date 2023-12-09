import pygame
import enemies
import math

class ThrownObject(pygame.sprite.Sprite):
    def __init__(self, position, width, height, damage):
        """_summary_

        Args:
            position (_type_): _description_
            width (_type_): _description_
            height (_type_): _description_
            damage (_type_): _description_
        """
        pygame.sprite.Sprite.__init__()
        (self.position_x, self.position_y) = position
        self.hitbox = pygame.rect.Rect(self.position_x, self.position_y, width, height)
        self.damage = damage
        
    def update(self) -> None:
        pygame.sprite.Sprite.update(self)
        
        if self.position