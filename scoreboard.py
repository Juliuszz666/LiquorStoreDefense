import json
import pygame
from settings import *
from screen import generate_buttons


def update_scoreboard(user_score, username):
    """
    Function updates scoreboard stored in json file

    Args:
        user_score (int): points that user scored
        username (str): name that user provided
    """
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
    """
    Fucntion loads scoreboard from json file

    Returns:
        List if dictionaries with user and its score
    """
    try:
        with open('json/scoreboard.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data


def scoreboard():
    """
    Displays scoreboard and allow user to scroll scores by
    using arrop up and arrow down
    """
    scores = load_scoreboard()
    scores = sorted(scores, key=lambda dict: dict['SCORE'], reverse=True)
    index = 0
    scoreboard_font = pygame.sysfont.SysFont("Times new roman", FONT_SIZE['S'])
    titles_font = pygame.sysfont.SysFont("Calibri", FONT_SIZE['L'])
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
            if event_key[pygame.K_DOWN] and index < len(scores) - MAX_ROWS:
                index += 1
            if event_key[pygame.K_UP] and index > 0:
                index -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(mouse_position):
                        running_score = False

        SCREEN.blit(BG, (0, 0))

        score_title_bg = pygame.Rect(
            0, 0, SCORE_TITLE_BG[0], SCORE_TITLE_BG[1])
        score_title_bg.center = (SCREEN.get_width()/2, SCREEN.get_height()/8)
        pygame.draw.rect(SCREEN, RED, score_title_bg, 0, RADIUS['big'])

        score_title_text = titles_font.render("SCOREBOARD", True, WHITE)
        score_title_rect = score_title_text.get_rect()
        score_title_rect.center = (SCREEN.get_width()/2, SCREEN.get_height()/8)
        SCREEN.blit(score_title_text, score_title_rect)

        score_bg = pygame.Rect(0, 0, SCORE_BG[0], SCORE_BG[1])
        score_bg.center = (
            SCREEN.get_width()/2, SCREEN.get_height()/4+(MAX_ROWS / 2 * FONT_SIZE['S']))
        pygame.draw.rect(SCREEN, BLACK, score_bg, 0, RADIUS['small'])
        if len(scores):
            for i in range(min(len(scores), MAX_ROWS)):
                score_data = scores[index+i]
                if score_data['SCORE'] == const['winning_score']:
                    score_text_user = scoreboard_font.render(
                        f"{score_data['USER']}: ", True, GREEN)
                    score_text = scoreboard_font.render(
                        f"{score_data['SCORE']}", True, GREEN)
                else:
                    score_text_user = scoreboard_font.render(
                        f"{score_data['USER']}: ", True, WHITE)
                    score_text = scoreboard_font.render(
                        f"{score_data['SCORE']}", True, WHITE)

                score_rect_user = score_text_user.get_rect()
                score_rect_user.left = SCREEN.get_width()/2 - \
                    SCORE_BG[0]/2 + SCORE_DELTA
                score_rect_user.top = SCREEN.get_height()/4 + i * \
                    FONT_SIZE['S']

                score_rect = score_text.get_rect()
                score_rect.right = SCREEN.get_width()/2 + \
                    SCORE_BG[0]/2 - SCORE_DELTA
                score_rect.top = SCREEN.get_height()/4 + i * FONT_SIZE['S']

                SCREEN.blit(score_text_user, score_rect_user)
                SCREEN.blit(score_text, score_rect)

        button_texts = ["Menu"]
        mouse_position = pygame.mouse.get_pos()
        buttons = generate_buttons(titles_font, len(
            button_texts), mouse_position, button_texts, SCORE_HEIGHT_CO)
        pygame.display.flip()
