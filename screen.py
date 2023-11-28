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
    
    costam = pygame.Surface((15, 15))
    costam.fill("pink")
    screen.blit(costam, (5,5))

#    eq_item_height = int(player_details.get_height()*0.8)
#    eq_item_space = int(player_details.get_height()*0.9)
#    eq_item_base = int(screen.get_height()/100)
#    
#    #eq_item = []
#    
#    #for i in range(0,9):
#    equipment_item = pygame.Surface((eq_item_height, eq_item_height))
#    equipment_item.fill("white")
#    #    eq_item.append(equipment_item)
#    player_details.blit(equipment_item, (eq_item_base, eq_item_base))
    
    pygame.display.flip()


    