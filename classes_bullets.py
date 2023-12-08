import pygame
import classes_beings as entities
import math

class ThrownObject(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__()
        
    def update(self) -> None:
        pygame.sprite.Sprite.update(self)