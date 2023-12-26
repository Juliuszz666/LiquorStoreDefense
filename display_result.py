import pygame
from scoreboard import update_scoreboard, scoreboard
from screen import SCREEN, BG, generate_buttons
from settings import *


def display_result(score, result, color):
    running_res = True
    update_scoreboard(score, settings['USERNAME'])
    while running_res:
        SCREEN.blit(BG, (0, 0))

        result_font = pygame.sysfont.SysFont('arial', 50, True)
        result_score_font = pygame.sysfont.SysFont('arial', 40, False, True)
        button_font = pygame.sysfont.SysFont('arial', 50)

        result_text = result_font.render(result, True, color)
        result_rect = result_text.get_rect()
        result_rect.centerx = SCREEN.get_width()/2
        result_rect.bottom = SCREEN.get_height()/4

        result_score_text = result_score_font.render(f"Score: {score}", True, "white")
        result_score_rect = result_score_text.get_rect()
        result_score_rect.centerx = SCREEN.get_width()/2
        result_score_rect.top = SCREEN.get_height()/4

        SCREEN.blit(result_text, result_rect)
        SCREEN.blit(result_score_text, result_score_rect)

        button_texts = ["Scoreboard", "Menu", "Quit game"]
        mouse_position = pygame.mouse.get_pos()
        buttons = generate_buttons(button_font, len(button_texts), mouse_position, button_texts, 2)

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
                                running_res = False
                                scoreboard()
                            case 1:
                                running_res = False
                            case 2:
                                exit()
        pygame.display.flip()
