import pygame


class Alive_Being:
    """
    Parent class for player and enemies
    """
    def __init__(self, health, speed, position, width, height, aura_range):
        """Constructor

        Args:
            health (int): it's obvious
            speed (int): it's obvious
            position (tuple): (x,y)
            width (int): used only to generate rect
            height (int): used only to generate rect
            visible (bool): used when being is destroyed
            aura_range (int): used for melee damage both for player and enemies
        """
        self.visible = True
        self.health_points = health
        self.speed = speed
        (self.position_x, self.position_y) = position
        self.hitbox = pygame.Rect(self.position_x, self.position_y, width, height)
        self.damage_aura = pygame.rect.Rect((self.position_x-((aura_range - width)/2),
                                             self.position_y-((aura_range -height)/2)), 
                                            (aura_range, aura_range))
        """
            damage_aura: area of melee damage
            hitbox: obvious??
        """