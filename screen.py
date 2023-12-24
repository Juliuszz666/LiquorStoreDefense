import pygame
from player import protagonist
from settings import *


screen_flag = 0
if settings['FULLSCREEN']:
    screen_flag = pygame.FULLSCREEN

screen = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']), screen_flag)
bg = pygame.image.load("img/background.png")
player_details = pygame.Surface((screen.get_width(),
                                    screen.get_height()/10), pygame.SRCALPHA)
player_details.fill((0,255,0, 128))

eq_item_height = int(player_details.get_height()*0.8)
eq_item_space = int(player_details.get_height()*0.9)
eq_item_base = int(screen.get_height()/100)

selected = 1

def scoreboard():
    print("Chuj")
    exit()

def main_menu():
    running = True
    while running:
        event_key = pygame.key.get_pressed()
        screen.blit(bg, (0,0))
        
        button_texts = ["Scoreboard", "Play", "Quit"]
        mouse_position = pygame.mouse.get_pos()
        buttons = []
        
        menu_font = pygame.sysfont.SysFont("Arial", 50)
        for i in range(3):
            button_surface = pygame.Surface((300, 100))
            button_rect = button_surface.get_rect()
            button_rect.center = ((i+1)*screen.get_width()/4, screen.get_height()/2)
            if button_rect.collidepoint(mouse_position):
                button_surface.fill("purple")
            else:
                button_surface.fill("red")
            buttons.append(button_rect)
            screen.blit(button_surface, button_rect)
            button_text = menu_font.render(button_texts[i], True, "white")
            button_text_rect = button_text.get_rect()
            button_text_rect.center = button_rect.center
            screen.blit(button_text, button_text_rect)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event_key[pygame.K_ESCAPE]:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(mouse_position):
                        match i:
                            case 0:
                                return "scoreboard"
                            case 1:
                                return "game"
                            case 2:
                                exit()

        pygame.display.flip()
        
def display():


    screen.blit(bg, (0, 0))
    screen.blit(player_details, (0, 0))
    display_health()
    display_weapons()
    display_score()

def display_health():
    if protagonist.health_points > 0:
        hp_percent = protagonist.health_points/const['player_init']['hp']
        if hp_percent > 1:
            hp_percent = 1
    else:
        hp_percent = 0
    hp_border = 300
    hp_border_display = pygame.Surface((hp_border, eq_item_height))
    hp_border_display.fill("black")
    hp_width = (300- 2 * const['ITEM_BORDER'])*hp_percent
    hp_display = pygame.Surface((hp_width, eq_item_height- 2*const['ITEM_BORDER']))
    hp_display.fill((255,0,0))
    screen.blit(hp_border_display, ((screen.get_width()-300)-eq_item_base, eq_item_base))
    screen.blit(hp_display, ((screen.get_width()-300 - eq_item_base + const['ITEM_BORDER'], eq_item_base + const['ITEM_BORDER'])))
    hp_font = pygame.sysfont.SysFont("Times New Roman", 50)
    hp_counter = hp_font.render("HP: "+str(protagonist.health_points), (0, 0, 0), "white")
    hp_prompt = hp_counter.get_rect()
    hp_prompt.center = (screen.get_width()-eq_item_base-150, screen.get_height()/20)
    screen.blit(hp_counter, hp_prompt)

def display_weapons():

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

        border = pygame.Rect(eq_item_base + i * eq_item_space, eq_item_base, eq_item_height, eq_item_height)

        equipment_item = pygame.image.load(f"img/item{i + 1}.png").convert_alpha()
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

def display_score():
    score_local = protagonist.score
    score_surface = pygame.Surface((300, eq_item_height))
    score_surface.fill("black")
    score_rect = score_surface.get_rect()
    score_rect.center = (screen.get_width()/2, screen.get_height()/20)
    screen.blit(score_surface, score_rect)
    score_font = pygame.sysfont.SysFont("Arial", 50)
    score_text = score_font.render(str(score_local), (0,0,0), "white")
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (screen.get_width()/2, screen.get_height()/20)
    screen.blit(score_text, score_text_rect)

def display_defeat():
    running = True
    score = protagonist.score
    user = "Julian"
    with open("scoreboard.json", "a") as dump:
        json.dump(f"{user}: {score},\n", dump)
    while running:

        
        screen.blit(bg, (0,0))
        
        defeat_font = pygame.sysfont.SysFont('arial', 50)
        
        defeat_text = defeat_font.render("YOU LOST", True, "white")
        defeat_rect= defeat_text.get_rect()
        defeat_rect.centerx = screen.get_width()/2
        defeat_rect.bottom = screen.get_height()/4
        
        defeat_score_text = defeat_font.render(f"Score: {score}", True, "white")
        defeat_score_rect = defeat_score_text.get_rect()
        defeat_score_rect.centerx = screen.get_width()/2
        defeat_score_rect.top = screen.get_height()/4
        
        screen.blit(defeat_text, defeat_rect)
        screen.blit(defeat_score_text, defeat_score_rect)
        
        button_texts = ["Scoreboard", "Quit game"]
        mouse_position = pygame.mouse.get_pos()
        buttons = []
        
        for i in range(2):
            button_surface = pygame.Surface((300, 100))
            button_rect = button_surface.get_rect()
            button_rect.center = ((i+1)*screen.get_width()/3, screen.get_height()/2)
            buttons.append(button_rect)
            if button_rect.collidepoint(mouse_position):
                button_surface.fill("purple")
            else:
                button_surface.fill("red")
            screen.blit(button_surface, button_rect)
            button_text = defeat_font.render(button_texts[i], True, "white")
            button_text_rect = button_text.get_rect()
            button_text_rect.center = button_rect.center
            screen.blit(button_text, button_text_rect)
            
        event_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event_key[pygame.K_ESCAPE]:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(mouse_position):
                        match i:
                            case 0:
                                scoreboard()
                            case 1:
                                exit()
        pygame.display.flip()
        
