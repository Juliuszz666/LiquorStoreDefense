from enemies import *
from player import *
from classes_bullets import *
import scoring
from screen import *
from sys import exit
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("LSD 1.0")
clock = pygame.time.Clock()

    
def is_gameover():
    for enemy in all_enemies:
        if enemy.rect.left < 0:
            return True
    if protagonist.is_dead():
        return True
    return False

def collisions_sprites():
    player_hit = pygame.sprite.spritecollide(protagonist, enemy_bullets, True)
    for bottle in player_hit:
        protagonist.get_damage(const['bottle']['dmg'])
    pistol_hit = pygame.sprite.groupcollide(all_enemies, pistol_bullets, False, True)
    shotgun_hit = pygame.sprite.groupcollide(all_enemies, shotgun_bullets, False, True)
    bow_hit = pygame.sprite.groupcollide(all_enemies, arrows, False, True)
    for enemy in pistol_hit.keys():
        enemy.get_damage(const['b_pistol']['dmg'])
    for enemy in shotgun_hit.keys():
        enemy.get_damage(const['b_shotgun']['dmg'])
    for enemy in bow_hit.keys():
        enemy.get_damage(const['arrow']['dmg'])

def game():
    
    running = True
    freeze = False
    time_score = 0
    scoring.score = 0
    # reset mechanism if player decided to replay
    for sprite in all_sprite:
        sprite.kill()
    protagonist.reset()
    all_sprite.add(protagonist)
    
    while running:
        """Game loop
        """

        event_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event_key[pygame.K_ESCAPE]:
                exit()
            if event_key[pygame.K_p]: # only for testing
                result = "lost"
                running = False
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
        #print(clock)

        if not freeze:
            display(protagonist.health_points, scoring.score)
            if random.random() < time_score/10000:
                spawn_enemy()
            all_sprite.update()
            collisions_sprites()
            time_score += 1
            if time_score%(settings['FPS']*1)==0:
                scoring.add_score(1)
            if is_gameover():
                result = "lost"        
                running = False
            if score >= 10**9:
                result = "won"
                running = False
        if freeze:
            pass
    
    match result:
        case "lost":
            display_defeat(scoring.score)
        case "won":
            print("Chuj")

if __name__ == "__main__":
    while 1:
        match main_menu():
            case "game":
                game()
            case "scoreboard":
                scoreboard()

pygame.quit()
