import pygame
import screen
from settings import *

class Alive_Being:
    """
    Mother class for player and enemies
    """
    def __init__(self, health, speed, position, width, height):
        """
        Constructor

        Args:
            health (int): health points
            speed (int): speed of movement
        """
        self.health_points = health
        self.speed = speed
        self.position = position
        self.hitbox = pygame.rect.Rect(width, height)

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
        Alive_Being (object): Parent class
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
        return 0
    
    def movement(self):
        """Function responsible for movement of player
        """
        self.hitbox.move_ip(self.speed)
        pygame.draw.rect(screen.screen, ("white"), self.hitbox)


player = Player(100, 100, (500,500), const['PLAYER_WIDTH'], const['PLAYER_HEIGHT'])