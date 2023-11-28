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
    
    eq_item = []
    
    if entities.player.handling_equipment():
        selected = entities.player.handling_equipment()
    
    for i in range(0,9):
            
        border = pygame.Surface((eq_item_height, eq_item_height))
        border.fill("black")
        if i == selected -1:
            border.fill("pink")
        equipment_item = pygame.Surface((eq_item_height-(2*const['ITEM_BORDER']), eq_item_height-(2*const['ITEM_BORDER'])))
        equipment_item.fill("white")
        border.blit(equipment_item, (const['ITEM_BORDER'], const['ITEM_BORDER']))
        eq_item.append(border)
        
                   
    
        screen.blit(eq_item[i], (eq_item_base + (i*eq_item_space), eq_item_base))
    
    pygame.display.flip()


    