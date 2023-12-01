import random
import pygame
import screen
from settings import *
import time

class Alive_Being:
    """
    Mother class for player and enemies
    """
    def __init__(self, health, speed, position, width, height):
        """Constructor

        Args:
            health (int): it's obvious
            speed (int): it's obvious
            position (tuple): (x,y)
            width (int): used only to generate rect
            height (int): used only to generate rect
            visible (bool): used when being is destroyed
        """
        self.visible = True
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
    def __init__(self, health, speed, position, width, height, color):
        """Abstract constructor

        Args:
            color (string): enemies color (in future image)
        """
        super().__init__(health, speed, position, width, height)
        self.color = color
        
    def movement(self):
        self.hitbox.move_ip(-self.speed, 0)
        pygame.draw.rect(screen.screen, self.color, self.hitbox)
    
class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): Parent class
    """
    def __init__(self, health, speed, position, width, height, color):
        super().__init__(health, speed, position, width, height, color)
        self.damage_aura = pygame.rect.Rect((self.position_x-((const['AURA_RANGE']-const['ENEMY_WIDTH'])/2), 
                                    self.position_y-((const['AURA_RANGE']-const['ENEMY_HEIGHT'])/2)), 
                                    (const['AURA_RANGE'], const['AURA_RANGE']))
            
    def attack(self, player_hitbox):
        self.damage_aura.move_ip(-self.speed, 0)
        #pygame.draw.rect(screen.screen, "yellow", self.damage_aura)
        
        if self.damage_aura.colliderect(player_hitbox):
            player.get_damage(const['MELEE_DAMAGE'])    
        #time.sleep(0.1)


class RangedEnemy(Enemy):
    """Class for ranged enemy

    Args:
        Enemy (object): Parent class
    """    
    def attack(self, player):
        pass

class Player(Alive_Being):
    """Player class

    Args:
        Alive_Being (object): Parent class
    """
             
    def handling_equipment(self) -> int:
        """Function detects if player pressed key responsible for selecting item from the equipment 

        Returns:
            int: index no. of item/weapon
        """
        if self.visible:
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
        if self.visible:
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
        
    def get_damage(self, damage):
        if self.health_points>=0 and self.visible:
            self.health_points -= damage
        else:
            self.visible = False
       
        

"""Initialazing player"""
player = Player(const['PLAYER_HEALTH'], const['PLAYER_SPEED'], 
                (0,(settings['SCREEN_HEIGHT']-const['PLAYER_HEIGHT'])/2), 
                const['PLAYER_WIDTH'], const['PLAYER_HEIGHT'])

enemies_m = []
enemies_r = []

for i in range(0, 50):
    height_range = random.randint(settings['SCREEN_HEIGHT']/10, settings['SCREEN_HEIGHT']-const['ENEMY_HEIGHT'])
    if height_range%7==0:
        enemy = RangedEnemy(const['RANGED_HEALTH'], const['ENEMY_SPEED'], 
                            (settings['SCREEN_WIDTH'], height_range), 50, 50, (255, 255, 5*i))
        enemies_r.append(enemy)
    else:
        enemy = MeleeEnemy(const['MELEE_HEALTH'], const['ENEMY_SPEED'], 
                           (settings['SCREEN_WIDTH']-const['ENEMY_WIDTH'], height_range), 50, 50, (0, 0, 255-(i*5)))
        enemies_m.append(enemy)
    