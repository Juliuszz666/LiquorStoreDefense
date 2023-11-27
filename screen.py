import pygame
import classes_beings as entities
from settings import *

screen_flag = 0
if settings['FULLSCREEN']:
    screen_flag = pygame.FULLSCREEN

screen = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']), screen_flag)
selected = 1

def display():
    global selected

    screen.fill("blue")    
    
    player_details = pygame.Surface((screen.get_width(), 
                                     screen.get_height()/10))
    player_details.fill("green")
    screen.blit(player_details, (0,0))

    eq_item_height = int(player_details.get_height()*0.8)
    eq_item_space = int(player_details.get_height()*0.9)
    eq_item_base = int(screen.get_height()/100)
    
    equipment_item = []
    
    for i in range(0,9):
        equipment_item.append(pygame.Surface((eq_item_height, eq_item_height)))
        equipment_item[i].fill("white")
        player_details.blit(equipment_item[i], (eq_item_base+(i*eq_item_space), eq_item_base))
    
    pygame.display.flip()


    