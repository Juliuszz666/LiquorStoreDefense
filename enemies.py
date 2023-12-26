import random
import screen
from settings import *
from alive_being import Alive_Being
from sprites_groups import *
from classes_bullets import *
from scoring import *


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

    def get_damage(self, damage):
        if self.health_points>0:
            self.health_points -= damage
        if self.health_points<=0:
            add_score(10)
            self.kill()

class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): Parent class
    """
    def __init__(self, position):
        Enemy.__init__(self, const['enemy_melee'], position)
        self.cooldown = 0
    
    def attack(self):
        if self.cooldown<=0:
            self.cooldown = const['enemies_other']['m_cooldown']
            return True
        else:
            self.cooldown -= 1
            return False
    
    def update(self):
        Enemy.update(self)
        self.attack()

class RangedEnemy(Enemy):
    """Class for ranged enemy

    Args:
        Enemy (object): Parent class
    """
    def __init__(self, position):
        Enemy.__init__(self, const['enemy_ranged'], position)
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
            enemy = MeleeEnemy((settings['SCREEN_WIDTH'], pos_y))
            all_melee.add(enemy)
        case 'ranged':
            enemy = RangedEnemy((settings['SCREEN_WIDTH'], pos_y))
    all_sprite.add(enemy)
    all_enemies.add(enemy)