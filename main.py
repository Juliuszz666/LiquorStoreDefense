from enemies import *
from player import *
from classes_bullets import *
from screen import *
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
    shotgun_hit = pygame.sprite.groupcollide(all_enemies, shotgun_bullets, False, False)
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

    while running:
        """Game loop
        """

        event_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event_key[pygame.K_ESCAPE]:
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
        print(clock)

        if not freeze:
            display()
            if random.random() < time_score/100000:
                spawn_enemy()
            all_sprite.update()
            collisions_sprites()
            time_score += 1
            if time_score%(settings['FPS']*1)==0:
                protagonist.add_score(1)
            if is_gameover():
                result = "lost"
                for sprite in all_sprite:
                    sprite.kill()
                running = False
            if protagonist.score >= 10**9:
                result = "won"
                running = False
        if freeze:
            pass
    
    match result:
        case "lost":
            print("KURWA")
            display_defeat()
        case "won":
            print("Chuj")

if __name__ == "__main__":
    game()

pygame.quit()
