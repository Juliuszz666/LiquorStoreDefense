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
        self.cooldown_bow = 0
        self.cooldown_medkit = 0
        self.medkit_uses = const['player_other']['medkit_uses']
        self.selected = 1
        self.flag = True
        
    def cooldown_list(self):
        max_cooldowns = const['player_other']
        return [[self.cooldown_melee, self.cooldown_pistol, self.cooldown_shotgun, self.cooldown_bow, self.cooldown_medkit],
               [max_cooldowns['m_cooldown'], max_cooldowns['p_cooldown'], max_cooldowns['s_cooldown'], 
                max_cooldowns['b_cooldown'], max_cooldowns['medkit_cooldown']]]

    def cooldown_reduction(self):
        self.cooldown_bow -= 1
        self.cooldown_medkit -= 1 
        self.cooldown_melee -= 1
        self.cooldown_pistol -= 1
        self.cooldown_shotgun -= 1
        
    def is_use(self):
        return pygame.key.get_pressed()[pygame.K_SPACE]
    
    def movement(self):
        self.player_movement = pygame.key.get_pressed()
        if self.player_movement[pygame.K_w] and self.rect.top>settings['SCREEN_HEIGHT']/10:
            self.rect.move_ip(0, -self.speed)
        if self.player_movement[pygame.K_a] and self.rect.left>0:
            self.rect.move_ip(-self.speed, 0)
        if self.player_movement[pygame.K_s] and self.rect.bottom<settings['SCREEN_HEIGHT']:
            self.rect.move_ip(0, self.speed)
        if self.player_movement[pygame.K_d] and self.rect.right<settings['SCREEN_WIDTH']:
            self.rect.move_ip(self.speed, 0)
             
    def handling_equipment(self):
        """Function detects if player pressed key responsible for selecting item from the equipment 

        Returns:
            int: index no. of item/weapon
        """
    
        player_controls = pygame.key.get_pressed()
        if player_controls[pygame.K_1] and self.flag:
            self.selected  = 1 
            self.flag = False
        if player_controls[pygame.K_2] and self.flag:
            self.selected = 2 
            self.flag = False
        if player_controls[pygame.K_3] and self.flag:
            self.selected = 3 
            self.flag = False
        if player_controls[pygame.K_4] and self.flag:
            self.selected = 4 
            self.flag = False
        if player_controls[pygame.K_5] and self.flag:
            self.selected = 5 
            self.flag = False
        else:
            self.flag = True
            
        match self.selected:
            case 1:
                pos = self.rect.topleft
                self.graphics = pygame.transform.scale_by(pygame.image.load(const['player_graphics'][0]), const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.machete()
            case 2:
                pos = self.rect.topleft
                self.graphics = pygame.transform.scale_by(pygame.image.load(const['player_graphics'][1]), const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.pistol()
            case 3:
                pos = self.rect.topleft
                self.graphics = pygame.transform.scale_by(pygame.image.load(const['player_graphics'][2]), const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.shotgun()
            case 4:
                pos = self.rect.topleft
                self.graphics = pygame.transform.scale_by(pygame.image.load(const['player_graphics'][3]), const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.bow()
            case 5:
                pos = self.rect.topleft
                self.graphics = pygame.transform.scale_by(pygame.image.load(const['player_graphics'][4]), const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.medkit()

    def machete(self):
        
        if self.is_use() and self.cooldown_melee<=0:
            self.cooldown_melee = const['player_other']['m_cooldown']

    def pistol(self):
        if self.is_use() and self.cooldown_pistol<=0:
            bullet_player = PistolBullet((self.rect.centerx+15, self.rect.centery-20))
            all_sprite.add(bullet_player)
            pistol_bullets.add(bullet_player)
            bullets.add(bullet_player)
            player_bullets.add(bullet_player)
            self.cooldown_pistol = const['player_other']['p_cooldown']
        
    def shotgun(self):
        
        if self.is_use() and self.cooldown_shotgun<=0:
            for i in range(-1, 2, 1):
                bullet_player = ShotgunBullet((self.rect.centerx+35, self.rect.centery-30), const['b_shotgun']['angle'], i)
                all_sprite.add(bullet_player)
                bullets.add(bullet_player)
                shotgun_bullets.add(bullet_player)
                player_bullets.add(bullet_player)
            self.cooldown_shotgun = const['player_other']['s_cooldown']
        else:
            self.cooldown_shotgun -= 1

    def bow(self):
        if self.is_use() and self.cooldown_bow<=0:
            bullet_player = Arrow((self.rect.centerx, self.rect.centery-25), const['arrow']['angle'])
            all_sprite.add(bullet_player)
            bullets.add(bullet_player)
            arrows.add(bullet_player)
            player_bullets.add(bullet_player)
            self.cooldown_bow = const['player_other']['b_cooldown']
    
    def medkit(self):
        if self.is_use() and self.medkit_uses and self.cooldown_medkit <= 0:
            self.health_points += const['player_other']['medkit_healing']
            self.medkit_uses -= 1
            self.cooldown_medkit = const['player_other']['medkit_cooldown']
    
    def update(self):
        """_summary_
        """
        Alive_Being.update(self)

        self.cooldown_reduction()
        self.movement()            
        self.handling_equipment()
     
        screen.screen.blit(self.graphics, self.rect)
        
    def get_damage(self, damage):
        if self.health_points>0:
            self.health_points -= damage
        if self.health_points<=0:
            self.kill()
        
            


"""Initialazing player"""
protagonist = Player((50, 200))
all_sprite.add(protagonist)