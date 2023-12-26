import pygame
import webbrowser
import settings
from screen import generate_buttons, screen, bg
from sys import exit



def blit_credits():
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
    
    return credits

def main_menu():
    active = False
    running_menu = True
    while running_menu:
        
        screen.blit(bg, (0,0))
        
        event_key = pygame.key.get_pressed()
        button_texts = ["Scoreboard", "Play", "Quit"]
        mouse_position = pygame.mouse.get_pos()
        
        
        menu_font = pygame.sysfont.SysFont("Arial", 50)
        username_font = pygame.sysfont.SysFont("Calibri", 30)
        
        buttons = generate_buttons(menu_font, 3, mouse_position, button_texts, 2)
        credits = blit_credits()
        
        username_bg = pygame.Rect(0,0, 300, 50)
        username_bg.centerx = screen.get_width()/2
        username_bg.bottom = 5.5 * screen.get_height()/8 - 3
        pygame.draw.rect(screen, "red", username_bg, 0, 10)
        
        username_text = username_font.render("You are playing as:", True, "white")
        username_rect = username_text.get_rect(center = username_bg.center)
        screen.blit(username_text, username_rect)
        
        text = settings.get_username()
        max_len = 12
        text_input = pygame.Rect(0,0,300,50)
        text_input.centerx = screen.get_width()/2
        text_input.top = 5.5 * screen.get_height()/8 + 3
        if not active:
            pygame.draw.rect(screen, "black", text_input, 0, 10)
        if active:
            pygame.draw.rect(screen, (32,32,32), text_input, 0, 10)
        
        text_sur = username_font.render(text, True, "white")
        text_rect = text_sur.get_rect(center = text_input.center)
        screen.blit(text_sur, text_rect)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event_key[pygame.K_ESCAPE]:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_input.collidepoint(mouse_position):
                    active = True
                else:
                    active = False
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
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text)<max_len:
                            text+=event.unicode
                            
        settings.save_username(text)
        pygame.display.flip()
        
    match action:
        case "scoreboard":
            return "scoreboard"
        case "game":
            return "game"