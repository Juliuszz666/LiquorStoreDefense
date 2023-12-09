import enemies
import player
import classes_bullets as bullet
from screen import *
import pygame


# pygame setup
pygame.init()
pygame.display.set_caption("LSD 1.0")
clock = pygame.time.Clock()
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

    if not freeze:
        display()
        player.player.handling_equipment()
        player.player.update()
        i = len(enemies.enemies_r)-1
        j = len(enemies.enemies_m)-1

        while(i or j):
            if(j):
                enemies.enemies_m[j].update()
                enemies.enemies_m[j].attack(player.player.hitbox)
                enemies.enemies_m[j].defeat()
                j -= 1
            if(i):
                enemies.enemies_r[i].update()
                enemies.enemies_r[i].attack()
                enemies.enemies_m[j].defeat()
                i -= 1


#  print(enemies.player.health_points)

    pygame.display.flip()
    clock.tick(settings['FPS'])  # limits FPS to 60

pygame.quit()
