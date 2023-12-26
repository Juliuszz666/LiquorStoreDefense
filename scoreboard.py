import json
import pygame
from screen import SCREEN, BG, generate_buttons

def update_scoreboard(user_score, username):
    try:
        with open('json/scoreboard.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
        
    new_entry = {'USER': username, 'SCORE': user_score}
    data.append(new_entry)

    with open('json/scoreboard.json', 'w') as file:
        json.dump(data, file, indent=2)
        
def load_scoreboard():
    try:
        with open('json/scoreboard.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

def scoreboard():
    scores = load_scoreboard()
    scores = sorted(scores, key=lambda dict: dict['SCORE'], reverse=True)
    max_rows = 10
    index = 0
    scoreboard_font = pygame.sysfont.SysFont("Times new roman", 35)
    titles_font = pygame.sysfont.SysFont("Calibri", 50)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(mouse_position):
                        running_score = False
                
        SCREEN.blit(BG, (0,0))
        
        score_title_bg = pygame.Rect(0,0,400,75)
        score_title_bg.center = (SCREEN.get_width()/2, SCREEN.get_height()/8)
        pygame.draw.rect(SCREEN, "red", score_title_bg, 0, 15)
        
        score_title_text = titles_font.render("SCOREBOARD", True, "white")
        score_title_rect = score_title_text.get_rect()
        score_title_rect.center = (SCREEN.get_width()/2, SCREEN.get_height()/8)
        SCREEN.blit(score_title_text, score_title_rect)
        
        score_bg = pygame.Rect(0,0, 400, 375)
        score_bg.center = (SCREEN.get_width()/2, SCREEN.get_height()/4+5*35)
        pygame.draw.rect(SCREEN, "black", score_bg, 0, 5)
        if len(scores):
            for i in range(min(len(scores), max_rows)):
                score_data = scores[index+i]
                if score_data['SCORE']==10**6:
                    score_text_user = scoreboard_font.render(f"{score_data['USER']}: ", True, (0, 255, 0))
                    score_text = scoreboard_font.render(f"{score_data['SCORE']}", True, (0, 255, 0))
                else:
                    score_text_user = scoreboard_font.render(f"{score_data['USER']}: ", True, (255, 255, 255))
                    score_text = scoreboard_font.render(f"{score_data['SCORE']}", True, (255, 255, 255))
                    
                score_rect_user = score_text_user.get_rect()
                score_rect_user.left = SCREEN.get_width()/2-185
                score_rect_user.top = SCREEN.get_height()/4 + i * 35
                

                score_rect = score_text.get_rect()
                score_rect.right = SCREEN.get_width()/2+185
                score_rect.top = SCREEN.get_height()/4 + i * 35
                
                SCREEN.blit(score_text_user, score_rect_user)
                SCREEN.blit(score_text, score_rect)
            
        button_texts = ["Menu"]
        mouse_position = pygame.mouse.get_pos()
        buttons = generate_buttons(titles_font, 1, mouse_position, button_texts, 8/7)
        pygame.display.flip()