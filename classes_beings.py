import pygame
from constants import *

class Alive_Being:
    """
    Mother class for player and enemies
    """
    def __init__(self, health, speed, position):
        """
        Constructor

        Args:
            health (int): health points
            speed (int): speed of movement
        """
        self.health_points = health
        self.speed = speed
        self.position = position
    def __del__(self):
        pass

class Enemy(Alive_Being):
    """
    Abstract class for enemies (zule i menele)

    Args:
        Alive_Being (object): heritance mechanism
    """
    def __init__(self, weapon_type, health, speed, position):
        Alive_Being.__init__(health, speed, position)
        self.weapon = weapon_type
    

class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): _description_
    """
    def attack(self, player):
        self.damage_aura = pygame.rect.Rect(self.position, (const['AURA_RANGE'], const['AURA_RANGE']))
        if self.damage_aura.colliderect(player):
            pass
        del self.damage_aura
        pass

class RangedEnemy(Enemy):
    """_summary_

    Args:
        Enemy (object): 
    """    

class Player(Alive_Being):
    """_summary_

    Args:
        Alive_Being (object): mother class ??
    """
             
    def handling_equipment(self) -> int:
        """Function detects if player pressed key responsible for selecting item from the equipment 

        Returns:
            int: index no. of item/weapon
        """
        self.player_controls = pygame.key.get_pressed()
        if self.player_controls[pygame.K_1]:
            return 1
        if self.player_controls[pygame.K_2]:
            return 2
        if self.player_controls[pygame.K_3]:
            return 3
        if self.player_controls[pygame.K_4]:
            return 4
        if self.player_controls[pygame.K_5]:
            return 5
        if self.player_controls[pygame.K_6]:
            return 6
        if self.player_controls[pygame.K_7]:
            return 7
        if self.player_controls[pygame.K_8]:
            return 8
        if self.player_controls[pygame.K_9]:
            return 9
        return 0
    
    def movement(self):
        pass


player = Player(100, 100, (5,5))