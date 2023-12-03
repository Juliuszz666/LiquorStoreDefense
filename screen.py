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
    match selected:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            entities.player.medkit()
    
    for i in range(0,5):
            
        border = pygame.Rect(0,0, eq_item_height-const['ITEM_BORDER']*2, eq_item_height-const['ITEM_BORDER']*2)
                
        equipment_item = pygame.image.load(f"img/item{i+1}.png")
        pygame.transform.scale(equipment_item,(eq_item_height-const['ITEM_BORDER']*2, eq_item_height-const['ITEM_BORDER']*2))
        eq_item.append(equipment_item)                   
        if i == selected -1:
            pygame.draw.rect(eq_item[i], "pink", border, const['ITEM_BORDER'])    
        else:
            pygame.draw.rect(eq_item[i], "yellow", border, const['ITEM_BORDER'])  
        screen.blit(eq_item[i], (eq_item_base + (i*eq_item_space), eq_item_base))
        
     