import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        pos_random_angle = self.velocity.rotate(random_angle)
        neg_random_angle = self.velocity.rotate(-random_angle)

        self.radius -= ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)

        asteroid_1.velocity = pos_random_angle * 1.2
        asteroid_2.velocity = neg_random_angle * 1.2