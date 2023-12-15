import random
import pygame
import screen
from settings import *
from alive_being import *
import player
import time



class Enemy(Alive_Being):
    """
    Abstract class for enemies (zule i menele)

    Args:
        Alive_Being (object): heritance mechanism
    """
    def update(self) -> None:
        Alive_Being.update(self)
        self.hitbox.move_ip(-self.speed, 0)
        pygame.draw.rect(screen.screen, "black", self.hitbox)
        if self.hitbox.left <= 0:
            screen.display_defeat()
        if self.health_points <=0:
            self.kill()

    def get_damage(self, dmg_type):
        match dmg_type:
            case "machete":
                self.health_points -= const['player_other']['machete_dmg']
            case "pistol":
                self.health_points -= const['player_other']['pistol_dmg']
            case "shotgun":
                self.health_points -= const['player_other']['shotgun_dmg']
            case "bow":
                self.health_points -= const['player_other']['bow_dmg']
            case _:
                pass

class MeleeEnemy(Enemy):
    """
    Class for melee enemies

    Args:
        Enemy (object): Parent class
    """
    def update(self) -> None:
        Enemy.update(self)

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
