import pygame
import classes_beings as entities
import math

class ThrownObject:
    
    def __init__(self, speed, position, direction, damage, width, height):
        """Constructor

        Args:
            speed (float): _description_
            position (tuple): _description_
            direction (-1/1): _description_
            damage (float): _description_
            width (int): _description_
            height (int): _description_
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

    def give_damage(self):
        """Function responsible for giving damage to objects
        """
        if self.hitbox.collidedict():
            del self
 
     