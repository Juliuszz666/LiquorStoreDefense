import pygame
import webbrowser
from settings import *
from screen import generate_buttons
from sys import exit


def blit_credits():
    """
    Funciton displays credits buttons

    Returns:
        List of buttons to be clicked (rect)
    """
    credits_texts = ["Software by Julian Bednarek",
                     "Graphics by Paweł Korabiewski"]
    credit_font = pygame.sysfont.SysFont("Times New Roman", 25, False, True)
    credits = []
    credit_bg = pygame.Rect(0, 0, CREDITS[0], CREDITS[1])
    credit_bg.center = (SCREEN.get_width()/2,
                        SCREEN.get_height() * CREDITS_HEIGHT_CO)
    pygame.draw.rect(SCREEN, WHITE, credit_bg, CREDITS_BORDER, RADIUS['big'])

    for i in range(len(credits_texts)):
        credits_text = credit_font.render(credits_texts[i], True, WHITE)
        credits_rect = credits_text.get_rect()
        credits_rect.centerx = SCREEN.get_width()/2
        match i:
            case 0:
                credits_rect.bottom = SCREEN.get_height() * (CREDITS_HEIGHT_CO - CREDITS_DELTA)
            case 1:
                credits_rect.top = SCREEN.get_height() * (CREDITS_HEIGHT_CO + CREDITS_DELTA)
        credits.append(credits_rect)
        SCREEN.blit(credits_text, credits_rect)

    return credits


def main_menu():
    """
    Fucntion displaying main menu
    In function player can decide what action they can take and also write down theirs' name

    Returns:
        Action which player decided to take: (scoreboard, game, exit)
    """
    active = False
    running_menu = True

    while running_menu:

        SCREEN.blit(BG, (0, 0))

        event_key = pygame.key.get_pressed()
        button_texts = ["Scoreboard", "Play", "Quit"]
        mouse_position = pygame.mouse.get_pos()

        menu_font = pygame.sysfont.SysFont("Arial", FONT_SIZE['L'])
        username_font = pygame.sysfont.SysFont("Calibri", FONT_SIZE['S'])
        title_font = pygame.sysfont.SysFont(
            "Times New Roman", FONT_SIZE['XXL'], False, True)

        title = title_font.render("Liquor Store Defense", 1, "black")
        title_rect = title.get_rect()
        title_rect.center = (SCREEN.get_width()/2, SCREEN.get_height()/4)
        SCREEN.blit(title, title_rect)

        buttons = generate_buttons(menu_font, len(
            button_texts), mouse_position, button_texts, MENU_HEIGHT_CO)
        credits = blit_credits()

        username_bg = pygame.Rect(0, 0, USERNAME[0], USERNAME[1])
        username_bg.centerx = SCREEN.get_width() / 2
        username_bg.bottom = USERNAME_HEIGHT_CO * SCREEN.get_height() - BORDER_VALUE
        pygame.draw.rect(SCREEN, "red", username_bg, 0, RADIUS['medium'])

        username_text = username_font.render(
            "You are playing as:", True, "white")
        username_rect = username_text.get_rect(center=username_bg.center)
        SCREEN.blit(username_text, username_rect)

        text = get_username()
        text_input = pygame.Rect(0, 0, USERNAME[0], USERNAME[1])
        text_input.centerx = SCREEN.get_width()/2
        text_input.top = USERNAME_HEIGHT_CO * SCREEN.get_height() + BORDER_VALUE
        if not active:
            pygame.draw.rect(SCREEN, "black", text_input, 0, RADIUS['medium'])
        if active:
            pygame.draw.rect(SCREEN, D_GREY, text_input, 0, RADIUS['medium'])

        text_sur = username_font.render(text, True, "white")
        text_rect = text_sur.get_rect(center=text_input.center)
        SCREEN.blit(text_sur, text_rect)

        controls = pygame.image.load("img/controls.png")
        controls_rect = controls.get_rect()
        controls_rect.bottomright = (SCREEN.get_width() - const['delta_controls'],
                                     SCREEN.get_height() - const['delta_controls'])
        pygame.draw.rect(SCREEN, "lightgreen",
                         controls_rect, 0, RADIUS['medium'])
        SCREEN.blit(controls, controls_rect)

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
                                webbrowser.open(
                                    r"https://github.com/Juliuszz666")
                            case 1:
                                webbrowser.open(
                                    r"https://www.instagram.com/xmakaronito/")
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < MAX_LEN:
                            text += event.unicode

        save_username(text)
        pygame.display.flip()

    match action:
        case "scoreboard":
            return "scoreboard"
        case "game":
            return "game"
