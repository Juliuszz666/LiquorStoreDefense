import classes_beings as entities
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
        entities.player.handling_equipment()
        entities.player.movement()
        i = len(entities.enemies_r)-1
        j = len(entities.enemies_m)-1

        while(i or j):
            if(j):
                entities.enemies_m[j].update()
                #ntities.enemies_m[j].attack(entities.player.hitbox)
                entities.enemies_m[j].defeat()
                j -= 1
            if(i):
                entities.enemies_r[i].update()
                #      entities.enemies_r[i].attack()
                entities.enemies_m[j].defeat()
                i -= 1


#  print(entities.player.health_points)

    pygame.display.flip()
    clock.tick(settings['FPS'])  # limits FPS to 60

pygame.quit()
