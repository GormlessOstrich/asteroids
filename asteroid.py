import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill() # Immediately removes the original asteroid.

        if self.radius <= ASTEROID_MIN_RADIUS:
            return # If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS it was a small asteroid, therefore no further steps are taken.

        random_angle = random.uniform(20, 50) # Randomises the angle of the split within a range of 20° and 50°.
        new_velocity_a = self.velocity.rotate(random_angle) # Applying rotation in opposite directions.
        new_velocity_b = self.velocity.rotate(-random_angle) 
        new_radius = self.radius - ASTEROID_MIN_RADIUS # Decrements the new asteroids' radii by ASTEROID_MIN_RADIUS (20).
        
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity_a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity_b * 1.2
