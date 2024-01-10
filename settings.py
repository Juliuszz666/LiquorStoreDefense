import pygame
import json

with open('json/constants.json', 'r') as constants:
    const = json.load(constants)

with open('json/settings.json', 'r') as options:
    settings = json.load(options)


def get_username():
    return settings['USERNAME']


def save_username(text):
    """
    Dumps current username to json file

    Args:
        text (str): recent username input
    """
    settings['USERNAME'] = text
    with open('json/settings.json', 'w') as file:
        json.dump(settings, file, indent=2)


# colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREEN_T = (0, 255, 0, 128)
L_GREEN = (144, 238, 144)
RED = (255, 0, 0)
D_RED = (139, 0, 0)
D_GREY = (32, 32, 32)
YELLOW_T = (255, 255, 0, 160)
GOLD = (255,215,0)

# display settings

display_dict = const['display']
FONT_SIZE = display_dict['font-sizes']
RADIUS = display_dict['radius']

# widths and heights of some surfaces/rects

BUTTON = [300, 100]
CREDITS = [400, 100]
SCORE_TITLE_BG = [400, 75]
SCORE_BG = [400, 375]
USERNAME = [300, 50]

# some other cooeficients related with displaying

BORDER_VALUE = display_dict['border']

MENU_HEIGHT_CO = 2
SCORE_HEIGHT_CO = 8/7
USERNAME_HEIGHT_CO = 5.5/8
CREDITS_HEIGHT_CO = 0.875

CREDITS_DELTA = 0.005
CREDITS_BORDER = 5

SCORE_DELTA = 10

SCREEN = pygame.display.set_mode(
    (settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']))
BG = pygame.image.load("img/tlo-dla-pawelka.png")
PLAYER_DETAILS = pygame.Surface((SCREEN.get_width(),
                                SCREEN.get_height()/10), pygame.SRCALPHA)
PLAYER_DETAILS.fill(GREEN_T)

EQ_ITEM_HEIGHT = int(PLAYER_DETAILS.get_height()*0.8)
EQ_ITEM_SPACE = int(PLAYER_DETAILS.get_height()*0.9)
EQ_ITEM_BASE = int(SCREEN.get_height()/100)

# other settings

MAX_ROWS = 10
MAX_LEN = 12
HP_BORDER_WIDTH = 300
