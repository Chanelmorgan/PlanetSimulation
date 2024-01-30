import pygame
import math
pygame.init()

# Setting up the window
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# colors used in the planets
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 29, 50)
DARK_GREY = (80, 78, 81)


# Planet Class
class Planet:

    # Astronomical units - is approximately equal to the distance to the earth from the sun
    # ( we want it in meters we are using times 1000)
    AU = 149.6e6 * 1000

    # Gravitational  constant - used in finding the force of attraction between objects
    G = 6.67428e-11

    # Scale for the movement of the planets in the pygame window
    SCALE = 240 / AU  # 1AU = 100 pixels

    # How much of time we want to simulate
    TIMESTEP = 3600 * 24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        # In order to  move in a circular direction
        # must have velocity in more than one direction
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT /2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

# Event Loop
def main():
    run = True

    # makes sure the frame rate won't go past a certain rate
    clock = pygame.time.Clock()

    # initialising planets with the real values
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mercury = Planet(0.387 * Planet.AU, 0, DARK_GREY, 0.33 * 10**24)

    planets = [sun, earth, mars, mercury]

    while run:
        # Maximum of 60 fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.draw(WINDOW)
        pygame.display.update()
    pygame.quit()


main()