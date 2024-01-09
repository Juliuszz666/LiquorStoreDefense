from enemies import *
from player import *
from classes_bullets import *
import scoring
from screen import *
from sys import exit
from display_menu import main_menu
from display_result import display_result
from scoreboard import scoreboard
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("LSD 4.2.0")
clock = pygame.time.Clock()


def is_gameover():
    """
    Function checks if there are satisfied losing conditions

    Returns:
        Bool: True/False
    """
    for enemy in all_enemies:
        if enemy.rect.left < 0:
            return True
    if protagonist.is_dead():
        return True
    return False


def collisions_sprites():
    """
    Function investigates if there are any collision beetween speciffic groups
    """
    player_hit_r = pygame.sprite.spritecollide(
        protagonist, enemy_bullets, True)
    for bottle in player_hit_r:
        protagonist.get_damage(const['bottle']['dmg'])

    player_hit_m = pygame.sprite.spritecollide(protagonist, all_melee, False)
    for melee_attack in player_hit_m:
        if melee_attack.attack():
            protagonist.get_damage(const['enemies_other']['m_dmg'])
    pistol_hit = pygame.sprite.groupcollide(
        all_enemies, pistol_bullets, False, True)
    shotgun_hit = pygame.sprite.groupcollide(
        all_enemies, shotgun_bullets, False, True)
    bow_hit = pygame.sprite.groupcollide(all_enemies, arrows, False, True)
    for enemy in pistol_hit.keys():
        enemy.get_damage(const['b_pistol']['dmg'])
    for enemy in shotgun_hit.keys():
        enemy.get_damage(const['b_shotgun']['dmg'])
    for enemy in bow_hit.keys():
        enemy.get_damage(const['arrow']['dmg'])


def game():
    """
    Main game funciton
    """

    running = True
    freeze = False
    # reset mechanism if player decided to replay
    time_score = 0
    scoring.score = 0
    for sprite in all_sprite:
        sprite.kill()
    protagonist.reset()
    all_sprite.add(protagonist)

    while running:
        """
        Game loop
        """

        event_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event_key[pygame.K_ESCAPE]:
                exit()
            # if event_key[pygame.K_p]:  # only for testing
            #     result = "lost"
            #     running = False
            # if event_key[pygame.K_o]:
            #     scoring.add_score(100000)
            if event.type == pygame.WINDOWFOCUSLOST:
                freeze = True
            if event.type == pygame.WINDOWFOCUSGAINED:
                freeze = False
            if event.type == pygame.WINDOWMINIMIZED:
                freeze = True
            if event.type == pygame.WINDOWRESTORED:
                freeze = False

        pygame.display.flip()
        clock.tick(settings['FPS'])

        if not freeze:
            display(protagonist.health_points, scoring.score)
            if random.random() < math.sqrt(time_score)/const['spawn_co'] + const['base_spawn']:
                spawn_enemy()
            all_sprite.update()
            collisions_sprites()
            time_score += 1
            if time_score % (settings['FPS']) == 0:
                scoring.add_score(1)
            if is_gameover():
                result = "lost"
                running = False
            if scoring.score >= const['winning_score']:
                result = "won"
                running = False

    match result:
        case "lost":
            display_result(scoring.score, "GAME OVER", D_RED)
        case "won":
            display_result(const['winning_score'], "YOU WON", L_GREEN)


if __name__ == "__main__":
    while 1:
        match main_menu():
            case "game":
                game()
            case "scoreboard":
                scoreboard()

pygame.quit()
