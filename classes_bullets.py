import pygame
import classes_beings as entities
import math

class ThrownObject:
    
    def __init__(self, speed, position, direction, damage, width, height):
        """Constructor

        Args:
            speed (float): it's obvious 
            position (tuple): it's obvious 
            direction (-1/1): -1 - left | 1 - right
            damage (float): it's obvious
            width (int): size of bullet on screen
            height (int): size of bullet on screen
        """
        self.speed = speed
        self.position = position
        self.direction = direction
        self.damage = damage
        self.width = width
        self.height = height
        self.hitbox = pygame.rect.Rect((self.position), (self.width, self.height))
        
    def move(self):
        """Method responsible for movement of object
        """
        self.bullet.move_ip(self.speed*self.direction, 0)

    def give_damage(self, target):
        """Function responsible for giving damage to objects
        """
        if self.hitbox.collidedict(target):
            del self
 
     