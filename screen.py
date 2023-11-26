import pygame
import classes_beings as entities


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
selected = 1

def display(player):

    global selected
    BORDER = 5

    screen.fill("purple")
    player_details = pygame.Surface((screen.get_width(), 
                                     screen.get_height()/10))

    player_details.fill("green")
    screen.blit(player_details, (0,0))

    eq_item_height = int(player_details.get_height()*0.8)
    eq_item_space = int(player_details.get_height()*0.9)

    
    