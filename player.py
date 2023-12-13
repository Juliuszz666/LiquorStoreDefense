import pygame
from alive_being import *
from enemies import *
from player import *
from settings import *
import screen

class Player(Alive_Being):
    """Player class

    Args:
        Alive_Being (object): Parent class
    """
    
    def __init__(self):
        Alive_Being.__init__(self, const['player_init'])
        self.cooldown_melee = 0
        self.cooldown_ranged = 0            
             
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

    def machete(self):
        
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.cooldown_melee<=0:
            pygame.draw.rect(screen.screen, "purple", self.damage_aura)
            self.cooldown_melee = const['player_other']['m_cooldown']
        else:
            self.cooldown_melee -= 1


    def pistol(self):
        global pistol_ammo
        shot = pygame.key.get_pressed()[pygame.K_SPACE]
        if shot and pistol_ammo:
            return None # bullet constructor
    
    def shotgun(self):
        pass

    def bow(self):
        pass
    
    def medkit(self):
        use = pygame.key.get_pressed()[pygame.K_SPACE]
        global medkit_uses
        if use and medkit_uses and self.health_points<250:
            self.health_points+=const['MEDKIT_POWER']
            medkit_uses -= 1
            print(self.health_points)
    
    def update(self):
        """_summary_
        """
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
        if self.health_points>=0:
            self.health_points -= damage
            print(self.health_points)
        else:
            self.kill()
            screen.display_defeat()

"""Initialazing player"""
player = Player()