import random
import pygame
import screen
from settings import *
from alive_being import *
import player
import time
from sprites_groups import *
from classes_bullets import *


class Enemy(Alive_Being):
    """
    Abstract class for enemies (zule i menele)

    Args:
        Alive_Being (object): heritance mechanism
    """
    def update(self) -> None:
        Alive_Being.update(self)
        self.rect.move_ip(-self.speed, 0)
        screen.screen.blit(self.graphics, self.rect)
        #if self.rect.left <= 0:
        #    screen.display_defeat()

    def get_damage(self, damage):
        if self.health_points>=0:
            self.health_points -= damage
        else:
            self.kill()

class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): Parent class
    """
    def update(self):
        Enemy.update(self)
        


class RangedEnemy(Enemy):
    """Class for ranged enemy

    Args:
        Enemy (object): Parent class
    """
    def __init__(self, being_dict, position):
        Enemy.__init__(self, being_dict, position)
        self.cooldown = 0        

    def attack(self):
        if  self.cooldown<=0:
            bullet_enemy = Bottle(self.rect.center, const['arrow']['angle'])
            all_sprite.add(bullet_enemy)
            bullets.add(bullet_enemy)
            enemy_bullets.add(bullet_enemy)
            self.cooldown = const['enemies_other']['r_cooldown']
        else:
            self.cooldown -= 1
            
    def update(self):
        Enemy.update(self)
        self.attack()

def spawn_enemy():
    pos_y = random.randint(settings['SCREEN_HEIGHT']/10, settings['SCREEN_HEIGHT']-const['enemy_height'])
    enemy_type = random.choice(['melee', 'ranged'])
    match enemy_type:
        case 'melee':
            enemy = MeleeEnemy(const['enemy_melee'], (settings['SCREEN_WIDTH'], pos_y))
        case 'ranged':
            enemy = RangedEnemy(const['enemy_ranged'], (settings['SCREEN_WIDTH'], pos_y))
    all_sprite.add(enemy)
    all_enemies.add(enemy)