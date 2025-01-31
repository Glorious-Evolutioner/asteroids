import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updatables = pygame.sprite.Group(player) 
    drawables = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    some_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        time = clock.tick(60)
        dt = time/1000
        updatables.update(dt)
        screen.fill("black")
        for thing in drawables:
            thing.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

