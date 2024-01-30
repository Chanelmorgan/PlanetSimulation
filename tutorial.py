import pygame
import math
pygame.init()

# Setting up the window

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
WHITE = (255, 255, 255)
# Event Loop


def main():
    run = True

    # makes sure the frame rate won't go past a certain rate
    clock = pygame.time.Clock()

    while run:
        # Maximum of 60 fps
        clock.tick(60)
        #WINDOW.fill(WHITE)
        #pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()