import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, velocity):
        asteroid = Asteroid(self.position.x, self.position.y, radius)
        asteroid.velocity = velocity * 1.2

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        self.spawn(self.radius - ASTEROID_MIN_RADIUS, self.velocity.rotate(angle))
        self.spawn(self.radius - ASTEROID_MIN_RADIUS, self.velocity.rotate(-angle))

        