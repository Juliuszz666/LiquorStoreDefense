import pygame
from settings import *
from alive_being import *
import enemies
import math

class ThrownObject(pygame.sprite.Sprite):
    def __init__(self, speed, position, width, height, damage, dir):
        """_summary_

        Args:
            speed (float): obiovus
            position (tuple): topleft of bullet (x,y)
            width (float): bullet width
            height (float): bullet height
            damage (float): _description_
            dir (-1/1): -1 left | 1 right
        """
        pygame.sprite.Sprite.__init__()
        (self.position_x, self.position_y) = position
        self.hitbox = pygame.rect.Rect(self.position_x, self.position_y, width, height)
        self.damage = damage
        self.speed = speed
        self.direction = dir
        
    def update(self):
        pygame.sprite.Sprite.update(self)
        
        if self.hitbox.top <= settings['SCREEN_HEIGHT'] / 10:
            self.kill()
        if self.hitbox.bottom >= settings['SCREEN_HEIGHT']:
            self.kill()
        if self.hitbox.right >= settings['SCREEN_WIDTH']:
            self.kill()
        if self.hitbox.left <= 0:
            self.kill()
        if self.hitbox.collideobjects(Alive_Being.hitbox):
            self.kill()
            
        self.hitbox.move_ip(self.speed * self.direction, 0)