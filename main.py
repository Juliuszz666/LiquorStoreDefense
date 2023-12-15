from enemies import *
from player import *
from classes_bullets import *
from screen import *
import pygame



# pygame setup
pygame.init()
pygame.display.set_caption("LSD 1.0")
clock = pygame.time.Clock()




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
        clock.tick(settings['FPS'])  # limits FPS to 60
    
        if not freeze:
            display()
            all_sprite.update()

if __name__ == "__main__":
    game_loop()
        
            
            
                                                            

    


pygame.quit()
