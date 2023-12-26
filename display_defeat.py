import pygame
from scoreboard import update_scoreboard, scoreboard
from screen import screen, bg, generate_buttons
from settings import *


def display_defeat(score):
    running_def = True
    update_scoreboard(score, settings['USERNAME'])
    while running_def:

        
        screen.blit(bg, (0,0))
        
        defeat_font = pygame.sysfont.SysFont('arial', 50)
        
        defeat_text = defeat_font.render("GAME OVER", True, "white")
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
        buttons = generate_buttons(defeat_font, 3, mouse_position, button_texts, 2)
            
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