import pygame
import math
pygame.init()

WIDTH, HEIGHT = 1700, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulator")
SPACE = "#ffffff"
YELLOW = '#ed7205'
BLUE = '#B5C0D0'
JUPITER = '#d8ca9d'
SUN_RADIUS = 30


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU # 1AU = 100 pixels
    TIMESTAMP = 3600*24 # 1day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distant_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, SUN_RADIUS, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1* Planet.AU, 0, SUN_RADIUS * 0.0914, BLUE, 5.9722 * 10**24)

    jupiter = Planet(-1.2* Planet.AU, 0, SUN_RADIUS * 0.1004, JUPITER, 1.89813 * 10**27)

    planets = [sun, earth, jupiter]

    while run:
        clock.tick(60)
        WIN.fill(SPACE) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)

        
        pygame.display.update()

    pygame.quit()
            

main()