import classes_beings as entities
import classes_bullets as bullet
from screen import display
import pygame




# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
freeze = False
chuj = entities.Player(100, 100)



while running:

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
        display(entities.player)
        chuj.handling_equipment()

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()