import pygame
import enemies
import player
from settings import *

screen_flag = 0
if settings['FULLSCREEN']:
    screen_flag = pygame.FULLSCREEN

screen = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']), screen_flag)
selected = 1

def display():
    global selected

    bg = pygame.transform.scale2x(pygame.image.load("img/bg_test.jpg"))    
    screen.blit(bg, (0, 0))
    
    player_details = pygame.Surface((screen.get_width(), 
                                     screen.get_height()/10))
    player_details.fill("green")
    screen.blit(player_details, (0,0))
    

    eq_item_height = int(player_details.get_height()*0.8)
    eq_item_space = int(player_details.get_height()*0.9)
    eq_item_base = int(screen.get_height()/100)
    
    eq_item = []
    
    if player.protagonist.handling_equipment():
        selected = player.protagonist.handling_equipment()
    match selected:
        case 1:
            player.protagonist.machete()
        case 2:
            player.protagonist.pistol()
        case 3:
            player.protagonist.shotgun()
        case 4:
            player.protagonist.bow()
        case 5:
            player.protagonist.medkit()
            
    
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

def display_defeat():
    screen.fill("black")
    defeat_font = pygame.sysfont.SysFont('arial', 50)
    defeat_text = defeat_font.render("YOU LOST", True, "white")
    screen.blit(defeat_text, (settings['SCREEN_WIDTH']/2, settings['SCREEN_HEIGHT']/2))    
    freeze = True
     