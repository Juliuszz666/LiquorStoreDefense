import pygame
import screen
from settings import *

class Alive_Being:
    """
    Mother class for player and enemies
    """
    def __init__(self, health, speed, position, width, height):
        """Constructor

        Args:
            health (int): it's obvious
            speed (int): it's obvious
            position (tuple): it's obvious
            width (int): used only to generate rect
            height (int): used only to generate rect
        """
        self.health_points = health
        self.speed = speed
        (self.position_x, self.position_y) = position
        self.hitbox = pygame.Rect(self.position_x, self.position_y, width, height)

class Enemy(Alive_Being):
    """
    Abstract class for enemies (zule i menele)

    Args:
        Alive_Being (object): heritance mechanism
    """
        
    def movement(self):
        self.hitbox.move_ip(-self.speed, 0)
        pygame.draw.rect(screen.screen, "green", self.hitbox)
    
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
        self.player_movement = pygame.key.get_pressed()
        if self.player_movement[pygame.K_w] and self.hitbox.top>settings['SCREEN_HEIGHT']/10:
            self.hitbox.move_ip(0, -self.speed)
        if self.player_movement[pygame.K_a] and self.hitbox.left>0:
            self.hitbox.move_ip(-self.speed, 0)
        if self.player_movement[pygame.K_s] and self.hitbox.bottom<settings['SCREEN_HEIGHT']:
            self.hitbox.move_ip(0, self.speed)
        if self.player_movement[pygame.K_d] and self.hitbox.right<settings['SCREEN_WIDTH']:
            self.hitbox.move_ip(self.speed, 0)                    

        pygame.draw.rect(screen.screen, "white", self.hitbox)
        
        

        """Initialazing player"""
player = Player(const['PLAYER_HEALTH'], const['PLAYER_SPEED'], 
                (0,(settings['SCREEN_HEIGHT']-const['PLAYER_HEIGHT'])/2), 
                const['PLAYER_WIDTH'], const['PLAYER_HEIGHT'])

enemies = []

for i in range(0, 10):
    enemy = Enemy(100, 3, (settings['SCREEN_WIDTH'], 300), 50, 50)
    enemies.append(enemy)