from settings import *
import pygame
import math
import screen


class ThrownObject(pygame.sprite.Sprite):
    """
    Abstract class for every bullet-like object in game
    """

    def __init__(self, bullet_dict, pos):
        """Abstract constructor

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
        img = pygame.image.load(bullet_dict['src_file'])
        self.graphics = pygame.transform.scale_by(img, bullet_dict['scale'])
        self.rect = self.graphics.get_rect()
        self.rect.bottomleft = (self.position_x, self.position_y)
        self.damage = bullet_dict['dmg']
        self.speed = bullet_dict['speed']
        self.direction = bullet_dict['dir']

    def update(self):
        """
        Fuction verifies if thrown object is in playable area and displays it
        """

        if self.rect.top <= settings['SCREEN_HEIGHT'] / 10:
            self.kill()
        if self.rect.bottom >= settings['SCREEN_HEIGHT']:
            self.kill()
        if self.rect.right >= settings['SCREEN_WIDTH']:
            self.kill()
        if self.rect.left <= 0:
            self.kill()

        screen.SCREEN.blit(self.graphics, self.rect)


class PistolBullet(ThrownObject):

    def __init__(self, pos):
        ThrownObject.__init__(self, const['b_pistol'], pos)

    def update(self):
        """
        Fucntion does the same thing as parent method and additionaly
        moves bullet
        """
        ThrownObject.update(self)
        self.rect.move_ip(self.speed * self.direction, 0)


class ShotgunBullet(ThrownObject):

    def __init__(self, pos, angle, dir_y):
        """
        This constructor additionaly takes angle
        and dir_y to make the shotgun effect

        Args:
            angle (degrees): delta angle
            dir_y (-1, 0, 1): up/none/down
        """
        ThrownObject.__init__(self, const['b_shotgun'], pos)
        self.angle = math.radians(angle)
        self.dir_y = dir_y

    def update(self):
        """
        Fucntion does the same thing as parent method and additionaly
        moves bullet
        """
        ThrownObject.update(self)
        self.rect.move_ip(self.speed * self.direction * math.cos(self.angle),
                          self.dir_y * self.speed * math.sin(self.angle))


class Arrow(ThrownObject):

    def __init__(self, pos, angle):
        """
        This constructor additionaly takes angle
        and dir_y to make the parabolic movement effect

        Args:
            angle (degrees): delta angle
            dir_y (-1, 0, 1): up/none/down
        """
        ThrownObject.__init__(self, const['arrow'], pos)
        self.angle = math.radians(angle)
        self.speed_x = math.cos(self.angle) * self.speed
        self.speed_y = -math.sin(self.angle) * self.speed

    def update(self):
        """
        Fucntion does the same thing as parent method and additionaly
        moves arrow
        """
        ThrownObject.update(self)

        self.rect.move_ip(self.speed_x, self.speed_y)
        self.speed_y += const['arrow']['gravity_a']

        if self.rect.top >= self.position_y:
            self.kill()


class Bottle(ThrownObject):

    def __init__(self, pos, angle):
        """
        This constructor additionaly takes angle
        and dir_y to make the parabolic movement effect

        Args:
            angle (degrees): delta angle
            dir_y (-1, 0, 1): up/none/down
        """
        ThrownObject.__init__(self, const['bottle'], pos)
        self.angle = math.radians(angle)
        self.speed_x = math.cos(self.angle) * self.speed
        self.speed_y = -math.sin(self.angle) * self.speed

    def update(self):
        """
        Fucntion does the same thing as parent method and additionaly
        moves bottle
        """
        ThrownObject.update(self)

        self.rect.move_ip(self.speed_x*self.direction, self.speed_y)
        self.speed_y += const['arrow']['gravity_a']
        if self.rect.top >= self.position_y:
            self.kill()
