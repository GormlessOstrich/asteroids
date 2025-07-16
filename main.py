import sys
import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Adding groups to containers
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Checks whether any objects of the 'asteroids' group are currently colliding with the player.
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.kill()
        
        # Replaces 'pygame.Surface.fill(screen, "black")'.
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        # Limits the framerate to 60 FPS.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
