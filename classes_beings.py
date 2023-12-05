import random
import pygame
import screen
from settings import *
from alive_being import *
import time

medkit_uses = const['MEDKIT_USES']

class Enemy(Alive_Being):
    """
    Abstract class for enemies (zule i menele)

    Args:
        Alive_Being (object): heritance mechanism
    """
    def __init__(self, health, speed, position, width, height, color, aura_range):
        """Abstract constructor

        Args:
            color (string): enemies color (in future image)
        """
        super().__init__(health, speed, position, width, height, aura_range)
        self.color = color
        
    def movement(self):
        if self.visible:
            self.hitbox.move_ip(-self.speed, 0)
            pygame.draw.rect(screen.screen, self.color, self.hitbox)
        
    def get_melee_damage(self):
        if self.visible and self.hitbox.colliderect(player.damage_aura):
            self.health_points -= const['MACHETE_DAMAGE']
        if self.health_points<=0:
            self.visible = False


class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): Parent class
    """
                
    def attack(self, player_hitbox):
        if self.visible:    
            self.damage_aura.move_ip(-self.speed, 0)
            #pygame.draw.rect(screen.screen, "yellow", self.damage_aura)
            if self.damage_aura.colliderect(player_hitbox):
                player.get_damage(const['MELEE_DAMAGE'])
                    
            


class RangedEnemy(Enemy):
    """Class for ranged enemy

    Args:
        Enemy (object): Parent class
    """    
    def attack(self):
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

    def machete(self):
        if self.visible and pygame.key.get_pressed()[pygame.K_SPACE]:
            pygame.draw.rect(screen.screen, "purple", self.damage_aura)
            i = len(enemies_r)-1
            j = len(enemies_m)-1

            while(i or j):
                if(j):
                    enemies_m[j].get_melee_damage()
                    j -= 1
                if(i):
                    enemies_r[i].get_melee_damage()
                    i -= 1
            

    def pistol():
        pass        
    
    def shotgun():
        pass

    def bow():
        pass
    
    def medkit(self):
        if self.visible:
            use = pygame.key.get_pressed()[pygame.K_SPACE]
            global medkit_uses
            if use and medkit_uses:
                self.health_points+=const['MEDKIT_POWER']
                medkit_uses -= 1
                print(self.health_points)
                use = 0
            elif not use:
                use = 1
    
    def movement(self):
        """Function responsible for movement of player
        """
        if self.visible:
            self.player_movement = pygame.key.get_pressed()
            if self.player_movement[pygame.K_w] and self.hitbox.top>settings['SCREEN_HEIGHT']/10:
                self.hitbox.move_ip(0, -self.speed)
                self.damage_aura.move_ip(0, -self.speed)
            if self.player_movement[pygame.K_a] and self.hitbox.left>0:
                self.hitbox.move_ip(-self.speed, 0)
                self.damage_aura.move_ip(-self.speed, 0)
            if self.player_movement[pygame.K_s] and self.hitbox.bottom<settings['SCREEN_HEIGHT']:
                self.hitbox.move_ip(0, self.speed)
                self.damage_aura.move_ip(0, self.speed)
            if self.player_movement[pygame.K_d] and self.hitbox.right<settings['SCREEN_WIDTH']:
                self.hitbox.move_ip(self.speed, 0)                    
                self.damage_aura.move_ip(self.speed, 0)

            pygame.draw.rect(screen.screen, "white", self.hitbox)
        
    def get_damage(self, damage):
        print("Halo")
        if self.health_points>=0 and self.visible:
            self.health_points -= damage
        else:
            self.visible = False

"""Initialazing player"""
player = Player(const['PLAYER_HEALTH'], const['PLAYER_SPEED'], 
                (0,(settings['SCREEN_HEIGHT']-const['PLAYER_HEIGHT'])/2), 
                const['PLAYER_WIDTH'], const['PLAYER_HEIGHT'], const['MACHETE_RANGE'])

enemies_m = []
enemies_r = []
enemy_rect = []


for i in range(0, 50):
    #nd_pos = random.randint(-3, 3)
    height_range = random.randint(settings['SCREEN_HEIGHT']/10, settings['SCREEN_HEIGHT']-const['ENEMY_HEIGHT'])
    if height_range%7==0:
        enemy = RangedEnemy(const['RANGED_HEALTH'], const['ENEMY_SPEED'], 
                            (settings['SCREEN_WIDTH']-const['ENEMY_WIDTH'], height_range), 50, 50, (55, 55, 5*i), const['AURA_RANGE'])
        enemy_rect.append(enemy.hitbox)
        enemies_r.append(enemy)
    else:
        enemy = MeleeEnemy(const['MELEE_HEALTH'], const['ENEMY_SPEED'], 
                            (settings['SCREEN_WIDTH']-const['ENEMY_WIDTH'], height_range), 50, 50, (150, 150, 255-(i*5)), const['AURA_RANGE'])
        enemy_rect.append(enemy.hitbox)
        enemies_m.append(enemy)
