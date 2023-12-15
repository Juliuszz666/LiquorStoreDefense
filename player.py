import pygame
from alive_being import *
from enemies import *
from player import *
from settings import *
from classes_bullets import *
from sprites_groups import *
import screen

class Player(Alive_Being):
    """Player class

    Args:
        Alive_Being (object): Parent class
    """
    
    def __init__(self, position):
        Alive_Being.__init__(self, const['player_init'], position)
        self.cooldown_melee = 0
        self.cooldown_pistol = 0            
        self.cooldown_shotgun = 0
             
    def handling_equipment(self) -> int:
        """Function detects if player pressed key responsible for selecting item from the equipment 

        Returns:
            int: index no. of item/weapon
        """
    
        player_controls = pygame.key.get_pressed()
        if player_controls[pygame.K_1]:
            return 1
        if player_controls[pygame.K_2]:
            return 2
        if player_controls[pygame.K_3]:
            return 3
        if player_controls[pygame.K_4]:
            return 4
        if player_controls[pygame.K_5]:
            return 5
        else:
            return 0

    def machete(self):
        
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.cooldown_melee<=0:
            self.cooldown_melee = const['player_other']['m_cooldown']
            #melee_collision = pygame.sprite.spritecollide(self, enemies, True)
            #for enemy in melee_collision:
            #    enemy.get_damage()
        else:
            self.cooldown_melee -= 1


    def pistol(self):
        shot = pygame.key.get_pressed()[pygame.K_SPACE]
        if shot and self.cooldown_pistol<=0:
            bullet_player = PistolBullet(const['b_pistol'], self.hitbox.topleft)
            all_sprite.add(bullet_player)
            bullets.add(bullet_player)
            player_bullets.add(bullet_player)
            self.cooldown_pistol = const['player_other']['p_cooldown']
        else:
            self.cooldown_pistol -= 1
        
    def shotgun(self):
        shot = pygame.key.get_pressed()[pygame.K_SPACE]
        if shot and self.cooldown_shotgun<=0:
            for i in range(-1, 2, 1):
                bullet_player = ShotgunBullet(self.hitbox.topleft, const['b_shotgun']['angle'], i)
                all_sprite.add(bullet_player)
                bullets.add(bullet_player)
                player_bullets.add(bullet_player)
            self.cooldown_shotgun = const['player_other']['s_cooldown']
        else:
            self.cooldown_shotgun -= 1

    def bow(self):
        pass
    
    def medkit(self):
        use = pygame.key.get_pressed()[pygame.K_SPACE]
        if use and medkit_uses and self.health_points<250:
            self.health_points+=const['MEDKIT_POWER']
            medkit_uses -= 1
            print(self.health_points)
    
    def update(self):
        """_summary_
        """
        Alive_Being.update(self)
        self.player_movement = pygame.key.get_pressed()
        if self.player_movement[pygame.K_w] and self.hitbox.top>settings['SCREEN_HEIGHT']/10:
            self.hitbox.move_ip(0, -self.speed)
        if self.player_movement[pygame.K_a] and self.hitbox.left>0:
            self.hitbox.move_ip(-self.speed, 0)
        if self.player_movement[pygame.K_s] and self.hitbox.bottom<settings['SCREEN_HEIGHT']:
            self.hitbox.move_ip(0, self.speed)
        if self.player_movement[pygame.K_d] and self.hitbox.right<settings['SCREEN_WIDTH']:
            self.hitbox.move_ip(self.speed, 0)
     
        screen.screen.blit(self.graphics, self.hitbox)
    
    
    def get_damage(self, damage):
        if self.health_points>=0:
            self.health_points -= damage
            print(self.health_points)
        else:
            self.kill()
            screen.display_defeat()

"""Initialazing player"""
protagonist = Player((50, 200))
all_sprite.add(protagonist)