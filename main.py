import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        
        for object in updatable:
            object.update(dt)

        for object in asteroids:
            if object.collision(player):
                print("Game Over!")
                exit()

            for shot in shots:
                if shot.collision(object):
                    shot.kill()
                    object.split()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()

        clock_delta_time = clock.tick(60)
        dt = clock_delta_time / 1000

if __name__ == "__main__":
    main()