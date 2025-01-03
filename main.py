import pygame
from constants import *
from player import Player


def gameloop():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        
        screen.fill((0, 0, 0))
            
        for object in updatable:
            object.update(dt)

        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()
        clock_delta_time = clock.tick(60)
        dt = clock_delta_time / 1000

def main() -> int:
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    gameloop()

    return 0

if __name__ == "__main__":
    main()