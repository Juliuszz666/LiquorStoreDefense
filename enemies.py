import random
import screen
from settings import *
from alive_being import AliveBeing
from sprites_groups import *
from classes_bullets import *
from scoring import *


class Enemy(AliveBeing):
    """
    Abstract class for enemies (zule i menele)

    Args:
        Alive_Being (object): parent class
    """

    def update(self) -> None:
        """
        This function is responsible for displaying and moving all enemies
        """
        AliveBeing.update(self)
        self.rect.move_ip(-self.speed, 0)
        SCREEN.blit(self.graphics, self.rect)

    def get_damage(self, damage):
        """This function is called when enemy is supposed to take damage
        from player, this function also is responsible for killing enemy
        and adding score after its death

        Args:
            damage (int/float): damage amount
        """
        if self.health_points > 0:
            self.health_points -= damage
            self.graphics.fill(RED, special_flags=pygame.BLEND_RGB_MULT)
        if self.health_points <= 0:
            add_score(10)
            self.kill()


class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): Parent class
    """

    def __init__(self, position):
        """
        Constructor for melee enemy

        Args:
            position (tuple): spawn position
        """
        Enemy.__init__(self, const['enemy_melee'], position)
        self.cooldown = 0

    def attack(self):
        """
        Melee damage occur to player when they collide with enemy with
        no cooldown so this function only changes cooldwon

        Returns:
            True/False: can/cannot give damage if collides with player
        """
        if self.cooldown <= 0:
            self.cooldown = const['enemies_other']['m_cooldown']
            return True
        else:
            self.cooldown -= 1
            return False

    def update(self):
        """
        Function is combination of Enemy.update()
        and attack function
        """
        Enemy.update(self)
        self.attack()


class RangedEnemy(Enemy):
    """
    Class for ranged enemy

    Args:
        Enemy (object): Parent class
    """

    def __init__(self, position):
        """Constructor for ranged enemy

        Args:
            position (tuple): spawn position
        """
        Enemy.__init__(self, const['enemy_ranged'], position)
        self.cooldown = 0

    def attack(self):
        """
        Ranged attack is about creating objects from class Bottle
        if there is no cooldown
        """
        if self.cooldown <= 0:
            bullet_enemy = Bottle(self.rect.center, const['arrow']['angle'])
            all_sprite.add(bullet_enemy)
            bullets.add(bullet_enemy)
            enemy_bullets.add(bullet_enemy)
            self.cooldown = const['enemies_other']['r_cooldown']
        else:
            self.cooldown -= 1

    def update(self):
        """
        Function is combination of Enemy.update()
        and attack function
        """
        Enemy.update(self)
        self.attack()


class Boss(Enemy):
    """
    Class for boss - enhanced enemy that spawn rarely

    Args:
        Enemy (object): parent class
    """

    def __init__(self, position):
        """
        Constructor for boss

        Args:
            position (tuple): spawn posistion
        """
        Enemy.__init__(self, const['boss'], position)
        self.cooldown_m = 0
        self.cooldown_r = 0

    def update(self):
        """
        Function blits boss to screen, calls attack and moves itself
        """
        Enemy.update(self)
        self.attack_r()
        self.attack()

    def attack_r(self):
        """
        Ranged attack
        """
        if self.cooldown_r <= 0:
            bullet_enemy = Bottle(self.rect.center, const['arrow']['angle'])
            all_sprite.add(bullet_enemy)
            bullets.add(bullet_enemy)
            enemy_bullets.add(bullet_enemy)
            self.cooldown_r = const['enemies_other']['r_cooldown']
        else:
            self.cooldown_r -= 1

    def attack(self):
        """Melee attack

        Returns:
            Bool: Whether boss can/cannot attack
        """
        if self.cooldown_m <= 0:
            self.cooldown_m = const['enemies_other']['m_cooldown']
            return True
        else:
            self.cooldown_m -= 1
            return False


def spawn_enemy():
    """
    Function responsible for randomized spawning both types of enemies,
    enemies spawn on the right side of the screen
    """
    if random.randint(0, const['boss_spawn_rate']) == 1:
        enemy_type = 'boss'
        pos_y = random.randint(settings['SCREEN_HEIGHT'] / 10,
                               settings['SCREEN_HEIGHT']
                               - const['enemies_other']['boss_height'])
    else:
        enemy_type = random.choice(['melee', 'ranged'])
        pos_y = random.randint(settings['SCREEN_HEIGHT'] / 10,
                               settings['SCREEN_HEIGHT']
                               - const['enemies_other']['enemy_height'])
    match enemy_type:
        case 'melee':
            enemy = MeleeEnemy((settings['SCREEN_WIDTH'], pos_y))
            all_melee.add(enemy)
        case 'ranged':
            enemy = RangedEnemy((settings['SCREEN_WIDTH'], pos_y))
        case 'boss':
            enemy = Boss((settings['SCREEN_WIDTH'], pos_y))
            all_melee.add(enemy)
    all_sprite.add(enemy)
    all_enemies.add(enemy)
