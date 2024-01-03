import pygame
from alive_being import AliveBeing
from settings import *
from classes_bullets import *
from sprites_groups import *
from scoring import *


class Player(AliveBeing):
    """
    Player class

    Args:
        AliveBeing (object): Parent class
    """

    def __init__(self, position):
        """
        Player's constructor

        Args:
            position (tuple): spawning position
        """
        AliveBeing.__init__(self, const['player_init'], position)
        self.cooldown_melee = 0
        self.cooldown_pistol = 0
        self.cooldown_shotgun = 0
        self.cooldown_bow = 0
        self.cooldown_medkit = 0
        self.selected = 1
        self.flag = True
        self.dead = False

    def cooldown_list(self):
        """
        Function crucial for displaying cooldown on screen

        Returns:
            2 list: first one are current cooldwons,
            second are maximum cooldown
        """
        max_cd = const['player_other']
        cooldown_lists = []
        cooldowns_current = [self.cooldown_melee,
                             self.cooldown_pistol,
                             self.cooldown_shotgun,
                             self.cooldown_bow,
                             self.cooldown_medkit]
        cooldowns_max = [max_cd['m_cooldown'],
                         max_cd['p_cooldown'],
                         max_cd['s_cooldown'],
                         max_cd['b_cooldown'],
                         max_cd['medkit_cooldown']]
        cooldown_lists.append(cooldowns_current)
        cooldown_lists.append(cooldowns_max)
        return cooldown_lists

    def cooldown_reduction(self):
        """
        Fuction responsible for reducing items' cooldowns over time
        """
        self.cooldown_bow -= 1
        self.cooldown_medkit -= 1
        self.cooldown_melee -= 1
        self.cooldown_pistol -= 1
        self.cooldown_shotgun -= 1

    def is_use(self):
        """
        Fuciton check if space is pressed

        Returns:
            Bool: pressed-True/not pressed-False
        """
        return pygame.key.get_pressed()[pygame.K_SPACE]

    def movement(self):
        """
        Movement controls and veryfication if player is not going outside screen
        """
        self.move = pygame.key.get_pressed()
        if self.move[pygame.K_w] and self.rect.top > settings['SCREEN_HEIGHT'] / 10:
            self.rect.move_ip(0, -self.speed)
        if self.move[pygame.K_a] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if self.move[pygame.K_s] and self.rect.bottom < settings['SCREEN_HEIGHT']:
            self.rect.move_ip(0, self.speed)
        if self.move[pygame.K_d] and self.rect.right < settings['SCREEN_WIDTH']:
            self.rect.move_ip(self.speed, 0)

    def handling_equipment(self):
        """
        Function responsible for weapon selection and using them.
        Function also changes graphics of player
        depending on weapon selected\n
        self.flag makes that selected weapon changes only
        when other weapon is selected
        """

        player_controls = pygame.key.get_pressed()
        if player_controls[pygame.K_1] and self.flag:
            self.selected = 1
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
                img = pygame.image.load(const['player_graphics'][0])
                self.graphics = pygame.transform.scale_by(
                    img, const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.machete()
            case 2:
                pos = self.rect.topleft
                img = pygame.image.load(const['player_graphics'][1])
                self.graphics = pygame.transform.scale_by(
                    img, const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.pistol()
            case 3:
                pos = self.rect.topleft
                img = pygame.image.load(const['player_graphics'][2])
                self.graphics = pygame.transform.scale_by(
                    img, const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.shotgun()
            case 4:
                pos = self.rect.topleft
                img = pygame.image.load(const['player_graphics'][3])
                self.graphics = pygame.transform.scale_by(
                    img, const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.bow()
            case 5:
                pos = self.rect.topleft
                img = pygame.image.load(const['player_graphics'][4])
                self.graphics = pygame.transform.scale_by(
                    img, const['player_init']['scale'])
                self.rect = self.graphics.get_rect()
                self.rect.topleft = pos
                self.medkit()

    def machete(self):
        """
        Function for player's melee damage, it creates damage aura which
        if there is no cooldown and player uses it
        aura give damage to every enemy in it's range
        """
        self.machete_aura = pygame.Rect(
            0, 0, const['player_other']['aura_range'], const['player_other']['aura_range'])
        self.machete_aura.center = self.rect.center
        if self.is_use() and self.cooldown_melee <= 0:
            self.cooldown_melee = const['player_other']['m_cooldown']
            for enemy in all_enemies:
                if enemy.rect.colliderect(self.machete_aura):
                    enemy.get_damage(const['player_other']['machete_dmg'])

    def pistol(self):
        """
        Fuction creates pistol bullets
        """
        if self.is_use() and self.cooldown_pistol <= 0:
            bullet_player = PistolBullet(
                (self.rect.centerx + const['pistol_vec'][0],
                 self.rect.centery + const['pistol_vec'][1]))
            all_sprite.add(bullet_player)
            pistol_bullets.add(bullet_player)
            bullets.add(bullet_player)
            player_bullets.add(bullet_player)
            self.cooldown_pistol = const['player_other']['p_cooldown']

    def shotgun(self):
        """
        Fuction creates 3 shotgun bullets which have different movement path
        """
        if self.is_use() and self.cooldown_shotgun <= 0:
            for i in range(-1, 2, 1):
                bullet_player = ShotgunBullet((self.rect.centerx + const['shotgun_vec'][0],
                                               self.rect.centery + const['shotgun_vec'][1]),
                                              const['b_shotgun']['angle'], i)
                all_sprite.add(bullet_player)
                bullets.add(bullet_player)
                shotgun_bullets.add(bullet_player)
                player_bullets.add(bullet_player)
            self.cooldown_shotgun = const['player_other']['s_cooldown']
        else:
            self.cooldown_shotgun -= 1

    def bow(self):
        """
        Fuction creates arrows
        """
        if self.is_use() and self.cooldown_bow <= 0:
            bullet_player = Arrow(
                (self.rect.centerx + const['bow_vec'][0],
                 self.rect.centery + const['bow_vec'][1]),
                const['arrow']['angle'])
            all_sprite.add(bullet_player)
            bullets.add(bullet_player)
            arrows.add(bullet_player)
            player_bullets.add(bullet_player)
            self.cooldown_bow = const['player_other']['b_cooldown']

    def medkit(self):
        """
        Fuction is responsible for using medkit and giving penalty for using it
        """
        if self.is_use() and self.cooldown_medkit <= 0:
            self.health_points += const['player_other']['medkit_healing']
            self.cooldown_medkit = const['player_other']['medkit_cooldown']
            add_score(-5)

    def update(self):
        """
        Function is combination of function, and it's crucial
        for player's proper working
        """
        AliveBeing.update(self)

        self.cooldown_reduction()
        self.movement()
        self.handling_equipment()

    def get_damage(self, damage):
        """This function is called when player is supposed to take damage
        from enemies, this function also is responsible for killing player

        Args:
            damage (int/float): damage amount
        """
        if self.health_points > 0:
            self.health_points -= damage
        if self.health_points <= 0:
            self.dead = True
            self.kill()

    def is_dead(self):
        """
        Checks if player is dead

        Returns:
            Bool: dead/alive - true/false
        """
        return self.dead

    def reset(self):
        """
        Function is called when player wants a replay
        to make sure that player parameters are allright
        """
        self.health_points = const['player_init']['hp']
        self.rect.topleft = (self.position_x, self.position_y)
        self.dead = False
        self.cooldown_melee = 0
        self.cooldown_pistol = 0
        self.cooldown_shotgun = 0
        self.cooldown_bow = 0
        self.cooldown_medkit = 0


"""Initialazing player"""
protagonist = Player(const['player_other']['ini_spawn'])
all_sprite.add(protagonist)
