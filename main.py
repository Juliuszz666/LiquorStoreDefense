from enemies import *
from player import *
from classes_bullets import *
from screen import *
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("LSD 1.0")
clock = pygame.time.Clock()


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

def game_loop():
    running = True
    freeze = False
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
            if random.random() < 0.01:
                enemies.spawn_enemy()
            all_sprite.update()
            collisions_sprites()


if __name__ == "__main__":
        game_loop()

pygame.quit()
