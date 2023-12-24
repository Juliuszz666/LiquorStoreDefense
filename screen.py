import pygame
import webbrowser
from player import protagonist
from settings import *
from scoreboard import *


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

def generate_buttons(font, num_of_buttons, mouse_pos, texts):
    buttons = []
    for i in range(num_of_buttons):
        button_rect = pygame.Rect(0,0, 300, 100)
        button_rect.center = ((i+1)*screen.get_width()/(num_of_buttons+1), screen.get_height()/2)
        if button_rect.collidepoint(mouse_pos):

            pygame.draw.rect(screen, "purple", button_rect, 0, 15)
        else:

            pygame.draw.rect(screen, "red", button_rect, 0, 15)
        buttons.append(button_rect)
        button_text = font.render(texts[i], True, "white")
        button_text_rect = button_text.get_rect()
        button_text_rect.center = button_rect.center
        screen.blit(button_text, button_text_rect)
    return buttons



def scoreboard():
    scores = load_scoreboard()
    scores = sorted(scores, key=lambda dict: dict['SCORE'], reverse=True)
    max_rows = 10
    index = 0
    scoreboard_font = pygame.sysfont.SysFont("Times new roman", 35)
    running_score = True
    while running_score:
        event_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event_key[pygame.K_ESCAPE]:
                exit()
            if event_key[pygame.K_p]:
                running_score = False
            if event_key[pygame.K_DOWN] and index<len(scores)-max_rows:
                index+=1
            if event_key[pygame.K_UP] and index>0:
                index-=1
        screen.blit(bg, (0,0))
        score_bg = pygame.Rect(0,0, 200, 400)
        score_bg.center = (screen.get_width()/2, screen.get_height()/6+5*35)
        pygame.draw.rect(screen, "black", score_bg, 0, 5)
        for i in range(max_rows):
            score_data = scores[index+i]
            score_text = scoreboard_font.render(f"{score_data['USER']}: {score_data['SCORE']}", True, (255, 255, 255))
            score_rect = score_text.get_rect()
            score_rect.left = screen.get_width()/2-70
            score_rect.top = screen.get_height()/6 + i * score_rect.height
            screen.blit(score_text, score_rect)
            
        button_texts = ["Menu", "Quit game"]
        mouse_position = pygame.mouse.get_pos()
        buttons = generate_buttons(scoreboard_font, 2, mouse_position, button_texts)
        pygame.display.flip()

def main_menu():
    running_menu = True
    while running_menu:
        event_key = pygame.key.get_pressed()
        screen.blit(bg, (0,0))
        
        button_texts = ["Scoreboard", "Play", "Quit"]
        mouse_position = pygame.mouse.get_pos()
        
        
        menu_font = pygame.sysfont.SysFont("Arial", 50)
        buttons = generate_buttons(menu_font, 3, mouse_position, button_texts)
            
        credits_texts = ["Software by Julian Bednarek", "Graphics by Paweł Korabiewski"]
        credit_font = pygame.sysfont.SysFont("Times New Roman", 25, False, True)
        credits = []
        credit_bg = pygame.Rect(0,0,400, 100)
        credit_bg.center = (screen.get_width()/2, screen.get_height()*0.875)
        pygame.draw.rect(screen, "white", credit_bg, 5, 15)
        
        for i in range(len(credits_texts)):
            credits_text = credit_font.render(credits_texts[i], True, "white")
            credits_rect = credits_text.get_rect()
            credits_rect.centerx = screen.get_width()/2
            match i:
                case 0:
                    credits_rect.bottom = screen.get_height()*0.87
                case 1:
                    credits_rect.top = screen.get_height()*0.88
            credits.append(credits_rect)
            screen.blit(credits_text, credits_rect)                    
        

            
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
                                action = "scoreboard"
                                running_menu = False
                            case 1:
                                action = "game"
                                running_menu = False
                            case 2:
                                exit()
                for i in range(len(credits)):
                    if credits[i].collidepoint(mouse_position):
                        match i:
                            case 0:
                                webbrowser.open(r"https://github.com/Juliuszz666")
                            case 1:
                                webbrowser.open(r"https://www.instagram.com/xmakaronito/")

        pygame.display.flip()
        
    match action:
        case "scoreboard":
            return "scoreboard"
        case "game":
            return "game"
        
def display(hp, score):


    screen.blit(bg, (0, 0))
    screen.blit(player_details, (0, 0))
    display_health(hp)
    display_weapons()
    display_score(score)

def display_health(player_hp):
    if player_hp > 0:
        hp_percent = player_hp/const['player_init']['hp']
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
    hp_counter = hp_font.render("HP: "+str(player_hp), (0, 0, 0), "white")
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

def display_score(score):
    score_surface = pygame.Surface((300, eq_item_height))
    score_surface.fill("black")
    score_rect = score_surface.get_rect()
    score_rect.center = (screen.get_width()/2, screen.get_height()/20)
    screen.blit(score_surface, score_rect)
    score_font = pygame.sysfont.SysFont("Arial", 50)
    score_text = score_font.render(str(score), (0,0,0), "white")
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (screen.get_width()/2, screen.get_height()/20)
    screen.blit(score_text, score_text_rect)

def display_defeat(score):
    running_def = True
    #user = "Julian"
    update_scoreboard(score)
    while running_def:

        
        screen.blit(bg, (0,0))
        
        defeat_font = pygame.sysfont.SysFont('arial', 50)
        
        defeat_text = defeat_font.render("YOU LOST", True, "white")
        defeat_rect = defeat_text.get_rect()
        defeat_rect.centerx = screen.get_width()/2
        defeat_rect.bottom = screen.get_height()/4
        
        defeat_score_text = defeat_font.render(f"Score: {score}", True, "white")
        defeat_score_rect = defeat_score_text.get_rect()
        defeat_score_rect.centerx = screen.get_width()/2
        defeat_score_rect.top = screen.get_height()/4
        
        screen.blit(defeat_text, defeat_rect)
        screen.blit(defeat_score_text, defeat_score_rect)
        
        button_texts = ["Scoreboard", "Menu", "Quit game"]
        mouse_position = pygame.mouse.get_pos()
        buttons = generate_buttons(defeat_font, 3, mouse_position, button_texts)
            
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
                                running_def = False
                                scoreboard()
                            case 1:
                                running_def = False
                            case 2:
                                exit()
        pygame.display.flip()
        
