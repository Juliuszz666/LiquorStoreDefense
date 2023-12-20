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

    bg = pygame.image.load("img/background.png").convert()
    screen.blit(bg, (0, 0))

    player_details = pygame.Surface((screen.get_width(),
                                     screen.get_height()/10))
    player_details.fill("green")
    screen.blit(player_details, (0, 0))

    display_weapons(player_details)


def display_weapons(player_details):

    global selected
    select_controls = pygame.key.get_pressed()
    flag = True

    if select_controls[pygame.K_1] and flag:
        selected = 1
        flag = False
    if select_controls[pygame.K_2] and flag:
        selected = 2
        flag = False
    if select_controls[pygame.K_3] and flag:
        selected = 3
        flag = False
    if select_controls[pygame.K_4] and flag:
        selected = 4
        flag = False
    if select_controls[pygame.K_5] and flag:
        selected = 5
        flag = False
    else:
        flag = True

    eq_item_height = int(player_details.get_height()*0.8)
    eq_item_space = int(player_details.get_height()*0.9)
    eq_item_base = int(screen.get_height()/100)

    eq_item = []
    cooldowns = player.protagonist.cooldown_list()

    for i in range(5):
        if cooldowns[0][i] > 0:
            cooldown_percent = cooldowns[0][i] / cooldowns[1][i]
        else:
            cooldown_percent = 0

        border = pygame.Rect(eq_item_base + i * eq_item_space, eq_item_base, eq_item_height, eq_item_height)

        equipment_item = pygame.image.load(f"img/item{i + 1}.png")
        equipment_item = pygame.transform.scale(equipment_item, (eq_item_height - const['ITEM_BORDER'] * 2,
                                                                 eq_item_height - const['ITEM_BORDER'] * 2))

        eq_item.append(equipment_item)
        eq_item_cooldown = pygame.Surface((eq_item_height, eq_item_height * cooldown_percent), pygame.SRCALPHA)
        eq_item_cooldown.fill((255, 0, 0, 128))

        if i == selected - 1:
            pygame.draw.rect(screen, "pink", border, const['ITEM_BORDER'])
        else:
            pygame.draw.rect(screen, "brown", border, const['ITEM_BORDER'])

        screen.blit(equipment_item, (eq_item_base + i * eq_item_space + const['ITEM_BORDER'],
                                     eq_item_base + const['ITEM_BORDER']))
        screen.blit(eq_item_cooldown, (eq_item_base + i * eq_item_space,
                                       eq_item_base+eq_item_height*(1-cooldown_percent)))


def display_defeat():
    screen.fill("black")
    defeat_font = pygame.sysfont.SysFont('arial', 50)
    defeat_text = defeat_font.render("YOU LOST", True, "white")
    screen.blit(defeat_text, (settings['SCREEN_WIDTH']/2, settings['SCREEN_HEIGHT']/2))
    freeze = True
