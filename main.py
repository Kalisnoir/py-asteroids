import pygame
from constants import *

def main() -> int:
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            
        screen.fill((0, 0, 0))
        pygame.display.flip()
    return 0

if __name__ == "__main__":
    main()