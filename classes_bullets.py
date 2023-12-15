import pygame
from settings import *
from alive_being import *
import math
import screen
import enemies
import math

class ThrownObject(pygame.sprite.Sprite):
    def __init__(self, bullet_dict, pos):
        """_summary_

        Args:
            speed (float): obiovus
            position (tuple): topleft of bullet (x,y)
            width (float): bullet width
            height (float): bullet height
            damage (float): _description_
            dir (-1/1): -1 left | 1 right
        """
        pygame.sprite.Sprite.__init__(self)
        (self.position_x, self.position_y) = pos
        self.graphics = pygame.transform.scale_by(pygame.image.load(bullet_dict['src_file']), bullet_dict['scale'])
        self.hitbox = self.graphics.get_rect()
        self.hitbox.topleft = (self.position_x, self.position_y)
        self.damage = bullet_dict['dmg']
        self.speed = bullet_dict['speed']
        self.direction = bullet_dict['dir']
        
    def update(self):
        
        if self.hitbox.top <= settings['SCREEN_HEIGHT'] / 10:
            self.kill()
        if self.hitbox.bottom >= settings['SCREEN_HEIGHT']:
            self.kill()
        if self.hitbox.right >= settings['SCREEN_WIDTH']:
            self.kill()
        if self.hitbox.left <= 0:
            self.kill()
            
        screen.screen.blit(self.graphics, self.hitbox)
        
class PistolBullet(ThrownObject):
    
    def update(self):
        ThrownObject.update(self)
        self.hitbox.move_ip(self.speed * self.direction, 0)
        
class ShotgunBullet(ThrownObject):
    
    def __init__(self, pos, angle, dir_y):
        ThrownObject.__init__(self, const['b_shotgun'], pos)
        self.angle = math.radians(angle)
        self.dir_y = dir_y
        
    def update(self):
        ThrownObject.update(self)
        self.hitbox.move_ip(self.speed * self.direction * math.cos(self.angle), self.dir_y * self.speed * math.sin(self.angle))
        
        
class Parabolic(ThrownObject):
    
    def __init__(self, bullet_dict, pos, angle):
        ThrownObject.__init__(self, bullet_dict, pos)
        self.angle - math.radians(angle)
        self.ini_pos = pos