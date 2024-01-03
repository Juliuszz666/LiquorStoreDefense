import pygame


class AliveBeing(pygame.sprite.Sprite):
    """
    Parent and abstract class for player and enemies
    """

    def __init__(self, being_dict, position):
        """Abstract constructor

        Args:
            being_dict (dictionary):\n
            Abstract dicitonary containint:
                \t-health\n
                \t-speed\n
                \t-source file of being's image, and it's scale\n
            position (tuple): initial position of being
        """
        pygame.sprite.Sprite.__init__(self)
        self.health_points = being_dict['hp']
        self.speed = being_dict['speed']
        (self.position_x, self.position_y) = position
        img = pygame.image.load(being_dict['src_file'])
        self.graphics = pygame.transform.scale_by(img, being_dict['scale'])
        self.rect = self.graphics.get_rect()
        self.rect.topleft = (self.position_x, self.position_y)

    def update(self) -> None:
        """Abstract class does nothing but it's convinient hook
        for child classes where we would upadate all sprites
        """
        pygame.sprite.Sprite.update(self)
