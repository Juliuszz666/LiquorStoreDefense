import random
import pygame
import screen
from settings import *
from alive_being import *
import player
import time

medkit_uses = const['MEDKIT_USES']
pistol_ammo = const['INIT_PISTOL_AMMO']

'''
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

    def update(self) -> None:
        self.hitbox.move_ip(-self.speed, 0)
        pygame.draw.rect(screen.screen, self.color, self.hitbox)
        if self.hitbox.colliderect(player.player.damage_aura):
            self.health_points -= const['MACHETE_DAMAGE']
            print(self.health_points)

    def defeat(self):
        if self.hitbox.left <= 0:
            screen.display_defeat()


class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): Parent class
    """

    def attack(self, player_hitbox):
        self.damage_aura.move_ip(-self.speed, 0)
        # pygame.draw.rect(screen.screen, "yellow", self.damage_aura)
        if self.damage_aura.colliderect(player_hitbox):
            player.player.get_damage(const['MELEE_DAMAGE'])


class RangedEnemy(Enemy):
    """Class for ranged enemy

    Args:
        Enemy (object): Parent class
    """

    def attack(self):
        pass


enemies_m = []
enemies_r = []
enemy_rect = []

for i in range(0, 50):
    # nd_pos = random.randint(-3, 3)
    height_range = random.randint(settings['SCREEN_HEIGHT'] / 10, settings['SCREEN_HEIGHT'] - const['ENEMY_HEIGHT'])
    if height_range % 7 == 0:
        enemy = RangedEnemy(const['RANGED_HEALTH'], const['ENEMY_SPEED'],
                            (settings['SCREEN_WIDTH'] - const['ENEMY_WIDTH'], height_range), 50, 50, (55, 55, 5 * i),
                            const['AURA_RANGE'])
        enemy_rect.append(enemy.hitbox)
        enemies_r.append(enemy)
    else:
        enemy = MeleeEnemy(const['MELEE_HEALTH'], const['ENEMY_SPEED'],
                           (settings['SCREEN_WIDTH'] - const['ENEMY_WIDTH'], height_range), 50, 50,
                           (150, 150, 255 - (i * 5)), const['AURA_RANGE'])
        enemy_rect.append(enemy.hitbox)
        enemies_m.append(enemy)
'''