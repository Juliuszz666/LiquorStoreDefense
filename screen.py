import pygame
from player import protagonist
from settings import *

selected = 1


def generate_buttons(font, num_of_buttons, mouse_pos, texts, height_co):
    """
    Function responsible for generator action buttons

    Args:
        font
        num_of_buttons (int): number of buttons to be generated
        mouse_pos (tuple: current mouse pos for hover effect
        texts (list of str): text to be displayed on buttons
        height_co (float): height coefficient
        (where vertically button will be places)

    Returns:
        List of buttons (rects) for further interaction
    """
    buttons = []
    for i in range(num_of_buttons):
        button_rect = pygame.Rect(0, 0, BUTTON[0], BUTTON[1])
        button_rect.center = ((i+1)*SCREEN.get_width()/(num_of_buttons+1), SCREEN.get_height()/height_co)
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(SCREEN, "purple", button_rect, 0, RADIUS['big'])
        else:
            pygame.draw.rect(SCREEN, "red", button_rect, 0, RADIUS['big'])
        buttons.append(button_rect)
        button_text = font.render(texts[i], True, WHITE)
        button_text_rect = button_text.get_rect()
        button_text_rect.center = button_rect.center
        SCREEN.blit(button_text, button_text_rect)
    return buttons


def display(hp, score):
    """
    Funciton responsible for displaying game

    Args:
        hp (int): player's health
        score (int): player's score
    """

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(PLAYER_DETAILS, (0, 0))

    # displaying player
    SCREEN.blit(protagonist.graphics, protagonist.rect)

    display_health(hp)
    display_weapons()
    display_score(score)


def display_health(player_hp):
    """
    Function responsible for displaying current player health

    Args:
        player_hp (int): player's health
    """
    if player_hp > 0:
        hp_percent = player_hp/const['player_init']['hp']
        if hp_percent > 1:
            hp_percent = 1
    else:
        hp_percent = 0

    hp_border_display = pygame.Surface((HP_BORDER_WIDTH, EQ_ITEM_HEIGHT))
    hp_border_display.fill("black")

    hp_width = (HP_BORDER_WIDTH - 2 * BORDER_VALUE)*hp_percent
    hp_display = pygame.Surface((hp_width, EQ_ITEM_HEIGHT - 2 * BORDER_VALUE))
    hp_display.fill(RED)

    SCREEN.blit(hp_border_display, ((SCREEN.get_width()-HP_BORDER_WIDTH)-EQ_ITEM_BASE, EQ_ITEM_BASE))
    SCREEN.blit(hp_display, ((SCREEN.get_width() - HP_BORDER_WIDTH - EQ_ITEM_BASE + BORDER_VALUE,
                              EQ_ITEM_BASE + BORDER_VALUE)))

    hp_font = pygame.sysfont.SysFont("Times New Roman", FONT_SIZE['L'])
    hp_counter = hp_font.render("HP: "+str(player_hp), (0, 0, 0), "white")
    hp_prompt = hp_counter.get_rect()
    hp_prompt.center = (SCREEN.get_width() - EQ_ITEM_BASE - (HP_BORDER_WIDTH / 2), SCREEN.get_height() / 20)

    SCREEN.blit(hp_counter, hp_prompt)


def display_weapons():
    """
    Function responsible for displaying player's equipment
    with items' cooldowns
    """

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

    eq_item = []
    cooldowns = protagonist.cooldown_list()

    # blitting items
    for i in range(5):
        if cooldowns[0][i] > 0:
            cooldown_percent = cooldowns[0][i] / cooldowns[1][i]
        else:
            cooldown_percent = 0

        border = pygame.Rect(EQ_ITEM_BASE + i * EQ_ITEM_SPACE, EQ_ITEM_BASE, EQ_ITEM_HEIGHT, EQ_ITEM_HEIGHT)

        equipment_item = pygame.image.load(f"img/item{i + 1}.png").convert_alpha()
        equipment_item = pygame.transform.scale(equipment_item, (EQ_ITEM_HEIGHT - BORDER_VALUE * 2,
                                                                 EQ_ITEM_HEIGHT - BORDER_VALUE * 2))

        eq_item.append(equipment_item)
        eq_item_cooldown = pygame.Surface((EQ_ITEM_HEIGHT, EQ_ITEM_HEIGHT * cooldown_percent), pygame.SRCALPHA)
        eq_item_cooldown.fill(YELLOW_T)

        if i == selected - 1:
            pygame.draw.rect(SCREEN, "pink", border, BORDER_VALUE)
        else:
            pygame.draw.rect(SCREEN, "brown", border, BORDER_VALUE)

        SCREEN.blit(equipment_item, (EQ_ITEM_BASE + i * EQ_ITEM_SPACE + BORDER_VALUE,
                                     EQ_ITEM_BASE + BORDER_VALUE))
        SCREEN.blit(eq_item_cooldown, (EQ_ITEM_BASE + i * EQ_ITEM_SPACE,
                                       EQ_ITEM_BASE+EQ_ITEM_HEIGHT*(1-cooldown_percent)))


def display_score(score):
    """
    Function responsible for displaying player's current score

    Args:
        score (int): player's score
    """
    score_surface = pygame.Surface((300, EQ_ITEM_HEIGHT))
    score_surface.fill("black")
    score_rect = score_surface.get_rect()
    score_rect.center = (SCREEN.get_width()/2, SCREEN.get_height()/20)

    SCREEN.blit(score_surface, score_rect)

    score_font = pygame.sysfont.SysFont("Arial", FONT_SIZE['L'])
    score_text = score_font.render(str(score), (0, 0, 0), "white")
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (SCREEN.get_width()/2, SCREEN.get_height()/20)

    SCREEN.blit(score_text, score_text_rect)
