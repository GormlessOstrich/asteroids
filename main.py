import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Adding both groups to a container
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        # Replaces 'pygame.Surface.fill(screen, "black")'
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        # Limits the framerate to 60 FPS.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
