import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shots = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)
    updatables = pygame.sprite.Group(player) 
    drawables = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    some_field = AsteroidField()
    Shot.containers = (updatables, drawables, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        time = clock.tick(60)
        dt = time/1000

        updatables.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for thing in drawables:
            thing.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

